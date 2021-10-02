# Repositories

The SDK is comprised of five repositories:

- [ElectionGuard Specification][election-guard-specification]
- [ElectionGuard Python][election-guard-python-source]
- [ElectionGuard C++][election-guard-cpp-source-code]
- [ElectionGuard Python API][election-guard-web-api-source]
- [ElectionGuard React UI][election-guard-ui-source]


![Code][code-image]

## Diagrams

```mermaid
flowchart TD
    subgraph "Repositories"
    spec["electionguard"] -.-> |python|e-python["electionguard-python"];
    spec["electionguard"] -.-> |C++|e-cpp["electionguard-cpp"];
    pypi --> web-api["electionguard-api-python"];
    e-python --> |pypi|pypi["python module: electionguard"]:::package;
    web-api --> e-ui["electionguard-ui"];
    e-cpp --> |nuget| nuget["ElectionGuard.Encryption"]:::package;
    end

    subgraph "Overview"
    specification -.-> |python|python["core"];
    specification -.-> |C++|cpp["encryption"];
    python --> |pypi|module:::package
    module --> api["web-api"];
    api --> ui["user interface"];
    cpp --> |nuget|package:::package
    end

    classDef package fill: teal, stroke: black;
```

<!-- Links -->
[election-guard-specification]: https://github.com/microsoft/electionguard "Election Guard Github"
[election-guard-python-source]: https://github.com/microsoft/electionguard-python "Election Guard Python source code"
[election-guard-cpp-source-code]: https://github.com/microsoft/electionguard-cpp/ "Election Guard C++ source code"
[election-guard-web-api-source]: https://github.com/microsoft/electionguard-api-python "Election Guard Web API source code"
[election-guard-ui-source]: https://github.com/microsoft/electionguard-ui "Election Guard UI source code"
[code-image]: ../images/undraw/code_2.svg "Image of two people using their laptops"
