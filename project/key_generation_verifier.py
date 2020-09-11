from project import json_parser, number
from project.generator import ParameterGenerator, FilePathGenerator
from project.interfaces import IVerifier


class KeyGenerationVerifier(IVerifier):
    """
    This class checks the key generation information are given correctly for each guardian. (box 2)
    """

    def __init__(self, param_g: ParameterGenerator, path_g: FilePathGenerator):
        super().__init__(param_g)
        self.path_g = path_g
        self.num_of_guardians = param_g.get_num_of_guardians()
        self.quorum = param_g.get_quorum()
        self.base_hash = param_g.get_base_hash()

    def verify_all_guardians(self) -> bool:
        """
        verify all guardians' key generation info by examining challenge values and equations
        :return: True if no error were found in any guardian, False if some errors found in some or all guardians
        """
        error = self.initialize_error()

        for i in range(self.num_of_guardians):
            res = self.verify_one_guardian(i)
            if not res:
                error = self.set_error()
                print("guardian {index} key generation verification failure. ".format(index=i))

        if not error:
            print("All guardians' key generation verification success. ")

        return not error

    def verify_one_guardian(self, index: int) -> bool:
        """
        verify one guardian's key generation
        :param index:  index of this guardian, (0 - number of guardians)
        :return: True if the guardian's key information gets verified, False if not
        """
        coefficients_dic = self.__get_guardian_coeff_by_index(index)

        error = self.initialize_error()

        # loop through every proof
        for i in range(self.quorum):
            error = self.initialize_error()
            # get given values
            coeff_proofs_dic = coefficients_dic.get('coefficient_proofs')[i]
            response = coeff_proofs_dic.get('response')      # u
            commitment = coeff_proofs_dic.get('commitment')  # h
            public_key = coeff_proofs_dic.get('public_key')  # k
            challenge = coeff_proofs_dic.get('challenge')    # c

            # compute challenge
            challenge_computed = self.__compute_guardian_challenge_threshold_separated(public_key, commitment)

            # check if the computed challenge value matches the given
            if not number.equals(challenge, challenge_computed):
                error = self.set_error()
                print("guardian {i}, quorum {j}, challenge number error. ".format(i=index, j=i))
            # check equation
            if not self.__verify_individual_key_computation(response, commitment, public_key, challenge):
                error = self.set_error()
                print("guardian {i}, quorum {j}, equation error. ".format(i=index, j=i))

        return not error

    def __get_guardian_coeff_by_index(self, index: int) -> dict:
        """
        verify the key information of guardian at a index position
        :param index: index of this guardian, (0 - number of guardians)
        :return: the corresponding key info stored in a dictionary
        """
        if index >= self.num_of_guardians or index < 0:
            raise IndexError("index out of bound")
        coeff_file_path = self.path_g.get_guardian_coefficient_file_path(index)
        return json_parser.read_json_file(coeff_file_path)

    def __compute_guardian_challenge_threshold_separated(self, public_key: int, commitment: int) -> int:
        """
        computes challenge (c_ij) with hash, H(cij = H(base hash, public key, commitment) % q, each guardian has
        quorum number of these challenges
        :param public_key: public key, under each guardian, previously listed as k
        :param commitment: commitment, under each guardian, previously listed as h
        :return: a challenge value of a guardian, separated by quorum
        """
        return number.mod_p(number.hash_elems(self.base_hash, public_key, commitment))

    def __verify_individual_key_computation(self, response: str, commitment: str, public_key: str, challenge: str) -> bool:
        """
        check the equation generator ^ response mod p = (commitment * public key ^ challenge) mod p
        :param response: response given by a guardian, ui,j
        :param commitment: commitment given by a guardian, hi,j
        :param public_key: public key of a guardian, Ki,j
        :param challenge: challenge of a guardian, ci,j
        :return: True if both sides of the equations are equal, False otherwise
        """
        response = int(response)
        commitment = int(commitment)
        public_key = int(public_key)
        challenge = int(challenge)

        left = pow(self.generator, response, self.large_prime)
        right = number.mod_p(commitment * pow(public_key, challenge, self.large_prime))

        return number.equals(left, right)
