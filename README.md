[![Microsoft Defending Democracy Program: ElectionGuard][election-guard-banner]](http://microsoft.github.io/electionguard/)

[![license][license-image]](LICENSE)

ElectionGuard is an **open source** software development kit (SDK) that makes voting more secure, transparent and accessible. Announced at the [Build developer conference][build-developer-conference], ElectionGuard enables end-to-end verification of elections as well as support the publication of results from ballot comparison audits. The ElectionGuard SDK leverages [homomorphic encryption][homomoprhic-encryption] to ensure that votes recorded by electronic systems of any type remain encrypted, secure, and secret. Results can be published online or made available to third-party organizations for secure validation, and allow individual voters to confirm their votes were correctly counted.

## ❤️ Open-Source

This library and all linked ElectionGuard projects, are licensed under the MIT license. There is no fee for using ElectionGuard.

## 🚀 Getting Started

ElectionGuard is always improving. To keep up with the latest, check our **[official site on GitHub Pages][election-guard-official-page]** and our [roadmap][election-guard-road-map]. For those looking to get started, we recommend the following repositories.

### Documentation

This repository is a living document to help everyone interact with ElectionGuard. The [official ElectionGuard site][election-guard-official-page] is built using the `/docs` folder and [mkdocs][mkdocs-official-site] with [mkdocs-material][material-mkdocs]. Ensure you have the python 3.8 or newer installed and run `make` to install the dependencies and start the site.

### Python

A core component of ElectionGuard implemented in python which includes ballot encryption, decryption, key generation, and tallying.

[📁 Source][election-guard-python-source] |
[📦 Package][election-guard-python-package] |
[📝 Documentation][election-guard-python-documentation]

### C ++

A subset of the ElectionGuard SDK implemented in C++ to support ballot encryption.

[📁 Source][election-guard-cpp-source-code] |
[📦 Package][election-guard-cpp-package] |
[📝 Documentation][election-guard-cpp-documentation]

### Web API

A Web API that wraps the python package to perform ballot encryption, casting, spoiling, and tallying.

[📁 Source][election-guard-web-api-source] | 
[🐳 Docker][election-guard-web-api-docker] | 
[📄 Documentation][election-guard-web-api-documentation]

### User Interface

Monorepo in React & Typescript consisting of an api client, components, and apps to demonstrate examples of user interface.

[📁 Source][election-guard-ui-source] |
[📄 Documentation][election-guard-ui-documentation]

## 🛡 Security Issues Reporting

We encourage the developer and security community to conduct research, report issues, and suggest improvements on this code base. However, unlike performance or feature bugs, please do **not** report security vulnerabilities in public Github comments. Each repository has a SECURITY file with instructions on responsibly reporting security vulnerabilities under Microsoft's CVD process.

## 🤝 Contributing

Help defend democracy and **[contribute to the project][]**.

[code of conduct]: CODE_OF_CONDUCT.md
[contribute to the project]: CONTRIBUTING.md

We welcome discussions on our [discussions page][election-guard-discussions], feel free to check in and ask your questions and drop your suggestions regarding the specifications over there.

## ❓ Questions

ElectionGuard would love for you to ask questions out in the open using Github Issues. If you really want to email the ElectionGuard team, reach out at electionguard@microsoft.com.

## 🎉 Thanks!

A huge thank you to those who helped to contribute to this project so far, including:

- Josh Benaloh (whose [PhD thesis][verifiable-search-ballot-elections-paper] was the genesis of much of this work)
- [InfernoRed Technology][infernored]
- [VotingWorks][voting-works]
- [Center for Civic Design][center-for-civic-design]
- [Oxide Design][oxide-design]
- Many teams within Microsoft

<!-- Links -->
[election-guard-banner]: docs/images/electionguard-banner.svg "Election Guard banner SVG"
[license-image]: https://img.shields.io/github/license/microsoft/electionguard "Election Guard license image"
[build-developer-conference]: https://blogs.microsoft.com/on-the-issues/?p=63211 "Protecting democratic elections through secure, verifiable voting"
[homomoprhic-encryptio]: https://en.wikipedia.org/wiki/Homomorphic_encryption "Homomorphic encryption"
[election-guard-official-page]: https://microsoft.github.io/electionguard "Official Election Guard site on Github Pages"
[election-guard-road-map]: https://microsoft.github.io/electionguard/Roadmap "Election Guard road map"
[mkdocs-official-site]: https://www.mkdocs.org/ "MkDocs official website"
[material-mkdocs]: https://squidfunk.github.io/mkdocs-material/ "Material for MkDocs"
[election-guard-python-source]: https://github.com/microsoft/electionguard-python "Election Guard Python source code"
[election-guard-python-package]: https://pypi.org/project/electionguard/ "Election Guard Python package"
[election-guard-python-documentation]: https://microsoft.github.io/electionguard-python/ "Election Guard Python documentation"
[election-guard-cpp-source-code]: https://github.com/microsoft/electionguard-cpp/ "Election Guard C++ source code"
[election-guard-cpp-package]: https://www.nuget.org/packages/ElectionGuard.Encryption/ "Election Guard C++ package"
[election-guard-cpp-documentation]: https://github.com/microsoft/electionguard-cpp#readme "Election Guard C++ documentation"
[election-guard-web-api-source]: https://github.com/microsoft/electionguard-api-python "Election Guard Web API source code"
[election-guard-web-api-docker]: https://hub.docker.com/r/electionguard/electionguard-web-api "Election Guard Web API Docker"
[election-guard-web-api-documentation]: https://microsoft.github.io/electionguard-api-python/ "Election Guard Web API documentation"
[election-guard-ui-source]: https://github.com/microsoft/electionguard-ui "Election Guard UI source code"
[election-guard-ui-documentation]: https://github.com/microsoft/electionguard-ui#readme "Election Guard UI documentation"
[election-guard-discussions]: https://github.com/microsoft/electionguard/discussions "Election Guard Discussions page"
[verifiable-search-ballot-elections-paper]: https://www.microsoft.com/en-us/research/publication/verifiable-secret-ballot-elections/ "Verifiable Secret-Ballot Elections - Microsoft Research, Josh Benaloh"
[infernored]: https://infernored.com/ "InfernoRed"
[voting-works]: https://voting.works/ "Voting works - Elections you can trust"
[center-for-civic-design]: https://civicdesign.org/ "Center for Civic Design"
[oxide-design]: https://oxidedesign.com/ "Oxide Design"
