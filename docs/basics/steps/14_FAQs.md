# ElectionGuard FAQ's

## Overview

Learn more about how ElectionGuard works and how it will be used in the pilot during the 2022 General Election.

####  About ElectionGuard 

???+ abstract "What is ElectionGuard?"
     ElectionGuard is a new election technology that lets every voter confirm that their ballot was counted and provides independent verification that the election results are correct, without revealing how anyone voted.  
???+ abstract "How does ElectionGuard Work?"
     ElectionGuard runs alongside the existing voting system. Voters mark their ballots as they always have, hand-marking a paper ballot. 
     
     Then, as they cast their vote, ElectionGuard encrypts their ballots and gives the voter a confirmation code that they can use to see for themselves that their ballot is included in the final count. All of the encrypted ballots are used to create a snapshot of the election.  This snapshot can be used to check the results of the election without revealing how anyone voted.
???+ abstract "How does ElectionGuard help verify the results of an election?"
     ElectionGuard provides transparency and confidence in the election process by involving community members, voters, and others in the voting process. Each person or organization that takes part does so independently, strengthening the verification that ElectionGuard provides. 
     
     * <strong>Election Guardians</strong> – trusted, independent members of the community - help set up the election. They create the locks, keep the keys secure, and unlock the election tallies. 
     * <strong>Voters</strong> can confirm that their vote was counted, by checking the confirmation code they receive when they cast their ballot.  
     * <strong>Voters</strong> run a BallotCheck, creating a ballot that can be reviewed to test the accuracy of the system (but which is not counted). 
     * <strong>Independent organizations</strong> create Election Verifiers - software tools that check the ElectionGuard record of the ballots to check that the votes have not been altered. 

     When a few voters run a BallotCheck and many more use their confirmation code to see that their ballot was counted, everyone is part of making elections more transparent.  

???+ abstract "Can ElectionGuard reveal how someone voted?"
     No. Your ballot is secret. The confirmation code does not include any voter identification. The ElectionGuard software can confirm that ballots were included in the count and the election results are correct, but does not reveal how anyone voted. Only the official tally can count the individual choices to produce the election results.  
     
     * BallotCheck ballots can be unlocked so the accuracy of the encryption can be checked, but are not included in the count.  
     * Independent Election Verifier tools do not decrypt the ballots but perform the mathematical checks described in the ElectionGuard specification. 
 <br>
####  About the ElectionGuard Pilot

The pilot of ElectionGuard will occur during the General Election of one jurisdiction as part of their commitment to innovative approaches that add confidence to the election process.  

???+ abstract "How is the pilot being conducted?"
     The ElectionGuard pilot runs alongside the normal election processes.   
     
     * Voters will mark their ballots as usual.   
     * They will use a scanner in the polling place to cast their ballots, instead of putting them in a box to be counted at the election office.  
     * The scanner will show them a summary of their vote, and then allow them to cast the ballot, make changes before casting, or opt to run a BallotCheck.  
???+ abstract "Who is part of the pilot?"
     The pilot will take place in one polling place on Election Day (location to be disclosed after the Election). Participation is optional - voters in the district can opt-out of the pilot. Poll workers will receive extra training so they can support voters using ElectionGuard. Two Election Guardians will create the locks and keys to set up ElectionGuard. The pilot election team will collect feedback during and after the election.  
???+ abstract "How will the votes be counted?"
     The jurisdiction will count all of the ballots and announce the official results as usual. The ElectionGuard pilot data will be compared to the official results as part of testing the new technology. 
???+ abstract "What will make the pilot a success?"
     The pilot is as chance to:

     <strong>Test the technology in a real environment</strong>, demonstrating that: 
     
     * All the parts of ElectionGuard can work together in a live election  
     * An independently created ElectionVerifier can check the results of the tally 
     * ElectionGuard does not interfere with existing election procedures 

     <strong>Learn about the impact on voters</strong>, especially whether they:

     * Understand the value and benefits of ElectionGuard 
     * Took the opportunity to confirm that their ballot counted 
     * Help ensure that the technology is working correctly, with a goal of 1% of voters running a BallotCheck 
     * Increase their confidence in the accuracy and security of elections. 
<br>
####  About the ElectionGuard Technology

ElectionGuard is an open-source software tool that is integrated into the voting system. It is a way of checking election results are accurate, and that votes have not been altered, suppressed, or tampered with in any way. It adds another form of transparency to the election process.  

???+ abstract "What does “independent verification” mean?"
     The ElectionGuard checks are done by individual voters, using tools created by separate companies, from an open specification. In other words, anyone can create or use tools to verify the election results independently of both the voting system and the software developed by ElectionGuard.  
     
     The key to independent verification is that ElectionGuard uses encryption technology that allows the data – ballots in this case - to be analyzed mathematically without unlocking the encryption and revealing individual votes.   
???+ abstract "How does ElectionGuard integrate into the voting system?"
     Hart InterCivic’s voting system Verity® is used in the pilot election. 
     
     The ElectionGuard software is installed on the Verity Scan ballot scanner.  As each ballot is scanned, ElectionGuard wraps a second copy of the votes in special encryption. 
     
     Voters can cast the ballot and get a confirmation code, ask for a replacement ballot to make a correction, or decide to run a BallotCheck.  
     
     The jurisdiction's elections office uses the Hart Verity system to count the ballots and announce the result of the election as usual.  
     
     After the election, the encrypted data is uploaded to an independent website where it is used to create a tally that is an independent verification of the election results. The data is also used for the other ElectionGuard-enabled tools like BallotCheck and ElectionVerifier. 
     
     Verity Scan is the scanner and tabulator used for in-person voting, whether the jurisdiction is using hand-marked paper ballots or printed ballots generated by an electronic ballot marking device. For the pilot, the Verity Scan only reads paper ballots marked by hand.  
     
     Hart will use what is learned in the pilot elections to decide on next steps and whether future Verity releases will include ElectionGuard. 
<br>
####  About ElectionGuard independent verification 

ElectionGuard includes several kinds of independent verification. Voter confirmation, BallotCheck, ElectionVerifiers, and the use of Election Guardians. Individual voters are an important part of making elections more transparent.

???+ abstract "How does a voter confirmation work?"
     Every voter receives a confirmation code as they cast their ballot at the scanner. The code is printed on a piece of paper and embedded in a QR code. 
     
     After the election, they go to the ElectionGuard website and scan or enter the code. If they find a matching code, they can see for themselves that their ballot is included in the final count. 
     
     The confirmation does not reveal how they voted, only that their ballot was counted.    
???+ abstract "How does a BallotCheck work?"
     A BallotCheck is a way for voters to independently verify that ElectionGuard is working correctly. They create a ballot that they can review to test the accuracy of the system – but which is not counted.  
     
     The BallotCheck starts at the polling place.  

     * After marking their ballot, the voter puts it into the scanner. The scanner prints a confirmation code. At the prompt on the scanner screen, instead of casting the ballot, they tell a poll worker that they want to run a BallotCheck.  
     
     * The ballot is set aside so it cannot be counted. These ballots are not connected to the voter.  
     
     * The voter takes the confirmation code from the scanner.   
     
     * The poll workers give the voter a new ballot that they can mark and cast to be counted. 

     After the election, the voter goes to the ElectionGuard website and uses the confirmation code to check that the ballot has been counted and the system recorded their vote accurately. 

     <em>EnhancedVoting built the website that hosts ballot confirmations and BallotCheck</em> 
???+ abstract "How does an ElectionVerifer work?"
     Independent ElectionVerifiers look at the results reported by ElectionGuard. They complement the BallotCheck that reviews the accuracy of an individual ballot.   
     
     After an election is completed, a verifier checks that the published results match the tally of all encrypted ballots. Verification is an objective process—a verifier’s job is to perform the mathematical checks described in the ElectionGuard specification.  

     * Verification does not require access to the content of individual ballots. The encryption tools used in ElectionGuard (“homomorphic encryption”) allow the encrypted ballots to be combined to create encrypted tallies without decrypting them. 
     * The decryption of encrypted tallies is checked by the verifier. Only the correct tally can be reported as the result of this decryption, or a verifier would notice. 
     * Verifiers check that the encrypted ballots comply with the ElectionGuard specification requirements and that the tally was correctly counted. 

     Verification can be performed by anyone, even those completely independent of the ElectionGuard team. Independent verification makes it possible to trust that ElectionGuard is working correctly and accurately reporting on the election. 
     
     <em>Mitre built the first ElectionVerifier for the pilot election. Learn more about the [MITRE ElectionGuard Verifier](https://mitre.github.io/ElectionGuardVerifier.jl/index.html)</em> 
???+ abstract "Who are the Election Guardians and what do they do?"
     Election Guardians are trusted, independent members of the community who help set up ElectionGuard. They have a special role in creating the cryptographic locks that secures the election: 

     * Before the election, Guardians create a special lock and key. The lock is loaded on the ballot scanners to encrypt all of the ballots for the election. 
     
     * During the election, Guardians each keep their part of the key secure. Having a small group of Guardians means that no one person can unlock the election on their own. 
     
     * When it’s time to count the ballots, Guardians return to unlock the election. They bring their keys back to the election office to unlock the tally and create the election record. 

     It a simple, but critical role.  It’s important that no single person - even the Clerk - can unlock the election alone. With several people acting as Guardians, they add independent security to the ElectionGuard lock and key.
<br>
####  Who are the partners in the ElectionGuard pilot? 

The most important partners in this pilot are the individuals from the pilot jurisdiction. Their commitment to running elections and willingness to try an innovative technology make this pilot possible. They are election heroes. The ElectionGuard pilot team brings together technology and election expertise and provides technical support for the use of ElectionGuard in this election. 

???+ abstract "ElectionGuard team"
     * [<strong>Hart InterCivic</strong>](https://www.hartintercivic.com/) integrated ElectionGuard software into their Verity® scanner for this election. Hart is the first major voting system manufacturer in the United States to provide independent verifiability. This pilot is part of their continued commitment to voting technology innovation that results in higher levels of voter confidence in the election process. 
     
     * The [<strong>Microsoft Democracy Forward</strong>](www.microsoft.com/en-us/corporate-responsibility/democracy-forward) program works to protect democratic processes through open and secure technologies. Microsoft sponsored the creation of the open-source software tools for ElectionGuard.   
     
     * [<strong>InfernoRed</strong>](infernored.com) is a premier independent software company that developed the open-source ElectionGuard SDK. 
     
     * The [<strong>MITRE</strong>](mitre.org) National Election Security Lab conducts cybersecurity assessments and testing to assist with securing election infrastructure. MITRE is building a publicly available, independent verifier for ElectionGuard. 
     
     * [<strong>Enhanced Voting</strong>](enhancedvoting.com) creates voting solutions that are secure, easy-to-use, and accessible to all. They built the public website where voters can check their confirmation codes and host the ElectionGuard data package for the pilot.  
     
     * [<strong>Center for Civic Design</strong>](civicdesign.org) brings their design, research, and communication skills to collecting feedback from voters during the pilot election. 


