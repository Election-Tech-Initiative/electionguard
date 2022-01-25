# Precinct Scan

!!! warning "Work in Progress"
    This is a work in progress. Feel free to contribute.

## Overview

By design, the ElectionGuard SDK can be used to enable end-to-end verifiability (e2e-v) in a variety of use cases. This article discusses the "default" use case of ElectionGuard: an end-to-end verifiable election that uses precinct scanners where ballots are inserted (and approved) by voters directly [^precinct-scan].

This document aims to provide a "[vertical slice][vertical-slices-and-scale]" of the considerations and practices necessary to add end-to-end verifiability to an existing precinct scanner. We necessarily make assumptions about the compute and storage capabilities of the scanner itself, and the modifications necessary to implement [end-to-end verifiability][verifiable-election]. In so doing, it illustrates the interlocking system of security and encryption that comprises an e2e-v _system_.

!!! info
    ElectionGuard relies on slight adaptations of existing voting processes to accommodate different aspects of [end-to-end verifiability][verifiable-election].

For example, many voting jurisdictions already have a procedure called _ballot spoiling_ to handle mistakes voters make when they fill out ballots. A voter may inadvertently fill out a contest incorrectly by selecting more candidates than allowed. When the voter then proceeds to scan the ballot, the scanner stops the ballot and alerts the voter of the _overvote_; the voter then has the opportunity, as allowed within the voting regulations and practices of the voting district, to start over with a new ballot; the ballot with the mistake is then _spoiled_ and stored separately to ensure it is not included in the tabulation.

ElectionGuard uses this spoil process to enable a voter to test the integrity of the system capturing their vote. Effectively, the voter acts as if they are going to vote, submitting their ballot into the scanner and enabling it to process and interpret the ballot. After the encryption of the ballot has occurred, and the verification code has been generated, the voter can decide NOT to cast this ballot via some kind of option on the summary screen presented by the scanner.

End-to-end verifiability mandates that these _challenged ballots_, unlike _cast ballots_, be published separately from the tally, and in addition that they be decrypted and published in their decrypted state. When voters use their verification code to look up the provenance of these challenged ballots after the election record have been published, they will be able to see both that the ballot they challenged was NOT included in the tally, and also what its contents would have been if it were.

When the contents of a challenged ballot are revealed to the voter and the selections match, their confidence about the provenance of their cast ballot is ideally bolstered. If the contents do not match their expectation, they should be given the means to flag this situation to election administrators to investigate.

Thus, challenge ballots serve the dual role of affording voters the opportunity to more meaningfully evaluate the disposition of their voting preferences while also providing a security check on the voting system itself. Because the system has to be prepared for ANY voter to challenge a ballot, and because that challenge occurs AFTER the ElectionGuard encryption has occurred, the scanner has already committed its choice to ElectionGuard. And since the scanner can only encrypt ballots (only the tally process overseen by a quorum of election guardians has the "power" to decrypt _anything_), the system is forced to act in good faith (if a small and random minority of voters can be relied upon to exercise challenges).

This document illustrates these e2e-v concepts in the context of setting up and running an election. It begins with a general discussion of the precinct scan user experience and technical assumptions of scanner capabilities, and then runs an election, outlining where ElectionGuard needs to be integrated and ideally providing any wider security and integrity context for any process alterations that may obtain relative to current general election practice.

## Current Precinct Scan Voter Experience

A typical voter flow for a precinct scan system is illustrated below.

After a voter has acquired their ballot, they fill it out by hand or using a ballot marking device. When they finish they proceed to the scanner and insert the completed ballot. The scanner scans and interprets the ballot and generates a [cast vote record][cast-vote-record], an electronic representation of the voter's selections.

If all contests in a ballot are filled out properly and interpreted as such by the scanner, the ballot is accepted and the voter is free to leave the voting booth.

If the scanner interprets the voter has voted for more options than the ballot contests allow (called an _overvote_), the scanner stops the ballot from being deposited into the ballot box and prompts the voter whether they would like to have the ballot returned to fix the discrepancy. If the voter agrees, a poll worker is alerted and the ballot remediated by whatever process obtains, which could involve issuance of a new ballot and "spoiling" of the overvoted ballot.

The scanner can also determine whether the voter didn't fill out all the contests available (called an _undervote_). The scanner can be programmed to follow the same process as an overvote (returning the ballot for remediation), but election administrators often assume the undervote is intentional by the voter.

## Adapting Precinct Scan for End-to-end Verifiability (E2E-V)

### Voter Experience

As outlined in the Verifiable Election page of the ElectionGuard SDK [^e2e-v], for end-to-end verifiability to apply, the precinct scanner itself must provide the following capabilities for each voter:

- immediately upon scanning the ballot, create an encrypted version of the ballot using the public key generated by the election guardians (see Key Ceremony)
- present the verification code generated by the encryption to the voter (ideally in paper format)
- present the means for the voter to cast or challenge (spoil) the ballot

### Technical Requirements

For end-to-end verifiability, the scanner has to implement the user experience described above as well as generate and _finalize_ an encrypted ballot reflecting the voter's selections. ElectionGuard assumes all other e2e-v functions such as key and tally ceremonies are performed independently of the scanner on modern laptop or desktop computers or secure cloud environments.

## Technical Implementation

### Overview and Operational Assumptions

Precinct scanners, unlike other components of voting systems, are assumed to follow the economics and performance characteristics of embedded devices rather than consumer off-the-shelf (COTS) devices such as laptops. ElectionGuard assumes these devices operate in storage-limited environments more akin to operating systems such as Raspberry Pi than Windows 10. Information transfer (if not base storage) is assumed to occur via USB drives with capacities designed for space-efficient data constructs, not 4096-bit encryptions.

To support operation in these environments, ElectionGuard enables an encryption-only library built in C++ from which it can target different standalone package deployments that generate encrypted ballots using a separately-provided public election key.

Because encrypted ballots in modern elections can each occupy up to 1MB or more of device storage, ElectionGuard also specifies a _dehydration_ "process" that allows a more space-efficient format for local storage and transmission post-election. Prior to initiating the tally and publishing process, these ballots are transferred to an external system and reconsitituted (and validated) by re-executing the encryption process using the dehydrated data as inputs. (See the discussions around ballot construction, chaining, etc., below to understand how dehydration should not affect system integrity or end-to-end verifiability.)

### General Election Setup

Elections can be considered to have three core "states": the election itself, where voters cast their ballots, but also election setup and post-election data collection and tally publishing. ElectionGuard necessarily manifests in each state.

Election setup generally consists of preparing the voting machines for the current election contests, running any pre-production testing, and final configuration for election readiness.

For ElectionGuard, the [public election key]() generated by the election guardians is deployed to the scanner at this time and, if necessary, the ElectionGuard executable (the scanner is assumed to be entirely offline and code and election-related data is transferred via USB storage devices). Poll workers should also be prompted to manually enter an election launch code (see below) generated uniquely for the current election at election instantiation.

In modern US elections, voters often vote multiple contests, determined by the type of election they're voting in and where they live. Because of the diversity of contests that different voters are eligible to vote in [even within a single county or precinct (imagine school districts, utility districts, city councillors, etc.)], a single precinct scanner may need to recognize and interpret tens or even hundreds of different _ballot styles_ in a single election.

#### Ballot manifest

Consider a [ballot manifest][ballot-manifest] the master list of all the contests voters could face in a single election. [ElectionGuard assumes and validates the ballot manifest for a variety of criteria][ballot-manifest-data-validation]. ElectionGuard uses manifests to properly interpret ballots generally, but for records created by precinct scanners the manifest provides the means to _reconstitute_ the encrypted ballots from the dehydrated records created.

Strictly speaking, the ballot manifest isn't necessary for ElectionGuard until the tally process evaluates the encrypted ballots generated during the election, but the precinct scanner needs to encode ballots and votes properly for their downstream construction, and that is dependent on the unique ballot styles presented to voters, which themselves need to follow proper convention as well.

#### Public encryption key

One of the core innovations of ElectionGuard is the use of multiple election guardians to administer the creation of the election record. Guardians are intended to be independent, trustworthy individuals. They don't need to have technical skills, but they do need to physically perform tasks collectively with the other guardians at the beginning and end of elections.

As part of the election setup process, or any time prior, the guardians meet to create the public key that will be used by the precinct scanner to encrypt voter ballots. The

#### Logic and Accuracy Testing

#### Scanner Final Production Setup

##### Launch Code

### Scanner Election Operation

#### Ballot Encryption

##### Generation of Verification Code

##### Ballot Chaining

##### Ballot **_Dehydration_**

###### Dehydrated ballot structure

A dehydrated ballot **_must_** provide the following data to be properly _rehydrated_ and preserve end-to-end verifiability.

| Label                         | Type    | Description                                                                                                                | Notes                                                                                                                                                         |
| ----------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ballot_object_id              | string  | Unique ID to identify each ballot in an election                                                                           |                                                                                                                                                               |
| session_id                    | string  | Unique ID to enable the correct sorting of the election ballot chain when rehydrated                                       | needs to be resilient across device restarts and other service interruptions                                                                                  |
| launch_code                   | integer | 10-digit ID generated at election initiation by rolling of 10-sided dice                                                   | used to protect against attacks to insert votes outside of election context. See [insert reference here](link to reference)                                   |
| ballot_style_id               | string  | Uniquely identifies the set of contests and responses a voter encounters with their ballot                                 | Used as part of the rehydration and tally processes to ensure the ballot is correctly interpreted and reconstituted                                           |
| ballot_finalization_indicator | flag    | Indicates whether ballot is CAST or CHALLENGED                                                                             | applied by scanner based on determination by voter                                                                                                            |
| ballot_selections             | array   | Set of responses (and, as applicable, non-responses) of voter to ballot style                                              | reflective of non-selections; critical for rehydration and re-establishment of ballot encryption artifacts                                                    |
| ballot_extra_data             | array   | Additional data applied at contest level to capture non-selection data                                                     | Principally envisioned for capturing ballot selection metadata for write-ins; each entry needs to identify contest and selection as well as extra data string |
| ballot_nonce                  | ?       | The [nonce][nist-nonce] used as input to the encryption of the ballot selections            | See spec on [Ballot Encryption][ballot-encryption]                                                              |
| previous_tracker_hash         | ?       | As discussed in [ballot chaining](#ballot-chaining) the previous_tracker_hash is an input to the current ballot encryption | See spec on [Ballot Encryption][ballot-encryption]                                     |
| verification_code_hash        | ?       | Hashed version of verification code generated by ballot encryption process                                                 |                                                                                                                                                               |

### Ballot _Finalization_

#### Cast ballots

#### Challenge ballots

[^precinct-scan]: As distinct from scanners used solely for central tabulation, which occurs with mail-in voting or any tabulation / aggregation scenario _where voters are not present when the cast vote record is created_
[^e2e-v]: [ElectionGuard Verifiable Election][verifiable-election] [https://www.electionguard.vote/guide/Verifiable_Election/]

<!-- Links -->
[vertical-slices-and-scale]: https://agileforall.com/vertical-slices-and-scale/
[verifiable-election]: https://www.electionguard.vote/guide/Verifiable_Election/
[ballot-manifest]: https://www.electionguard.vote/guide/Election_Manifest/
[ballot-manifest-data-validation]: https://www.electionguard.vote/guide/Election_Manifest/#data-validation
[nist-nonce]: https://csrc.nist.gov/glossary/term/nonce
[ballot-encryption]: ../../spec/web/6_Ballot_Encryption/

[cast-vote-record]: ../overview/Glossary.md#cast-vote-record
