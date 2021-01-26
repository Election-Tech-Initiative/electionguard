# Verifiable Decryption

## Discussion

To decrypt an aggregate encryption $(A,B)$ (or an individual encryption such as one on a spoiled ballot), each available election guardian $T_i$ uses its secret key $s_i$ to compute its share of the decryption as

$$
M_i=A^{s_i} \bmod p
$$

Each guardian $T_i$ also publishes a Chaum-Pedersen proof of the correctness of $M_i$ as follows.

### NIZK Proof by Guardian $T_i$ of knowledge of $s_i \in Z_p^r$ for which both $M_i=A^{s_i} \bmod p$ and $K_i=g^{s_i}  \bmod p$ 

Guardian $T_i$ selects a random value $u_i$ in $Z_q$ and commits to the pair

$$
(a_i,b_i )=\left(g^{u_i} \bmod p,A^{u_i}  \bmod p\right)
$$

The values $(A,B)$, $(a_i,b_i )$, and $M_i$ are hashed together with the extended base hash value $\bar{Q}$ to form a challenge value 

$$
c_i=H\left(\bar{Q},(A,B),(a_i,b_i ),M_i \right)
$$

and guardian T_i responds with 

$$
v_i=(u_i+c_i s_i )  \bmod q
$$

!!! important
    An election verifier must then confirm for each (non-placeholder) option in each contest in the ballot coding file the following for each decrypting guardian $T_i$.

    (A) The given value $v_i$ is in the set $Z_q$.

    (B) The given values $a_i$ and $b_i$ are both in the set $Z_q^r$.       
	
    (C) The challenge value $c_i$ satisfies 

    $$
    c_i=H\left(\bar{Q},(A,B),(a_i,b_i ),M_i \right)
    $$

    (D) The equation 

    $$
    g^(v_i )  mod p=(a_i K_i^{c_i} )  \bmod p
    $$

    is satisfied.

    (E) The equation 


    $$
    A^{v_i} \bmod p=(b_i M_i^{c_i} )  \bmod p
    $$

    is satisfied.

## Decryption when all guardians are present

If all guardians are present and have posted suitable proofs, the next step is to publish the value

$$
M=\frac{B}{\left(\prod_{i=1}^n{M_i}\right)}  \bmod p
$$

This $M$ has the property that $M=g^t  \bmod p$ where $t$ is the tally of the associated option.

In general, computation of this tally value t is computationally intractable.  However, in this application, t is relatively small – bounded by the number of votes cast.  Election administrators can determine this tally value t from M by exhaustive search, by precomputing a table of all possible M values in the allowable range and then performing a single look-up, or by a combination in which some exponentiations are precomputed and a small search is used to find the value of t (e.g., a partial table consisting of g^100  mod p, g^200  mod p, g^300  mod p, … is precomputed and the value M is repeatedly divided by g until a value is found that is in the partial table).  The value t is published in the election record, and verifiers should check both that M=g^t  mod p and that 

$$
B= \left(M⋅\prod_{i=1}^n M_i \right)  \bmod p
$$

## Decryption with missing guardians

If one or more of the election guardians are not available for decryption, any k available guardians can use the information they have to reconstruct the partial decryptions for missing guardians as follows.

If guardian $T_i$ is missing during decryption, each of at least $k$ available guardians $T_l$ should use its share $P_i (l)$ of the secret value $s_i$ previously shared by $T_i$ to compute a share of the missing partial decryption $M_i$ in the same way that it used its own secret $s_l$.  Specifically, guardian $T_l$ publishes partial decryption share

$$
M_{i,l}=A^{P_i (l)}  \bmod p
$$

Guardian $T_l$ also publishes a Chaum-Pedersen proof of the correctness of $M_(i,l)$ as follows.

### NIZK Proof by Guardian $T_l$ of knowledge of $s_{i,l} \in Z_p^r$ for which both $M_{i,l}=A^{s_{i,l}}  \bmod p$ and $g^{s_i} \bmod p=\prod_{j=0}^{k-1} K_{i,j}^{l^j}   \bmod p$

Guardian $T_l$ selects a random value $u_{i,l}$ in $Z_q$ and commits to the pair

$$
\left(a_{i,l},b_{i,l} \right)=\left(g^{u_{i,l} }  \bmod p,A^{u_{i,l}}  \bmod p\right)
$$

The values $(A,B)$, $(a_{i,l},b_{i,l} )$, and $M_(i,l)$ are hashed together with the extended base hash value $\bar{Q}$ to form a challenge value

$$
c_{i,l}=H\left(\bar{Q},(A,B),(a_{i,l},b_{i,l} ),M_{i,l} \right)
$$

and guardian $T_l$ responds with

$$
v_{i,l}=\left(u_{i,l}+c_{i,l} P_i (l)\right)  \bmod q
$$

It is important to note here that although the value $P_i (l)$ is known to both the missing guardian $T_i$ and the guardian $T_l$, it need not published or generally known.  However, the value 

$$
g^{P_i (l)}  \bmod p
$$

can be computed from public values as

$$
g^{P_i (l)}  \bmod p=\prod_{j=0}^{k-1} K_{i,j}^{l^j}  \bmod p.
$$

!!! important
    An election verifier must confirm the following for each (non-placeholder) option in each contest in the ballot coding file the following for each missing guardian $T_i$ and for each surrogate guardian $T_l$.

    (A) The given value $v_{i,l}$ is in the set $Z_q$.

    (B) The given values $a_{i,l}$ and $b_{i,l}$ are both in the set $Z_q^r$.

    (C) The challenge value $c_{i,l}$ satisfies 

    $$
    c_{i,l}=H\left(\bar{Q},(A,B),(a_{i,l},b_{i,l} ),M_{i,l} \right)
    $$

    (D) The equation 

    $$
    g^{v_{i,l}}  \bmod p=\left(a_{i,l}\cdot \left(\prod_{j=0}^{k-1} K_{i,j}^{l^j} \right)^{c_{i,l}} \right)  \bmod p
    $$

    is satisfied.

    (E)	The equation 

    $$
    A^{v_{i,l}}  \bmod p=\left(b_{i,l} M_{i,l}^{c_{i,l} } \right) \bmod p 
    $$

    is satisfied.

The final step to reconstruct a missing partial decryption $M_i$ is to compute Lagrange coefficients for a set of $k$ available guardians ${T_l \colon l \in U}$ with $|U|=k$ as

$$
w_l=\frac{(\prod_{j \in (U-{l})} j)}{\left(\prod_{j \in (U-{l})}(j-l) \right) } \bmod q.
$$

!!! important
    An election verifier should confirm that for each guardian $T_l$ serving to help compute a missing share of a tally, that its Lagrange coefficient $w_l$ is correctly computed by confirming the folloing equation 

    $$
    \left(\prod_{j \in (U-\{\ell \})}j\right)  \bmod q=\left(w_\ell \cdot \left(\prod_{j \in (U-\{\ell \})} \left(j-\ell \right) \right) \right) \bmod q
    $$

    An election verifier should then confirm the correct missing tally share for each (non-placeholder) option in each contest in the ballot coding file for each missing guardian $T_i$ as 

    $$
    M_i=\prod_{\ell  \in U}\left(M_{i,\ell }\right)^{w_\ell}  \bmod p
    $$

!!! note
    The missing secret $s_i$ could be computed directly via the equation below.  However, it is preferable to not release the missing secret and instead only release the partial decryption that the missing secret would have produced.  This prevents the missing secret $s_i$ from being used for additional decryptions without the cooperation of at least $k$ guardians.

$$
s_i=\sum_{\ell \in U} w_\ell P_i(\ell)  \bmod q
$$

!!! note ""
    As an example, consider an election with five guardians and a threshold of three.  If two guardians are missing at the time of decryption, the remaining three can perform any required decryptions by constructing missing partial descriptions as described in the text above.  If, instead, they take the shortcut of simply reconstructing and then using the two missing secrets, then any of the three could, at a later time, use its own secret together with the two reconstructed secrets to perform additional decryptions without cooperation of any other **guardian**.

The final step is to verify the tallies themselves.

!!! important
    An election verifier should confirm the following equations for each (non-placeholder) option in each contest in the ballot coding file.

    (A)

    $$
    B=\left(M⋅\left(\prod_{i=1}^n M_i \right)\right)  \bmod p
    $$

    (B)

    $$
    M=g^t  \bmod p.
    $$

    An election verifier should also confirm that the text labels listed in the election record match the corresponding text labels in the ballot coding file.

## Decryption of Spoiled Ballots

Every ballot spoiled in an election is individually verifiably decrypted in exactly the same way that the aggregate ballot of tallies is decrypted.  Election verifiers should confirm all such decryptions so that casual observers can simply view the decryptions and confirm that they match their expectations.

!!! important
    An election verifier should confirm the correct decryption of each spoiled ballot using the same process that was used to confirm the election tallies.
    An election verifier should also confirm that for each decrypted spoiled ballot, the selections listed in text match the corresponding text in the ballot coding file.

