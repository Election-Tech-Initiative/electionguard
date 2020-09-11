from .generator import ParameterGenerator, VoteLimitCounter


class IVerifier:
    """
    This represents an abstract class of a verifier, all concrete verifier extends from this class,
    defines all the parameters including generator, extended hash, elgamal public key, large prime p,
    and small prime q
    """
    def __init__(self, param_g: ParameterGenerator):
        """
        initializer
        :param param_g: a parameter generator memorizing the path to files
        """
        self.param_g = param_g
        self.generator = self.param_g.get_generator()
        self.extended_hash = self.param_g.get_extended_hash()
        self.public_key = self.param_g.get_elgamal_key()
        self.large_prime = self.param_g.get_large_prime()
        self.small_prime = self.param_g.get_small_prime()

    @staticmethod
    def set_error() -> bool:
        """
        always sets error to True, used when error occurs
        :return: True
        """
        return True

    @staticmethod
    def initialize_error() -> bool:
        """
        always initiate error to False at the beginning of verification
        :return: False
        """
        return False


class IBallotVerifier(IVerifier):

    def __init__(self, param_g: ParameterGenerator, limit_counter: VoteLimitCounter):
        super().__init__(param_g)
        self.limit_counter = limit_counter


class IContestVerifier(IVerifier):
    """
    Contest verifier as an interface, will be implemented in every contest-level verifier,
    including BallotContestVerifier and DecryptionContestVerifier
    """
    def verify_a_contest(self) -> bool:
        pass


class ISelectionVerifier(IVerifier):
    """
    Selection verifier as an interface, will be implemented in every selection-level verifier,
    including BallotSelectionVerifier and DecryptionContestVerifier
    """
    def get_pad(self) -> int:
        pass

    def get_data(self) -> int:
        pass
