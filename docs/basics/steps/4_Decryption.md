# Decryption

At the conclusion of voting, all of the cast ballots are published in their encrypted form in the election record together with the proofs that the ballots are well-formed. Additionally, all of the encryptions of each option are homomorphically-combined to form an encryption of the total number of times that each option was selected. The homomorphically-combined encryptions are decrypted to generate the election tally. Individual cast ballots are not decrypted. Individual spoiled ballots are decrypted and the plaintext values are published along with the encrypted representations and the proofs.

In order to decrypt the homomorphically-combined encryption of each selection, each Guardian participating in the decryption must compute a specific Decryption Share of the decryption. It is preferable that all guardians be present for decryption, however in the event that guardians cannot be present, Electionguard includes a mechanism to decrypt with the Quorum of Guardians.

![Encrypt][encrypt-image]

<!-- Links -->
[encrypt-image]: ../../images/undraw/guardian_1.svg "Image of an ElectionGuard guardian"

During the Key Ceremony a Quorum of Guardians is defined that represents the minimum number of guardians that must be present to decrypt the election. If the decryption is to proceed with a Quorum of Guardians greater than or equal to the Quorum count, but less than the total number of guardians, then a subset of the Available Guardians must also each construct a Partial Decryption Share for the missing Missing Guardian, in addition to providing their own Decryption Share.

It is important to note that mathematically not every present guardian has to compute a Partial Decryption Share for every Missing Guardian. Only the Quorum Count of guardians are necessary to construct Partial Decryption Shares in order to compensate for any Missing Guardian.


![Encrypt][encrypt-image]

<!-- Links -->
[encrypt-image]: ../../images/undraw/guardian_2.svg "Image of an ElectionGuard guardian"

In this implementation, ElectionGuard takes an approach that utilizes all Available Guardians to compensate for Missing Guardians. When it is determined that guardians are missing, all available guardians each calculate a Partial Decryption Share for the missing guardian and publish the result. A Quorum of Guardians count of available Partial Decryption Shares is randomly selected from the pool of available partial decryption shares for a givenMissing Guardian. If more than one guardian is missing, we randomly choose to ignore the Partial Decryption Share provided by one of the Available Guardians whose partial decryption share was chosen for the previous Missing Guardian, and randomly select again from the pool of available Partial Decryption Shares. This ensures that all available guardians have the opportunity to participate in compensating for Missing Guardians.
