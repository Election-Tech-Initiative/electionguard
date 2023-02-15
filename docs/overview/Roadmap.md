# ElectionGuard Roadmap

![Roadmap][roadmap-image]

## 2023 Roadmap

Coming soon

## 2022 Roadmap

Coming soon

## 2021 Roadmap

The 2021 roadmap takes lessons learned from the deployment of applications during 2020 and rationalizes them into a *practice* to establish with the community in 2021. The goal is to grow a community of participants and contributors within which Microsoft takes part and provides architectural and implementation guidance, but is fundamentally driven by the needs of the community in establishing the best ways to implement end-to-end verifiable elections and post-election audits.

A big step toward this new vision occurred with the release of the `electionguard-cpp` ballot-encryption repo. The `electionguard-python` repo implements the full suite of ElectionGuard SDK functionality and the base `electionguard` specification and documentation repo provides the foundation for future development. The goal for the first half of 2021 is to have a full suite of code, tests, workflows, and package deployments more directly associated with the conventions and requirements indicated by the specification. The goal is also to publish and generate more comprehensive and also more granular examples and use cases to enable easier and more focused contributions by the community.

??? todo "1.0 Specification"

    * a final, fully-developed specification integrated directly into the SDK;
    * updates to election manifest and election artifact descriptions and specifications
    * a more modular approach to documentation and contribution to lessen the learning curve and overhead necessary to participate and contribute
    * more prescriptive guidance on verifier construction


??? done "C++ ballot encryption library"

    * repo that performs encryption exclusively (for embedded encryption applications such as precinct scanners)
    * standalone source that uses a version of HACL* packaged up by [EverCrypt][evercrypt] for high assurance (thank you EverCrypt team!)
    * enables ElectionGuard to eliminate GMP as a dependency 

??? done "Release an ElectionGuard.Encryption nuget package built from `electionguard-cpp` as a ballot encrypter for low performance devices"

    * Establish publishing pattern
    * First target will be [Windows 10 / UWP][windows-universal-application-guide]

??? todo  "A consistent, efficient set of data interfaces across the ElectionGuard, C++, and Python repos"

    * Data serialization using [Protobuf][protobuf-source] for input/output/data consistency across `electionguard-cpp` and `electionguard-python`
    * Restructuring ballot and device aggregation to better support audits and scalability in general
    * Renaming and refactoring all repos for more descriptive and specific naming patterns

??? done "Compose community changes into `electionguard-python` release v1.1.16"

??? todo "Optimization changes for service implementations of `electionguard-python` release v1.4.0 "

??? done "Introduce service docker containers in `electionguard-api`"

## 2020 In Review

2020 provided many lessons.

During the first half of the year ElectionGuard was used successfully as a [Pilot in Fulton, WI][fulton-wi-election-pilot] with the help of [VotingWorks][voting-works] and [InfernoRed][infernored]. Subsequent to the pilot ElectionGuard released the [Python][election-guard-python-source] repo as a new reference implementation.

In the [second half of the year][election-guard-security-pilot], responding to COVID, led to the development of a remote voting app with [InfernoRed][infernored], [Markup][markup], and the US House Democratic Caucus to enable representatives to [vote by secret ballot safely, securely, and remotely for Caucus leadership positions][dems-virtual-leadership-election]. 

In a further collaborate with VotingWorks, Rice University professor Dan Wallach contributed an integration with [Arlo][arlo] to enable ElectionGuard to provide the "back end" for [Inyo County's Risk-limiting Audit of the November 3 election][inyo-risk-limiting-audit].  

Last, and definitely not least, ElectionGuard [developed and published its first independent verifiers][election-guard-contribute].

## 2020 Roadmap

??? done "Use ElectionGuard in a real-world end-to-end verifiable election"

    * Run a verifiable election [Fulton, Wisconsin][Fulton] with [VotingWorks][voting-works] using smart cards, a ballot box, an admin device, and a ballot tracking site.
    * Integrate ElectionGuard with the VotingWorks print station and user flow
    * Build ballot box functionality to capture and seal ballots
    * Build admin device to enable tallies and key ceremonies
    * Build tracking site to enable verification code lookup and tally/results download

??? done "Use ElectionGuard in a real-world post-election audit"

    * Run a post-election election audit with Inyo, California using [VotingWorks Arlo][voting-works] using ElectionGuard as a back end
    * Identify learnings and code refactoring necessary to reflect the different data structures and scalability considerations of audits

??? done "Update the ElectionGuard Specification to 1.0.0-preview-1"

??? done "Support building ElectionGuard into additional voting systems"

    * Enable remote, secret-ballot voting for Democratic Caucus of the US House of Representatives
    * Work with [InfernoRed][infernored] and [Markup][markup] to enable House-distributed iPhones to perform ballot encryption and House Democratic leadership to schedule and tally secret-ballot elections for leadership and committee positions

??? done "Release and iterate on `electionguard-python` as a core implementation that meets specification 1.0.0-preview-1"

    * Implement a *canonical* library addressing all ElectionGuard SDK functionality:
      * Key generation
      * Ballot encryption
      * Ballot sealing 
      * Tally generation
      * Verifier specification
    * Build library with an eye to *extensibility* rather than performance and local language optimization (i.e., we'll be less *Pythonic* than some might prefer for the base implementation)

??? done "Integrate ElectionGuard into a [set of election tools][ElectionTools]"

## 2019 Roadmap

??? done "Initial specification and `electionguard-c` release"

??? done "Demonstrate ElectionGuard Reference Implementation at Aspen Security Conference"

<!-- Links -->
[ElectionTools]: https://blogs.microsoft.com/on-the-issues/2020/12/04/electionguard-2020-elections-security-pilot/
[Fulton]: https://news.microsoft.com/on-the-issues/2020/05/13/microsoft-electionguard-pilot-wisconsin/
[roadmap-image]: ../images/undraw/roadmap.svg "Image of a car on a road with mountains"
[evercrypt]: https://github.com/project-everest/hacl-star#evercrypt "Evercrypt"
[windows-universal-application-guide]: https://docs.microsoft.com/en-us/windows/uwp/get-started/universal-application-platform-guide "Windows Universal APplication platform guide"
[election-guard-python-source]: https://github.com/microsoft/electionguard-python "Election Guard Python source code"
[election-guard-security-pilot]: https://blogs.microsoft.com/on-the-issues/2020/12/04/electionguard-2020-elections-security-pilot/ "Election Guard security pilot 2020"
[protobuf-source]: https://github.com/protocolbuffers/protobuf "Protobuf source code"
[fulton-wi-election-pilot]: https://www.cnn.com/2020/02/22/tech/microsoft-election-guard-voting-test/index.html "Fulton, Wisconsin election pilot"
[voting-works]: https://voting.works "Voting works"
[arlo]: https://voting.works/risk-limiting-audits/ "Voting Works risk limiting audits"
[inyo-risk-limiting-audit]: https://elections.inyocounty.us/post-election-audits/ "Inyo's risk limiting post-election audit"
[infernored]: https://infernored.com "InfernoRed"
[markup]: https://markup.law
[dems-virtual-leadership-election]: https://www.dems.gov/newsroom/press-releases/house-democrats-successfully-conclude-first-ever-virtual-leadership-elections "house democrats successfully conclude first-ever virtual leadership elections"

[election-guard-contribute]: ../contribute/index.md "Election Guard Contribute"
