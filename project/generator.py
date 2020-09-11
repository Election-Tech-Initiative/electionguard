from json_parser import read_json_file
import glob
import number
import os


class FilePathGenerator:
    """
    This class is responsible for navigating to different data files in the given dataset folder,
    the root folder path can be changed to where the whole dataset is stored and its inner structure should
    remain unchanged.
    """

    def __init__(self, root_folder_path="../data/"):
        """
        generate a file name generator with parameters from the json files
        """
        self.DATA_FOLDER_PATH = root_folder_path
        self.FILE_TYPE_SUFFIX = '.json'
        self.FOLDER_SUFFIX = '/'

    def get_coefficients_folder_path(self) -> str:
        """
        get the folder path to the coefficients
        :return:
        """
        coeff_folder_path = '/coefficients'
        return self.DATA_FOLDER_PATH + coeff_folder_path + self.FOLDER_SUFFIX

    def get_guardian_coefficient_file_path(self, index: int) -> str:
        """
        generate a coefficient file path given the guardian's index
        :param index: index of a guardian, (0 - number of guardians)
        :return: a string of the coefficient
        """
        coeff_file_path = 'coefficient_validation_' \
                          'set_hamilton-county-canvass-board-member-'

        return self.get_coefficients_folder_path() + coeff_file_path + str(index) + self.FILE_TYPE_SUFFIX

    def get_context_file_path(self) -> str:
        """
        gets the file path to the context.json file
        :return: a string representation of file path to the context.json file
        """
        return self.DATA_FOLDER_PATH + 'context' + self.FILE_TYPE_SUFFIX

    def get_constants_file_path(self) -> str:
        """
        gets the file path to the constants.json file
        :return: a string representation of file path to the constants.json file
        """
        return self.DATA_FOLDER_PATH + 'constants' + self.FILE_TYPE_SUFFIX

    def get_tally_file_path(self) -> str:
        """
        gets the file path to the tally.json file
        :return: a string representation of file path to the tally.json file
        """
        return self.DATA_FOLDER_PATH + 'tally' + self.FILE_TYPE_SUFFIX

    def get_description_file_path(self) -> str:
        """
        gets the file path to the description.json file
        :return: a string representation of file path to the description.json file
        """
        return self.DATA_FOLDER_PATH + 'description' + self.FILE_TYPE_SUFFIX

    def get_encrypted_ballot_folder_path(self) -> str:
        """
        get a path to the encrypted_ballots folder
        :return: a string representation of path to the encrypted_ballots folder
        """

        return self.DATA_FOLDER_PATH + 'encrypted_ballots' + self.FOLDER_SUFFIX

    def get_spoiled_ballot_folder_path(self) -> str:
        """
        get a path to the spoiled_ballots folder
        :return: a string representation of path to the spoiled_ballots folder
        """
        return self.DATA_FOLDER_PATH + '/spoiled_ballots' + self.FILE_TYPE_SUFFIX

    def get_device_folder_path(self) -> str:
        """
        get a path to the devices folder
        :return: a string representation of path to the devices.json file
        """
        return self.DATA_FOLDER_PATH + '/devices' + self.FILE_TYPE_SUFFIX


class ParameterGenerator:
    """
    This class should be responsible for accessing parameters stored in dataset files
    with the help of the file path file generator to locate the files. Parameters in this
    case only include those that are higher than ballot-level. Those that are directly related
    to each specific ballot, contest, or selection will be taken care of by each level of verifiers.
    """
    def __init__(self, path_g: FilePathGenerator):
        """
        initializer
        :param path_g: FilePathGenerator that helps to get the paths of files
        """
        self.path_g = path_g

    def get_context(self) -> dict:
        """
        get all context information as a dictionary
        :return: a dictionary of context info
        """
        context_path = self.path_g.get_context_file_path()
        return read_json_file(context_path)

    def get_constants(self) -> dict:
        """
        get all constants as a dictionary
        :return: a dictionary of constants info
        """
        constants_path = self.path_g.get_constants_file_path()
        return read_json_file(constants_path)

    def get_generator(self) -> int:
        """
        get generator, set default name to be generator
        :return: generator 'g' in integer
        """
        return int(self.get_constants().get('generator'))

    def get_large_prime(self) -> int:
        """
        get large prime p
        :return: large prime 'p' in integer
        """
        return int(self.get_constants().get('large_prime'))

    def get_small_prime(self) -> int:
        """
        get small prime q
        :return: small prime 'q' in integer
        """
        return int(self.get_constants().get('small_prime'))

    def get_cofactor(self) -> int:
        """
        get cofactor r
        :return: cofactor 'r' in integer
        """
        return int(self.get_constants().get('cofactor'))

    def get_extended_hash(self) -> int:
        """
        get extended base hash Q-bar
        :return: extended base hash Q-bar in integer
        """
        return int(self.get_context().get('crypto_extended_base_hash'))

    def get_base_hash(self) -> int:
        """
        get extended base hash Q
        :return: base hash Q in integer
        """
        return int(self.get_context().get('crypto_base_hash'))

    def get_elgamal_key(self) -> int:
        """
        get Elgamal key K
        :return: Elgamal key K in integer
        """
        return int(self.get_context().get('elgamal_public_key'))

    def get_public_key_of_a_guardian(self, index: int) -> int:
        """
        get the public key Ki of a guardian
        :param index: guardian index
        :return: public key Ki of guardian i in integer
        """
        file_path = self.path_g.get_guardian_coefficient_file_path(index)
        coefficients = read_json_file(file_path)
        return int(coefficients.get('coefficient_commitments')[0])

    def get_public_keys_of_all_guardians(self) -> list:
        """
        get all the public keys of all guardians as a list
        :return: a list of guardians' public keys
        """
        num_of_guardians = self.get_num_of_guardians()
        for i in range(num_of_guardians):
            yield self.get_public_key_of_a_guardian(i)

    def get_description(self) -> dict:
        """
        get the election description information as dictionary
        :return: a dictionary representation of the description.json
        """
        file_path = self.path_g.get_description_file_path()
        return read_json_file(file_path)

    def get_num_of_guardians(self) -> int:
        """
        check consistency and return the number of guardians of this election
        :return: number of guardians in integer if the number is the same from context file and coefficient folder
                if the number is inconsistent, returns -1
        """
        num_context = self.__get_num_of_guardians_from_context()
        num_coeff = self.__get_num_of_guardians_from_file()
        if num_context == num_coeff:
            return num_context
        else:
            print("Number of guardian error. ")
            return -1

    def __get_num_of_guardians_from_context(self) -> int:
        """
        get number of guardians from the context.json
        :return: number of guardians n in integer
        """
        context_file_path = self.path_g.get_context_file_path()
        context = read_json_file(context_file_path)
        return int(context.get('number_of_guardians'))

    def __get_num_of_guardians_from_file(self) -> int:
        """
        get number of guardians from the number of coefficient files in the coefficients folder
        :return: number of guardians n in integer
        """
        coeff_folder_path = self.path_g.get_coefficients_folder_path()
        coeff_files = next(os.walk(coeff_folder_path))[2]
        return len(coeff_files)

    def get_quorum(self) -> int:
        """
        get the minimum number of presenting guardians in this election
        :return: the minimum number of presenting guardians in integer
        """
        context_file_path = self.path_g.get_context_file_path()
        context = read_json_file(context_file_path)
        return int(context.get('quorum'))

    def get_num_of_ballots(self) -> int:
        """
        get the number of ballots by checking the number of ballot files (including spoiled ballots)
         in the encrypted ballot folder
        :return: number of ballots in integer
        """
        ballot_folder_path = self.path_g.get_encrypted_ballot_folder_path()
        ballot_files = next(os.walk(ballot_folder_path))[2]
        return len(ballot_files)

    def get_num_of_spoiled_ballots(self) -> int:
        """
        get the number of spoiled ballots by checking the number of spoiled ballot files
        in the spoiled ballot folder
        :return: number of spoiled ballots in integer
        """
        spoiled_ballot_folder_path = self.path_g.get_spoiled_ballot_folder_path()
        spoiled_ballot_files = next(os.walk(spoiled_ballot_folder_path))[2]
        return len(spoiled_ballot_files)

    def get_device_id(self) -> str:
        """
        get the id of recording device
        :return: the device id as string
        """
        device_folder_path = self.path_g.get_device_folder_path()
        for file in glob.glob(device_folder_path + '*json'):
            dic = read_json_file(file)
            return dic.get('uuid')

    def get_location(self) -> str:
        """
        get the location information of the election
        :return: location information as a string
        """
        device_folder_path = self.path_g.get_device_folder_path()
        for file in glob.glob(device_folder_path + '*json'):
            dic = read_json_file(file)
            return dic.get('location')


class VoteLimitCounter:
    """
    This VoteLimitCounter class keeps track of the vote limits of all the contests in an election, generates a
    dictionary of "contest name - maximum votes allowed" pairs. Used in the encryption verifier.
    """
    def __init__(self, param_g: ParameterGenerator):
        self.description_dic = param_g.get_description()
        self.contest_vote_limits = {}

    def get_contest_vote_limits(self) -> dict:
        """
        get the vote limits of a specific contest, used to confirm a ballot's correctness,
        whether the vote exceeds the vote limits of any contests in this ballots
        :return: a dictionary of contest vote limits of all the contests in this election
        """
        # fill in dictionary when it's empty
        if not bool(self.contest_vote_limits):
            self.__fill_contest_vote_limits()

        return self.contest_vote_limits

    def __fill_contest_vote_limits(self):
        """
        fill in the num_max_vote dictionary, key- contest name, value- maximum votes allowed for this contest
        source: description
        """
        contests = self.description_dic.get('contests')
        for contest in contests:
            contest_name = contest.get('object_id')
            num_max_vote = contest.get('votes_allowed')
            self.contest_vote_limits[contest_name] = int(num_max_vote)


class SelectionInfoAggregator:
    """
    This SelectionInfoAggregator class aims at collecting and storing all the selection information across contest
     in one place. Its final purpose is to create a list of dictionaries, each dictionary stands for a contest, inside a
     dictionary are corresponding selection name and its alpha or beta values. Used in decryption verifier.
    """
    def __init__(self, path_g: FilePathGenerator, param_g: ParameterGenerator):
        self.param_g = param_g
        self.path_g = path_g
        self.order_names_dic = {}   # a dictionary to store the contest names and its sequence
        self.names_order_dic = {}
        self.contest_selection_names = {}  # a dictionary to store the contest names and its selection names
        self.dics_by_contest = []   # a list to store all the dics, length = 2 * contest_names
        self.total_pad_dic = {}
        self.total_data_dic = {}

    def get_dics(self):
        """
        get the whole list of dictionaries of contest selection information
        :return:a list of dictionaries of contest selection information
        """
        if len(self.dics_by_contest) == 0:
            self.__create_inner_dic()
            self.__fill_in_dics()
        return self.dics_by_contest

    def get_dic_id_by_contest_name(self, contest_name: str, type: str) -> int:
        """
        get the corresponding dictionary id in the dictionary list by the name of contest
        :param contest_name: name of a contest, noted as "object id" under contest
        :param type: a or b, a stands for alpha, b stands for beta, to denote what values the target dictionary contains
        :return: a dictionary of alpha or beta values of all the selections of a specific contest
        """
        if type == 'a':
            return 2 * self.order_names_dic[contest_name]
        elif type == 'b':
            return 2 * self.order_names_dic[contest_name] + 1

    def __create_inner_dic(self):
        """
        create 2 * contest names number of dicts. Two for each contest, one for storing pad values,
        one for storing data values. Fill in column names with selections in that specific contest
        :return: none
        """
        # get number of contest names
        if len(self.order_names_dic.keys()) == 0:
            self.__fill_in_contest_dicts()

        num = len(self.order_names_dic.keys())

        # create 2 * contest name number of lists
        for i in range(num * 2):

            # get the corresponding contest and selections of this list
            contest_idx = int(i / 2)
            contest_name = self.names_order_dic.get(contest_idx)
            selection_names = self.contest_selection_names.get(contest_name)

            # create new dict
            curr_dic = {}
            for selection_name in selection_names:
                curr_dic[selection_name] = ''  # store strings not integers in dic

            # append to dic list
            self.dics_by_contest.append(curr_dic)

    def __fill_in_dics(self):
        """
        loop over the folder that stores all encrypted ballots once, go through every ballot to get the selection
        alpha/pad and beta/data
        :return: none
        """
        # get to the folder
        ballot_folder_path = self.path_g.get_encrypted_ballot_folder_path()

        # loop over every ballot file
        for ballot_file in glob.glob(ballot_folder_path + '*json'):
            ballot = read_json_file(ballot_file)
            ballot_name = ballot.get('object_id')
            ballot_state = ballot.get('state')

            # ignore spoiled ballots
            if ballot_state == 'CAST':

                # loop over every contest
                contests = ballot.get('contests')
                for contest in contests:
                    contest_name = contest.get('object_id')
                    selections = contest.get('ballot_selections')
                    contest_idx = self.order_names_dic.get(contest_name)
                    curr_pad_dic = self.dics_by_contest[contest_idx * 2]
                    curr_data_dic = self.dics_by_contest[contest_idx * 2 + 1]

                    # loop over every selection
                    for selection in selections:
                        selection_name = selection.get('object_id')
                        is_placeholder_selection = selection.get('is_placeholder_selection')

                        # ignore placeholders
                        if not is_placeholder_selection:
                            pad = selection.get('ciphertext', {}).get('pad')
                            data = selection.get('ciphertext', {}).get('data')
                            self.__get_accum_product(curr_pad_dic, selection_name, int(pad))
                            self.__get_accum_product(curr_data_dic, selection_name, int(data))

    @staticmethod
    def __get_accum_product(dic: dict, selection_name: str, num: int):
        """
        get the accumulative product of alpha/pad and beta/data for all the selections
        :param dic: the dictionary alpha or beta values are being added into
        :param selection_name: name of a selection, noted as "object id" under a selection
        :param num: a number being multiplied to get the final product
        :return: none
        """
        if dic.get(selection_name) == '':
            dic[selection_name] = str(num)
        else:
            temp = int(dic[selection_name])
            product = number.mod_p(temp * num)
            dic[selection_name] = str(product)

    def __fill_total_pad_data(self):
        """
        loop over the tally.json file and read alpha/pad and beta/data of each non dummy selections in all contests,
        store these alphas and betas in the corresponding contest dictionary
        :return: none
        """
        tally_path = self.path_g.get_tally_file_path()
        tally = read_json_file(tally_path)
        contests = tally.get('contests')
        contest_names = list(contests.keys())
        for contest_name in contest_names:
            curr_dic_pad = {}
            curr_dic_data = {}
            contest = contests.get(contest_name)
            selections = contest.get('selections')
            selection_names = list(selections.keys())
            for selection_name in selection_names:
                selection = selections.get(selection_name)
                total_pad = selection.get('message', {}).get('pad')
                total_data = selection.get('message', {}).get('data')
                curr_dic_pad[selection_name] = total_pad
                curr_dic_data[selection_name] = total_data
            self.total_pad_dic[contest_name] = curr_dic_pad
            self.total_data_dic[contest_name] = curr_dic_data

    def __fill_in_contest_dicts(self):
        """
        get contest names, its corresponding sequence, and its corresponding selection names from description,
        (1) order_names_dic : key - sequence order, value - contest name
        (2) contest_selection_names: key - contest name, value - a list of selection names
        :return: None
        """
        description_dic = self.param_g.get_description()
        contests = description_dic.get('contests')

        for contest in contests:
            # fill in order_names_dic dict
            # get contest names
            contest_name = contest.get('object_id')
            # get contest sequence
            contest_sequence = contest.get('sequence_order')
            self.order_names_dic[contest_name] = contest_sequence
            self.names_order_dic[contest_sequence] = contest_name

            # fill in contest_selection_names dict
            curr_list = []
            self.contest_selection_names[contest_name] = curr_list
            selections = contest.get('ballot_selections')
            for selection in selections:
                # get selection names
                selection_name = selection.get('object_id')
                curr_list.append(selection_name)

    def get_total_pad(self):
        """
        get the total alpha/pad of tallies of all contests
        :return: a dictionary of alpha/pad of tallies of all contests
        """
        if len(self.total_pad_dic.keys()) == 0:
            self.__fill_total_pad_data()

        return self.total_pad_dic

    def get_total_data(self):
        """
        get the total beta/data of tallies of all contests
        :return: a dictionary of beta/data of tallies of all contests
        """
        if len(self.total_data_dic.keys()) == 0:
            self.__fill_total_pad_data()

        return self.total_data_dic






