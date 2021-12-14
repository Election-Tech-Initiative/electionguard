# Data Format

ElectionGuard expects data to be formatted in a particular way. The expectation is to keep this format versioned alongside the specification. The data format will be defined here to indicate to developers what they should be expecting. 

Keep in mind that not all serialized files should be public. The [election record][election-record] includes the list of all data formats that should be public. [Sample data][sample-data] for the election is also available for developers. This will include both what is in the Election Record, but also some private data only available for testing. 

## Schema ![Version 0.95.0][shield-green-0.95.0]

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
- [Submitted Ballot][submitted_ballot] / `SubmittedBallot` -  Submitted cast or spoiled ballot

### Tally
- [Tally][plaintext_tally] / `PlaintextTally` - Plaintext tally
- [Encrypted Tally][published_ciphertext_tally] / `PublishedCiphertextTally` - Encrypted tally


<!-- Links -->
[shield-green-0.95.0]: https://img.shields.io/badge/🗳%20ElectionGuard%20Specification-0.95.0-green
[json-schema]: https://json-schema.org/specification.html "Json Schema Specification"

[election-record]: ../Election_Record
[election-record]: ../Sample_Data
[manifest]: https://github.com/microsoft/electionguard/blob/main/data/0.95.0/schema/manifest.schema.json "Manifest Json Schema"
[ciphertext_election_context]: https://github.com/microsoft/electionguard/blob/main/data/0.95.0/schema/ciphertext_election_context.schema.json "Ciphertext Election Context Json Schema"
[election_constants]: https://github.com/microsoft/electionguard/blob/main/data/0.95.0/schema/election_constants.schema.json "Election Constants Json Schema"
[encryption_device]: https://github.com/microsoft/electionguard/blob/main/data/0.95.0/schema/encryption_device.schema.json "Encryption Device Json Schema"
[guardian_record]: https://github.com/microsoft/electionguard/blob/main/data/0.95.0/schema/guardian_record.schema.json "Guardian Record Json Schema"
[lagrange_coefficients_record]: https://github.com/microsoft/electionguard/blob/main/data/0.95.0/schema/lagrange_coefficients_record.schema.json "Guardian Record Json Schema"
[plaintext_ballot]: https://github.com/microsoft/electionguard/blob/main/data/0.95.0/schema/plaintext_ballot.schema.json "Guardian Record Json Schema"
[ciphertext_ballot]: https://github.com/microsoft/electionguard/blob/main/data/0.95.0/schema/ciphertext_ballot.schema.json "Guardian Record Json Schema"
[submitted_ballot]: https://github.com/microsoft/electionguard/blob/main/data/0.95.0/schema/submitted_ballot.schema.json "Guardian Record Json Schema"
[plaintext_tally]: https://github.com/microsoft/electionguard/blob/main/data/0.95.0/schema/plaintext_tally.schema.json "Guardian Record Json Schema"
[published_ciphertext_tally]: https://github.com/microsoft/electionguard/blob/main/data/0.95.0/schema/published_ciphertext_tally.schema.json "Guardian Record Json Schema"