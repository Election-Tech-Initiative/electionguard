# Verifiable Decryption

To decrypt an aggregate encryption $(A, B)$ (or an individual encryption such as one on a spoiled ballot), each available election guardian $T_i$ uses its secret key $s_i$ to compute its share of the decryption as

$$
M_i = A^{s_i} \bmod p
$$

Each guardian $T_i$ also publishes a Chaum-Pedersen proof of the correctness of $M_i$ as follows.

<u>NIZK Proof by Guardian 𝑇𝑖 of knowledge of $s_i \in \mathbb{Z}^r_p$ for which both $M_i = A^{s_i} \bmod p$ and $K_i = g^{s_i} \bmod p$ </u>

Guardian $T_i$ selects a random value $u_i$ in $\mathbb{Z}_q$ and commits too the pair $(a_i, b_i) = (g^{u_i} \bmod p, A^{u_i} \bmod p)$. The values $(A, B), (a, b)$ and $M$ are hashed together with the extended base hash value $\overline{Q}$ t
to form a challenge value $c_i = H(\overline{Q}, (A, B), (a_i, b_i), M)$, and the guardian $T_i$ responds with $v_i = (u_i + c_i s_i) \bmod q$.

!!! important
    An election verifier must then confirm for each (non-placeholder) option in each contest in the ballot coding ffile the following for each decrypting guardian $T_i$:

    (A) The given value $v_i$ is in the set $\mathbb{Z}_q^r$

    (B) The given values $a_i$ and $b_i$ are both in the set $\mathbb{Z}_q^r$

    (C) The challenge value $c_i$ satisfies $c_i = H(\overline{Q}, (A, B), (a_i, b_i), M)$.

    (D) The equation $g^{v_i} \bmod p = (a_i K_i^{c_i}) \bmod p$ is satisfied.

    (E) The equation $A^{v_i} \bmod p = (b_i M_i^{c_i}) \bmod p$ is satisfied.

## Decryption when all guardians are present
If all guardians are present and have posted suitable proofs, the next step is to publish the
value

$$
M = B / (\prod_{i=1}^n M_i) \bmod p.
$$

This $M$ has the property that $M = g_t \bmod p$ where $t$ is the tally of the associated option.

In general, computation of this tally value $t$ is computationally intractable. However, in this application, $t$ is relatively small - bounded by the number of votes cast. Election administrators can determine this tally value $t$ from $M$ by exhaustive search, by precomputing a table of all possible $M$ values in the allowable range and then performing a single look-up, or by a combination in which some exponentiations are precomputed and a small search is used to find the value of $t$ (e.g., a partial table consisting of $g^{100} \bmod p, g^{200} \bmod p, g^{300} \bmod p$ … is precomputed and the value $M$ is repeatedly divided by $g$ until a value is found that is in the partial table). The value $t$ is published in the election record, and verifiers  should check both that $M = g^t \bmod p$ and that $B = (M \cdot \prod^n_{i=1} M_i) \bmod p$.

## Decryption with missing guardians
If one or more of the election guardians are not available for decryption, any $k$ available
guardians can use the information they have to reconstruct the partial decryptions for missing
guardians as follows.

If guardian $T_i$ is missing during decryption, each of at least $k$ available guardians $T_\ell$ should use its share $P_i(\ell)$ of the secret value $s_i$ previously shared by $T_i$ to compute a share of the missing partial decryption $M_i$ in the same way that it used its own secret $s_\ell$. Specifically, guardian $T_\ell$ publishes partial decryption share

$$
M_{i, \ell} = A^{P_i(\ell)} \bmod p
$$

Guardian $T_\ell$ also publishes a Chaum-Pedersen proof of the correctness of $M_{i, \ell}$ as follows.

<u>NIZK Proof by Guardian $T_\ell$ of knowledge of $s_{i, \ell} \in \mathbb{Z}^r_p$ for which both $M_{i, \ell} = A^{s_{i, \ell}} \bmod p$ and $g^{s_i} \bmod p = \prod^{k=1}_{j=0}K^{\ell^j}_{i, j} \bmod p$</u>

Guardian $T_\ell$ selects a random value $u_{i, \ell}$ in $\mathbb{Z}_q$ and commits to the pair $(a_{i, \ell}, b_{i, \ell}) = (g^{u_{i, \ell}} \bmod p, A^{u_{i, \ell}} \bmod p)$. The values $(A, B)$, $(a_{i, \ell}, b_{i, \ell})$, and $M_{i, \ell}$ are hashed together with the extended base hash value $\bar{Q}$ to form a challenge value $c_{i, \ell} = H(\bar{Q}, (A, B), (a_{i, \ell}, b_{i, \ell}), M_{i, \ell})$, and the guardian $T_\ell$ responds with $v_{i, \ell} = (u_{i, \ell} + c_{i, \ell} P_i(\ell)) \bmod q$.

It is important to note here that although the value $P_i(\ell)$ is known to both the missing guardian $T_i$ and the guardian $T_\ell$, it need not published or generally known. However, the value $g^{P_i(\ell)} \bmod p$ can be computer form public values as

$$
g^{P_i(\ell)} \bmod p = \prod_{j=0}^{k-1} K^{\ell^j}_{i, j} \bmod p.
$$

!!! important
    An election verifier must confirm for each (non-placeholder) option in each contest in the ballot coding file the following for each missing guardian $T_i$ and for each surrogate guardian $T_\ell$.

    (A) The given value $v_{i, \ell}$ is in the set $\mathbb{Z}_q$.

    (B) The given values $a_{i, \ell}$ and $b_{i, \ell}$ are both in the set $\mathbb{Z}_q^r$.

    (C) The challenge value $c_{i, \ell}$ satisfies $c_{i, \ell} = H(\bar{Q}, (A, B), (a_{i, \ell}, b_{i, \ell}), M_{i, \ell})$.

    (D) The equation $g^{v_{i, \ell}} \bmod p = (a_{i, \ell} K_{i, \ell}^{c_{i, \ell}}) \bmod p$ is satisfied.

    (E) The equation $A^{v_{i, \ell}} \bmod p = (b_{i, \ell} M_{i, \ell}^{c_{i, \ell}}) \bmod p$ is satisfied.

The final step to reconstruct a missing partial decryption $M_i$ is to compute Lagrange coefficients for a set of $k$ available guardians $\{ T_\ell:\ell \in U \}$ with $|U| = k$ as

$$
w_\ell = \frac{(\prod_{j \in (U - \{\ell\})}j)}{(\prod_{j \in (U - \{\ell\}))}(j - \ell))} \bmod q.
$$

!!! important
    An election verifier should confirm that for each guardian $T_\ell$ serving to help compute a missing share of a tally, that its Lagrange coefficient $w_\ell$ is correctly computer by confirming the equation $(\prod_{j\in(U = \{\ell\})} j) \bmod q = (w_\ell (\prod_{j \in (U - \{\ell\})} (j-\ell))) \bmod q$.

    An election verifier should then confirm the correcty missing tally share for each (non-placeholder) option in each contest in the ballot coding file for each missing guardian $T_i$ as $M_i = \prod_{\ell \in U} (M_{i, \ell})^{w_\ell} \bmod p$.

!!! info
    Note that the missing secret $s_i$ could be computed directly as $s_i = \sum_{\ell \in U}w_\ell P_i(\ell) \bmod q$. However, it is preferable to not release the missing secret and instead only release the partial decryption that the missing secret would have produced. This prevents the missing secret $s_i$ from being used for additional decryptions without the cooperation of at least $k$ guardians.

    As an example, consider an election with five guardians and a threshold of three. If two guardians are missing at the time of decryption, the remaining three can perform any required decryption, the remaining three can perform any required decryptions by constructing missing partial descriptions as described in the text above. If, instead, they take the shortcut of simply reconstructing and then using the two missing secrets, then any of the three could, at a later time, use its own secret together with the two reconstructed secrets to perform additional decryptions without cooperation of any other guardian.

The final step is to verify the tallies themselves.

!!! important
    An election verifier should confirm the following equations for each (non-placeholder) option in each contest in the ballot coding file.

    (A) $B = (M (\prod^n_{i=i} M_i)) \bmod p$.
    
    (B) $M = g^t \bmod p$.

    An election verifier should also confirm that the text labels listed in the election record match the corresponding text labels in the ballot coding file.

## Decryption of spoiled ballots
Every ballot spoiled in an election is individually verifiably decrypted in exactly the same way that the aggregate ballot of tallies is decrypted. Election verifiers should confirm all such decryptions so that casual observers can simply view the decryptions and confirm that they match their expectations.

!!! important
    An election verifier should confirm the correct decryption of each spoiled ballot using the same process that was used to confirm the election tallies.

    An election verifier should also confirm that for each decrypted spoiled ballot, the selections listed in text match the corresponding text in the ballot coding file.