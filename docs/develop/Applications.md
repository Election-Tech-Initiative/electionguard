# Applications

There are many different paths for creating applications that work using ElectionGuard. For many of these paths, there are reference implementations that can be forked or used as examples or used as packages. Many reference implementations include packaging or containerization for easy consumption. Below are some examples of paths a developer could take when developing using ElectionGuard. This is by no means the limit and some of these paths can be combined for different applications and use cases. 

If you develop an app for ElectionGuard, we suggest you [utilize our badges][badges] to indicate which version of the specification your application targets. 

## Paths

### ElectionGuard Core

An ElectionGuard core is an application that implements the base level [features][features] such as Ballot Encryption by implementing them according to the specification. The internal examples of this are the python and c++ reference implementations. There is a community example of this with the java port don by the community. 

### Ballot Marking

Ballot marking means marking ballots with a voters selections, for the uninitiated, a voting application. The app would display the contests in the manifest according to voter's ballot style and language and allow the voter to vote. The result would be a plaintext ballot.

### Ballot Encryption

Encrypting ballots is the base of ElectionGuard. This is a tool that takes a plaintext ballot and encrypts the ballot into an encrypted aka ciphertext ballot. 

Two quick ways to start are by using the ElectionGuard [encryption nuget package][encryption nuget package] or or [python package][python package].

### Ballot Box

A ballot box simply takes the encrypted ballot of a voter and allows a user to submit the ballot as cast or spoil/challenge the ballot. This takes a ciphertext ballot and turns it into a submitted ballot that is aggregated into a tally.

### Administer Election

Administering an election for ElectionGuard usual requires the following steps. An example of this is available in [electionguard-ui repository][admin app].

1. Setup Election - An election should be setup with a manifest and selected guardians
2. Key Ceremony - A key ceremony should be run that results in the encryption key that can be used for the ballots.
3. Tally Ceremony - A tally ceremony when run will decrypt the tally and any challenge ballots
4. Election Record - An election record should be retrievable at the end of the election for publication and verification purposes. 

A quick way to start is to use the [electionguard api-client][api client] and the [electionguard-python-api][api].

### Publish Election

The results of election can be displayed after an election is closed. An example of this is available in [electionguard-ui repository][result app]. This application should contain three pieces. 

1. **Results** - Using decrypted tally and manifest, the tallied results should be displayed. 
2. **Ballot Confirmation** - Confirm a ballot is in the Election Record.
    - Cast Ballot - Confirm a ballot has been cast
    - Challenge Ballot - Confirm a ballot has been challenged and display decrypted ballot
3. **Download Election Record** - The Election Record should be downloadable for the public. 

### Verify Election

A verifier verifies an election by using the public information about a finished election. At the close of an election using ElectionGuard, an election record should be created and made public. ElectionGuard encourages third parties to create their own verifiers and help verify election records. A very basic example of a verifier can be found within the [electionguard-python repository][verifier], but  verifiers should aim to be as thorough as possible. Verifiers can validate everything from the key ceremony to the decryption since the election is end to end verifiable. To verify an election, the app just needs to consume the files in the election record and produce 


<!--Links-->
[badges]: Badges.md
[features]: ../overview/Features.md
[admin app]: https://github.com/microsoft/electionguard-ui/tree/main/packages/admin-app
[result app ]: https://github.com/microsoft/electionguard-ui/tree/main/packages/result-app
[api client]: https://github.com/microsoft/electionguard-ui/tree/main/packages/api-client
[api]:https://github.com/microsoft/electionguard-api-python
[election record]: Election_Record.md
[verifier]: https://github.com/microsoft/electionguard-python/tree/main/src/electionguard_verify
[encryption nuget package]: https://www.nuget.org/packages/ElectionGuard.Encryption/
[python package]: https://pypi.org/project/electionguard/



