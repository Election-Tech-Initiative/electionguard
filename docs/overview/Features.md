# Features

This serves as a list of features included within the ElectionGuard reference implementations.

## 🛡 End-to-End Verifiability

ElectionGuard uses end-to-end verifiable election techniques to enable individual voters to check crucial ingredients
of election results.

## 🔐 Ballot Encryption 

Ballot encryption uses ElGamal encryption to securely encrypt a voter's plaintext ballot. These ballots are then homomorphically added to maintain encryption while creating an aggregate ballot or tally. 

## ✅ Ballot Confirmation

Ballot confirmation allows voters to confirm their ballots were counted. Encrypted ballots provide a ballot code that can be used to verify a vote was submitted and whether it was cast or spoiled.

## 📝 Challenge Ballots

To allow for challenging the system, a spoiled ballot can be submitted for decryption along with the tally. Post election, this allows a voter to both confirm their ballot was not included in the tally and view the plaintext decryption of said ballot.

## 🤏 Compact Ballots

Compact ballots assist with smaller machines and ballot encryption by providing a compact format for ballots. This format can be expanded to include all verifiable proofs.  

## 🔑 Key Ceremony

The key ceremony is provided as a toolset to be perform a ceremony between multiple guardians to generate an encryption key. This key can then be used to encrypt the ballots.

## 🔓 Tally Ceremony

The tally ceremony is provided as a toolset to perform a ceremony between multiple guardians to decrypt the tally or election results from an election. This includes quorum decryption when guardians from the key ceremony may be missing.
