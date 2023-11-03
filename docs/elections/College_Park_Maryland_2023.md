![ElectionGuard College Park Banner][College-Park-Banner]
# ElectionGuard in the November 2023 College Park General Election

This November will see College Park use the Hart VerityScan scanner with ElectionGuard in a similar configuration to what was used in the [Preston Idaho election in 2022](Preston_Idaho_2022.md). This year, voters will fill out ballots either by hand or using Hart's [Verity TouchWriter](https://www.youtube.com/watch?v=_GA0kzJrM-s). The official tally will be conducted with the Hart system, which will include mail-in ballots scanned with the VerityScan scanner but, because the voters were not present to collect the confirmation code receipt, will not be able to verify that their ballots were included.

!!! info "Vote by mail is a feature of the [ElectionGuard 2.0 Specification](/spec/#v20)"

## New Capabilities

While the core Hart system and voting process will be identical to [the system used in Preston, Idaho](/docs/elections/Preston_Idaho_2022.md) the ElectionGuard software will be *almost* (see below) a full [implementation of the 2.0 specification](/docs/spec/index.md). It incorporates most of the new encryption structures, including a new implementation of guardian architecture and elimination of placeholder votes.  A fully new version of the admin and guardian software used to run the key and tally ceremonies has also been developed.

The biggest new capability is a full implementation of thresholding. Thresholding enables a quorum of guardians to participate in a tally ceremony rather than requiring all guardians to be present. (College Park will be using 5 guardians with a quorum of 3 to be present to run the tally ceremony.) Each guardian and the ElectionGuard administrator will be assigned their own Surface Go tablet to run the ceremonies and will use Windows Hello to authenticate on their assigned device.

## Ballot Confirmation

Voters will be able to confirm that their votes were counted using Enhanced Voting's [Confirmation Code lookup website](https://app.enhancedvoting.com/results/public/cc/CollegePark/nov23), as happened in Preston. The ElectionGuard election record will be hosted there as well, enabling independent verifiers to access and confirm the election results.

## Independent Verification of the College Park Election

In order to meet the deadline to support College Park and its integration with Hart, the ElectionGuard software was *frozen* prior to completion of the full 2.0 implementation. As a result, the software used in College Park will be an implementation hybrid of the 2.0, 1.53, and 1.1 specs (officially 1.91.18).

!!! warning "ElectionGuard 1.91.18 should not be used outside of the College Park election"
    The ElectionGuard software used in College Park is not general release software. It is published here for the purposes of creating a public record of the College Park election. While this release creates an independently verifiable set of artifacts, it should not be used in other elections.

As a result,there are known aspects of the full 2.0 specification that will not be delivered for November. Specifically, Verification 6 (Adherence to vote limits) and 7.A and 7.B of Verification 7 (Validation of Confirmation codes) were not implemented correctly so cannot be verified. Full support for handling encrypted data was not enabled so Verification 11 (Correctness of decryptions of contest data) and Verification 14 (Correctness of contest data decryptions for challenged ballots) could not be implemented by an independent verifier, either.

There are fixes already in place that will be published after College Park, but to meet deployment and QA timelines were not released as part of 1.91.18. While it is not best practice by any means to intentionally omit support of components of independent verifier validations, some validations are more important than others, and the implementation risk of missing our deadlines for College Park outweighed the incremental benefit of delivery of the missing elements.

In addition, there are features that are outlined in the [2.0 spec](/spec/#v20) that are not used in the College Park election, and independent verifier support is thus not necessary nor expected for 1.91.18:

* Ballot chaining
* Pre-encrypted ballots
* Instant verification (BallotCheck)
* Any voting method other than precinct scan
* Encrypted contest data (write-ins, overvotes/undervotes, extended data)

!!! abstract "The [MITRE Requirements document](/images/college-park-verifier-requirements.pdf) outlines in detail the 2.0 encryption and election record capabilities adopted by their verifier for College Park and will be linked to as soon as it is published."

## Survey and Feedback from Voters

In-person voters will be asked to participate in an exit survey, and all College Park residents are welcome to participate in an election survey collecting general election feedback in addition to perspectives on ElectionGuard. Upon survey completion, the Center for Civic Design will publish a report on voter sentiment. 

<!-- Links -->
[College-Park-Banner]: /images/ElectionGuard_College_Park_2023.svg "College Park Banner"
[hart-scanner]: /images/votingmachine.jpeg