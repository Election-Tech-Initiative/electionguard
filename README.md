[![Microsoft Defending Democracy Program: ElectionGuard][election-guard-banner]](http://microsoft.github.io/electionguard/)

[![license][license-image]](LICENSE)

ElectionGuard is an **open source** software development kit (SDK) that makes voting more secure, transparent and accessible. Announced at the [Build developer conference][build-developer-conference], ElectionGuard enables end-to-end verification of elections as well as support the publication of results from ballot comparison audits. The ElectionGuard SDK leverages [homomorphic encryption][homomoprhic-encryption] to ensure that votes recorded by electronic systems of any type remain encrypted, secure, and secret. Results can be published online or made available to third-party organizations for secure validation, and allow individual voters to confirm their votes were correctly counted.

## ❤️ Open-Source

This library and all linked ElectionGuard projects, are licensed under the MIT license. There is no fee for using ElectionGuard.

## 🚀 Getting Started

ElectionGuard is always improving. To keep up with the latest, check our **[official site on GitHub Pages][election-guard-official-page]** and our [roadmap][election-guard-road-map]. For those looking to get started, we recommend the following repositories.

### Documentation

This repository is a living document to help everyone interact with ElectionGuard. The [official ElectionGuard site][election-guard-official-page] is built using the `/docs` folder and [mkdocs][mkdocs-official-site] with [mkdocs-material][material-mkdocs]. Ensure you have the Python 3.8 or newer installed and run `make` to install the dependencies and start the site.

#### Setup

This repo uses [pipenv](https://pipenv.pypa.io/en/latest/) for package and environment management. Disregard the `requirements.txt` file as it will be removed in a subsequent release.

1. Install packages

```sh
pipenv install
```

1. Run `make build` command from within the virtualenv

```sh
pipenv run make build
```

1. Serve the site

```sh
pipenv run make serve
```

### C ++

An ElectionGuard Core implemented in C++ to support ballot encryption and all phases of the Guardian key and tally ceremonies, including creation of the election package and production of the election record.

[📁 Source][election-guard-core2] |
[📦 Package][election-guard-core2-package] |
[📝 Documentation][election-guard-core2-documentation]

## 🛡 Security Issues Reporting

We encourage the developer and security community to conduct research, report issues, and suggest improvements on this code base. However, unlike performance or feature bugs, please do **not** report security vulnerabilities in public Github comments. Each repository has a SECURITY file with instructions on responsibly reporting security vulnerabilities under Microsoft's CVD process.

## 🤝 Contributing

Help defend democracy and **[contribute to the project][]**.

[code of conduct]: CODE_OF_CONDUCT.md
[contribute to the project]: CONTRIBUTING.md

We welcome discussions on our [discussions page][election-guard-discussions], feel free to check in and ask your questions and drop your suggestions regarding the specifications over there.

## ❓ Questions

ElectionGuard would love for you to ask questions out in the open using Github Issues. If you really want to email the ElectionGuard team, reach out via the discussions page.

## 🎉 Thanks!

A huge thank you to those who helped to contribute to this project so far.

<!-- Links -->
[election-guard-banner]: docs/images/electionguard-banner.svg "Election Guard banner SVG"
[license-image]: https://img.shields.io/github/license/microsoft/electionguard "Election Guard license image"
[build-developer-conference]: https://blogs.microsoft.com/on-the-issues/?p=63211 "Protecting democratic elections through secure, verifiable voting"
[homomoprhic-encryption]: https://en.wikipedia.org/wiki/Homomorphic_encryption "Homomorphic encryption"
[election-guard-official-page]: https://microsoft.github.io/electionguard "Official Election Guard site on Github Pages"
[election-guard-road-map]: https://www.electionguard.vote/overview/Roadmap/ "Election Guard road map"
[mkdocs-official-site]: https://www.mkdocs.org/ "MkDocs official website"
[material-mkdocs]: https://squidfunk.github.io/mkdocs-material/ "Material for MkDocs"
[election-guard-core2-source-code]: https://github.com/microsoft/electionguard-core2/ "Election Guard C++ source code"
[election-guard-ui-source]: https://github.com/microsoft/electionguard-ui "Election Guard UI source code"
[election-guard-ui-documentation]: https://github.com/microsoft/electionguard-ui#readme "Election Guard UI documentation"
[election-guard-discussions]: https://github.com/microsoft/electionguard/discussions "Election Guard Discussions page"
[verifiable-search-ballot-elections-paper]: https://www.microsoft.com/en-us/research/publication/verifiable-secret-ballot-elections/ "Verifiable Secret-Ballot Elections - Microsoft Research, Josh Benaloh"
[infernored]: https://infernored.com/ "InfernoRed"
[voting-works]: https://voting.works/ "Voting works - Elections you can trust"
[center-for-civic-design]: https://civicdesign.org/ "Center for Civic Design"
[oxide-design]: https://oxidedesign.com/ "Oxide Design"
