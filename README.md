[![Microsoft Defending Democracy Program: ElectionGuard](docs/images/electionguard-banner.svg)](http://microsoft.github.io/electionguard/)

[![license](https://img.shields.io/github/license/microsoft/electionguard)](LICENSE)

ElectionGuard is an **open source** software development kit (SDK) that makes voting more secure, transparent and accessible. Announced on at the [Build developer conference](https://blogs.microsoft.com/on-the-issues/?p=63211), ElectionGuard enables end-to-end verification of elections as well as support the publication of results from ballot comparison audits. The ElectionGuard SDK leverages [homomorphic encryption](https://en.wikipedia.org/wiki/Homomorphic_encryption) to ensure that votes recorded by electronic systems of any type remain encrypted, secure, and secret. Results can be published online or made available to third-party organizations for secure validation, and allow individual voters to confirm their votes were correctly counted.

## ❤️ Open-Source

This library and all linked ElectionGuard projects, are licensed under the MIT license. There is no fee for using ElectionGuard.

## 🚀 Getting Started

ElectionGuard is always improving. To keep up with the latest, check our **[official site on GitHub Pages](https://microsoft.github.io/electionguard)** and our [roadmap](https://microsoft.github.io/electionguard/Roadmap). For those looking to get started, we recommend the following repositories.

### Documentation

This repository is a living document to help everyone interact with ElectionGuard. The [official ElectionGuard site](https://microsoft.github.io/electionguard) is built using the `/docs` folder and [mkdocs](https://www.mkdocs.org/) with [mkdocs-material](https://squidfunk.github.io/mkdocs-material/). Ensure you have the python 3.8 or newer installed and run `make` to install the dependencies and start the site.

### Python

A core component of ElectionGuard implemented in python which includes ballot encryption, decryption, key generation, and tallying.

[📁 Source](https://github.com/microsoft/electionguard-python) |
[📦 Package](https://pypi.org/project/electionguard/) |
[📝 Documentation](https://microsoft.github.io/electionguard-python/)

### C ++

A subset of the ElectionGuard SDK implemented in C++ to support ballot encryption.

[📁 Source](https://github.com/microsoft/electionguard-cpp) |
[📦 Package](https://www.nuget.org/packages/ElectionGuard.Encryption/) |
[📝 Documentation](https://github.com/microsoft/electionguard-cpp#readme)

### Web API

A Web API that wraps the python package to perform ballot encryption, casting, spoiling, and tallying.

[📁 Source](https://github.com/microsoft/electionguard-api-python) | [🐳 Docker](https://hub.docker.com/r/electionguard/electionguard-web-api) | [📄 Documentation](https://microsoft.github.io/electionguard-api-python/)

### User Interface

Monorepo in React & Typescript consisting of an api client, components, and apps to demonstrate examples of user interface.

[📁 Source](https://github.com/microsoft/electionguard-ui) | [📄 Documentation](https://github.com/microsoft/electionguard-ui#readme)

## 🛡 Security Issues Reporting

We encourage the developer and security community to conduct research, report issues, and suggest improvements on this code base. However, unlike performance or feature bugs, please do **not** report security vulnerabilities in public Github comments. Each repository has a SECURITY file with instructions on responsibly reporting security vulnerabilities under Microsoft's CVD process.

## 🤝 Contributing

Help defend democracy and **[contribute to the project][]**.

[code of conduct]: CODE_OF_CONDUCT.md
[contribute to the project]: CONTRIBUTING.md

We welcome discussions on our [discussions page](https://github.com/microsoft/electionguard/discussions), feel free to check in and ask your questions and drop your suggestions regarding the specifications over there.

## ❓ Questions

ElectionGuard would love for you to ask questions out in the open using Github Issues. If you really want to email the ElectionGuard team, reach out at electionguard@microsoft.com.

## 🎉 Thanks!

A huge thank you to those who helped to contribute to this project so far, including:

- Josh Benaloh (whose [PhD thesis](https://www.microsoft.com/en-us/research/publication/verifiable-secret-ballot-elections/) was the genesis of much of this work)
- [InfernoRed Technology](https://infernored.com/)
- [VotingWorks](https://voting.works/)
- [Center for Civic Design](https://civicdesign.org/)
- [Oxide Design](https://oxidedesign.com/)
- Many teams within Microsoft
