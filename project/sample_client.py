from project.decryption_verifier import DecryptionVerifier
from project.generator import FilePathGenerator, ParameterGenerator, VoteLimitCounter
from project.baseline_verifier import BaselineVerifier
from project.key_generation_verifier import KeyGenerationVerifier
from project.encryption_verifier import AllBallotsVerifier

if __name__ == '__main__':
    # set up
    path_g = FilePathGenerator()
    param_g = ParameterGenerator(path_g)
    vlc = VoteLimitCounter(param_g)

    # baseline parameter check
    blv = BaselineVerifier(param_g)
    blv.verify_all_params()

    # key generation check
    kgv = KeyGenerationVerifier(param_g, path_g)
    kgv.verify_all_guardians()

    # all ballot check
    abv = AllBallotsVerifier(param_g, path_g, vlc)
    abv.verify_all_ballots()

    # tally and spoiled ballot check
    dv = DecryptionVerifier(path_g, param_g)
    dv.verify_cast_ballot_tallies()
