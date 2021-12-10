# Architecture

There are five repositories in the ElectionGuard SDK.

- [ElectionGuard Specification][election-guard-specification]
- [ElectionGuard Python][election-guard-python-source]
- [ElectionGuard C++][election-guard-cpp-source-code]
- [ElectionGuard Python API][election-guard-web-api-source]
- [ElectionGuard React UI][election-guard-ui-source]

The specification repository focuses on explaining ElectionGuard as a whole including documentation and the specification itself. The other repositories are all reference implementations. These reference implementations are designed to demonstrate to developers how to implement a system using the ElectionGuard specification. In depth descriptions of the repositories are detailed in the [repositories][repositories] page.

With the specification as guidance, the reference repositories take two pathways; one starting with Python and one starting with C++. Each of these creating a stack. This chart shows the relationship of the specification to the reference implementations by repository. This paints the picture of how the repositories are related to each other.  

```mermaid
flowchart TD
    spec["electionguard"] -.-> |Python|e-python["electionguard-python"];
    spec["electionguard"] -.-> |C++|e-cpp["electionguard-cpp"];
    e-python --> web-api["electionguard-api-python"];
    web-api --> e-ui["electionguard-ui"];
```

Using more plain language, the specification is the guide used to create the core repositories. There are two main paths within the core reference implementations of ElectionGuard. At the base, one is written in Python and one is written in C++. These can used together, but have different feature sets.  

```mermaid
flowchart TD
    specification -.-> |Python|python["full featured core"];
    specification -.-> |C++|cpp["encryption core"];
    python --> api["web-api"];
    api --> ui["user interface"];
```

The Python reference implementation is full featured including all elements of the specification to showcase ElectionGuard to its fullest. The C++ reference implementation is designed with a focus on encrypting ballots. Its goal is to allow developers to use the ElectionGuard encryption on encryption devices.

| Feature           | `electionguard-python` |  `electionguard-cpp` |
| ----------------- | :--------------------: | :------------------: |
| Ballot Encryption | :material-check:       | :material-check:     |
| Ballot Decryption | :material-check:       |                      |
| Key Generation    | :material-check:       |                      |
| Key Ceremony      | :material-check:       |                      |
| Tally Ceremony    | :material-check:       |                      |
| Tally Decryption  | :material-check:       |                      |


## Python Stack

The Python reference implementation is full featured including all elements of the specification to showcase ElectionGuard to its fullest. There is a full stack provided for Python so there are many different approaches and entry points a developer could use when starting here. The following suggested approaches can be used to develop apps like those listed in the [applications][application-paths] list.

### Suggested Approaches

**Approach 1:** Build a Python app utilizing `electionguard-python` package

**Approach 2:** Utilize `election-api-python` as API and integrating `electionguard-ui`'s api client into a web app.

**Approach 3:** Utilize `election-api-python` as API with a web app directly consuming api.

**Approach 4:** Utilize `electionguard-api-python` and fork `electionguard-ui`'s web apps

## C++ Stack

For the C++ stack, the included C++ reference implementation and resulting packages are currently designed with a focus on encrypting ballots. Its goal is to allow developers to use ElectionGuard encryption on encryption devices. The following suggested approaches can be used to develop a ballot encryption app or integration as described in the [applications][application-encryption] list.

### Suggested Approaches

**Approach 1:** Use C++ directly

**Approach 2:** Use Nuget Package


[repositories]: ../Repositories
[application-paths]: ../Applications/#paths
[application-encryption]: ../Applications/#ballot-encryption
[election-guard-specification]: https://github.com/microsoft/electionguard "Election Guard Github"
[election-guard-python-source]: https://github.com/microsoft/electionguard-python "Election Guard Python source code"
[election-guard-cpp-source-code]: https://github.com/microsoft/electionguard-cpp/ "Election Guard C++ source code"
[election-guard-web-api-source]: https://github.com/microsoft/electionguard-api-python "Election Guard Web API source code"
[election-guard-ui-source]: https://github.com/microsoft/electionguard-ui "Election Guard UI source code"