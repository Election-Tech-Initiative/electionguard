
# Reference Implementations

These are reference implementations to showcase the scope of ElectionGuard. These repos can be seen as singular components or parts of the broader solution to fully verify an election. 

## Web API
A thin stateless API wrapping `electionguard-python` to perform ballot encryption, casting, spoiling, and tallying. 

[:fontawesome-brands-github: Source](https://github.com/microsoft/electionguard-web-api) | [:fontawesome-brands-docker: Docker](https://hub.docker.com/r/electionguard/electionguard-web-api) | [:fontawesome-regular-file: Documentation](https://microsoft.github.io/electionguard-web-api/)

## Archived

!!! warning 
    The following repositories are considered deprecated and are for research purposes not development. For active development, please look at **non-archived** section.

### Admin Device
An application used to administer ElectionGuard election processes, including key generation, trustee provisioning, and post-election tallying, partial decryptions, and zero-knowledge proofs.

[:fontawesome-brands-github: Source](https://github.com/microsoft/electionguard-admin-device)

### Ballot Box
Used to scan ballots to generate lists of cast and spoiled ballots in an election; used in tallying to finalize ballot operations (cast or spoil, etc.) for publishing results.

[:fontawesome-brands-github: Source](https://github.com/microsoft/electionguard-ballot-box)


### Ballot Marking Device
Working instance of ballot marking device (BMD). Built by VotingWorks in consultation with the [Center for Civic Design](https://civicdesign.org), this front-end provides an interface for a voter to complete and print a ballot which, in an end-to-end verifiable use case, would be accompanied by a printed tracking ID. This BMD front-end is provided as one, potential implementation.

[:fontawesome-brands-github: Source](https://github.com/microsoft/electionguard-ballot-marking-device)


### Tracking Site
An application that demonstrates publication of ElectionGuard election artifacts to a public website to enable verification ID lookup, downloadable zip files of the election result (for third-party verifiers), and election results summaries.

[:fontawesome-brands-github: Source](https://github.com/microsoft/electionguard-tracking-site)

### Verifiers
A verifier application is used to perform an external, independent verification of an election tally. This repository contains a reference implementation of a verifier built against the ElectionGuard specifications. This is not meant to be the *only* verifier application, but rather an example. This library should be used in tandem with the technical specifications and usage guidelines contained in the [specifications](https://github.com/microsoft/electionguard/wiki).

[:fontawesome-brands-github: Source](https://github.com/microsoft/electionguard-verifier)

#### Community Verifiers
- [:fontawesome-brands-github: Python Verifier](https://github.com/rainbowhuanguw/ElectionGuard-verifier-python) by Rainbow Huang
- [:fontawesome-brands-github: C# Verifier](https://github.com/brandon-irl/ElectionGuard-Verifier-C-) by Brandon Alexander
- [:fontawesome-brands-github: Java Verifier](https://github.com/JohnLCaron/electionguard-java) by John Caron
- [:fontawesome-brands-github: Python Verifier (electionguard-verify)](https://github.com/nickboucher/electionguard-verify) by Nicholas Boucher
