from project.interfaces import IVerifier, IContestVerifier, ISelectionVerifier
from project.generator import ParameterGenerator, FilePathGenerator, SelectionInfoAggregator
from project import number
from project.json_parser import read_json_file


class DecryptionVerifier(IVerifier):
    """
    This class is responsible for box 6, tally decryption, where the verifier will check the total
    tally of ballot selections matches the actual selections
    """

    def __init__(self, path_g: FilePathGenerator, param_g: ParameterGenerator):
        super().__init__(param_g)
        self.path_g = path_g
        self.tally_dic = read_json_file(path_g.get_tally_file_path())
        self.contests = self.tally_dic.get('contests')
        self.spoiled_ballots = self.tally_dic.get('spoiled_ballots')

    def verify_cast_ballot_tallies(self) -> bool:
        """
        confirm for each (non-dummy) option in each contest in the ballot coding file that the aggregate encryption,
        (𝐴, 𝐵) satisfies 𝐴 = ∏ 𝛼 and 𝐵 = ∏ 𝛽 where the (𝛼 , 𝛽) are the corresponding encryptions on all cast ballots
        in the election record.
        verify confirm for each (non-dummy) option in each contest in the ballot coding file the
        following for each decrypting trustee 𝑇
        :return:
        """
        total_error, share_error = self.initialize_error(), self.initialize_error()

        tally_name = self.tally_dic.get('object_id')
        contest_names = list(self.contests.keys())

        # confirm that the aggregate encryption are the accumulative product of all
        # corresponding encryptions on all cast ballots
        aggregator = SelectionInfoAggregator(self.path_g, self.param_g)
        dics_by_contest = aggregator.get_dics()
        total_data_dic = aggregator.get_total_data()
        total_pad_dic = aggregator.get_total_pad()
        total_res = self.__match_total_across_ballots(aggregator, contest_names,
                                                      dics_by_contest, total_pad_dic, total_data_dic)
        if not total_res:
            total_error = self.set_error()

        # confirm for each decrypting trustee Ti
        share_res = self.__make_all_contest_verification(self.contests, contest_names, tally_name)
        if not share_res:
            share_error = self.set_error()

        return not (total_error and share_error)

    def __match_total_across_ballots(self, aggregator: SelectionInfoAggregator, contest_names: list,
                                     dics: list, total_pad_dic: dict, total_data_dic: dict) -> bool:
        """
        check if the total pad and data from the tally file with the accumulative product across ballots
        are equal
        :param dics:
        :return:
        """
        error = self.initialize_error()

        for contest_name in contest_names:
            # get the corresponding index of pad and data dictionaries given contest name
            pad_dic_idx = aggregator.get_dic_id_by_contest_name(contest_name, 'a')
            data_dic_idx = aggregator.get_dic_id_by_contest_name(contest_name, 'b')
            pad_dic = dics[pad_dic_idx]
            data_dic = dics[data_dic_idx]

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

        :param ballot_name:
        :return:
        """
        spoiled_ballot = self.spoiled_ballots.get(ballot_name)
        contest_names = list(spoiled_ballot.keys())
        return self.__make_all_contest_verification(spoiled_ballot, contest_names, ballot_name)

    def verify_all_spoiled_ballots(self) -> bool:
        """

        :return:
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

    def __make_all_contest_verification(self, contest_dic: dict, contest_names: list, tally_name: str) -> bool:
        """
        helper function
        :param contest_dic:
        :param contest_names:
        :param tally_name:
        :return:
        """
        error = self.initialize_error()
        for contest_name in contest_names:
            contest = contest_dic.get(contest_name)
            tcv = DecryptionContestVerifier(contest, self.param_g)
            if not tcv.verify_a_contest():
                error = self.set_error()

        if error:
            print(tally_name + ' [box 9] decryption verification failure. ')
        else:
            print(tally_name + ' [box 9] decryption verification success. ')

        return not error


class DecryptionContestVerifier(IContestVerifier):
    """
    This class is responsible for checking a contest
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

        :return:
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
    def __init__(self, selection_dic: dict, param_g: ParameterGenerator):
        super().__init__(param_g)
        self.selection_dic = selection_dic
        self.selection_id = selection_dic.get('object_id')
        self.pad = int(self.selection_dic.get('message', {}).get('pad'))
        self.data = int(self.selection_dic.get('message', {}).get('data'))
        self.public_keys = param_g.get_public_keys_of_all_guardians()

    def get_pad(self) -> int:
        """
        get a selection's alpha and beta
        :return:
        """
        return self.pad

    def get_data(self) -> int:
        return self.data

    def verify_a_selection(self) -> bool:
        """

        :return:
        """
        shares = self.selection_dic.get('shares')
        sv = ShareVerifier(shares, self.param_g, self.pad, self.data)
        res = sv.verify_all_shares()
        if not res:
            print(self.selection_id + " tally verification error. ")

        return res


class ShareVerifier(IVerifier):
    """
    This class is used to check shares of decryption under each selections in election tally and spoiled ballots
    """

    def __init__(self, shares: list, param_g: ParameterGenerator, selection_pad: int, selection_data: int):
        # calls IVerifier init
        super().__init__(param_g)

        self.shares = shares
        self.selection_pad = selection_pad
        self.selection_data = selection_data

    def verify_all_shares(self) -> bool:
        """
        verify all shares of a tally decryption
        :return: True if no error occur in any share, False if some error
        """
        error = self.initialize_error()
        for index, share in enumerate(self.shares):
            if not self.__verify_a_share(share):
                error = self.set_error()
                print("Guardian {} decryption error. ".format(index))

        return not error

    def __verify_a_share(self, share_dic: dict) -> bool:
        """
        verify one share at a time, check if
        :param share_dic: a specific share inside the shares list
        :return: True if no error found in share partial decryption, False if any error
        """
        error = self.initialize_error()

        # check if the response vi is in the set Zq
        response_correctness = self.__check_response(share_dic)

        # check if the given ai, bi are both in set Zrp
        pad_data_correctness = self.__check_data(share_dic) and self.__check_pad(share_dic)

        if not response_correctness or not pad_data_correctness:
            error = self.set_error()
            print("partial decryption failure. ")

        return not error

    @staticmethod
    def __check_response(share_dic: dict) -> bool:
        """
        check if the share response vi is in the set Zq
        :param share_dic: a dictionary of a share
        :return: True if the response is in set Zq, False if not
        """
        response = share_dic.get('proof', {}).get('response')

        res = number.is_within_set_zq(response)
        if not res:
            print("response error. ")

        return res

    @staticmethod
    def __check_pad(share_dic: dict) -> bool:
        """
        check if the given ai/pad of a share is in set Zrp
        :param share_dic: a dictionary of a share
        :return: True if this value is in set Zrp, False if not
        """
        pad = share_dic.get('proof', {}).get('pad')
        res = number.is_within_set_zrp(pad)
        if not res:
            print("a/pad value error. ")

        return res

    @staticmethod
    def __check_data(share_dic: dict) -> bool:
        """
        check if the given bi/data of a share is in set Zrp
        :param share_dic: a dictionary of a share
        :return: True if this value is in set Zrp, False if not
        """
        data = share_dic.get('proof', {}).get('data')
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

    # TODO: add semantic meaning
    def __check_equation1(self, response: int, pad: int, challenge: int, public_key: int) -> bool:
        """
        check if equation g ^ vi = ai * (Ki ^ ci) mod p is satisfied
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

    # TODO: add semantic meaning
    def __check_equation2(self, response: int, data: int, challenge: int, partial_decrypt: int) -> bool:
        """
        check if equation A ^ vi = bi * (M i^ ci) mod p is satisfied
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
