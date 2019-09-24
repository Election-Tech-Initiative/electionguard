
# ElectionGuard SDK

# Intro
ElectionGuard is an open source software development kit (SDK) that makes voting more secure, transparent, accessible. 

The ElectionGuard SDK leverages [homomorphic encryption](https://en.wikipedia.org/wiki/Homomorphic_encryption) to ensure that votes recorded by electronic systems of any type remain encrypted, secure, and secret. Meanwhile, ElectionGuard also allows verifiable and accurate tallying of ballots by any 3rd party organization without compromising secrecy or security. 


# ElectionGuard Components
At launch, the ElectionGuard SDK consists of four separate repositories. These repos, although intended to be used together as components of a broader solution, can also stand alone if developers wish to only research or implement one component.

## 1. Specifications, Documentation, and Academic Details
This library contains the fundamental specifications, documentation, architecture, and mathematical/cryptographic proofs that underpin ElectionGuard. If you're looking to understand the system better, or want to know how to integrate the various components, there is a lot of valuable information contained here.

**Specifications Repo**: [https://github.com/microsoft/ElectionGuard-SDK-Specification](https://github.com/microsoft/ElectionGuard-SDK-Specification)

## 2. Core ElectionGuard API SDK 
This is the core SDK that performs election functions such as vote encryption, decryption, key generation, and tallying. This code is meant to be run on voting system hardware and to be integrated into existing (or new) voting system software. The ElectionGuard SDK is written in C and is meant to add end-to-end verifiability and encryption into 3rd party comprehensive voting systems. There is also a simplistic, proof-of-concept C application to understand how the API should be called. 

**ElectionGuard C SDK Repo**: [https://github.com/microsoft/ElectionGuard-SDK-C-Implementation](https://github.com/microsoft/ElectionGuard-SDK-C-Implementation)  


## 3. Verifier (Reference Implementation) 
The verifier application is used to perform an external, independent verification of an election tally. This repository contains a reference implementation of a verifier built against the ElectionGuard specifications. This is not meant to be the *only* verifier application, but rather an example. This library should be used in tandem with the technical specifications and usage guidelines contained in the [Specifications Repo](https://github.com/microsoft/ElectionGuard-SDK-Specification).

**Verifier Repo**: [https://github.com/microsoft/ElectionGuard-SDK-Reference-Verifier](https://github.com/microsoft/ElectionGuard-SDK-Reference-Verifier)


## 4. Ballot Marking Device Reference Implementation
This repository contains a working instance of ballot marking device (BMD). Built by VotingWorks in consultation with the [Center for Civic Design](https://civicdesign.org), this front-end provides an interface for a voter to complete and print a ballot which, in an end-to-end verifiable use case, would be accompanied by a printed tracking ID. This BMD front-end is provided as one, potential implementation.

**Ballot Marking Device Repo**: [https://github.com/microsoft/ElectionGuard-SDK-Ballot-Marking-Device-Reference-Implementation](https://github.com/microsoft/ElectionGuard-SDK-Ballot-Marking-Device-Reference-Implementation)



# Open-Source
This library, and the four linked ElectionGuard projects, are licensed under the MIT license. There is no fee for using ElectionGuard.

# Security Issues Reporting
We encourage the developer and security community to conduct research, report issues, and suggest improvements on this code base. However, unlike performance or feature bugs, please do **not** report security vulnerabilities in public Github comments. Each repository has a SECURITY file with instructions on responsibly reporting security vulnerabilities under Microsoft's CVD process.

# Thanks!
A huge thank you to those who helped to contribute to this project so far, including:
* Josh Benaloh (whose [PhD thesis](https://www.microsoft.com/en-us/research/publication/verifiable-secret-ballot-elections/) was the genesis of much of this work)
* Galois / Free & Fair
* VotingWorks
* Center for Civic Design
* Oxide Design
* Many teams within Microsoft
 
# Background:
Announced on May 6 at the Build developer conference, ElectionGuard will enable end-to-end verification of elections, open results to third-party organizations for secure validation, and allow individual voters to confirm their votes were correctly counted.

Read more information in [the announcement blog post](https://blogs.microsoft.com/on-the-issues/?p=63211).

It will be available starting this summer to election officials and election technology suppliers who can incorporate the technology into voting systems. We encourage the election technology community to work with us and begin building offerings based on this technology and expect early prototypes using ElectionGuard will be ready for piloting during the 2020 elections in the United States, with significant deployments for subsequent election cycles. Over time we will seek to update and improve the SDK to support additional voting scenarios such as mail-in ballots and ranked choice voting. 
