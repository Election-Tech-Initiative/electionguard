from interfaces import IVerifier, IContestVerifier, ISelectionVerifier
from generator import ParameterGenerator, FilePathGenerator, SelectionInfoAggregator
import number
from json_parser import read_json_file

"""
This module does the decryption work on cast ballot tallies and each spoiled ballots.

For both cast ballot tallies and individual spoiled ballots, the decryption goes down from ballot, contest, selection, 
to guardian share-level. To mimic such hierarchy, the following 4 classes, DecryptionVerifier, 
DecryptionContestVerifier, DecryptionSelectionVerifier, and ShareVerifier, are created. 

Class: 
    DecryptionVerifier
    DecryptionContestVerifier
    DecryptionSelectionVerifier
    ShareVerifier
"""


class DecryptionVerifier(IVerifier):
    """
    This class is responsible for checking ballot decryption, its major work include,
    1. checking box 6, cast ballot tally decryption, where the verifier will check the total
    tallies of ballot selections match the actual selections.
    2. checking box 9, confirm two equations for each (non-dummy) option in each contest in the ballot coding file.
    3. checking box 10, spoiled ballot decryption, where spoiled ballots need to be checked individually.
    Note: user can check one single spoiled ballot or all the spoiled ballots in the folder by calling
    verify_a_spoiled_ballot(str) and verify_all_spoiled_ballots(), respectively

    Methods:
        verify_cast_ballot_tallies()
        verify_a_spoiled_ballot(str)
        verify_all_spoiled_ballots()
    """

    def __init__(self, path_g: FilePathGenerator, param_g: ParameterGenerator):
        super().__init__(param_g)
        self.path_g = path_g
        self.tally_dic = read_json_file(path_g.get_tally_file_path())
        self.contests = self.tally_dic.get('contests')
        self.spoiled_ballots = self.tally_dic.get('spoiled_ballots')

    def verify_cast_ballot_tallies(self) -> bool:
        """
        check if the ballot tally satisfies the equations in box 6, including:
        confirming for each (non-dummy) option in each contest in the ballot coding file that the aggregate encryption,
        (𝐴, 𝐵) satisfies 𝐴 = ∏ 𝛼 and 𝐵 = ∏ 𝛽 where the (𝛼 , 𝛽) are the corresponding encryptions on all cast ballots
        in the election record;
        confirming for each (non-dummy) option in each contest in the ballot coding file the
        following for each decrypting trustee 𝑇i, including:
                        the given value vi is in set Zq,
                        ai and bi are both in Zrp,
                        challenge ci = H(Q-bar, (A,B), (ai, bi), Mi))
                        equations g ^ vi = ai * Ki ^ ci mod p and A ^ vi = bi * Mi ^ ci mod p
        :return: true if all the above requirements are satisfied, false if any hasn't been satisfied
        """
        total_error, share_error = self.initialize_error(), self.initialize_error()

        tally_name = self.tally_dic.get('object_id')
        contest_names = list(self.contests.keys())

        # confirm that the aggregate encryption are the accumulative product of all
        # corresponding encryption on all cast ballots
        aggregator = SelectionInfoAggregator(self.path_g, self.param_g)
        total_res = self.__match_total_across_ballots(aggregator, contest_names)
        if not total_res:
            total_error = self.set_error()

        # confirm for each decrypting trustee Ti
        share_res = self.__make_all_contest_verification(self.contests, contest_names, tally_name)
        if not share_res:
            share_error = self.set_error()

        return not (total_error and share_error)

    def __match_total_across_ballots(self, aggregator: SelectionInfoAggregator, contest_names: list) -> bool:
        """
        matching the given tallies with accumulative products calculated across all ballots
        :param aggregator: a SelectionInfoAggregator instance for accessing information of a selection
        :param contest_names: a list of unique contest names, listed as "object_id" under contests
        :return: true if all the tallies match, false if not
        """
        error = self.initialize_error()

        dics_by_contest = aggregator.get_dics()
        total_data_dic = aggregator.get_total_data()
        total_pad_dic = aggregator.get_total_pad()

        for contest_name in contest_names:
            # get the corresponding index of pad and data dictionaries given contest name
            pad_dic_idx = aggregator.get_dic_id_by_contest_name(contest_name, 'a')
            data_dic_idx = aggregator.get_dic_id_by_contest_name(contest_name, 'b')
            pad_dic = dics_by_contest[pad_dic_idx]
            data_dic = dics_by_contest[data_dic_idx]

            selection_names = list(pad_dic.keys())
            for selection_name in selection_names:
                accum_pad = pad_dic.get(selection_name)
                tally_pad = total_pad_dic.get(contest_name, {}).get(selection_name)
                accum_data = data_dic.get(selection_name)
                tally_data = total_data_dic.get(contest_name, {}).get(selection_name)
                if not number.equals(accum_pad, tally_pad):
                    error = self.set_error()
                if not number.equals(accum_data, tally_data):
                    error = self.set_error()
        if error:
            print("Tally error.")

        return not error

    def verify_a_spoiled_ballot(self, ballot_name: str) -> bool:
        """
        verify a spoiled ballot's correctness by repeating the steps on cast_ballot_tallies, everything in box 6 & 9
        :param ballot_name: a unique name of a ballot, listed under "object_id" under a ballot
        :return: true if all the requirements have been met, false if not
        """
        spoiled_ballot = self.spoiled_ballots.get(ballot_name)
        contest_names = list(spoiled_ballot.keys())
        return self.__make_all_contest_verification(spoiled_ballot, contest_names, ballot_name)

    def verify_all_spoiled_ballots(self) -> bool:
        """
        verify all the spoiled ballots in the spoiled_ballots folder by checking each one individually
        :return true if all the spoiled ballots are verified as valid, false otherwise
        """
        error = self.initialize_error()

        spoiled_ballot_names = list(self.spoiled_ballots.keys())
        for spoiled_ballot_name in spoiled_ballot_names:
            if not self.verify_a_spoiled_ballot(spoiled_ballot_name):
                error = self.set_error()

        if error:
            print("Spoiled ballot decryption failure. ")
        else:
            print("Spoiled ballot decryption success. ")

        return not error

    def __make_all_contest_verification(self, contest_dic: dict, contest_names: list, field_name: str) -> bool:
        """
        helper function used in verify_cast_ballot_tallies() and verify_a_spoiled_ballot(str),
        verifying all contests in a ballot by calling the DecryptionContestVerifier
        :param contest_dic: the dictionary read from the given dataset, containing all the ballot tally or
        spoiled ballot info
        :param contest_names: a list of all the contest names in this election
        :param field_name: 'object_id' under the cast ballot tallies or each individual spoiled ballot,
         used as an identifier to signal whether this is a check for the cast ballot tallies or spoiled ballots
        :return: true if no error has been found in any contest verification in this cast ballot tallies or
        spoiled ballot check, false otherwise
        """
        error = self.initialize_error()
        for contest_name in contest_names:
            contest = contest_dic.get(contest_name)
            tcv = DecryptionContestVerifier(contest, self.param_g)
            if not tcv.verify_a_contest():
                error = self.set_error()

        if error:
            print(field_name + ' [box 6 & 9] decryption verification failure. ')
        else:
            print(field_name + ' [box 6 & 9] decryption verification success. ')

        return not error


class DecryptionContestVerifier(IContestVerifier):
    """
    This class is responsible for checking a contest in the decryption process.

    Contest is the first level under each ballot. Contest data exist in individual cast ballots, cast ballot tallies,
    and individual spoiled ballots. Therefore, DecryptionContestVerifier will also be used in the aforementioned places
    where contest data exist. Aggregates the selection checks done by DecryptionSelectionVerifier,
    used in DecryptionVerifier.

    Methods:
        verify_a_contest()
    """

    def __init__(self, contest_dic: dict, param_g: ParameterGenerator):
        super().__init__(param_g)
        self.contest_dic = contest_dic
        self.public_keys = param_g.get_public_keys_of_all_guardians()
        self.selections = self.contest_dic.get('selections')
        self.selection_names = list(self.selections.keys())
        self.contest_id = self.contest_dic.get('object_id')

    def verify_a_contest(self) -> bool:
        """
        Verifies one contest inside the cast ballot tallies or a spoiled ballot at a time.
        It combines all the error checks for all the selections under this contest.
        :return: true if all the selection checks are passed, false otherwise
        """
        error = self.initialize_error()
        for selection_name in self.selection_names:
            selection = self.selections.get(selection_name)
            tsv = DecryptionSelectionVerifier(selection, self.param_g)
            if not tsv.verify_a_selection():
                error = self.set_error()

        if error:
            print(self.contest_id + ' tally decryption failure. ')

        return not error


class DecryptionSelectionVerifier(ISelectionVerifier):
    """
    This class works on handling selection decryption.

    Selection is the layer under contest and above guardian shares. Methods in this class provides public access to
    a selection's pad and data values for convenience and aggregates the guardian share check conducted by
    ShareVerifier. Used in DecryptionContestVerifier.

    Method:
        get_pad()
        get_data()
        verify_a_selection()
    """
    def __init__(self, selection_dic: dict, param_g: ParameterGenerator):
        super().__init__(param_g)
        self.selection_dic = selection_dic
        self.selection_id = selection_dic.get('object_id')
        self.pad = int(self.selection_dic.get('message', {}).get('pad'))
        self.data = int(self.selection_dic.get('message', {}).get('data'))
        self.public_keys = param_g.get_public_keys_of_all_guardians()

    def get_pad(self) -> int:
        """
        get the alpha/pad value of a selection
        :return: the pad value of a selection
        """
        return self.pad

    def get_data(self) -> int:
        """
        get the beta/data value of a selection
        :return: the data value of a selection
        """
        return self.data

    def verify_a_selection(self) -> bool:
        """
        verifies a selection at a time. It combines all the checks separated by guardian shares
        :return: true if no error has found in any share verification of this selection, false otherwise
        """
        shares = self.selection_dic.get('shares')
        sv = ShareVerifier(shares, self.param_g, self.pad, self.data)
        res = sv.verify_all_shares()
        if not res:
            print(self.selection_id + " tally verification error. ")

        return res


class ShareVerifier(IVerifier):
    """
    This class is used to check shares of decryption under each selections in cast ballot tallies and spoiled ballots.

    The share level is the deepest level the data of cast ballot tallies and spoiled ballots can go, therefore, most of
    the computation needed for decryption happen here.

    Method:
        verify_all_shares()
    """

    def __init__(self, shares: list, param_g: ParameterGenerator, selection_pad: int, selection_data: int):
        # calls IVerifier init
        super().__init__(param_g)

        self.shares = shares
        self.selection_pad = selection_pad
        self.selection_data = selection_data
        self.public_keys = param_g.get_public_keys_of_all_guardians()

    def verify_all_shares(self) -> bool:
        """
        verify all shares of a tally decryption
        :return: True if no error occur in any share, False if some error
        """
        error = self.initialize_error()
        for index, share in enumerate(self.shares):
            curr_public_key = int(self.public_keys[index])
            if not self.__verify_a_share(share, curr_public_key):
                error = self.set_error()
                print("Guardian {} decryption error. ".format(index))

        return not error

    def __verify_a_share(self, share_dic: dict, public_key: int) -> bool:
        """
        verify one share at a time, check box 6 requirements,
        (1) if the response vi is in the set Zq
        (2) if the given ai, bi are both in set Zrp
        :param share_dic: a specific share inside the shares list
        :return: True if no error found in share partial decryption, False if any error
        """
        error = self.initialize_error()

        # get values
        pad = self.__get_share_pad(share_dic)
        data = self.__get_share_data(share_dic)
        response = self.__get_share_response(share_dic)
        challenge = self.__get_share_challenge(share_dic)
        partial_decryption = self.__get_partial_decryption(share_dic)

        # check if the response vi is in the set Zq
        response_correctness = self.__check_response(response)

        # check if the given ai, bi are both in set Zrp
        pad_data_correctness = self.__check_data(data) and self.__check_pad(pad)

        # check if challenge is correctly computed
        challenge_correctness = self.__check_challenge(challenge, pad, data, partial_decryption)

        # check equations
        equ1_correctness = self.__check_equation1(response, pad, challenge, public_key)
        equ2_correctness = self.__check_equation2(response, data, challenge, partial_decryption)

        # error check
        if not (response_correctness and pad_data_correctness and challenge_correctness
                and equ1_correctness and equ2_correctness):
            error = self.set_error()
            print("partial decryption failure. ")

        return not error

    def __check_equation1(self,  pad: int, response: int,challenge: int, public_key: int) -> bool:
        """
        check if equation g ^ vi = ai * (Ki ^ ci) mod p is satisfied.

        The equation is checked along with the one specified in check_equation2() to give proof that the guardian has
        knowledge about the secret key that would give the secret key without revealing the actual secret.
        :param response: response of a share, vi
        :param pad: pad of a share, ai
        :param public_key: public key of a guardian, Ki
        :param challenge: challenge of a share, ci
        :return True if the equation is satisfied, False if not
        """
        left = pow(self.generator, response, self.large_prime)
        right = number.mod_p(pad * pow(public_key, challenge, self.large_prime))

        res = number.equals(left, right)
        if not res:
            print("equation 1 error. ")

        return res

    def __check_equation2(self, response: int, data: int, challenge: int, partial_decrypt: int) -> bool:
        """
        check if equation A ^ vi = bi * (Mi^ ci) mod p is satisfied.
        The equation is checked along with the one specified in check_equation1() to give proof that the guardian has
        knowledge about the secret key that would give the secret key without revealing the actual secret.

        :param response: response of a share, vi
        :param data: data of a share, bi
        :param challenge: challenge of a share, ci
        :param partial_decrypt: partial decryption of a guardian, Mi
        :return True if the equation is satisfied, False if not
        """
        left = pow(self.selection_pad, response, self.large_prime)
        right = number.mod_p(data * pow(partial_decrypt, challenge, self.large_prime))

        res = number.equals(left, right)
        if not res:
            print("equation 2 error. ")

        return res

    @staticmethod
    def __check_response(response: int) -> bool:
        """
        check if the share response vi is in the set Zq
        :param response: response value vi of a share
        :return: True if the response is in set Zq, False if not
        """
        res = number.is_within_set_zq(response)
        if not res:
            print("response error. ")

        return res

    @staticmethod
    def __check_pad(pad: int) -> bool:
        """
        check if the given ai/pad of a share is in set Zrp
        :param pad: a pad value ai of a share
        :return: True if this value is in set Zrp, False if not
        """
        res = number.is_within_set_zrp(pad)
        if not res:
            print("a/pad value error. ")

        return res

    @staticmethod
    def __check_data(data: int) -> bool:
        """
        check if the given bi/data of a share is in set Zrp
        :param data: a data value bi of a share
        :return: True if this value is in set Zrp, False if not
        """
        res = number.is_within_set_zrp(data)
        if not res:
            print("b/data value error. ")

        return res

    def __check_challenge(self, challenge: int, pad: int, data: int, partial_decrypt: int) -> bool:
        """
        check if the given challenge values Ci satisfies ci = H(Q-bar, (A,B), (ai, bi), Mi)
        :param challenge: given challenge of a share, Ci, for comparison
        :param pad: pad of a share, ai
        :param data: data number of a share, bi
        :param partial_decrypt: partial decryption of a guardian, Mi
        :return: True if the given Ci equals to the ci computed using hash
        """
        challenge_computed = number.hash_elems(self.extended_hash, self.selection_pad, self.selection_data,
                                               pad, data, partial_decrypt)

        res = number.equals(challenge, challenge_computed)

        if not res:
            print("challenge value error. ")

        return res

    @staticmethod
    def __get_share_pad(share_dic: dict) -> int:
        """
        get the alpha/pad of a share, noted as ai
        :param share_dic: the dictionary holding all the share info
        :return: alpha/pad of a share in integer
        """
        return int(share_dic.get('proof', {}).get('pad'))

    @staticmethod
    def __get_share_data(share_dic: dict) -> int:
        """
        get the beta/data of a share, noted as bi
        :param share_dic: the dictionary holding all the share info
        :return: beta/data of a share in integer
        """
        return int(share_dic.get('proof', {}).get('data'))

    @staticmethod
    def __get_share_challenge(share_dic: dict) -> int:
        """
        get the challenge value of a share, noted as ci
        :param share_dic: the dictionary holding all the share info
        :return: the challenge value of a share in integer
        """
        return int(share_dic.get('proof', {}).get('challenge'))

    @staticmethod
    def __get_share_response(share_dic: dict) -> int:
        """
        get the response value of a share, noted as vi
        :param share_dic: the dictionary holding all the share info
        :return: the response value of a share in integer
        """
        return int(share_dic.get('proof', {}).get('response'))

    @staticmethod
    def __get_partial_decryption(share_dic: dict) -> int:
        """
        get the partial decryption of a selection by a guardian i, noted as Mi
        :param share_dic: the dictionary holding all the share info
        :return: a partial decryption of a selection in integer
        """
        return int(share_dic.get('share'))
