# ElectionGuard Structure

In an election, a set of *guardians* is enlisted to serve as trustees who manage cryptographic keys.
The members of a canvassing board can serve as guardians. 
Prior to the commencement of voting or auditing, the guardians work together to form a public encryption key that will be used to encrypt individual ballots.

After the conclusion of voting or auditing, a *quorum* of guardians is necessary to produce the artifacts required to enable public verification of the tally.

## Key Generation

Prior to the start of voting (for an E2E-verifiable election) or auditing (for an RLA), the election guardians participate in a process wherein they generate public keys to be used in the election.
Each guardian generates an election key – for use in encrypting votes – and an auxiliary key – for use in encrypting other data.<sup id="footnotelink1">[1](#footnote1)</sup> 
Additional keys are generated to facilitate sharing of private keys so that the election verifiable data can be produced after voting or auditing is complete – even if not all guardians are available at that time.

The key generation ceremony begins with each guardian publishing its public keys together with proofs of knowledge of the associated private keys. 
Once all of the public keys are published, each guardian uses each other guardian’s public auxiliary key to encrypt shares of its own private keys. 
Finally, each guardian decrypts the shares it receives from other guardians and checks them for consistency. 
If the received shares verify, the receiving guardian announces its completion. 
If any shares fail to verify, the receiving guardian challenges the sender.
In this case, the sender is obliged to reveal the shares it sent. 
If it does so and the shares verify, the ceremony concludes and the election proceeds.
If a challenged guardian fails to produce key shares that verify, that guardian is removed and the key generation ceremony restarts with a replacement guardian.

## Ballot Encryption

In most uses, the election system makes a single call to the *ElectionGuard* API after each voter completes the process of making selections or with each ballot to be encrypted for an RLA.
*ElectionGuard* will encrypt the selections made by the voter and return a verification code which the system should give to the voter.<sup id="footnotelink2">[2](#footnote2)</sup>

This is the only point where an existing election system must interface with *ElectionGuard*. 
In certain vote-by-mail scenarios and when *ElectionGuard* is used within an RLA, cast-vote records can be provided in batch without any interface between the voting equipment and *ElectionGuard*. 
There is no need to provide verification codes in the RLA scenario.

The encrypted ballots are published along with non-interactive zero-knowledge proof of their integrity.
The encrypted method used herein has a homomorphic property which allows the encrypted ballots to be combined into a single aggregate ballot which consists of encryptions of the election tallies.

## Verifiable Decryption

In the final step, election guardians independently use their secret keys to decrypt the election tallies and associated verification data. 
It is not necessary for all guardians to be available to complete this step.
If some guardians are missing, a quorum of guardians can use the previously shared key fragments to reconstruct the missing verification data.

Observers can use this open specification and/or accompanying materials to write *election verifiers* that can confirm the integrity of each encrypted ballot, the correct aggregation of these ballots, and the accurate decryption of election tallies.

The details of the ElectionGuard Application Programming Interface (API) are included in a separate document.
The principal purposes of this document are to specify the functionality of the ElectionGuard toolkit and to provide details necessary for independent parties to write election verifiers that consume the artifacts produced by the toolkit.

---

<small><b id="footnote1">1</b>. While the format of the election keys is critical to the process and carefully delineated in this document, the auxiliary keys are for internal use only and their format is left up to individual implementations. 
[↩](#footnotelink1)</small>

<small><b id="footnote2">2</b>. The verification code is not necessary for RLA usage.[↩](#footnotelink2)</small>