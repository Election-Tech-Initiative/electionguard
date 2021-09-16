# Data

To better understand the data formats used by ElectionGuard, sample data is provided here to guide new developers.

## Four Sample Elections

We have provided sample data for four different elections:

- **Minimal** - This is the most minimal election manifest file possible, designed to be easy to inspect and quick to develop against for rapid testing. All optional fields have been removed from the election manifest file. The election contains a single Yes/No referendum with a single ballot style in a single geopolitical unit.

- **Small** - This is designed to be a relatively small and simple election, but with more complexity than the minimal election. This is a good sample data set to begin understanding more complex ballot types with two or more geopolitical units or ballot styles. Three contests are listed (one of each type: Yes/No Referendum, Select One, and Select n of m), two GP units, two ballot styles, and a small number of recommended optional fields are included.

- **Full** - This is a more realistic example for a primary election for a municipality. This ballot contains several geopolitical units with multiple ballot styles and contains all optional metadata fields. This sample has multi-language support and multiple submitted ballot samples.

- **Hamilton General** - This is a complete example for a general election for a fictional municipality. This example contains many geopolitical units with multiple ballot styles and demonstrates how political districts overlap. This sample has multi-language support and multiple submitted ballot samples. The Hamilton General example also includes the election [private data](hamilton_election_private) that includes guardian private keys. More information about the Hamilton General Example can be found in the [Election Manifest Documentation](election_manifest_docs).

![Data](../images/undraw/data.svg)

## Election Manifests

The [Election Manifest](../concepts/Election_Manifest.md) contains all the details of the election (such as contests, candidates, selections, ballot styles, etc.) and is required at the start of an ElectionGuard election.

**Manifest Examples:** [minimal][minimal_election_manifest] | [small][small_election_manifest] | [full][full_election_manifest] | [hamilton][hamilton_election_manifest]

## Submitted Ballots

Submitted Ballots are encrypted ballots that have been cast or spoiled.
Cast ballots will be tallied and spoiled ballots are decrypted.

**Submitted Ballot Examples:** [minimal][minimal_election_ballot] | [small][small_election_ballot] | [full][full_election_ballot] | [hamilton][hamilton_election_ballot]

## Artifacts

Election Artifacts are the files required at the end of the election to verify the election and are intended to be posted publicly. There should not be any sensitive data (eg: no guardian private keys) in the artifacts. These include the following:

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

**Artifacts Examples:** [minimal][minimal_election_artifacts] | [small][small_election_artifacts] | [full][full_election_artifacts] | [hamilton][hamilton_election_artifacts]

[minimal_election_manifest]: https://github.com/microsoft/electionguard/blob/main/data/minimal/manifest.json
[minimal_election_ballot]: https://github.com/microsoft/electionguard/blob/main/data/minimal/ballots
[minimal_election_artifacts]: https://github.com/microsoft/electionguard/blob/main/data/minimal/artifacts
[small_election_manifest]: https://github.com/microsoft/electionguard/blob/main/data/small/manifest.json
[small_election_ballot]: https://github.com/microsoft/electionguard/blob/main/data/small/ballots
[small_election_artifacts]: https://github.com/microsoft/electionguard/blob/main/data/small/artifacts
[full_election_manifest]: https://github.com/microsoft/electionguard/blob/main/data/full/manifest.json
[full_election_ballot]: https://github.com/microsoft/electionguard/blob/main/data/full/ballots
[full_election_artifacts]: https://github.com/microsoft/electionguard/blob/main/data/full/artifacts
[hamilton_election_manifest]: https://github.com/microsoft/electionguard/blob/main/data/hamilton-general/manifest.json
[hamilton_election_ballot]: https://github.com/microsoft/electionguard/blob/main/data/hamilton-general/ballots
[hamilton_election_artifacts]: https://github.com/microsoft/electionguard/blob/main/data/hamilton-general/artifacts
[hamilton_election_private]: https://github.com/microsoft/electionguard/blob/main/data/hamilton-general/private
[election_manifest_docs]: https://www.electionguard.vote/guide/Election_Manifest/#introducing-hamilton-county-oz
