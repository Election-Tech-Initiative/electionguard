# Key Generation

Before an election, the number of guardians $(n)$ is fixed together with a quorum value $(k)$  that describes the number of guardians necessary to decrypt tallies and produce election verification data. The values $n$ and $k$ are integers subject to the constraint that $1 \le k \le n$. Canvassing board members can often serve the role of election guardians, and typical values for $n$ and $k$ could be 5 and 3 – indicating that 3 of 5 canvassing board members must cooperate to produce the artifacts that enable election verification. The reason for not setting the quorum value $k$ too low is that it will also be possible for $k$ guardians to decrypt individual ballots.

!!! info
    Note that decryption of individual ballots does not directly compromise voter privacy since links between encrypted ballots and the voters who cast them are not retained by the system. However, voters receive verification codes that can be associated with individual encrypted ballots, so any group that has the ability to decrypt individual ballots can also coerce voters by demanding to see their tracking codes.

Threshold ElGamal encryption is used for encryption of ballots. This form of encryption makes it very easy to combine individual guardian public keys into a single public key for encrypting votes and ballots. It also offers a homomorphic property that allows individual encrypted votes to be combined to form encrypted tallies.

The guardians of an election will each generate a public-private key pair. The public keys will then be combined (as described in the following section) into a single election public key which is used to encrypt all selections made by voters in the election.

Ideally, at the conclusion of the election, each guardian will use its private key to form a verifiable partial decryption of each tally. These partial decryptions will then be combined to form full verifiable decryptions of the election tallies.

To accommodate the possibility that one or more of the guardians will not be available at the conclusion of the election to form their partial decryptions, the guardians will cryptographically share15 their private keys amongst each other during key generation in a manner to be detailed in the next section. A pre-determined threshold value $(k)$  out of the $(n)$ guardians will be necessary to produce a full decryption.

Additionally, each guardian will also generate an auxiliary public-private key pair. These auxiliary keys will be used by the guardians to exchange fragments of their principal vote- encryption keys and for other scenarios in which non-vote data may need to be encrypted.

## Overview of Key Generation

The $n$ guardians of an election are denoted by $T_1,T_2,\ldots, T_n$. Each guardian $T_i$ generates an
independent ElGamal public-private key pair by generating a random integer secret $s_i \in Z_q$ and forming the public key  $K_i=g^{s_i}\bmod p$. Each of these public keys will be published in the election record together with a non-interactive zero-knowledge Schnorr proof of knowledge of possession of the associated private key.

The joint election public key will be

$$
K = \prod_{i=1}^n K_i \bmod p
$$

To enable robustness and allow for the possibility of missing guardians at the conclusion of an election, the ElectionGuard key generation includes a sharing of private keys between guardians to enable decryption by any $k$ guardians. This sharing is verifiable, so that receiving guardians can confirm that the shares they receive are meaningful; and the process allows for decryption without explicitly reconstructing private keys of missing guardians.

Each guardian $T$ generates $k-1$ random polynomial coefficients $a_{i,j}$ such that $0\lt j \lt k$ and $0 \le a_{i,j} \le q$ and forms the polynomial

$$
P_i(x) = \sum_{j=0}^{k-1}a_{i,j}x^j\bmod q
$$

by setting $a_{i,0}$ equal to its secret value $s_i$. Guardian $T_i$ then publishes commitments $K_{i,j}= g^{a_{i,j}} \bmod p$ to each of its random polynomial coefficients. As with the primary secret keys, each guardian should provide a Schnorr proof of knowledge of the secret coefficient value $a_{i,j}$ associated with each published commitment $K_{i,j}$. Since polynomial coefficients will be generated and managed in precisely the same fashion as secret keys, they will be treated together in a single step below.

At the conclusion of the election, individual encrypted ballots will be homomorphically combined into a single encrypted aggregate ballot – consisting of an encryption of the tally for each option offered to voters. Each guardian will use its secret key to generate a partial decryption of each encrypted tally value, and these partial decryptions will be combined into full decryptions. If any election guardians are missing during tallying, any set of $k$ guardians who are available can cooperate to reconstruct the missing partial decryption.

All spoiled ballots are individually decrypted in precisely the same fashion.

## Details of Key Generation


Each guardian $T$ in an election with a decryption threshold of $k$ generates $k$ secret polynomial $i$
coefficients $a_{i,j}$ such that $0\le j \le k$ and $0 \le a_{i,j} \lt q$ and forms the polynomial

$$
P_i(x) = \sum_{j=0}^{k-1} a_{i,j}x^j \bmod q
$$

Guardian $T_i$ then publishes commitments $K_{i,j} = g^{a_{i,j}} \bmod q$ for each of its random polynomial coefficients. The constant term $a_{i,0}$ of this polynomial will serve as the private key for guardian $T_i$ and will also be denoted as $K_i = K_{i,0}$.

In order to prove possession of the coefficient associated with each public commitment, for each $K_{i,j}$ with $0 \le j \lt k$, guardian $T_i$ generates a Schnorr proof of knowledge for each of its coefficients.

This Non-Interactive Zero-Knowledge (NIZK) proof proceeds as follows.

### NIZK Proof by Guardian $T_i$ of its knowledge of secrets $a_{i,j}$ such that $K_{i,j}= g^{a_{i,j}} \bmod p$

For each $0 \le j \lt k$, Guardian $T_i$ generates random integer values $R_{i,j}$ in $Z_q$ and computes $h_{i,j}=g^{R_{i,j}} \bmod p$. Then, using the hash function SHA-256 (as defined in NIST PUB FIPS 180-4), guardian $T_i$ then performs a single hash computation $c_{i,j} = H(Q, K_{i,j}, h_{i,j} \bmod q$ and publishes the values $K_{i,j},h_{i,j},c_{i,j}$ and $u_{i,j} = (R_{i,j} + c_{i,j}a_{i,j}) \bmod q$.

!!! important
    An election verifier must confirm (A) and (B) for each guardian $T_i$ and for each $j \in Z_k$:

(A) The challenge $c_{i,j}$ is correctly computed as

$$
c_{i,j} = H(Q,K_{i,j},h_{i,j}) \bmod q
$$

(B) The equation

$$
g_{u_{i,j}} \bmod p = h_{i,j}K_{i,j}^{c_{i,j}} \bmod p
$$

is satisfied.

It is worth noting here that for any fixed constant $\alpha$, the value $g^{P_i(\alpha)} \bmod p$ can be computed entirely from the published commitments as

$$
g^{P_i(\alpha)} = g^{\sum_{j=0}^{k-1}a_{i,j}\alpha^j} \bmod p= \prod_{j=0}^{k-1}g_{a_{i,j}}\alpha^j \bmod p = \prod_{j=0}^{k-1}(g^{a_{i,j}})^{\alpha_j} \bmod p = \prod_{j=0}^{k-1} K_{i,j}^{\alpha^j}
$$

!!! info
    Although this formula includes double exponentiation – raising a given value to the power $\alpha^j$ – in what follows, $\alpha$ and $j$ will always be small values (bounded by $n$). This can also be reduced if desired since the same result will be achieved if the exponents $\alpha^j$ are reduced to $\alpha^j \bmod q$.

To share secret values amongst each other, it is assumed that each guardian $T_i$ has previously shared an auxiliary public encryption function $E_i$ with the group.
Each guardian $T_i$ then publishes the encryption $E_\ell ( R_{i,\ell}, P_i(\ell))$  for every other guardian $T_{\ell}$ – where $R_{i,\ell}$ is a random nonce.

Guardian $T_{\ell}$ can now decrypt each $P_i(\ell)$ encrypted to its public key and verify its validity against the commitments made by $T_i$ to its coefficients $K_{i,0},K_{i,0},\ldots,K_{i,k-1},$ by confirming that the following equation holds

$$
g^{P_i(\ell)} \bmod p = \prod_{j=0}^{k-1}(K_{i,j})^{\ell^j} \bmod p
$$

Guardians then publicly report having confirmed or failed to confirm this computation. If the recipient guardian $T_{\ell}$ reports not receiving a suitable value $P_i(\ell)$, it becomes incumbent on the sending guardian $T_i$ to publish this $P_i(\ell)$, together with the nonce $R_{i,\ell}$ it used to encrypt $P_i(\ell)$ under the public key $E_{\ell}$ of recipient guardian $T_{\ell}$. If guardian $T_i$ fails to produce a suitable $P_i(\ell)$ and nonce $R_{i,\ell}$ that match both the published encryption and the above equation, it should be excluded from the election and the key generation process should be restarted with an
alternate guardian. If, however, the published $P_i(\ell)$ and $R_{i,\ell}$ satisfy both the published encryption and the equation above, the claim of malfeasance is dismissed and the key generation process continues undeterred.

Once the baseline parameters have been produced and confirmed, all of the public commitments $K_{i,j}$ are hashed together with the base hash $Q$ to form an extended base hash $\bar{Q}$ that will form the basis of subsequent hash computations. The hash function SHA-256 will be used here and for all hash computations for the remainder of this document.

!!! important
    An election verifier must verify the correct computation of the joint election public key (A) and extended base hash (B).

(A)

$$
\bar{Q}=H(Q,K_{1,0},K_{1,1},K_{1,2},\ldots,K_{1,k-1},K_{2,0},K_{2,1},K_{2,2},\ldots,K_{2,k-1},\ldots,K_{n,0},K_{n,1},K_{n,2},\ldots,K_{n,k-1})
$$

(B)

$$
K = \prod_{i=1}^n K_i \bmod p
$$
