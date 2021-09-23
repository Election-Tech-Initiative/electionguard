# Key Ceremony

The ElectionGuard Key Ceremony is the process used by Election Officials to share encryption keys for an election. Before an election, a fixed number of Guardians are selection to hold the private keys needed to decrypt the election results. A Quorum count of Guardians can also be specified to compensate for guardians who may be missing at the time of Decryption. For instance, 5 Guardians may be selected to hold the keys, but only 3 of them are required to decrypt the election results.

Guardians are typically Election Officials, Trustees Canvass Board Members, Government Officials or other trusted authorities who are responsible and accountable for conducting the election.

## Summary

The Key Ceremony is broken into several high-level steps. Each Guardian must announce their attendance in the key ceremony, generate their own public-private key pairs, and then share those key pairs with the Quorum. Then the data that is shared is mathematically verified using Non-Interactive Zero Knowledge Proofs, and finally a joint public key is created to encrypt ballots in the election.

### Attendance

Guardians exchange all public keys and ensure each fellow guardian has received an election and auxiliary public key ensuring at all guardians are in attendance.

### Key Sharing

Guardians generate a partial key backup for each guardian and share with that designated key with that guardian. Then each designated guardian sends a verification back to the sender. The sender then publishes to the group when all verifications are received.

### Joint Key

The final step is to publish the joint election key after all keys and backups have been shared.

![Guardian](../../images/undraw/guardian_1.svg)