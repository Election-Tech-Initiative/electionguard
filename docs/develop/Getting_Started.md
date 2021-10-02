# Getting Started

If you're looking to develop for ElectionGuard, it might help if you pick something you're familiar with. The following repositories showcase the language to assist you in finding the right place. Each repository contains information on the best way to contribute and how to setup the development environment. Take a look and see what appeals to you.

![Code][code-image]

## <div style="display: flex; align-items: center;">ElectionGuard Specification<span style="display: flex; align-items: center; margin-left: 16px"> ![Markdown][markdown-logo] <span></div>

The ElectionGuard Specification repo addresses the mathematical and conceptual underpinnings of end-to-end verifiability in a manner that comfortably accommodates post-election audits. The specification houses the core data constructs, tests, and datasets that we recommend to ensure portability and data integrity.

The ElectionGuard site is also built from this repository using mkdocs. This can be a friendly place to start out for new developers trying to get started.

[:fontawesome-brands-github: ElectionGuard Specification][election-guard-spec-overview]

## <div style="display: flex; align-items: center;">ElectionGuard Python<span style="display: flex; align-items: center; margin-left: 16px"> ![Python][python-logo] <span></div>

The ElectionGuard Python library is the _reference implementation_ of the ElectionGuard SDK. It covers the entire suite of functionality and processes necessary to implement an end-to-end verifiable election as part a voting system:

- Key generation ceremony
- Ballot encryption
- Tally ceremony
- Ballot decryption

It is designed to be _portable_ over _performant_, _universal_ over _Pythonic_ (although we do try to adhere to the [Zen of Python][zen-of-python]).

Any real-world voting use case will need to incorporate the capabilities of the Python library to run an [end-to-end verifiable election][election-guard-verifiability] or [post-election audit][election-guard-post-election-audit].

[:fontawesome-brands-github: Source][election-guard-python-source] | 
[:fontawesome-brands-python: Package][election-guard-python-package] | 
[:fontawesome-regular-file: Documentation][election-guard-python-documentation]

!!! info "Community-sourced Java port"
    Check out our [community contributions for a java port](../contribute/index.md).

## <div style="display: flex; align-items: center;">ElectionGuard C++<span style="display: flex; align-items: center; margin-left: 16px"> ![C++][cpp-logo]![C][c-logo]![C#][c-sharp-logo] <span></div>

The ElectionGuard C++ library performs ballot encryption. It is designed for devices that handle the user experience of voting. These devices follow the economics and performance of embedded systems: special-purpose devices designed for low cost. We assume Intel Atom class processor-level performance and Raspberry Pi 3 types of operating systems. In addition to the C++ library itself, there is some focus on target different standalone packages. This leads to the usage of other languages like C and C#.

[:fontawesome-brands-github: Source][election-guard-cpp-source]

<!-- Links -->
[code-image]: ../images/undraw/code_1.svg "Two people sitting at a computer"
[markdown-logo]: ../images/markdown-language.png "Markdown logo"
[python-logo]: ../images/python-language.png "Python logo"
[cpp-logo]: ../images/c++-language.png "C++ logo"
[c-logo]: ../images/c-language.png "C logo"
[c-sharp-logo]: ../images/c-sharp-language.png "C# logo"


[zen-of-python]: https://www.python.org/dev/peps/pep-0020/ "Zen of Python - Tim Peters"
[election-guard-python-source]: https://github.com/microsoft/electionguard-python "Election Guard Python source code"
[election-guard-python-package]: https://pypi.org/project/electionguard/ "Election Guard Python package"
[election-guard-python-documentation]: https://microsoft.github.io/electionguard-python/ "Election Guard Python documentation"
[election-guard-cpp-source]: https://github.com/microsoft/electionguard-cpp "Election Guard C++ source code"

[election-guard-spec-overview]: ../spec/0.95.0/1_Overview.md "Election Guard Specification Overview"
[election-guard-verifiability]: ../concepts/Verifiability.md "Election Guard Verifiability"
[election-guard-post-election-audit]: ../Glossary/#post-election-audit "Election Guard Post-Election Audit"