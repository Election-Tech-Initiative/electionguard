# ElectionGuard Specification ![Version 0.95.0](https://img.shields.io/badge/Version-v1.0.0-yellow)

Josh Benaloh (Microsoft Research)

## Overview

This document describes the technical details of the ElectionGuard toolkit which can be used in conjunction with many new and existing voting systems to enable both end-to-end (E2E) verifiability and privacy-enhanced risk-limiting audits (RLAs). ElectionGuard is not a complete election system. It instead provides components that are designed to be flexible and to promote innovation by election officials and system developers. When properly used, it can promote voter confidence by empowering voters to independently verify the accuracy of election results.

### End-to-end (E2E) verifiability

An E2E-verifiable election provides artifacts which allow voters to confirm that their votes have been accurately recorded and counted. Specifically, an election is End-to-end (E2E) verifiable if two properties are achieved.

1. Individual voters can verify that their votes have been accurately recorded.
2. Voters and observers can verify that all the recorded votes have been accurately counted.

An E2E-verifiable tally can be used as the primary tally in an election or as a verifiable secondary tally alongside traditional methods. ElectionGuard is compatible with in-person voting – either using an electronic ballot-marking device or an optical scanner capable of reading hand-marked or machine-marked ballots, with voting by mail, and even with Internet voting.

### Risk-limiting audits (RLAs)

RLAs offer election administrators efficient methods to validate reported election tallies against physical ballot records. There are several varieties of RLAs, but the most efficient and practical are ballot-comparison audits in which electronic cast-vote records (CVRs) are individually compared against physical ballots.

The challenge with ballot-comparison audits is that public release of the full set of CVRs can compromise voter privacy while an audit without public disclosure of CVRs offers no basis for public confidence in the outcome. ElectionGuard can bridge this gap by enabling public disclosure of encrypted ballots that can matched directly to physical ballots selected for auditing and can also be proven to match the reported tallies.

### About this specification

This specification can be used by expert reviewers to evaluate the details of the ElectionGuard process and by independent parties to write ElectionGuard verifiers to confirm the consistency of election artifacts with announced election results. The details of the ElectionGuard Application Programming Interface (API) are provided in a separate document.

## ElectionGuard Structure

In an election, a set of guardians is enlisted to serve as trustees who manage cryptographic
keys. The members of a canvassing board can serve as guardians. Prior to the commencement of voting or auditing, the guardians work together to form a public encryption key that will be used to encrypt individual ballots.

After the conclusion of voting or auditing, a quorum of guardians is necessary to produce the artifacts required to enable public verification of the tally.

### Key Generation

Prior to the start of voting (for an E2E-verifiable election) or auditing (for an RLA), the election guardians participate in a process wherein they generate public keys to be used in the election. Each guardian generates an election key – for use in encrypting votes – and an auxiliary key – for use in encrypting other data.[^1] Additional keys are generated to facilitate sharing of private keys so that the election verifiable data can be produced after voting or auditing is complete – even if not all guardians are available at that time.

The key generation ceremony begins with each guardian publishing its public keys together with proofs of knowledge of the associated private keys. Once all of the public keys are published, each guardian uses each other guardian’s public auxiliary key to encrypt shares of its own private keys. Finally, each guardian decrypts the shares it receives from other guardians and checks them for consistency. If the received shares verify, the receiving guardian announces its completion. If any shares fail to verify, the receiving guardian challenges the sender. In this case, the sender is obliged to reveal the shares it sent. If it does so and the shares verify, the ceremony concludes and the election proceeds. If a challenged guardian fails to produce key shares that verify, that guardian is removed and the key generation ceremony restarts with a replacement guardian.

### Ballot Encryption

In most uses, the election system makes a single call to the ElectionGuard API after each voter completes the process of making selections or with each ballot to be encrypted for an RLA. ElectionGuard will encrypt the selections made by the voter and return a verification code which the system should give to the voter. [^2]

This is the only point where an existing election system must interface with ElectionGuard. In certain vote-by-mail scenarios and when ElectionGuard is used within an RLA, cast-vote records can be provided in batch without any interface between the voting equipment and ElectionGuard. There is no need to provide verification codes in the RLA scenario.

The encrypted ballots are published along with non-interactive zero-knowledge proof of their integrity. The encrypted method used herein has a homomorphic property which allows the encrypted ballots to be combined into a single aggregate ballot which consists of encryptions of the election tallies.

### Verifiable Decryption

In the final step, election guardians independently use their secret keys to decrypt the election tallies and associated verification data. It is not necessary for all guardians to be available to complete this step. If some guardians are missing, a quorum of guardians can use the previously shared key fragments to reconstruct the missing verification data.

Observers can use this open specification and/or accompanying materials to write election verifiers that can confirm the integrity of each encrypted ballot, the correct aggregation of these ballots, and the accurate decryption of election tallies.

The details of the ElectionGuard Application Programming Interface (API) are included in a separate document. The principal purposes of this document are to specify the functionality of the ElectionGuard toolkit and to provide details necessary for independent parties to write election verifiers that consume the artifacts produced by the toolkit.

[^1]: While the format of the election keys is critical to the process and carefully delineated in this document, the auxiliary keys are for internal use only and their format is left up to individual implementations.
[^2]: The verification code is not necessary for RLA usage.
