# Getting Started

If you're looking to develop for ElectionGuard, it might help if you pick something you're familiar with. The following repositories showcase the language to assist you in finding the right place. Each repository contains information on the best way to contribute and how to setup the development environment. Take a look and see what appeals to you.

![Code](../images/undraw/code_1.svg)

## <div style="display: flex; align-items: center;">ElectionGuard Specification<span style="display: flex; align-items: center; margin-left: 16px"> ![Markdown](../images/markdown-language.png) <span></div>

The ElectionGuard Specification repo addresses the mathematical and conceptual underpinnings of end-to-end verifiability in a manner that comfortably accommodates post-election audits. The specification houses the core data constructs, tests, and datasets that we recommend to ensure portability and data integrity.

The ElectionGuard site is also built from this repository using mkdocs. This can be a friendly place to start out for new developers trying to get started.

[:fontawesome-brands-github: ElectionGuard Specification](../spec/0.95.0/1_Overview.md)

## <div style="display: flex; align-items: center;">ElectionGuard Python<span style="display: flex; align-items: center; margin-left: 16px"> ![Python](../images/python-language.png) <span></div>

The ElectionGuard Python library is the _reference implementation_ of the ElectionGuard SDK. It covers the entire suite of functionality and processes necessary to implement an end-to-end verifiable election as part a voting system:

- Key generation ceremony
- Ballot encryption
- Tally ceremony
- Ballot decryption

It is designed to be _portable_ over _performant_, _universal_ over _Pythonic_ (although we do try to adhere to the [Zen of Python](https://www.python.org/dev/peps/pep-0020/)).

Any real-world voting use case will need to incorporate the capabilities of the Python library to run an [end-to-end verifiable election](../concepts/Verifiability.md) or [post-election audit](../Glossary/#post-election-audit).

[:fontawesome-brands-github: Source](https://github.com/microsoft/electionguard-python) | [:fontawesome-brands-python: Package](https://pypi.org/project/electionguard/) | [:fontawesome-regular-file: Documentation](https://microsoft.github.io/electionguard-python/)

!!! info "Community-sourced Java port"
    Check out our [community contributions for a java port](../contribute/index.md).

## <div style="display: flex; align-items: center;">ElectionGuard C++<span style="display: flex; align-items: center; margin-left: 16px"> ![C++](../images/c++-language.png)![C++](../images/c-language.png)![C#](../images/c-sharp-language.png) <span></div>

The ElectionGuard C++ library performs ballot encryption. It is designed for devices that handle the user experience of voting. These devices follow the economics and performance of embedded systems: special-purpose devices designed for low cost. We assume Intel Atom class processor-level performance and Raspberry Pi 3 types of operating systems. In addition to the C++ library itself, there is some focus on target different standalone packages. This leads to the usage of other languages like C and C#.

[:fontawesome-brands-github: Source](https://github.com/microsoft/electionguard-cpp)
