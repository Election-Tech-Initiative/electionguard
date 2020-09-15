from generator import ParameterGenerator, VoteLimitCounter


class IVerifier:
    """
    This represents an abstract class of a verifier, all concrete verifier extends from this class,
    defines all the parameters including generator, extended hash, elgamal public key, large prime p,
    and small prime q

    Concrete classes:
        BaselineVerifier
        KeyGeneratorVerifier
        AllBallotsVerifier
        BallotEncryptionVerifier
        BallotContestVerifier
        BallotSelectionVerifier
        DecryptionVerifier
        DecryptionContestVerifier
        DecryptionSelectionVerifier
        ShareVerifier
    """

    def __init__(self, param_g: ParameterGenerator):

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
    """
    Sample ballot verifier abstract class that all ballot-level verifiers extend from,
    provides an initializer sample

    Concrete class:
        AllBallotsVerifier
        BallotEncryptionVerifier
        DecryptionVerifier
    """

    def __init__(self, param_g: ParameterGenerator, limit_counter: VoteLimitCounter):
        super().__init__(param_g)
        self.limit_counter = limit_counter


class IContestVerifier(IVerifier):
    """
    Contest verifier abstract class that all  will be implemented in every contest-level verifier.

    Concrete class:
        BallotContestVerifier
        DecryptionContestVerifier
    """
    def verify_a_contest(self) -> bool:
        pass


class ISelectionVerifier(IVerifier):
    """
    Selection verifier as an interface, will be implemented in every selection-level verifier.

    Concrete class:
        BallotSelectionVerifier
        DecryptionSelectionVerifier
    """
    def get_pad(self) -> int:
        pass

    def get_data(self) -> int:
        pass
