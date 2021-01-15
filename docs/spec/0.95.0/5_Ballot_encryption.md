# Ballot Encryption

An ElectionGuard ballot is comprised entirely of encryptions of one (indicating selection made) and zero (indicating selection not made). To enable homomorphic addition (for tallying), these values are exponentiated during encryption. Specifically, to encrypt a ballot entry $(V)$, a random value $R$ is selected such that $0 \le R \lt q$ and the following computation is performed:

Zero (not selected) is encrypted as 

$$
(g^R \bmod p, K^R \bmod p)
$$

One (selected) is encrypted as 

$$
(g^R \bmod p, g \cdot K^R \bmod p)
$$

Note that if multiple encrypted votes 

$$
\left(g^{R_i} \bmod p, g^{V_i} \cdot K^{R_i} \bmod p\right)
$$

are formed, their component-wise product 

$$
\left(g^{\sum_{i}V_i} \cdot K^{\sum_{i}R_i} \bmod p\right)
$$

serves as an encryption of $\sum_iV_i$ – _**which is the tally of those votes**_.[^19]

A contest in an election consists of a set of options together with a selection limit that indicates the number of selections that are allowed to be made in that contest. In most elections, most contests have a selection limit of one. However, a larger selection limit (*e.g.*, select up to three) is not uncommon in some elections. Approval voting can be achieved by setting the selection limit to the total number of options in a contest. Ranked choice voting is not supported in this version of *ElectionGuard*, but it may be enabled in a future version.[^20] Also, write-ins are assumed to be explicitly registered or allowed to be lumped into a single "write-ins" category for the purpose of verifiable tallying. Verifiable tallying of free-form write-ins may be best done with a MixNet[^21] design.

 A legitimate vote in a contest consists of a set of selections with cardinality not exceeding the selection limit of that contest. To accommodate legitimate undervotes, the internal representation of a contest is augmented with “placeholder” options equal in number to the selection limit. Placeholder options are selected as necessary to force the total number of selections made in a contest to be equal to the selection limit. When the selection limit is one, for example, the single placeholder option can be thought of as a “none of the above” option.

With larger selection limits, the number of placeholder options selected corresponds to the number of additional options that a voter could have selected in a contest.

!!! info
    For efficiency, the placeholder options could be eliminated in an approval vote. However, to simplify the construction of election verifiers, we presume that placeholder options are always present – even for approval votes.

Two things must now be proven about the encryption of each vote to ensure the integrity of a ballot.

1. The encryption associated with each option is either an encryption of zero or an encryption of one.
2. The sum of all encrypted values in each contest is equal to the selection limit for that contest (usually one).

The use of ElGamal encryption enables efficient zero-knowledge proofs of these requirements, and the Fiat-Shamir heuristic can be used to make these proofs non-interactive. Chaum- Pedersen proofs are used to demonstrate that an encryption is that of a specified value, and these are combined with the Cramer-Damgård-Schoenmakers technique to show that an encryption is that of one of a specified set of values – particularly that a value is an encryption of either zero or one. The encryptions of selections in a contest are homomorphically combined, and the result is shown to be an encryption of that contest’s selection limit – again using a Chaum-Pedersen proof.

!!! info
    Note that the decryption of the selection limit could be more efficiently demonstrated by just releasing the sum of the nonces used for each of the individual encryptions. But, again to simplify the construction of election verifiers, a Chaum-Pedersen proof is used here as well.

The “random” nonces used for the ElGamal encryption of the ballot nonces are derived from a single 256-bit master nonce $R_B$ for each ballot. For each contest listed in the ballot coding file, a contest nonce $R_C$ is derived from the master nonce $(R_B)$ and the contest label $(L_C)$ as 

$$
R_C= H(L_C,R_B)
$$ 

using the hash function SHA-256. For each option listed in the ballot coding file, the nonce used to encrypt that option is derived from the contest nonce $(R_C)$ and the selection label for that option $(L_S)$ as 

$$
R=H(L_S,R_C)
$$

A user of ElectionGuard may optionally provide an additional public key. If such a key is provided, ElectionGuard uses that key to encrypt each ballot’s master nonce $R_B$ and return this encryption together with the encrypted ballot.

Ballot nonces may be independent across different ballots, and only the nonces used to encrypt ballot selections need to be derived from the master nonce. The use of a single master nonce for each ballot allows the entire ballot encryption to be re-derived from the contents of a ballot and the master nonce. It also allows the encrypted ballot to be fully decrypted with the single master nonce.

## Outline for proofs of ballot correctness

To prove that an ElGamal encryption pair $(\alpha, \beta)$ is an encryption of zero, the Chaum-Pedersen protocol proceeds as follows.

### NIZK Proof that $(\alpha, \beta)$ is an encryption of zero (given knowledge of encryption nonce $R$)

The prover selects a random value $u$ in $Z_q$ and commits to the pair 

$$(g^u \bmod p, K^u \bmod p)
$$

A hash computation is then performed (using the Fiat-Shamir heuristic) to create a pseudo-random challenge value

$$
c=H(\bar{Q},(\alpha,\beta),(a,b))
$$

and the prover responds with 

$$
v=(u + cR) \bmod q
$$

A verifier can now confirm the claim by checking that both 

$$
g^V \bmod p = a \cdot \alpha^C \bmod p
$$ 

and 

$$
K^V \bmod p = b \cdot \beta^{C} \mod p
$$

are true.

### NIZK Proof that $(\alpha,\beta)$ is an encryption of one (given knowledge of encryption nonce $R$)

To prove that $(\alpha, \beta)$ is an encryption of one, $\frac{\beta}{g} \bmod p$ is substituted for $\beta$ in the above. The verifier can be relieved of the need to perform a modular division by computing $\beta \bar{g} \bmod p$ rather than $\beta \bmod p$. As an alternative, the verifier can confirm that 

$$
g^c \cdot K^v \bmod p = b \cdot \left(\frac{\beta}{g}\right)^c
$$

instead of

$$
K^v \bmod p = b \cdot \left(\frac{\beta}{g}\right)^c \bmod p
$$

As with many zero-knowledge protocols, if the prover knows a challenge value prior to making its commitment, it can create a false proof.  For example, if a challenge $c$ is known to be forthcoming, a prover can generate a random $v$ in $Z_q$ and commit to 

$$
(a,b)=\left(\frac{g^v}{α^c} \bmod p,\frac{K^v}{\beta^c} \bmod p\right)=\left(g^v \alpha^{(q-c)} \bmod p,K^v \beta^{(q-c)} \bmod p\right)
$$

This selection will satisfy the required checks for (α,β) to appear as an encryption of zero regardless of the values of (α,β).  Similarly, setting

$$
(a,b)=\left(\frac{g^v}{α^c} \bmod p,\frac{K^v g^c}{β^c} \bmod p\right)=\left(g^v α^{(q-c)} \bmod p,K^v \beta^{(q-c)} \bmod p\right)
$$
 
will satisfy the required checks for $(\alpha,\beta)$ to appear as an encryption of one regardless of the values of (α,β).  This quirk is what enables the Cramer-Damgård-Schoenmakers technique to prove a disjunction of two predicates.

### Sketch of NIZK Proof that (\alpha, \beta) is an encryption of zero or one

After the prover makes commitments $(a_0,b_0 )$ and $(a_1,b_1 )$ to the respective assertions that $(α,β)$ is an encryption of zero and $(α,β)$ is an encryption of one, a single challenge value $c$ is selected by hashing all commitments and baseline parameters.  The prover must then provide challenge values $c_0$ and $c_1$ such that $c=c_0+c_1 \bmod q$.  Since the prover has complete freedom to choose one of $c_0$ and $c_1$, the prover can fix one value in advance – either $c_0$ if $(α,β)$ is actually an encryption of one or $c_1$ if $(α,β)$ is actually an encryption of zero.  In response to the resulting challenge $c$, the prover uses this freedom to answer its faux claim with its chosen challenge value and then uses the remaining challenge value (as forced by the constraint that $c=(c_0+c_1 ) \bmod q)$ to demonstrate the truth of the other claim.  An observer can see that one of the two claims must be true but cannot tell which.

## Details for proofs of ballot correctness

The full protocol proceeds as follows – fully divided into the two cases.
To encrypt an “unselected” option on a ballot, a random nonce R is selected uniformly Z_q and an encryption of zero is formed as

$$
(α,β)=(g^R \bmod p,K^R  \bmod p)
$$

### NIZK Proof that $(\alpha,\beta)$ is an encryption of zero or one (given knowledge of encryption nonce $R$ for which $(α,β)$ is an encryption of zero)

To create the proof that $(α,β)$ is an encryption of a zero or a one, randomly select $c_1$, $v_1$, and $u_0$ from $Z_q$ and form the commitments 

$$
(a_0,b_0 )=(g^{u_0} \bmod p,K^{u_0} \bmod p)
$$

and

$$
(a_1,b_1 )=\left(\frac{g^{v_1}}{\alpha^{c_1}} \bmod p,\frac{K^{v_1} g^{c_1}}{\beta^{c_1}}  \bmod p\right)=\left(g^{v_1 } \alpha^{(q-c_1)}  \bmod p,K^{v_1} g^{c_1} \beta^{(q-c_1)} \bmod p\right)
$$

A challenge value $c$ is formed by hashing the extended base hash $\bar{Q}$ together with $(\alpha,\beta)$, $(a_0,b_0 )$, and $(a_1,b_1 )$ to form a challenge value 

$$
c=H\left(Q ̅,(α,β),(a_0,b_0 ),(a_1,b_1 )\right)
$$

The proof is completed by forming $c_0=(c-c_1 )  \bmod q$ and $v_0=(u_0+c_0 \cdot R)  \bmod q$ and answering the challenge by returning $c_0$, $c_1$, $v_0$, and $v_1$.

To encrypt a “selected” option on a ballot, a random nonce $R$ is selected uniformly from $Z_q$ and an encryption of one is formed as $(\alpha,\beta)=(g^r  \bmod p, g \cdot K^r  \bmod p)$.

### NIZK Proof that $(\alpha,\beta)$ is an encryption of zero or one (given knowledge of encryption nonce $R$ for which $(\alpha,\beta)$ is an encryption of one)

To create the proof that $(\alpha,\beta)$ is an encryption of a zero or a one, randomly select $c_0$, $v_0$, and $u_1$ from $Z_q$ and form the commitments

$$
(a_0,b_0) = \left( \frac{g^{v_0}}{\alpha^{c_0}} \bmod p,\frac{K^{v_0}}{\beta^{c_0 }} \bmod p\right) = \left(g^{v_0} α^{(q-c_0)}  \bmod p,K^{v_0} \beta^{(q-c_0 )} \bmod p\right)
$$

and

$$
(a_1,b_1 )=(g^{u_1} \bmod p,K^{u_1}  \bmod p)
$$

A challenge value $c$ is formed by hashing the extended base hash $\bar{Q}$ together with $(\alpha,\beta)$, $(a_0,b_0 )$, and $(a_1,b_1 )$ to form a challenge value 

$$
c=H\left(\bar{Q},(\alpha,\beta),(a_0,b_0 ),(a_1,b_1 )\right)
$$

The proof is completed by forming 

$$
c_1=(c-c_0 )  \bmod q
$$

and 

$$
v_1=(u_1+c_1\cdot R)  \bmod q
$$ 

and answering the challenge by returning $c_0$, $c_1$, $v_0$, and $v_1$.

In either of the two above cases, what is published in the election record is the encryption $(\alpha,\beta)$ together with the commitments $(a_0,b_0 )$ and $(a_1,b_1 )$ which are all hashed together with the election’s extended base hash to form the challenge value c which is published together with values $c_0$, $c_1$, $v_0$, and $v_1$.

!!! important
    An election verifier must confirm the following for each possible selection on a ballot:

(A) The given values $\alpha$, $\beta$, $a_0$, $b_0$, $a_1$, and $b_1$ are all in the set $Z_p^r$.  (A value $x$ is in $Z_p^r$ if and only if $x$ is an integer such that $0 \le x \lt p$ and $x^q  \bmod p=1$ is satisfied.)

(B) The challenge $c$ is correctly computed as

$$
c=H\left(\bar{Q},(\alpha,\beta),(a_0,b_0 ),(a_1,b_1 )\right)
$$

(C) The given values c_0, c_1, v_0, and v_1 are each in the set Z_q.  (A value $x$ is in $Z_q$ if and only if $x$ is an integer such that $0 \le x \lt q$).

(D) The equation 

$$
c=(c_0+c_1 ) \bmod q
$$

is satisfied.

(E) The equation 

$$
g^{v_0}  \bmod p=a_0 α^{c_0}  \bmod p
$$

is satisfied.

(F) The equation 

$$
g^{v_1} \bmod p=a_1 \alpha^{c_1}  \bmod p 
$$

is satisfied.

(G) The equation 

$$
K^{v_0} \bmod p=b_0 \beta^{c_0}  \bmod p
$$

is satisfied.

(H) The equation

$$
g^{c_1} K^{v_1}  \bmod p=b_1 \beta^{c_1}  \bmod p
$$

is satisfied.

## Proof of satisfying the selection limit

The final step in proving that a ballot is well-formed is demonstrating that the selection limits for each contest have not been exceeded.  This is accomplished by homomorphically combining all of the $(\alpha_i,\beta_i )$ values for a contest by forming the aggregate contest encryption 

$$
(\alpha,\beta)=(\prod_i \alpha_i  \bmod p,\prod_i \beta_i  \bmod p)
$$

and proving that $(\alpha,\beta)$ is an encryption of the total number of votes allowed for that contest (usually one).  The simplest way to complete this proof is to combine all of the random nonces $R_i$ that were used to form each

$$
(\alpha_i,\beta_i )=\left(g^{R_i} \bmod p,K^{R_i}  \bmod p\right)
$$

or

$$
(\alpha_i,\beta_i )=\left(g^{R_i}  \bmod p,g \cdot K^{R_i}  \bmod p\right)
$$

depending on whether the value encrypted is zero or one.  The aggregate nonce

$$
R=\sum_i R_i  \bmod q
$$

matches the aggregate contest encryption as 

$$
(\alpha,\beta)=(\prod_i\alpha_i  \bmod p,\prod_i \beta_i  \bmod p)= (g^R \bmod p,g^L K^R \bmod p)
$$

where $L$ is the selection limit for the contest.  (Recall that $L$ extra “placeholder” positions will be added to each contest and set to one as necessary to ensure that exactly $L$ selections are made for the contest.)

### NIZK Proof that $(\alpha,\beta)$ is an encryption of $L$ (given knowledge of aggregate encryption nonce $R$)

An additional Chaum-Pedersen proof of $(\alpha,\beta)$ being an encryption of $L$ is performed by selecting a random $U$ in $Z_q$, publishing

$$
(a,b)=(g^U  \bmod p,K^U \bmod p)
$$

then hashing these values together with the election’s extended base hash $\bar{Q}$ to form a pseudo-random challenge

$$
C=H\left(\bar{Q},(\alpha,\beta),(a,b)\right)
$$

and responding by publishing [^22]

$$
V=(U+CR) \bmod q
$$

Note that all of the above proofs can be performed directly by the entity performing the public key encryption of a ballot without access to the decryption key(s).  All that is required is the nonces $R_i$ used for the individual selection encryptions.

!!! important
    An election verifier must confirm the following for each contest on the ballot:

(A) The number of **placeholder** positions matches the contest’s selection limit $L$

(B) The contest total $(A,B)$ satisfies

$$
A=\prod_i \alpha_i  \bmod p
$$

and

$$
B=\prod_i \beta_i  \bmod p
$$

where the $(\alpha_i,\beta_i )$ represent all possible selections (including placeholder selections) for the contest.

(C) The given value $V$ is in $Z_q$.

(D) The given values $a$ and $b$ are each in $Z_p^r$.

(E) The challenge value $C$ is correctly computed as

$$
C=H\left(\bar{Q},(A,B),(a,b)\right)
$$

(F) The equation

$$
g^V  \bmod p=(aA^C )  \bmod p
$$

is satisfied.

(G) The equation

$$
(〖g^{(LC K^V} \bmod p=(bB^C ) \bmod p
$$

is satisfied.

## Verification Codes

Upon completion of the encryption of each ballot, a verification code is prepared for each voter.  The code is a running hash that begins with the extended base hash code $\bar{Q}$ and includes an identifier for the voting device, the location of the voting device, the date and time that the ballot was encrypted, and, of course, the encryption of the ballot itself.  The hash $(H)$ used for this purpose is SHA-256.  

The tracking code is formed as follows.  

$$
H_0=H(\bar{Q})
$$

where  $\bar{Q}$ is the extended base hash code of the election.  For ballot with index $i>0$, 

$$
H_i=H(H_{i-1},D,T,B_i)
$$

where $D$ consists of the voting device information described above, $T$ is the date and time of ballot encryption, and $B_i$ is an ordered list of the individual encryptions on the ballot – with the ordering as specified by the ballot coding file.  At the conclusion of a voting period (this may be the end of a day in a multi-day election), the hash chain is closed by computing  

$$
\bar{H}=H(H_l, \text{“CLOSE"})
$$

where $H_l$ is the final tracking code produced by that device during that voting period.  The close of the hash chain can be computed either by the voting device or subsequently by election administrators, and it is published as part of the election record.

!!! important
    An election verifier must confirm that each of the values in the running hash is correctly computed.  Specifically, an election verifier must confirm each of the following.

(A) The equation $H_0=H(\bar{Q})$ is satisfied.

(B) 	For each ballot 

$$
B_i, H_i=H\left(H_{i-1},D,T,B_i\right)
$$

is satisfied.

(C) The closing hash 

$$
\bar{H}=H(H_l,\text{“CLOSE"})
$$ 

is correctly computed from the final tracking code $H_l$

Once in possession of a tracking code (__*and never before*__), a voter is afforded an option to either cast the associated ballot or spoil it and restart the ballot preparation process.  The precise mechanism for voters to make these selections may vary depending upon the instantiation, but this choice would ordinarily be made immediately after a voter is presented with the tracking code, and the status of the ballot would be undetermined until the decision is made.  It is possible, for instance, for a voter to make the decision directly on the voting device, or a voter may instead be afforded an option to deposit the ballot in a receptacle or to take it to a poll worker to be spoiled.  For vote-by-mail scenarios, a voter can be sent (hashes of) two complete sets of encryptions for each selectable option and can effect a ballot challenge implicitly by choosing which encryptions to return.

[^19]: The initial decryption actually forms the value $g^\sum_i V_i \bmod p$.  However, since $\sum_i V_i$ is a relatively small value, it can be effectively computed from $g^\sum_i V_i \bmod p$ by means of an exhaustive search or similar methods.

[^20]: Benaloh J., Moran. T, Naish L., Ramchen K., and Teague V.  Shuffle-Sum:  Coercion-Resistant Verifiable Tallying for STV Voting  (2009) in Transactions of Information Forensics and Security

[^21]: Chaum D.  Untraceable Electronic Mail, Return Addresses, and Digital Pseudonyms (1981) Communications of the ACM

[^22]: One could simply release the aggregate nonce $R=\prod_i R_i  \bmod q$ to complete this proof.  However, since Chaum-Pedersen proofs are being performed elsewhere, it is simpler for a verifier to just repeat the same steps.
