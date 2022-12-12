#

![Microsoft Defending Democracy Program: ElectionGuard][election-guard-banner]

???+ abstract "ElectionGuard Pilot Partners"
     In the Franklin County 2022 General Election, voters participated in a pilot of ElectionGuard technology. The ElectionGuard partners included:

     * [Hart InterCivic](https://www.hartintercivic.com/hart-and-microsoft-announce-partnership-to-make-elections-more-secure-verifiable/) integrated ElectionGuard software into their Verity® scanner for this election. Hart is the first major voting system manufacturer in the United States to provide independent verifiability. This pilot is part of their continued commitment to voting technology innovation that results in higher levels of voter confidence in the election process. 
     
     * The [Microsoft Democracy Forward](https://www.microsoft.com/en-us/corporate-responsibility/democracy-forward) program works to protect democratic processes through open and secure technologies. Microsoft sponsored the creation of the open-source software tools for ElectionGuard.   
     
     * [InfernoRed](https://www.infernored.com/work/microsoft-electionguard) is a premier independent software company that developed the open-source ElectionGuard SDK. 
     
     * The [MITRE](https://electionintegrity.mitre.org/verifier/) National Election Security Lab conducts cybersecurity assessments and testing to assist with securing election infrastructure. MITRE built a publicly available, independent verifier for ElectionGuard and verified the election results. 
     
     * [Enhanced Voting](https://www.enhancedvoting.com/projects/) creates voting solutions that are secure, easy-to-use, and accessible to all. They built the public website where voters checked their confirmation codes and hosted the ElectionGuard data package for the pilot.  
     
     * [Center for Civic Design](https://www.civicdesign.org) brought their design, research, and communication skills to collecting feedback from voters during the pilot election. 

!!! info "Idaho Pilot Information"
    If you are looking for information on the ElectionGuard Pilot in Preston, Idaho, click [here][IdahoPage]

## What is ElectionGuard?

ElectionGuard is an **open source** software development kit (SDK) that makes voting more secure, transparent and accessible. It is designed for election system vendors to incorporate [end-to-end verifiability][glossary-end-to-end-verifiable] into their systems and any interested organization to perform and publish [post-election audits][glossary-post-election-audit].

!!! info "New to ElectionGuard?"
    Welcome! Thanks for your interest. Trying to figure out how to help and learn? If you're a developer, head over to the [**developer getting started**][develop-getting-started]. If you're an election administrator or want to learn more about ElectionGuard and its underpinnings, start with [**the guide**][configure-an-election]. If you want to help and aren't a developer, all kinds of help with documentation, outreach, and advocacy is welcomed. Follow [**discussions**][election-guard-discussions], join the [**office hours**][weekly-office-hours], and check out the [**roadmap**][roadmap] to see where it's intended to go.

![Voting][casting-ballot]

## Open-Source

This library and all linked ElectionGuard projects, are licensed under the MIT license. There is no fee for using ElectionGuard.

## Security Issues Reporting

We encourage the developer and security community to conduct research, report issues, and suggest improvements on this code base. However, unlike performance or feature bugs, please do **not** report security vulnerabilities in public Github comments. Each repository has a SECURITY file with instructions on responsibly reporting security vulnerabilities under Microsoft's CVD process.

## Contributing

Help defend democracy and **[contribute to the project][contribute-index]**.

We welcome discussions on our [discussions page][election-guard-discussions], feel free to check in and ask your questions and drop your suggestions regarding the specifications over there.

## Questions

ElectionGuard would love for you to ask questions out in the open using Github Issues. If you really want to email the ElectionGuard team, reach out at [electionguard@microsoft.com][election-guard-email].

## Thank you

A huge thank you to those who have helped us along the way:

- Josh Benaloh (whose [PhD thesis][verifiable-search-ballot-elections-paper] was the genesis of much of this work)
- Our [**contributors**][contribute-index] and community
- [InfernoRed Technology][infernored]
- [Hart InterCivic](https://www.hartintercivic.com/)
- [MITRE](https://www.mitre.org/)
- [Enhanced Voting](https://www.enhancedvoting.com/)
- [VotingWorks][voting-works]
- [Center for Civic Design][center-for-civic-design]
- [Oxide Design][oxide-design]
- Many teams within Microsoft

<!-- Links -->
[election-guard-banner]: images/electionguard-banner.svg "ElectionGuard banner"
[IdahoPage]: events/Idaho_Pilot_2022.md "Pilot Site"
[casting-ballot]: images/undraw/voting.svg "Image of people casting ballots"

[election-guard-discussions]: https://github.com/microsoft/electionguard/discussions "ElectionGuard Discussions page"
[election-guard-email]: mailto:electionguard@microsoft.com "electionguard@microsoft.com"
[weekly-office-hours]: https://github.com/microsoft/electionguard/discussions/78
[verifiable-search-ballot-elections-paper]: https://www.microsoft.com/en-us/research/publication/verifiable-secret-ballot-elections/ "Verifiable Secret-Ballot Elections - Microsoft Research, Josh Benaloh"
[infernored]: https://infernored.com/ "InfernoRed"
[voting-works]: https://voting.works/ "Voting works - Elections you can trust"
[center-for-civic-design]: https://civicdesign.org/ "Center for Civic Design"
[oxide-design]: https://oxidedesign.com/ "Oxide Design"

[contribute-index]: contribute/index.md "Contributors"
[glossary-end-to-end-verifiable]: overview/Glossary/#end-to-end-verifiable-elections "End-to-End Verifiable Elections"
[glossary-post-election-audit]: overview/Glossary/#post-election-audit "Post-election audit"
[develop-getting-started]: develop/Getting_Started.md "Developer - Getting Started"
[configure-an-election]: basics/steps/0_Configure_Election.md "Configure an Election"
[roadmap]: overview/Roadmap.md "ElectionGuard - Roadmap"