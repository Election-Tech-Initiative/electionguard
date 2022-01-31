# Sample Data

To better understand the data formats used by ElectionGuard, sample data is provided here to guide new developers. 

## Four Sample Elections

We have provided sample data for four different elections:

- **Minimal** - This is the most minimal election manifest file possible, designed to be easy to inspect and quick to develop against for rapid testing. All optional fields have been removed from the election manifest file. The election contains a single Yes/No referendum with a single ballot style in a single geopolitical unit.

- **Small** - This is designed to be a relatively small and simple election, but with more complexity than the minimal election. This is a good sample data set to begin understanding more complex ballot types with two or more geopolitical units or ballot styles. Three contests are listed (one of each type: Yes/No Referendum, Select One, and Select n of m), two GP units, two ballot styles, and a small number of recommended optional fields are included.

- **Full** - This is a more realistic example for a primary election for a municipality. This ballot contains several geopolitical units with multiple ballot styles and contains all optional metadata fields. This sample has multi-language support and multiple submitted ballot samples.

- **Hamilton General** - This is a complete example for a general election for a fictional municipality. This example contains many geopolitical units with multiple ballot styles and demonstrates how political districts overlap. This sample has multi-language support and multiple submitted ballot samples. The Hamilton General example also includes the election [private data][hamilton-election-private] that includes guardian private keys. More information about the Hamilton General Example can be found in the [Election Manifest Documentation][election-manifest-docs].

![Data][data-image]

## Data ![Version 0.95][badge-0.95]

### Election Manifests

The [Election Manifest][manifest-building] contains all the details of the election (such as contests, candidates, selections, ballot styles, etc.) and is required at the start of an ElectionGuard election.

**Manifest Examples:** [minimal][minimal-election-manifest] | [small][small-election-manifest] | [full][full-election-manifest] | [hamilton][hamilton-election-manifest]

### Submitted Ballots

Submitted Ballots are encrypted ballots that have been cast or spoiled.
Cast ballots will be tallied and spoiled ballots are decrypted.

**Submitted Ballot Examples:** [minimal][minimal-election-ballot] | [small][small-election-ballot] | [full][full-election-ballot] | [hamilton][hamilton-election-ballot]

### Election Record

The Election Record are the files required at the end of the election to verify the election and are intended to be posted publicly. There should not be any sensitive data (eg: no guardian private keys) in the record. 

**Artifacts Examples:** [minimal][minimal-election-artifacts] | [small][small-election-artifacts] | [full][full-election-artifacts] | [hamilton][hamilton-election-artifacts]

[data-image]: ../images/undraw/data.svg "Image of computer"

<!-- Links -->
[badge-0.95]: https://img.shields.io/badge/🗳%20ElectionGuard%20Specification-v0.95-green
[minimal-election-manifest]: https://github.com/microsoft/electionguard/blob/main/data/0.95.0/sample/minimal/manifest.json
[minimal-election-ballot]: https://github.com/microsoft/electionguard/blob/main/data/0.95.0/sample/minimal/ballots
[minimal-election-artifacts]: https://github.com/microsoft/electionguard/blob/main/data/0.95.0/sample/minimal/artifacts
[small-election-manifest]: https://github.com/microsoft/electionguard/blob/main/data/0.95.0/sample/small/manifest.json
[small-election-ballot]: https://github.com/microsoft/electionguard/blob/main/data/0.95.0/sample/small/ballots
[small-election-artifacts]: https://github.com/microsoft/electionguard/blob/main/data/0.95.0/sample/small/artifacts
[full-election-manifest]: https://github.com/microsoft/electionguard/blob/main/data/0.95.0/sample/full/manifest.json
[full-election-ballot]: https://github.com/microsoft/electionguard/blob/main/data/0.95.0/sample/full/ballots
[full-election-artifacts]: https://github.com/microsoft/electionguard/blob/main/data/0.95.0/sample/full/artifacts
[hamilton-election-manifest]: https://github.com/microsoft/electionguard/blob/main/data/0.95.0/sample/hamilton-general/manifest.json
[hamilton-election-ballot]: https://github.com/microsoft/electionguard/blob/main/data/0.95.0/sample/hamilton-general/ballots
[hamilton-election-artifacts]: https://github.com/microsoft/electionguard/blob/main/data/0.95.0/sample/hamilton-general/artifacts
[hamilton-election-private]: https://github.com/microsoft/electionguard/blob/main/data/0.95.0/sample/hamilton-general/private
[election-manifest-docs]: https://www.electionguard.vote/guide/Election_Manifest/#introducing-hamilton-county-oz

[manifest-building]: ../concepts/Manifest_Building.md