# Sample Data

To assist with formatting data, sample data is provided here to guide new developers.

## Election Manifests

The [Election Manifest](Election_Manifest.md) contains all the details of the election and is required at the start of the election.

**Examples:** [minimal][minimal_election_manifest] | [small][small_election_manifest] | [full][full_election_manifest]

## Submitted Ballots

Submitted Ballots are encrypted ballots that have been cast or spoiled.
Cast ballots will be tallied and spoiled ballots are decrypted.

**Examples:** [minimal][minimal_election_ballot] | [small][small_election_ballot] | [full][full_election_ballot]

## Artifacts

Election Artifacts are the files required at the end of the election to verify the election. These include the following:

- Manifest
- Election Context
- Election Constants
- Encrypted Tally
- Decrypted Tally
- Guardian Records
- Encryption Device Information
- Encrypted Ballots
- Decrypted Spoiled Ballots

**Example Folder Structure:**

```
📂 artifacts
--- 📄 manifest.json
--- 📄 context.json
--- 📄 constants.json
--- 📄 encrypted_tally.json
--- 📄 tally.json
--- 📁 guardians
--- 📁 devices
--- 📁 encrypted_ballots
--- 📁 spoiled_ballots
```

**Examples:** [minimal][minimal_election_artifacts] | [small][small_election_artifacts] | [full][full_election_artifacts]

[minimal_election_manifest]: https://github.com/microsoft/electionguard/blob/main/data/minimal/manifest.json
[minimal_election_ballot]: https://github.com/microsoft/electionguard/blob/main/data/minimal/ballots
[minimal_election_artifacts]: https://github.com/microsoft/electionguard/blob/main/data/minimal/artifacts
[small_election_manifest]: https://github.com/microsoft/electionguard/blob/main/data/small/manifest.json
[small_election_ballot]: https://github.com/microsoft/electionguard/blob/main/data/small/ballots
[small_election_artifacts]: https://github.com/microsoft/electionguard/blob/main/data/small/artifacts
[full_election_manifest]: https://github.com/microsoft/electionguard/blob/main/data/full/manifest.json
[full_election_ballot]: https://github.com/microsoft/electionguard/blob/main/data/full/ballots
[full_election_artifacts]: https://github.com/microsoft/electionguard/blob/main/data/full/artifacts
