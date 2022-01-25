# ElectionGuard Web Specification ![Version 0.95.0][green-badge-0.95.0]

!!! warning "Incomplete"
    The web version is being constructed by the open source community for the convenience of web viewing. However, it is incomplete at this time and should not be used for reference purposes. If you need a complete reference, refer to the [official specifications].

## Overview

This document describes the technical details of the _ElectionGuard_ toolkit which can be used in conjunction with many new and existing voting systems to enable both end-to-end (E2E) verifiability and privacy-enhanced risk-limiting audits (RLAs). _ElectionGuard_ is not a complete election system. It instead provides components that are designed to be flexible and to promote innovation by election officials and system developers. When properly used, it can promote voter confidence by empowering voters to independently verify the accuracy of election results.

### End-to-end (E2E) verifiability

An E2E-verifiable election provides artifacts which allow voters to confirm that their votes have been accurately recorded and counted. Specifically, an election is _End-to-end (E2E) verifiable_ if two properties are achieved.

1. Individual voters can verify that their votes have been accurately recorded.
2. Voters and observers can verify that the recorded votes have been accurately counted.

An E2E-verifiable tally can be used as the primary tally in an election or as a verifiable secondary tally alongside traditional methods. _ElectionGuard_ is compatible with in-person voting – either using an electronic ballot-marking device or an optical scanner capable of reading hand-marked or machine-marked ballots, with voting by mail, and even with Internet voting.

### Risk-limiting audits (RLAs)

RLAs offer election administrators efficient methods to validate reported election tallies against physical ballot records. There are several varieties of RLAs, but the most efficient and practical are _ballot-comparison audits_ in which electronic _cast-vote records (CVRs)_ are individually compared against physical ballots.

The challenge with ballot-comparison audits is that public release of the full set of CVRs can compromise voter privacy while an audit without public disclosure of CVRs offers no basis for public confidence in the outcome. _ElectionGuard_ can bridge this gap by enabling public disclosure of encrypted ballots that can matched directly to physical ballots selected for auditing and can also be proven to match the reported tallies.

### About this specification

This specification can be used by expert reviewers to evaluate the details of the _ElectionGuard_ process and by independent parties to write _ElectionGuard_ verifiers to confirm the consistency of election artifacts with announced election results. The details of the _ElectionGuard_ Application Programming Interface (API) are provided in a separate document.

<!-- Links -->

[green-badge-0.95.0]: https://img.shields.io/badge/Version-v0.95.0-green
[spec-0.95.0]: https://github.com/microsoft/electionguard/releases/download/v0.95.0/ElectionGuard_Specification_v0_95_0.pdf "Election Guard Specification 0.95.0"
[official specifications]: ../../
