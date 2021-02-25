# ElectionGuard Roadmap

![Microsoft Defending Democracy Program: ElectionGuard](images/electionguard-banner.svg)
## 2021 Roadmap

Our 2021 roadmap takes the learnings from the different applications we deployed in 2020 and rationalizes them into a *practice* we hope to establish with the community in 2021. Our goal is to empower a community of participants and contributors within which Microsoft takes part in and provides architectural and implementation guidance, but is fundamentally driven by the needs of the community in establishing the best ways to implement end-to-end verifiable elections and post-election audits.

We took a big step toward this new vision with the release of the `electionguard-cpp` ballot-encryption repo. Combined with the `electionguard-python` repo that implements the full suite of ElectionGuard SDK functionality and the base `electionguard` specification and documentation repo, we have laid the foundation for our future direction. Our goal for the first half of 2021 is to have a full suite of code, tests, workflows, and package deployments more directly associated with the conventions and requirements indicated by the specification. We plan to publish and generate both more comprehensive but also granular examples and use cases to enable easier and more focused contributions by the community as well.

We will also continue to enthusiastically support innovative pilot opportunities exemplifying end-to-end verifiable elections and post-election audits. Join our [monthly calls](https://github.com/microsoft/electionguard/discussions/61), post ideas and issues, and otherwise [let us know](mailto:electionguard@microsoft.com) how ElectionGuard can help improve trust in elections.

??? todo "1.0 Specification"
    * a final, fully-developed specification integrated directly into the SDK;
    * updates to election manifest and election artifact descriptions and specifications
    * a more modular approach to documentation and contribution to lessen the learning curve and overhead necessary to participate and contribute
    * more prescriptive guidance on verifier construction


??? done "C++ ballot encryption library"
    * repo that performs encryption exclusively (for embedded encryption applications such as precinct scanners)
    * standalone source that uses a version of HACL* packaged up by [EverCrypt](https://github.com/project-everest/hacl-star#evercrypt) for high assurance (thank you EverCrypt team!)
    * enables ElectionGuard to eliminate GMP as a dependency 

??? todo "Release an ElectionGuard.Encrypt nuget package built from `electionguard-cpp` as a ballot encrypter for low performance devices"
    * Establish publishing pattern
    * First target will be [Windows 10 / UWP](https://docs.microsoft.com/en-us/windows/uwp/get-started/universal-application-platform-guide)

??? todo  "A consistent, efficient set of data interfaces across the ElectionGuard, C++, and Python repos"
    * Data serialization using [Protobuf](https://github.com/protocolbuffers/protobuf) for input/output/data consistency across `electionguard-cpp` and `electionguard-python`
    * Restructuring ballot and device aggregation to better support audits and scalability in general
    * Renaming and refactoring all repos for more descriptive and specific naming patterns

??? todo "Compose community changes into `electionguard-python` release v1.1.16"

??? todo "Optimization changes for service implementations of `electionguard-python` release v1.2.0 "

??? todo "Introduce service docker containers in `electionguard-api`"

??? done "Migrate 0.95 specification to Github"
    * Implement specification in diffable, searchable format in Github
    * Adopt [mkdocs material template](https://squidfunk.github.io/mkdocs-material/) for documentation and integrate with remaining ElectionGuard guide

## 2020 In Review

2020 taught many lessons. 

In the first half of the year, after our successful [Fulton, WI Election Pilot](https://www.cnn.com/2020/02/22/tech/microsoft-election-guard-voting-test/index.html) with [VotingWorks](https://voting.works) and [InfernoRed](https://infernored.com) as well as feedback from our [Bounty Program](https://www.microsoft.com/en-us/msrc/bounty-electionguard), we chose to migrate from the C library we released in September 2019 to [Python](https://github.com/microsoft/electionguard-python) and [establish a revamped reference implementation](https://github.com/microsoft/electionguard-python) in a language suitable for translation into multiple *other* languages. (As such, our implementation doesn't focus on *Pythonic* optimizations necessarily, but  emphasizes structures and practices replicable across many languages.)

In the [second half of the year](https://blogs.microsoft.com/on-the-issues/2020/12/04/electionguard-2020-elections-security-pilot/), responding to COVID caused us to develop a remote voting app with [InfernoRed](https://infernored.com), [Markup](https://markup.law), and the US House Democratic Caucus to enable representatives to [vote by secret ballot safely, securely, and remotely for Caucus leadership positions](https://www.dems.gov/newsroom/press-releases/house-democrats-successfully-conclude-first-ever-virtual-leadership-elections). We also worked with the Canadian voting company [Neuvote](https://neuvote.com) to showcase their electronic- and remote-paper-based system in Brazil as part of a demonstration of future voting system options.

We also had the opportunity to further collaborate with VotingWorks, this time on post-election audits. Driven principally by Rice University professor Dan Wallach's work with [Arlo](https://voting.works/risk-limiting-audits/), ElectionGuard provided the "back end" for [Inyo County's Risk-limiting Audit of the November 3 election](https://elections.inyocounty.us/post-election-audits/).  

Last and definitely not least, we had our [first independent verifiers developed and published](Contributions.md).

We thank all our collaborators and contributors for their contributions, of course, but also how they're informing our future direction.


## 2020 Roadmap

??? done "Use ElectionGuard in a real-world end-to-end verifiable election"
    * Run a verifiable election [Fulton, Wisconsin](Fulton) with [VotingWorks](https://voting.works) using smart cards, a ballot box, an admin device, and a ballot tracking site.
    * Integrate ElectionGuard with the VotingWorks print station and user flow
    * Build ballot box functionality to capture and seal ballots
    * Build admin device to enable tallies and key ceremonies
    * Build tracking site to enable verification code lookup and tally/results download

??? done "Use ElectionGuard in a real-world post-election audit"
    * Run a post-election election audit with Inyo, California using [VotingWorks Arlo](https://voting.works) using ElectionGuard as a back end
    * Identify learnings and code refactoring necessary to reflect the different data structures and scalability considerations of audits

??? done "Update the ElectionGuard specification to 0.95.0"

??? done "Support building ElectionGuard into additional voting systems"
    * Enable remote, secret-ballot voting for Democratic Caucus of the US House of Representatives
    * Work with [InfernoRed](https://infernored.com) and [Markup](https://markup.law) to enable House-distributed iPhones to perform ballot encryption and House Democratic leadership to schedule and tally secret-ballot elections for leadership and committee positions

??? done "Release and iterate on `electionguard-python` as a core implementation that meets specification 0.95.0"
    * Implement a *canonical* library addressing all ElectionGuard SDK functionality:
      * Key generation
      * Ballot encryption
      * Ballot sealing 
      * Tally generation
      * Verifier specification
    * Build library with an eye to *extensibility* rather than performance and local language optimization (i.e., we'll be less *Pythonic* than some might prefer for the base implementation)


??? done "Integrate ElectionGuard into a [set of election tools](ElectionTools)"
## 2019 Roadmap

??? done "Initial specification and `electionguard-c` release"

??? done "Demonstrate ElectionGuard Reference Implementation at Aspen Security Conference"


<!-- Links -->
[ElectionTools]: https://blogs.microsoft.com/on-the-issues/2020/12/04/electionguard-2020-elections-security-pilot/
[Fulton]: https://news.microsoft.com/on-the-issues/2020/05/13/microsoft-electionguard-pilot-wisconsin/

[Python 1.15.0]: https://github.com/microsoft/electionguard-python/releases/tag/1.1.15
