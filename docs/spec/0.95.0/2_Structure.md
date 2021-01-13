# ElectionGuard Structure

ElectionGuard has four principal components:

1. Baseline Parameters – These are general parameters that are standard in every election. An alternate means for generating parameters is described, but the burden of verifying an election is increased if alternate parameters are used because a verifier would need to verify the proper construction of any alternate parameters.
2. Key Generation – Prior to each individual election, guardians must generate individual public-private key pairs and exchange shares of private keys to enable completion of an election even if some guardians become unavailable. Although it is preferred to generate new keys for each election, it is permissible to use the same keys for multiple elections so long as the set of guardians remains the same. A complete new set of keys must be generated if even a single guardian is replaced.
3. Ballot Encryption – While encrypting the contents of a ballot is a relatively simple operation, most of the work of ElectionGuard is the process of creating externally verifiable artifacts to prove that each encrypted ballot is well-formed (i.e., its decryption is a legitimate ballot without overvotes or improper values).
4. Verifiable Decryption – At the conclusion of each election, guardians use their private keys to produce election tallies together with verifiable artifacts that prove that the tallies are correct.

## Notation

In the remainder of this specification, the following notation will be used:

* $ℤ = \{\dots , −3, −2, −1, 0, 1, 2, 3, \dots\}$ is the set of integers.
* $ℤ_\eta = \{0, 1, 2, \dots , n − 1\}$ is the additive group of the integers modulo $p$.
* $Z_\eta^*$ is the multiplicative subgroup of $Z_\eta$. When $p$ is a prime, $Z_p^* = \{1,2,3, \dots, p-1\}$.
* $Z_p^r$ is the set of $r^{th}$-residues in $Z_p^*$. Formally, $Z_p^r = \{ y \in Z_p^*$ for which $\exists x \in Z_p^*$ such that $y=x^r\bmod p \}$. When $p$ is a prime for which $p-1=qr$ with $q$ a prime that is not a divisor of integer $r$, then $Z_r^p$ is an order $q$ cyclic subgroup of $Z_p^*$ and for each $y\in Z_p^*$, $y\in Z_r^p$ if and only if $y^q \bmod p = 1$.
* $x\equiv_n y$ is the predicate that is true if and only if $x \bmod n = y \bmod n$.
* The function $H()$ shall be use to designate the SHA-256 hash function (as defined in NIST PUB FIPS 180-4).
* In general, the variable pairs $(\alpha, \beta)$, $(a, b)$, and $(A,B)$ will be used to denote encryptions. Specifically, $(\alpha,\beta)$ will be used to designate encryptions of votes (*always* an encryption of a zero or one), $(A,B)$ will be used to denote aggregations of encryptions (which may be encryptions of larger values), and $(a,b)$ will be used to denote encryption commitments used to prove properties of other encryptions.
