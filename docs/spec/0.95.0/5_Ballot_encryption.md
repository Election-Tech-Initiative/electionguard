# Ballot Encryption

An ElectionGuard ballot is comprised entirely of encryptions of one (indicating selection made) and zero (indicating selection not made). To enable homomorphic addition (for tallying), these values are exponentiated during encryption. Specifically, to encrypt a ballot entry $(V)$, a random value $R$ is selected such that $0 \le R \lt q$ and the following computation is performed:

* Zero (not selected) is encrypted as $(g^R \bmod p, K^R \bmod p)$
* One (selected) is encrypted as $(g^R \bmod p, g \cdot K^R \bmod p)$.

Note that if multiple encrypted votes $(g^{R_i} \bmod p, g^{V_i} \cdot K^{R_i} \bmod p)$ are formed, their component-wise product $(g^{\sum_{i}V_i} \cdot K^{\sum_{i}R_i} \bmod p)$ serves as an encryption of $\sum_iV_i$ – which is the tally of those votes.

A contest in an election consists of a set of options together with a selection limit that indicates the number of selections that are allowed to be made in that contest. In most elections, most contests have a selection limit of one. However, a larger selection limit (*e.g.*, select up to three) is not uncommon in some elections. Approval voting can be achieved by setting the selection limit to the total number of options in a contest. Ranked choice voting is not supported in this version of *ElectionGuard*, but it may be enabled in a future version. Also, write-ins are assumed to be explicitly registered or allowed to be lumped into a single "write-ins" category for the purpose of verifiable tallying. Verifiable tallying of free-form write-ins may be best done with a MixNet design.

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

The “random” nonces used for the ElGamal encryption of the ballot nonces are derived from a single 256-bit master nonce $R_B$ for each ballot. For each contest listed in the ballot coding file, a contest nonce $R_C$ is derived from the master nonce $(R_B)$ and the contest label $(L_C)$ as $R_C= H(L_C,R_B)$ using the hash function SHA-256. For each option listed in the ballot coding file, the nonce used to encrypt that option is derived from the contest nonce $(R_C)$ and the selection label for that option $(L_S)$ as $R=H(L_S,R_C)$.

A user of ElectionGuard may optionally provide an additional public key. If such a key is provided, ElectionGuard uses that key to encrypt each ballot’s master nonce $R_B$ and return this encryption together with the encrypted ballot.

Ballot nonces may be independent across different ballots, and only the nonces used to encrypt ballot selections need to be derived from the master nonce. The use of a single master nonce for each ballot allows the entire ballot encryption to be re-derived from the contents of a ballot and the master nonce. It also allows the encrypted ballot to be fully decrypted with the single master nonce.

## Outline for proofs of ballot correctness

To prove that an ElGamal encryption pair $(\alpha, \beta)$ is an encryption of zero, the Chaum-Pedersen protocol proceeds as follows.

### NIZK Proof that $(\alpha, \beta)$ is an encryption of zero (given knowledge of encryption nonce $R$)

The prover selects a random value $u$ in $Z_q$ and commits to the pair $(g^u \bmod p, K^u \bmod p)$. A hash computation is then performed (using the Fiat-Shamir heuristic) to create a pseudo-random challenge value $c=H(\bar{Q},(\alpha,\beta),(a,b))$, and the prover responds with $v=(u + cR) \bmod q$. A verifier can now confirm the claim by checking that both $g^V \bmod p = a \cdot \alpha^C \bmod p$ and $K^V \bmod p = b \cdot \beta^{C} \mod p$ are true.

### NIZK Proof that $(\alpha,\beta)$ is an encryption of one (given knowledge of encryption nonce $R$)

To prove that $(\alpha, \beta)$ is an encryption of one, $\frac{\beta}{g} \bmod p$ is substituted for $\beta$ in the above. The
verifier can be relieved of the need to perform a modular division by computing $\beta \bar{g} \bmod p$ rather than $\beta \bmod p$. As an alternative, the verifier can confirm that $g^c \cdot K^v \bmod p = b \cdot (\frac{\beta}{g})^c$ instead of $K^v \bmod p = b \cdot (\frac{\beta}{g})^c \bmod p$.
