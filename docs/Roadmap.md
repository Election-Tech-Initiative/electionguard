# ElectionGuard Roadmap

![Microsoft Defending Democracy Program: ElectionGuard](images/electionguard-banner.svg)
## 2021 Roadmap

??? todo "1.0 Specification"
    * a final, fully-developed specification integrated directly into the SDK;
    * updates to election manifest and election artifact descriptions and specifications
    * a more modular approach to documentation and contribution to lessen the learning curve and overhead to participate


??? done "C++ ballot encryption library"
    * repo that performs encryption exclusively (for embedded encryption applications)"
    * a final, fully-developed specification integrated directly into the SDK;

??? todo "Release an ElectionGuard.Encrypt nuget package from electionguard-cpp as a ballot encrypter for low performance devices"
     / environment configurations off the Python repo (for E2E-V and audit applications)

??? todo  "A consistent, efficient set of data interfaces across the ElectionGuard, C++, and Python repos"

??? todo "Compose community changes into `electionguard-python` release v1.1.16"

??? todo "Optimization changes for service implementations of `electionguard-python` release v1.2.0 "

??? todo "Introduce service docker containers in `electionguard-api`"

## 2020 In Review

2020 taught many lessons. 

In the first half of the year, after our successful [Fulton, WI Election Pilot](https://www.cnn.com/2020/02/22/tech/microsoft-election-guard-voting-test/index.html) with [VotingWorks](https://voting.works) and [InfernoRed](https://infernored.com) as well as feedback from our [Bounty Program](https://www.microsoft.com/en-us/msrc/bounty-electionguard), we chose to migrate from the C library we released in September 2019 to [Python](https://github.com/microsoft/electionguard-python) and [establish a revamped reference implementation](https://github.com/microsoft/electionguard-python) in a language suitable for translation into multiple *other* languages. (As such, our implementation doesn't focus on *Pythonic* optimizations necessarily, but  emphasizes structures and practices replicable across many languages.)

In the [second half of the year](https://blogs.microsoft.com/on-the-issues/2020/12/04/electionguard-2020-elections-security-pilot/), responding to COVID caused us to develop a remote voting app with [InfernoRed](https://infernored.com), [Markup](https://markup.law), and the US House Democratic Caucus to enable representatives to [vote by secret ballot safely, securely, and remotely for Caucus leadership positions](https://www.dems.gov/newsroom/press-releases/house-democrats-successfully-conclude-first-ever-virtual-leadership-elections). We also worked with the Canadian voting company [Neuvote](https://neuvote.com) to showcase their electronic- and remote-paper-based system in Brazil as part of a demonstration of future voting system options.

We also had the opportunity to further collaborate with VotingWorks, this time on post-election audits. Driven principally by Rice University professor Dan Wallach's work with [Arlo](https://voting.works/risk-limiting-audits/), ElectionGuard provided the "back end" for [Inyo County's Risk-limiting Audit of the November 3 election](https://elections.inyocounty.us/post-election-audits/).  

Last and definitely not least, we had our [first independent verifiers developed and published](guide/Implementations.md).

We thank all our collaborators and contributors for their contributions, of course, but also how they're informing our future direction.


## 2020 Roadmap

??? done "Run a Verifiable Election"
    Run a verifiable election for [Fulton in Wisconsin](Fulton) utilizing smart cards, QR scanners, a ballot box, an admin device, and a ballot tracking site.


??? done "Integrate electionguard into [various election tools](ElectionTools)"

??? done "Run a verifiable election for [Fulton in Wisconsin](Fulton) using smart cards, a ballot box, an admin device, and a ballot tracking site"

??? done "Update the ElectionGuard specification to 0.95.0"

??? done "Release and iterate on `electionguard-python` as a core implementation that meets specification 0.95.0"

## 2019 Roadmap

??? done "Release `electionguard-c` as a core implementation meeting specification 0.85.0"


<!-- Links -->
[ElectionTools]: https://blogs.microsoft.com/on-the-issues/2020/12/04/electionguard-2020-elections-security-pilot/
[Fulton]: https://news.microsoft.com/on-the-issues/2020/05/13/microsoft-electionguard-pilot-wisconsin/

[Python 1.15.0]: https://github.com/microsoft/electionguard-python/releases/tag/1.1.15
