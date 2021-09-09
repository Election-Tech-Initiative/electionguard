# Architecture

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
