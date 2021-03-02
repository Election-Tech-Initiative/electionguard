# Getting Started

There are many ways to adopt or contribute to ElectionGuard. It is an open source platform and depends on an active community and ecosystem.

The ElectionGuard SDK comprises three Github repos:

* ElectionGuard Specification
* ElectionGuard Python
* ElectionGuard C++

Whenever possible and as a guiding principle, the evolution of the ElectionGuard SDK will be driven by the use cases and priorities of the community and in service of best-practice implementations of real-world, secret-ballot public elections

!!! info "Ways to get involved and find out what's actively being worked on"
    If you have questions or ideas, there are multiple ways to get feedback and help:
    
    * Post questions or ideas in our [***discussion boards***](https://github.com/microsoft/electionguard/discussions) 
    * Join our [monthly ***office hours videoconference***](https://github.com/microsoft/electionguard/discussions/61)
    * Check out and volunteer to work on issues in the repos with tags of [**good first issue**](https://github.com/microsoft/electionguard-python/labels/good%20first%20issue), [**help wanted**](https://github.com/microsoft/electionguard-cpp/labels/help%20wanted) and, as always, [**documentation**](https://github.com/microsoft/electionguard/issues?q=is%3Aissue+is%3Aopen+label%3Adocumentation)


## ElectionGuard Specification

The ElectionGuard Specification repo addresses the mathematical and conceptual underpinnings of end-to-end verifiability in a manner that comfortably accommodates post-election audits.

The specification houses the core data constructs, tests, and datasets that we recommend to ensure portability and data integrity.

[:fontawesome-brands-github: **ElectionGuard Specification**](../../spec/0.95.0/1_Overview.md)
## ElectionGuard Python

![Python](../../images/python-language.png)

The ElectionGuard Python library is the *reference implementation* of the ElectionGuard SDK. It covers the entire suite of functionality and processes necessary to implement an end-to-end verifiable election as part a voting system: 

* Key generation ceremony
* Ballot encryption 
* Tally ceremony 
* Ballot decryption

It is designed to be *portable* over *performant*, *universal* over *Pythonic* (although we do try to adhere to the [Zen of Python](https://www.python.org/dev/peps/pep-0020/)).

Any real-world voting use case will need to incorporate the capabilities of the Python library to run an [end-to-end verifiable election](../use_cases/Verifiable_Election.md) or [post-election audit](../Glossary/#post-election-audit).

[:fontawesome-brands-github: **Source**](https://github.com/microsoft/electionguard-python) | [:fontawesome-brands-python: **Package**](https://pypi.org/project/electionguard/) | [:fontawesome-regular-file: **Documentation**](https://microsoft.github.io/electionguard-python/)

!!! info "Community-sourced Java port"
    ![Java](../../images/java.png) If you prefer Java, @JohnLCaron contributed a [**Java port**](https://github.com/JohnLCaron/electionguard-java) of our Python library. Thank you John! 
    
    [:fontawesome-brands-github: **Source**](https://github.com/JohnLCaron/electionguard-java)
## ElectionGuard C++

![C++](../../images/c++-language.png)

The ElectionGuard C++ library performs ballot encryption. It is designed for devices that handle the user experience of voting. These devices follow the economics and performance of embedded systems: special-purpose devices designed for low cost. We assume Intel Atom class processor-level performance and Raspberry Pi 3 types of operating systems. 

[:fontawesome-brands-github: **Source**](https://github.com/microsoft/electionguard-cpp)

In addition to the C++ library itself, we plan to target different standalone packages
