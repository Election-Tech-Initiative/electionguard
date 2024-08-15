# Data Schema

ElectionGuard expects data to be formatted in a particular way according to a set of [JSON schemas](https://json-schema.org/). The expectation is to keep these schemas alongside the specification. The schemas will be defined here to indicate to developers what they should be expecting.

Keep in mind that not all serialized files should be public. The [election record][election-record] includes the list of all data formats that should be public. [Sample data][sample-data] for the election is also available for developers. This will include both what is in the Election Record, but also some private data only available for testing. 

## Schema ![Version 1.91][shield-green-1.91]

Currently, JSON is used as the primary serialization format of the artifacts from an election. These are [JSON schema][json-schema] files that can be used to verify the schema of the setup files like the manifest pre-election and the election record files post-election. This represents the full list of items that can be serialized / deserialized, but not all elections will use every file type. 

!!! warning "Work in Progress"
    This is a work in progress. Feel free to contribute.

### Election

- [Manifest][manifest] / `Manifest` - Election manifest
- [Context][ciphertext_election_context] / `CiphertextElectionContext` - Context for encryption for specific election
- [Constants][election_constants] / `ElectionConstants`- Constants of election
- [Encryption Device][encryption_device] / `EncryptionDevice` - Encryption device information

### Ceremony
- [Guardian][guardian_record] / `GuardianRecord` - Single guardian's record
- [Lagrange Coefficients][lagrange_coefficients_record] / `LagrangeCoefficientsRecord` - Lagrange coefficients

### Ballot

- [Ballot][plaintext_ballot] / `PlaintextBallot` - Plaintext ballot
- [Compact Ballot][compact_ballot] / `CompactBallot` - Compact ballot
- [Encrypted Ballot][ciphertext_ballot] / `CiphertextBallot` - Encrypted ballot
- [Spoiled Ballot][spoiled_ballot] / `SpoiledBallot` -  Submitted spoiled ballot

### Tally
- [Tally][plaintext_tally] / `PlaintextTally` - Plaintext tally
- [Encrypted Tally][published_ciphertext_tally] / `PublishedCiphertextTally` - Encrypted tally


<!-- Links -->
[shield-green-0.95]: https://img.shields.io/badge/🗳%20ElectionGuard-v0.95-green
[json-schema]: https://json-schema.org/specification.html "Json Schema Specification"

[election-record]: Election_Record.md
[sample-data]: Sample_Data.md
[manifest]: https://github.com/microsoft/electionguard/blob/main/data/1.91/schema/manifest.schema.json "Manifest Json Schema"
[ciphertext_election_context]: https://github.com/microsoft/electionguard/blob/main/data/1.91/schema/ciphertext_election_context.schema.json "Ciphertext Election Context Json Schema"
[election_constants]: https://github.com/microsoft/electionguard/blob/main/data/1.91/schema/election_constants.schema.json "Election Constants Json Schema"
[encryption_device]: https://github.com/microsoft/electionguard/blob/main/data/1.91/schema/encryption_device.schema.json "Encryption Device Json Schema"
[guardian_record]: https://github.com/microsoft/electionguard/blob/main/data/1.91/schema/guardian_record.schema.json "Guardian Record Json Schema"
[lagrange_coefficients_record]: https://github.com/microsoft/electionguard/blob/main/data/1.91/schema/lagrange_coefficients_record.schema.json "Lagrange Coefficients Record Json Schema"
[plaintext_ballot]: https://github.com/microsoft/electionguard/blob/main/data/1.91/schema/plaintext_ballot.schema.json "Plaintext Ballot Json Schema"
[ciphertext_ballot]: https://github.com/microsoft/electionguard/blob/main/data/1.91/schema/ciphertext_ballot.schema.json "Ciphertext Ballot Json Schema"
[spoiled_ballot]: https://github.com/microsoft/electionguard/blob/main/data/1.91/schema/spoiled_ballot.schema.json "Spoiled Ballot Json Schema"
[plaintext_tally]: https://github.com/microsoft/electionguard/blob/main/data/1.91/schema/plaintext_tally.schema.json "Plaintext Tally Json Schema"
[published_ciphertext_tally]: https://github.com/microsoft/electionguard/blob/main/data/1.91/schema/published_ciphertext_tally.schema.json "Published Ciphertext Tally Json Schema"

--8<-- "includes/abbreviations.md"