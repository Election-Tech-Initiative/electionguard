# ElectionGuard Official Specifications 

The official versions of the ElectionGuard Specifications are listed below and stand as the primary source of reference when discussing the [ElectionGuard Specification]. Each version includes a [badge] that can be used to quickly display which versions are supported or used by products following the specification. To follow along with the code versioning, see the [versioning].

Version | Specification                                  | Recommended      | Badge
:------ |:-----------------------------------------------|:----------------:| :-----------
2.0     |  [:material-download: Download][spec-2.0]                               |        :material-check:          | ![Version 2.0][badge-2.0]
1.1     | [:material-download: Download][spec-1.1]       |  | ![Version 1.1][badge-1.1]
1.0     | [:material-download: Download][spec-1.0]       |        | ![Version 1.0][badge-1.0]
0.95    | [:material-download: Download][spec-0.95]      |        | ![Version 0.95][badge-0.95]
0.85    | [:material-download: Download][spec-0.85]      |                  | ![Version 0.85][badge-0.85]

### Release Notes

#### v2.0

2.0 is a major refactor of the ElectionGuard specification. It includes the following capabilities

- The size of the proofs in the election record has been reduced by more than 90% – reducing the size of the full election record by about a factor of 3.
- Computing the proofs takes about 20% less time.
- Placeholder selections have been eliminated entirely.
- Guardians are no longer part of the election record as their partial decryptions and proofs have been administratively combined into single full decryptions and proofs.
- Range proofs are now included to support voting systems like cumulative voting, range voting, STAR-voting, Borda count, and others.
- A new pre-encrypted ballot format is included to support vote-by-mail, central count, and paper-only poll sites.
- Support is now available for instant verification allowing voters to confirm the accuracy of challenge ballots without waiting for the election record to be published.
- New default parameters are used with ln(2) replacing the Euler-Mascheroni constant as the basis for generation of the large prime.
- The data format of hashes has been clearly described to eliminate ambiguities.
#### v1.0

_Updates from previous version_

- The large prime p and corresponding cofactor r were changed to correctly match the result of the process for the derivation of the prime.
- The equations for generating proofs of ballot correctness have been optimized.
- Auxiliary keys have been eliminated in favor of using the existing keys for both ordinary and exponential ElGamal encryption.
- A more flexible structure of ballot chaining has been introduced to allow for non-linear chaining or no chaining at all.
- Smaller parameters suitable for testing are included.
- The election record of this version should match that of the prior v0.95 and therefore require no verifier changes (with the exception of using the corrected prime).

#### v0.95

_Updates from previous version_

- The large prime p and corresponding cofactor r were changed to move the prime p further from 2^4096.
- A section specifically about writing verifiers was added.
- Various small clarifications and corrections were included.

#### v0.85

- Initial public release of specification for ElectionGuard

<!-- Links -->
[ElectionGuard Specification]: ../overview/Glossary/#electionguard-specification
[badge]: ../develop/Badges/
[versioning]: ../develop/Versioning.md

[badge-2.0]: https://img.shields.io/badge/🗳%20ElectionGuard-v2.0-green
[spec-2.0]: https://github.com/microsoft/electionguard/releases/download/v2.0/EG_Spec_2_0.pdf "Election Guard Specification 2.0"

[badge-1.1]: https://img.shields.io/badge/🗳%20ElectionGuard-v1.1-green
[spec-1.1]: https://github.com/microsoft/electionguard/releases/download/v1.1/EG_spec_v1_1.pdf "Election Guard Specification 1.1"

[badge-1.0]: https://img.shields.io/badge/🗳%20ElectionGuard-v1.0-yellow
[spec-1.0]: https://github.com/microsoft/electionguard/releases/download/v1.0/EG_spec_v1_0.pdf "Election Guard Specification 1.0"

[badge-0.95]: https://img.shields.io/badge/🗳%20ElectionGuard-v0.95-yellow
[spec-0.95]: https://github.com/microsoft/electionguard/releases/download/v1.0.0-preview-1/EG_spec_v0_95.pdf "Election Guard Specification 0.95"

[badge-0.85]: https://img.shields.io/badge/🗳%20ElectionGuard-v0.85-red
[spec-0.85]: https://github.com/microsoft/electionguard/releases/download/v0.85.0/EG_spec_V0_85.pdf "Election Guard Specification 0.85"
