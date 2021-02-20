# The Election Record

The record of an election should be a full accounting of all of the election artifacts.  Specifically, it should contain the following:

* Date and location of an election
* The [election manifest](../../Glossary.md#election-manifest) (also see [The Election Manifest](../../guide/Election_Manifest.md) article)
* The baseline parameters
  * Primes $p$ and $q$ and integer $r$ such that $p=qr+1$ and $r$ is not a multiple of $q$
  * A generator $g$ of the order $q$ multiplicative subgroup $Z_p^*$
  * The number $n$ of election guardians
  * The quorum threshold $k$ of guardians required to complete verification
* The [base hash value](../../Glossary.md#base-hash-q) $Q$ computed from the above
* The commitments from each election guardian to each of their polynomial coefficients
* The proofs from each guardian of possession of each of the associated coefficients
* The election public key
* The extended base hash value $\bar{Q}$ computed from the above
* Every encrypted ballot prepared in the election (whether cast or spoiled)
* All of the encrypted options on each ballot (including “placeholder” options)
  * The proofs that each such value is an encryption of either zero or one
  * The selection limit for each contest
  * The proof that the number of selections made matches the selection limit
  * The device information for the device that encrypted the ballot
  * The date and time of the ballot encryption
  * The tracker code produced for the ballot
* The decryption of each spoiled ballot
  * The selections made on the ballot
  * The cleartext representation of the selections
  * Partial decryptions by each guardian of each option
  * Proofs of each partial decryption
  * Shares of each missing partial decryption (if any)
  * Proofs of shares of each missing partial decryption (if any)
  * Lagrange coefficients used for replacement of any missing partial decryptions (if any)
* Tallies of each option in an election
  * The encrypted tally of each option
  * Full decryptions of each encrypted tally
  * Cleartext representations of each tally
  * Partial decryptions by each guardian of each tally
  * Proofs of partial decryption of each tally
  * Shares of each missing partial decryption (if any)
  * Proofs of shares of each missing partial decryption (if any)
  * Lagrange coefficients used for replacement of any missing partial decryptions (if any)
* Ordered lists of the ballots encrypted by each device

An election record should be digitally signed by election administrators together with the date of the signature.  The entire election record and its digital signature should be published and made available for full download by any interested individuals.  Tools should also be provided for easy look up of tracking codes by voters.





