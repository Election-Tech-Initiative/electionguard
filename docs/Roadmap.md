
# Roadmap

This page outlines specific features and fixes that are scheduled or planned for given releases. We typically look out 6 months and we establish topics we want to work on. We don't start with our roadmap on a blank sheet. We develop it based on our last roadmap, the findings we made over the course of the last year, and of course what we heard from you.

When we execute on our roadmap, we keep learning and our assessment of some of the topics listed changes. As a result, we may add or drop topics as we go. As always, we listen to your feedback and adapt our plans if needed.

**Legend of annotations:**

| Mark	                             | Description        |
| :--------------------------------: | :----------------- |
| :fontawesome-regular-circle:       | Not Started        |
| :fontawesome-solid-spinner:	     | In Progress        |
| :fontawesome-regular-check-circle: | Completed          |



## Future

:fontawesome-regular-circle: Improve serialization and deserialization of python models


## 2021

**Specification**

:fontawesome-solid-spinner: Update to 1.0.0 including updates to election manifest and election artifact descriptions and specifications

**Python**

:fontawesome-solid-spinner: Compose community changes into `electionguard-python` release v1.1.16 

:fontawesome-regular-circle: Add core optimization changes for service implementations as `electionguard-python` release v1.2.0 

:fontawesome-regular-circle: Introduce service docker containers in `electionguard-api`

**C++**

:fontawesome-solid-spinner: Release `electionguard-cpp` as an open source project

:fontawesome-solid-spinner: Release a `ElectionGuard.Encrypt` nuget package from `electionguard-cpp` as a ballot encrypter for low performance devices to encrypt ballots

## 2019-2020

**Overview**

:fontawesome-regular-check-circle: Integrate electionguard into [various election tools](ElectionTools).

:fontawesome-regular-check-circle: Run a verifiable election for [Fulton in Wisconsin](Fulton) utilizing smart cards, QR scanners, a ballot box, an admin device, and a ballot tracking site.

**Specification**

:fontawesome-regular-check-circle: Update the ElectionGuard specification to 0.95.0

**Python**

:fontawesome-regular-check-circle: Release and iterate on `electionguard-python` as a core implementation meeting specification 0.95.0

**C**

:fontawesome-regular-check-circle: Introduce the world to ElectionGuard capabilities with `electionguard-c` as a core implementation meeting specification 0.85.0




<!-- Links -->
[ElectionTools]: https://blogs.microsoft.com/on-the-issues/2020/12/04/electionguard-2020-elections-security-pilot/
[Fulton]: https://news.microsoft.com/on-the-issues/2020/05/13/microsoft-electionguard-pilot-wisconsin/

[Python 1.15.0]: https://github.com/microsoft/electionguard-python/releases/tag/1.1.15
