[![Microsoft Defending Democracy Program: ElectionGuard][1]](http://microsoft.github.io/electionguard/)

[![license][2]](LICENSE)

ElectionGuard is an **open source** software development kit (SDK) that makes voting more secure, transparent and accessible. Announced at the [Build developer conference][3], ElectionGuard enables end-to-end verification of elections as well as support the publication of results from ballot comparison audits. The ElectionGuard SDK leverages [homomorphic encryption][4] to ensure that votes recorded by electronic systems of any type remain encrypted, secure, and secret. Results can be published online or made available to third-party organizations for secure validation, and allow individual voters to confirm their votes were correctly counted.

## ❤️ Open-Source

This library and all linked ElectionGuard projects, are licensed under the MIT license. There is no fee for using ElectionGuard.

## 🚀 Getting Started

ElectionGuard is always improving. To keep up with the latest, check our **[official site on GitHub Pages][5]** and our [roadmap][6]. For those looking to get started, we recommend the following repositories.

### Documentation

This repository is a living document to help everyone interact with ElectionGuard. The [official ElectionGuard site][5] is built using the `/docs` folder and [mkdocs][7] with [mkdocs-material][8]. Ensure you have the python 3.8 or newer installed and run `make` to install the dependencies and start the site.

### Python

A core component of ElectionGuard implemented in python which includes ballot encryption, decryption, key generation, and tallying.

[📁 Source][9] |
[📦 Package][10] |
[📝 Documentation][11]

### C ++

A subset of the ElectionGuard SDK implemented in C++ to support ballot encryption.

[📁 Source][12] |
[📦 Package][13] |
[📝 Documentation][14]]

### Web API

A Web API that wraps the python package to perform ballot encryption, casting, spoiling, and tallying.

[📁 Source][15] | 
[🐳 Docker][16] | 
[📄 Documentation][17]

### User Interface

Monorepo in React & Typescript consisting of an api client, components, and apps to demonstrate examples of user interface.

[📁 Source][18] |
[📄 Documentation][19]

## 🛡 Security Issues Reporting

We encourage the developer and security community to conduct research, report issues, and suggest improvements on this code base. However, unlike performance or feature bugs, please do **not** report security vulnerabilities in public Github comments. Each repository has a SECURITY file with instructions on responsibly reporting security vulnerabilities under Microsoft's CVD process.

## 🤝 Contributing

Help defend democracy and **[contribute to the project][]**.

[code of conduct]: CODE_OF_CONDUCT.md
[contribute to the project]: CONTRIBUTING.md

We welcome discussions on our [discussions page][20], feel free to check in and ask your questions and drop your suggestions regarding the specifications over there.

## ❓ Questions

ElectionGuard would love for you to ask questions out in the open using Github Issues. If you really want to email the ElectionGuard team, reach out at electionguard@microsoft.com.

## 🎉 Thanks!

A huge thank you to those who helped to contribute to this project so far, including:

- Josh Benaloh (whose [PhD thesis][21] was the genesis of much of this work)
- [InfernoRed Technology][22]
- [VotingWorks][23]
- [Center for Civic Design][24]
- [Oxide Design][25]
- Many teams within Microsoft

[1]: docs/images/electionguard-banner.svg "Election Guard banner SVG"
[2]: https://img.shields.io/github/license/microsoft/electionguard "Election Guard license image"
[3]: https://blogs.microsoft.com/on-the-issues/?p=63211 "Protecting democratic elections through secure, verifiable voting"
[4]: https://en.wikipedia.org/wiki/Homomorphic_encryption "Homomorphic encryption"
[5]: https://microsoft.github.io/electionguard "Official Election Guard site on Github Pages"
[6]: https://microsoft.github.io/electionguard/Roadmap "Election GUard road map"
[7]: https://www.mkdocs.org/ "MkDocs official website"
[8]: https://squidfunk.github.io/mkdocs-material/ "Material for MkDocs"
[9]: https://github.com/microsoft/electionguard-python "Election Guard Python source code"
[10]: https://pypi.org/project/electionguard/ "Election Guard Python package"
[11]: https://microsoft.github.io/electionguard-python/ "Election Guard Python documentation"
[12]: https://github.com/microsoft/electionguard-cpp/ "Election Guard C++ source code"
[13]: https://www.nuget.org/packages/ElectionGuard.Encryption/ "Election Guard C++ package"
[14]: https://github.com/microsoft/electionguard-cpp#readme "Election Guard C++ documentation"
[15]: https://github.com/microsoft/electionguard-api-python "Election Guard Web API source code"
[16]: https://hub.docker.com/r/electionguard/electionguard-web-api "Election Guard Web API Docker"
[17]: https://microsoft.github.io/electionguard-api-python/ "Election Guard Web API documentation"
[18]: https://github.com/microsoft/electionguard-ui "Election Guard UI source code"
[19]: https://github.com/microsoft/electionguard-ui#readme "Election Guard UI documentation"
[20]: https://github.com/microsoft/electionguard/discussions "Election Guard Discussions page"
[21]: https://www.microsoft.com/en-us/research/publication/verifiable-secret-ballot-elections/ "Verifiable Secret-Ballot Elections - Microsoft Research, Josh Benaloh"
[22]: https://infernored.com/ "InfernoRed"
[23]: https://voting.works/ "Voting works - Elections you can trust"
[24]: https://civicdesign.org/ "Center for civic design"
[25]: https://oxidedesign.com/ "Oxide Design"
