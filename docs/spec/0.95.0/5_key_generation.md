 # Key Generation

 Before an election, the number of guardians (𝑛) is fixed together with a quorum value (𝑘) that describes the number of guardians necessary to decrypt tallies and produce election verification data. The values 𝑛 and 𝑘 are integers subject to the constraint that 1 ≤ 𝑘 ≤ 𝑛. Canvassing board members can often serve the role of election guardians, and typical values for 𝑛 and 𝑘 could be 5 and 3 – indicating that 3 of 5 canvassing board members must cooperate to produce the artifacts that enable election verification. The reason for not setting the quorum value 𝑘 too low is that it will also be possible for 𝑘 guardians to decrypt individual ballots.
 
!!! note

        Note that decryption of individual ballots does not directly compromise voter privacy since links between encrypted ballots and the voters who cast them are not retained by the system. However, voters receive verification codes that can be associated with individual encrypted ballots, so any group that has the ability to decrypt individual ballots can also coerce voters by demanding to see their tracking codes.

    

Threshold ElGamal encryption is used for encryption of ballots. This form of encryption makes it very easy to combine individual guardian public keys into a single public key for encrypting votes and ballots. It also offers a homomorphic property that allows individual encrypted votes to be combined to form encrypted tallies. 

The guardians of an election will each generate a public-private key pair. The public keys will then be combined (as described in the following section) into a single election public key which is used to encrypt all selections made by voters in the election.

 Ideally, at the conclusion of the election, each guardian will use its private key to form a verifiable partial decryption of each tally. These partial decryptions will then be combined to form full verifiable decryptions of the election tallies.



To accommodate the possibility that one or more of the guardians will not be available at the conclusion of the election to form their partial decryptions, the guardians will cryptographically share[^1] their private keys amongst each other during key generation in a manner to be detailed in the next section. A pre-determined threshold value (𝑘) out of the (𝑛) guardians will be necessary to produce a full decryption. 

Additionally, each guardian will also generate an auxiliary public-private key pair. These auxiliary keys will be used by the guardians to exchange fragments of their principal vote encryption keys and for other scenarios in which non-vote data may need to be encrypted.

## Overview of key generation
The 𝑛 guardians of an election are denoted by 𝑇1, 𝑇2, … , 𝑇𝑛. Each guardian 𝑇𝑖 generates an independent ElGamal public-private key pair by generating a random integer secret 𝑠𝑖 ∈ ℤ𝑞 and forming the public key 𝐾𝑖 = 𝑔 𝑠𝑖 mod 𝑝. Each of these public keys will be published in the election record together with a non-interactive zero-knowledge Schnorr proof of knowledge of possession of the associated private key.

The joint election public key will be


$$ K= \Pi_{i=1}^{n} K_i mod  p.$$
 

 To enable robustness and allow for the possibility of missing guardians at the conclusion of an election, the ElectionGuard key generation includes a sharing of private keys between guardians to enable decryption by any 𝑘 guardians. This sharing is verifiable, so that receiving guardians can confirm that the shares they receive are meaningful; and the process allows for decryption without explicitly reconstructing private keys of missing guardians.

Each guardian 𝑇𝑖 generates 𝑘 − 1 random polynomial coefficients 𝑎<sub>𝑖,𝑗</sub> such that 0 < 𝑗 < 𝑘 and 0 ≤ 𝑎<sub>𝑖,𝑗</sub>  < 𝑞 and forms the polynomial



$$ P_i(x) =  \sum_{j=0}^{k-1} a_{ij} x^jmod  q $$
 


by setting 𝑎<sub>𝑖,0</sub> equal to its secret value 𝑠<sub>𝑖</sub> . Guardian 𝑇<sub>𝑖</sub> then publishes commitments 𝐾<sub>𝑖,𝑗</sub> = 𝑔 <sup>𝑎<sub>𝑖,𝑗</sub></sup> mod 𝑝 to each of its random polynomial coefficients. As with the primary secret keys, each guardian should provide a Schnorr proof of knowledge of the secret coefficient value 𝑎<sub>𝑖𝑗</sub>, associated with each published commitment 𝐾<sub>𝑖,𝑗</sub> . Since polynomial coefficients will be generated and managed in precisely the same fashion as secret keys, they will be treated together in a single step below.




At the conclusion of the election, individual encrypted ballots will be homomorphically combined into a single encrypted aggregate ballot – consisting of an encryption of the tally for each option offered to voters. Each guardian will use its secret key to generate a partial decryption of each encrypted tally value, and these partial decryptions will be combined into full decryptions. If any election guardians are missing during tallying, any set of 𝑘 guardians who are available can cooperate to reconstruct the missing partial decryption.

 All spoiled ballots are individually decrypted in precisely the same fashion.

## Details of key generation
 
Each guardian 𝑇<sub>𝑖</sub> in an election with a decryption threshold of 𝑘 generates 𝑘 secret polynomial coefficients 𝑎𝑖,𝑗 such that 0 ≤ 𝑗 < 𝑘 and 0 ≤ 𝑎<sub>𝑖,𝑗</sub> < 𝑞 and forms the polynomial

$$P_i(x) =\sum_{j=0}^{k-1}a_{ij}x^j mod q$$

 

Guardian 𝑇<sub>𝑖</sub> then publishes commitments 𝐾<sub>𝑖,𝑗</sub> = 𝑔 <sup>𝑎<sub>𝑖,𝑗<sub></sup> mod 𝑝 for each of its random polynomial coefficients. The constant term 𝑎<sub>𝑖,0</sub> of this polynomial will serve as the private key for guardian 𝑇<sub>𝑖</sub> , and for convenience we denote 𝑠<sub>𝑖</sub> = 𝑎<sub>𝑖,0</sub>, and its commitment 𝐾<sub>𝑖,0</sub> will serve as the public key for guardian 𝑇<sub>𝑖</sub>  and will also be denoted as 𝐾<sub>𝑖</sub> = 𝐾<sub>𝑖,0</sub>.

 In order to prove possession of the coefficient associated with each public commitment, for each 𝐾<sub>𝑖,𝑗</sub> with 0 ≤ 𝑗 < 𝑘, guardian 𝑇<sub>𝑖</sub> generates a Schnorr proof of knowledge for each of its coefficients as follows.

This Non-Interactive Zero-Knowledge (NIZK) proof proceeds as follows.

<u>NIZK Proof by Guardian 𝑇<sub>𝑖 </sub> of its knowledge of secrets 𝑎<sub>𝑖,𝑗</sub>  such that 𝐾<sub>𝑖,𝑗</sub> = 𝑔 <sup>𝑎<sub>𝑖,𝑗</sub></sup> mod p</u>

For each 0 ≤ 𝑗 < 𝑘, Guardian 𝑇<sub>𝑖</sub> generates random integer values 𝑅<sub>𝑖,𝑗</sub> in ℤ<sub>𝑞</sub> and computes ℎ<sub>𝑖,𝑗</sub> = 𝑔 <sup>𝑅<sub>𝑖,𝑗</sub></sup> mod 𝑝. Then, using the hash function SHA-256 (as defined in NIST PUB FIPS 180- 4 [^2]), guardian 𝑇<sub>𝑖</sub> then performs a single hash computation 𝑐<sub>𝑖,𝑗</sub> = 𝐻(𝑄,𝐾<sub>𝑖,𝑗</sub> , ℎ<sub>𝑖,𝑗</sub>) mod 𝑞 and publishes the values 𝐾<sub>𝑖,𝑗</sub> , ℎ<sub>𝑖,𝑗</sub> , 𝑐<sub>𝑖,𝑗</sub> , and 𝑢<sub>𝑖,𝑗</sub> = (𝑅<sub>𝑖,𝑗</sub> + 𝑐<sub>𝑖</sub>,𝑗𝑎<sub>𝑖,𝑗</sub>) mod 𝑞.

!!! note

    An election verifier must confirm the following for each guardian $$𝑇_𝑖$ and for each 𝑗 ∈ ℤ<sub>𝑘</sub>: 
    (A) The challenge 𝑐<sub>𝑖,𝑗</sub> is correctly computed as 𝑐<sub>𝑖,𝑗</sub> = 𝐻(𝑄,𝐾<sub>𝑖,𝑗</sub> , ℎ<sub>𝑖,𝑗</sub>) mod 𝑞. 
    (B) The equation 𝑔 <sup>𝑢<sub>𝑖,𝑗</sub></sup> mod 𝑝 = ℎ<sub>𝑖,𝑗</sub>𝐾<sub>𝑖,𝑗</sub><sup> 𝑐<sub>𝑖,𝑗<sub></sup> mod 𝑝 is satisfied.

    It is worth noting here that for any fixed constant 𝛼, the value 𝑔 <sup>𝑃<sub>𝑖</sub> (𝛼)</sup> mod 𝑝 can be computed entirely from the published commitments as


$$
g^{P_i(\alpha)}= g^{\sum_{j=0}^{k-1}{a_{i,j^{\alpha^j}}}} mod p = \pi_{j=0}^{k-1}g^{a^i,j^{\alpha^j}}mod p = \pi _{j=0}^{k-1} (g^{a_{i,j}})^{\alpha^j} = \pi _{j=0}^{k-1} K _{i,j}^{\alpha^j} mod p
$$ 

 

  

 



 

!!! note

    Although this formula includes double exponentiation – raising a given value to the power $\alpha^𝑗$ – in what follows, 𝛼 and 𝑗 will always be small values (bounded by 𝑛). This can also be reduced if desired since the same result will be achieved if the exponents $\alpha^𝑗$ are reduced to 𝛼<sup> 𝑗</sup> mod 𝑞.


To share secret values amongst each other, it is assumed that each guardian 𝑇<sub>𝑖 </sub>has previously shared an auxiliary public encryption function 𝐸<sub>𝑖</sub> with the group.[^3] Each guardian 𝑇<sub>𝑖</sub> then publishes the encryption 𝐸<sub>ℓ</sub> (𝑅<sub>𝑖,ℓ</sub> , 𝑃<sub>𝑖</sub> (ℓ) ) for every other guardian 𝑇<sub>ℓ</sub> – where 𝑅<sub>𝑖,ℓ</sub> is a random nonce. 

Guardian $𝑇_ℓ$ can now decrypt each $𝑃_i(ℓ)$ encrypted to its public key and verify its validity against the commitments made by $𝑇_𝑖$ to its coefficients $𝐾_{𝑖,0},𝐾_{𝑖,1}, … ,𝐾_{𝑖,𝑘−1}$ by confirming that the following equation holds:


$$
𝑔 ^{𝑃_i (ℓ)} mod 𝑝 =\pi_{j=0}^{k-1} K_{i,j}^{ℓ^j}\mod p
$$

Guardians then publicly report having confirmed or failed to confirm this computation. If the recipient guardian 𝑇<sub>ℓ</sub> reports not receiving a suitable value 𝑃<sub>𝑖</sub>(ℓ), it becomes incumbent on the sending guardian 𝑇<sub>𝑖</sub> to publish this 𝑃<sub>𝑖</sub>(ℓ) together with the nonce 𝑅<sub>𝑖,ℓ</sub> it used to encrypt 𝑃<sub>𝑖</sub>(ℓ) under the public key 𝐸<sub>ℓ</sub> of recipient guardian 𝑇<sub>ℓ</sub> . If guardian 𝑇<sub>𝑖</sub> fails to produce a suitable 𝑃<sub>𝑖</sub>(ℓ) and nonce 𝑅<sub>𝑖,ℓ</sub> that match both the published encryption and the above equation, it should be excluded from the election and the key generation process should be restarted with an alternate guardian. If, however, the published 𝑃<sub>𝑖</sub> (ℓ) and 𝑅<sub>𝑖,ℓ</sub> satisfy both the published encryption and the equation above, the claim of malfeasance is dismissed and the key generation process continues undeterred.[^4]

 Once the baseline parameters have been produced and confirmed, all of the public commitments 𝐾<sub>𝑖,𝑗</sub> are hashed together with the base hash 𝑄 to form an extended base hash 𝑄<sup>-</sup> that will form the basis of subsequent hash computations. The hash function SHA-256 will be used here and for all hash computations for the remainder of this document.




!!! note

    An election verifier must verify the correct computation of the joint election public key and extended base hash.
    (A) 𝑄̅ =𝐻(𝑄,𝐾<sub>1,0</sub>,𝐾<sub>1,1</sub>,𝐾<sub>1,2</sub>, … ,𝐾<sub>1,𝑘−1</sub>,𝐾<sub>2,0</sub>,𝐾<sub>2,1</sub>,𝐾<sub>2,2</sub>, … ,𝐾<sub>2,𝑘−1</sub>, … ,𝐾<sub>𝑛,0</sub>,𝐾<sub>𝑛,1</sub>,𝐾<sub>𝑛,2</sub>, … , 𝐾<sub>𝑛,𝑘−1</sub>) 
    (B)
    $$ 
    𝐾 = \pi_{i=1}^{n}K_imod p
    $$


[^1]: If alternative parameters are allowed, election verifiers
must confirm that 𝑝, 𝑞, 𝑟, and 𝑔 are such that both 𝑝 and 𝑞 are prime (this may be done probabilistically using the Miller-Rabin algorithm), that 𝑝 −1 = 𝑞𝑟 is satisfied, that 𝑞 is not a divisor of 𝑟, that 1 < 𝑔 <  𝑝, that $𝑔^ 𝑞 mod 𝑝 = 1$, and that generation of the parameters is consistent with the cited standard.

[^1]: Shamir A. How to Share a Secret. (1979) Communications of the ACM.
1
[^2]: NIST (2015) Secure Hash Standard (SHS). In: FIPS 180-4. [https://csrc.nist.gov/publications/detail/fips/180/4/final](https://csrc.nist.gov/publications/detail/fips/180/4/final)

[^3]: A “traditional” ElGamal public key is fine for this purpose. But the baseline ElectionGuard parameters 𝑝 and 𝑞 are tuned for homomorphic purposes and are not well-suited for encrypting large values. The ElectionGuard guardian keys can be used by breaking a message into small pieces (e.g. individual bytes) and encrypting a large value as a sequence of small values. However, traditional public-key encryption methods are more efficient. Since this key is only used internally, its form is not specified herein. 

[^4]: It is also permissible to dismiss any guardian that makes a false claim of malfeasance. However, this is not required as the sensitive information that is released as a result of the claim could have been released by the claimant in any case.
