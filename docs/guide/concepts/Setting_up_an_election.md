# Setting Up an Election

As discussed in detail in the [Precinct Scan](use_cases/Precinct_Scan.md) overview, ElectionGuard typically slots in alongside the hosting vendor system and *its* operation. In the case of ElectionGuard-specific practices such as the key and tally ceremonies, there are additional administration obligations and practices to consider.

## Stages of an ElectionGuard Election

* Creating the Election Record
* Managing the Key Ceremony
* Ballot Encryption
* Managing the Tally Ceremony
* Publishing the Election Record

### Creating the Election Record

Creating an election record involves specifying the following details:

* Election metadata
* Number of guardians and tally quorum
* Launch code
* Ballot manifest

#### Election metadata

Election metadata can consist of the following:

* Date
* Title
* Location
* Description
* Geospatial ID

#### Number of guardians and quorum

A core component of the ElectionGuard security architecture involves *election guardians*. Election guardians are trustworthy, independent individuals that participate in the key and tally ceremonies of ElectionGuard e2e-v elections.

By using multiple guardians to conduct the tally process, no one person controls all the keys necessary to decrypt ballots. However, with multiple actors it becomes necessary to compensate for guardians going missing or obstructing the tally process by supporting quorums and dispute resolution when a guardian challenges a result, as they are allowed.

As such, it is necessary when setting up an election to specify the maximum number of guardians that can participate, but also the quorum, the minimum number of guardians necessary to perform a tally. The more guardians that are allowed, the higher the quorum can (and should) be set (a high number of guardians with a low quorum creates an opportunity for collusion among guardians). It is advised to set quorums not just above majority levels but as high as can be reasonably expected (*e.g.* set a quorum of 5 or 6, not 4, for an election with 7 guardians).

#### Launch code

### Managing the Key Ceremony

After the number of guardians have been established



### Publishing the Election Record

