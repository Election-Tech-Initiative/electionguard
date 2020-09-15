from decryption_verifier import DecryptionVerifier
from generator import FilePathGenerator, ParameterGenerator, VoteLimitCounter
from baseline_verifier import BaselineVerifier
from key_generation_verifier import KeyGenerationVerifier
from encryption_verifier import AllBallotsVerifier

if __name__ == '__main__':
    # set up
    path_g = FilePathGenerator()
    param_g = ParameterGenerator(path_g)
    vlc = VoteLimitCounter(param_g)
    print("set up finished. ")

    # baseline parameter check
    print(" ------------ [box 1] baseline parameter check ------------")
    blv = BaselineVerifier(param_g)
    blv.verify_all_params()
    print()

    # key generation check
    print(" ------------ [box 2] key generation parameter check ------------")
    kgv = KeyGenerationVerifier(param_g, path_g)
    kgv.verify_all_guardians()
    print()

    # all ballot check
    print(" ------------ [box 3, 4, 5] ballot encryption check ------------")
    abv = AllBallotsVerifier(param_g, path_g, vlc)
    abv.verify_all_ballots()
    print()

    # tally and spoiled ballot check
    print(" ------------ [box 6, 9] cast ballot tally check ------------")
    dv = DecryptionVerifier(path_g, param_g)
    dv.verify_cast_ballot_tallies()
    print()
    print(" ------------ [box 10] spoiled ballot check ------------")
    dv.verify_all_spoiled_ballots()