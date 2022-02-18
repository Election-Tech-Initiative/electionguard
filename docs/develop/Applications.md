# Applications

There are many different paths for creating applications that work using ElectionGuard. For many of these paths, there are reference implementations that can be forked or used as examples or used as packages. Many reference implementations include packaging or containerization for easy consumption. Below are some examples of paths a developer could take when developing using ElectionGuard. This list is by no means complete and some of these paths can be combined for different applications and use cases. 

If you develop an app for ElectionGuard, we suggest you [utilize our badges][badges] to indicate which version of the specification your application targets. 

## Paths

### ElectionGuard Core

An ElectionGuard Core is an application that implements the base level [features] such as Ballot Encryption by implementing them according to the specification. The internal examples of this are the Python and C++ reference implementations. There is a community example of this with the Java port done by the community. 

### Ballot Marking

Ballot marking is the process of recording a voter's [selections] on a ballot. A ballot marking app displays the contests from the manifest according to an individuals voter's ballot style and language. The voter then votes and the [selections] are recorded on a [plaintext ballot][plaintext-ballot]. 

### Ballot Encryption

Ballot encryption is the process of converting voter [selections] into data such that it cannot be read by unauthorized parties. A ballot encryption app provides this fundamental functionality. The app functions as a tool that encrypts a [plaintext ballot][plaintext-ballot] into a encrypted ballot aka [ciphertext ballot][ciphertext-ballot]. 

Two quick ways to start are by using the ElectionGuard [encryption nuget package][encryption nuget package] or or [python package][python package].

### Ballot Box

A ballot box app takes the encrypted ballot of a voter and allows a user to submit the ballot as [cast][cast-ballot] or [spoil][spoiled-ballot] the ballot. A submitted cast ballot is aggregated into the tally. A submitted spoiled ballot is added to the list of spoiled ballots. 

### Administer Election

Administering an election for ElectionGuard usually requires the following steps. An example of this is available in [electionguard-ui repository][admin app].

1. Setup Election - An election should be setup with a manifest and selected guardians
2. Key Ceremony - A key ceremony should be run that results in the encryption key that can be used for the ballots.
3. Tally Ceremony - A tally ceremony when run will decrypt the tally and any spoiled ballots
4. Election Record - An election record should be retrievable at the end of the election for publication and verification purposes. 

A quick way to start is to use the [electionguard api-client][api client] and the [electionguard-python-api][api].

### Publish Election

The results of election can be displayed after an election is closed. An example of this is available in [electionguard-ui repository][result app]. This application should contain three pieces. 

1. **Results** - Using decrypted tally and manifest, the tallied results should be displayed. 
2. **Ballot Confirmation** - Confirm a ballot is in the Election Record.
    - Confirm Cast - Confirm a ballot was cast and included in tally
    - Challenge Ballot - Confirm a ballot was spoiled and display decrypted spoiled ballot to user
3. **Download Election Record** - The Election Record should be downloadable for the public. 

### Verify Election

A verifier app verifies an election is true and accurate by using the publicly published information about a completed election. At the close of an election using ElectionGuard, an election record should be created and made public. ElectionGuard encourages third parties to create their own verifiers and help verify election records. A basic example of a verifier can be found within the [electionguard-python repository][verifier], but  verifiers should aim to be as thorough as possible. After consuming the files in an election record, verifiers can validate everything from the key ceremony to the decryption since the election is end to end verifiable. 

<!--Links-->
[selections]: ../../overview/Glossary/#selection
[plaintext-ballot]: ../../overview/Glossary/#plaintext-ballot
[ciphertext-ballot]: ../../overview/Glossary/#ciphertext-ballot
[cast-ballot]: ../../overview/Glossary/#cast-ballot
[spoiled-ballot]: ../../overview/Glossary/#spoiled-ballot
[badges]: ../Badges
[features]: ../../overview/Features
[admin app]: https://github.com/microsoft/electionguard-ui/tree/main/packages/admin-app
[result app ]: https://github.com/microsoft/electionguard-ui/tree/main/packages/result-app
[api client]: https://github.com/microsoft/electionguard-ui/tree/main/packages/api-client
[api]:https://github.com/microsoft/electionguard-api-python
[election record]: Election_Record.md
[verifier]: https://github.com/microsoft/electionguard-python/tree/main/src/electionguard_verify
[encryption nuget package]: https://www.nuget.org/packages/ElectionGuard.Encryption/
[python package]: https://pypi.org/project/electionguard/

--8<-- "includes/abbreviations.md"