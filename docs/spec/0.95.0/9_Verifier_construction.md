# Verifier Construction

While it is desirable for anyone who may construct an ElectionGuard verifier to have as complete understanding as possible of the ElectionGuard design, this section isolates the items which must be verified and maps the variables used in the specification equations herein to the labels provided in the artifacts produced in an election. [^23]

## Implementation details

There are four operations which must be performed – all on very large integer values: modular addition, modular multiplication, modular exponentiation, and SHA-256 hash computations.  These operations can be performed using a programming language that provides native support, by importing tools to perform these large integer operations, or by implementing these operations from scratch.

### Modular Addition

To compute 

$$
(a+b) \bmod n
$$

one can compute 

$$
((a \bmod n)+(b \bmod n)) \bmod n
$$

However, this is rarely beneficial.  If it is known that $a,b \in Z_n$, then one can choose to avoid the division normally inherent in the modular reduction and just use 

$$
(a+b) \bmod n=a+b
$$
 
(if $a+b \lt n$) or 

$$
a+b-n
$$ 

(if $a+b \ge n$).

### Modular Multiplication

To compute 

$$
(a \times b) \bmod n
$$

one can compute 

$$
((a \bmod n) \times(b \bmod n))  \bmod n
$$

Unless it is already known that $a,b \in Z_n$, it is usually beneficial to perform modular reduction on these intermediate values before computing the product.  However, it is still necessary to perform modular reduction on the result of the multiplication.

### Modular Exponentiation

To compute

$$
a^b  \bmod n
$$

one can compute 

$$
(a \bmod n)^b  \bmod n
$$

but one should not perform a modular reduction on the exponent.[^24] One should, however, never simply attempt to compute the exponentiation $a^b$ before performing a modular reduction as the number $a^b$ would likely contain more digits then there are particles in the universe.  Instead, one should use a special-purpose modular exponentiation method such as repeated squaring which prevents intermediate values from growing excessively large.  Some languages include a native modular exponentiation primitive, but when this is not available a specialized modular exponentiation tool can be imported or written from scratch.

### Hash Computation

Hashes are computed using the SHA-256 hash function in NIST (2015) Secure Hash Standard (SHS) which is published in FIPS 180-4 and can be found in [https://csrc.nist.gov/publications/detail/fips/180/4/final](https://csrc.nist.gov/publications/detail/fips/180/4/final).  

For the purposes of SHA-256 hash computations, all inputs – whether textural or numeric – are represented as utf-8 encoded strings.  Numbers are represented as strings in base ten.  The hash function expects a single-dimensional array of input elements that are hashed iteratively, rather than concatenated together.  Each element in the hash is separated by the pipe character (“|”). When dealing with multi-dimensional arrays, the elements are hashed recursively in the order in which they are input into the hash function.  For instance, calling 

$$
H(1,2,[3,4,5],6)
$$

is a function call with 4 parameters, where the 3rd parameter is itself an array.  The hash function will process arguments 1 and 2, when it gets to argument 3 it will traverse the array (and hash the values 3, 4 ,5) before hashing the final fourth argument (whose value is 6).  When hashing an array element that is empty, the array is instead replaced with the word “null” as a placeholder.

## Parameter Validation

!!! important
    An *ElectionGuard* version 1 election verifier may assume that the baseline parameters match the parameters provided above.  However, it is recommended that the below parameters be checked against the parameters of each election to accommodate the possibility of different parameters in future versions of *ElectionGuard*.[^25]

| Variable | Meaning | Folder | File | Level |
| -------  | ------- | ------ | ---- | ----- |
| $p$ | 4096-bit modulus | root | constants.json | large_prime |
| $q$ | 256-bit prime order of subgroup $Z_p^*$ of encryptions | root | constants.json | small_prime |
| $r$ | co-factor of $q$ | root | constants.json | cofactor |
| $g$ | generator of order $q$ multiplicative subgroup of $Z_p^*$ | root | contstants.json | generator |
| $n$ | number of guardians | root | context.json | number_of_guardians |
| $k$ | minimum number of guardians required to decrypt tallies and produce verification data | root | context.json | quorum |
| $Q$ | base hash value formed by $p$, $q$, $g$, $n$, $k$, date, and jurisdictional information | root | context.json | crypto_base_hash |

## Guardian Public Key Validation

!!! important
    An election verifier must confirm the following for each guardian $T_i$ and for each $j \in Z_k$:

	(A) The challenge $c_{i,j}$ is correctly computed as 

	$$
	c_{i,j}=H(Q,K_{i,j},h_{i,j} )  \bmod q
	$$

	(B) The equation 

	$$
	g^{u_{i,j} }  \bmod p=h_{i,j} K_{i,j}^{c_{i,j} }  \bmod p 
	$$

    is satisfied.

| Variable | Meaning | Folder | File | Level |
| -------  | ------- | ------ | ---- | ----- |
| $K_{i,j}$ | public form of each random coefficient $a_{i,j}$ | coefficients | every file in this folder | large_prime | coefficient_proofs $\rightarrow$ [Item] $\rightarrow$  public_key |
| $h_(i,j)$ | coefficient commitments | coefficients | every file in this folder | coefficient_proofs $\rightarrow$ [Item] $\rightarrow$ commitment |
| $c_i$ | challenge value | coefficients | every file in this folder | coefficient_proofs $\rightarrow$ [Item] $\rightarrow$ challenge |
| $u_{i,j}$ | response | coefficients | every file in this folder | coefficient_proofs $\rightarrow$ [Item] $\rightarrow$ response |

## Election Public Key Validation

!!! important
    An election verifier must verify the correct computation of the joint election public key and extended base hash.

    (A) Joint election public key

	$$
	K=\prod_{i=1}^n K_i  \bmod p
	$$

    (B) Extended base hash

	$$
	\bar{Q} = H(Q,K_1,0,K_1,1,K_1,2,\ldots,K_{1,k-1},K_2,0,K_2,1,K_2,2,\ldots,K_{2,k-1},\ldots,K_{n,0},K_{n,1},K_{n,2},\ldots,K_{n,k-1})
	$$


| Variable | Meaning | Folder | File | Level |
| -------  | ------- | ------ | ---- | ----- |
| $\bar{Q}$ | extended base hash | Root | context.json | crypto_extended_base_hash |
| $K$ | joint election public key | Root | context.json | elgamal_public_key |

## Correctness of Selection Encryptions

!!! important
    An election verifier must confirm the following for each possible selection on a ballot:

    The given values $\alpha$, $\beta$, $a_0$, $b_0$, $a_1$, and $b_1$ are all in the set $Z_p^r$.  (A value $x$ is in $Z_p^r$ if and only if $x$ is an integer such that $0 \le x \lt p$ and $x^q  \bmod p=1$ is satisfied.)

	(J) The challenge $c$ is correctly computed as 

	$$
	c=H(\bar{Q},(\alpha,\beta),(a_0,b_0 ),(a_1,b_1 ))
	$$

	(K) The given values $c_0$, $c_1$, $v_0$, and $v_1$ are each in the set $Z_q$.  (A value $x$ is in $Z_q$ if and only if $x$ is an integer such that 0 \le x \lt q.)

	(L) The equation 
		
	$$
	c=(c_0+c_1 )  \bmod q
	$$

    is satisfied.

    (M) The equation 

	$$
	g^{v_0}  \bmod p= a_0 \alpha^{c_0}  \bmod p
	$$

    is satisfied.

	(N) The equation 

	$$
	g^{v_1}  \bmod p=a_1 \alpha^{c_1}  \bmod p
	$$

    is satisfied.

	(O) The equation 

	$$
	K^{v_0}  \bmod p=b_0 \beta^{c_0}  \bmod p
	$$

    is satisfied.

	(P) The equation 

	$$
	g^{c_1} K^{v_1}  \bmod p=b_1 \beta^{c_1}  \bmod p
	$$

    is satisfied.

| Variable | Meaning | Folder | File | Level |
| -------  | ------- | ------ | ---- | ----- |
| $(\alpha,\beta)$ | encryption of vote | encrypted_ballots | every file in this folder | contests $\rightarrow$ [Item] $\rightarrow$ ballot_selections $\rightarrow$ [Item] $\rightarrow$ ciphertext $\rightarrow$ pad, data |
| (a_0,b_0) | commitment to vote being an encryption of zero | encrypted_ballots | every file in this folder | contests $\rightarrow$ [Item] $\rightarrow$ ballot_selections $\rightarrow$ [Item] $\rightarrow$ proof $\rightarrow$ proof_zero_pad, proof_zero_data |
| $(a_1,b_1)$ | commitment to vote being an encryption of one | encrypted_ballots | every file in this folder | contests $\rightarrow$ [Item] $\rightarrow$ ballot_selections $\rightarrow$ [Item] $\rightarrow$ proof $\rightarrow$ proof_one_pad, proof_one_data |
| $c$ | challenge | encrypted_ballots | every file in this folder | contests $\rightarrow$ [Item] $\rightarrow$ ballot_selections $\rightarrow$ [Item] $\rightarrow$ proof $\rightarrow$ proof_challenge |
| $c_0$ | derived challenge to encryption of zero | encrypted_ballots | every file in this folder | contests $\rightarrow$ [Item] $\rightarrow$ ballot_selections $\rightarrow$ [Item] $\rightarrow$ proof $\rightarrow$ proof_zero_challenge |
| $c_1$ | derived challenge to encryption of one | encrypted_ballots | every file in this folder | contests $\rightarrow$ [Item] $\rightarrow$ ballot_selections $\rightarrow$ [Item] $\rightarrow$ proof $\rightarrow$ proof_one_challenge |
| $v_0$ | response to zero challenge | encrypted_ballots | every file in this folder | contests $\rightarrow$ [Item] $\rightarrow$ ballot_selections $\rightarrow$ [Item] $\rightarrow$ proof $\rightarrow$ proof_zero_response |
| $v_1$ | response to one challenge | encrypted_ballots | every file in this folder | contests $\rightarrow$ [Item] $\rightarrow$ ballot_selections $\rightarrow$ [Item] $\rightarrow$ proof $\rightarrow$ proof_one_response |

## Adherence to Vote Limits

!!! important
    An election verifier must confirm the following for each contest on the ballot:

	(H) The number of placeholder positions matches the contest’s selection limit $L$.

	(I) The contest total $(A,B)$ satisfies
	
	$$
	A=\prod_i \alpha_i  \bmod p
	$$ 
	
	and 
	
	$$
	B=\prod_i \beta_i  \bmod p
	$$
	
	where the $(\alpha_i,\beta_i )$ represent all possible selections (including placeholder selections) for the contest.

	(J) The given value $V$ is in $Z_q$.

	(K) The given values a and b are each in $Z_p^r$.

	(L) The challenge value $C$ is correctly computed as 
	
	$$
	C=H(\bar{Q},(A,B),(a,b))
	$$

	(M) The equation 
	
	$$
	g^V  \bmod p=(aA^C )  \bmod p
	$$ 
	
	is satisfied.

	(N) The equation 
	
	$$
	((g^{LC} K)^V )  \bmod p=(bB^C )  \bmod p
	$$ 
	
	is satisfied.

| Variable | Meaning | Folder | File | Level |
| -------  | ------- | ------ | ---- | ----- |
| $(\alpha_i,\beta_i)$ | encryption of $i^th$ vote in contest | encrypted_ballots | every file in this folder | contests $\rightarrow$ [Item] $\rightarrow$ ballot_selections $\rightarrow$ [Item] $\rightarrow$ ciphertext $\rightarrow$ pad, data |
| $(A,B)$ | encryption of total votes in contest | encrypted_ballots | every file in this folder | contests $\rightarrow$ [Item] $\rightarrow$ total $\rightarrow$ pad, data |
| $(a,b)$ | commitment to vote being an encryption of one | encrypted_ballots | every file in this folder | contests $\rightarrow$ [Item] $\rightarrow$ total $\rightarrow$ proof $\rightarrow$ pad, data |
| $C$ | selection limit challenge | encrypted_ballots | every file in this folder | contests $\rightarrow$ [Item] $\rightarrow$ proof $\rightarrow$ challenge |
| $L$ | contest selection limit | root | description.json | contests $\rightarrow$ [Item] $\rightarrow$ votes_allowed |
| $V$ | response to selection limit challenge | encrypted_ballots | every file in this folder | contests $\rightarrow$ [Item] $\rightarrow$ proof $\rightarrow$ response |

## Validation of Ballot Chaining

!!! important
    An election verifier must confirm that each of the values in the running hash is correctly computed.  Specifically, an election verifier must confirm each of the following.

	(D) The equation $H_0=H(\bar{Q})$ is satisfied.

	(E) For each ballot 
	
	$$
	B_i, H_i=H(H_{i-1},D,T,B_i)
	$$ 
	
	is satisfied.

	(F) The closing hash 
	
	$$
	\bar{H} =H(H_l,\text{“CLOSE"})
	$$ 
	
	is correctly computed from the final tracking code $H_l$.

| Variable | Meaning | Folder | File | Level |
| -------  | ------- | ------ | ---- | ----- |
| $H_i$  | running hash of ballots produced | encrypted_ballots | every file in this folder | tracking_hash (also previous_tracking_hash) |

## Correctness of Ballot Aggregation

!!! important
    An election verifier must confirm for each (non-placeholder) option in each contest in the ballot coding file that the aggregate encryption $(A,B)$ satisfies 
	
	$$
	A=\prod_j\alpha_j
	$$  
	
	and 
	
	$$
	\beta=\prod_j \beta_j
	$$ 
	
	where the $(\alpha_j,\beta_j )$ are the corresponding encryptions on all cast ballots in the election record.

| Variable | Meaning | Folder | File | Level |
| -------  | ------- | ------ | ---- | ----- |
| $(\alpha_j,\beta_j)$ | encryption of vote | encrypted_ballots | every file in this folder	 | contests $\rightarrow$ [Item] $\rightarrow$ ballot_selections $\rightarrow$ [Item] $\rightarrow$ ciphertext $\rightarrow$ pad, data |
| $(A,B)$ | encrypted aggregate total of votes in contest | root | tally.json | [prefix] $\rightarrow$ message $\rightarrow$ pad, data |

## Correctness of Partial Decryptions

!!! important
    An election verifier must then confirm for each (non-placeholder) option in each contest in the ballot coding file the following for each decrypting trustee $T_i$.

	The given value $v_i$ is in the set $Z_q$.

	The given values $a_i$ and $b_i$ are both in the set $Z_q^r$.

	The challenge value $c_i$ satisfies 
	
	$$
	c_i=H(\bar{Q},(A,B),(a_i,b_i ),M_i )
	$$
 
	The equation 

	$$
	g^{v_i}  \bmod p=(a_i K_i^{c_i} )  \bmod p
	$$

    is satisfied.

    The equation $A^{v_i}  \bmod p=(b_i M_i^{c_i} )  \bmod p$ is satisfied.

## Correctness of Partial Decryptions

!!! important
	An election verifier must then confirm for each (non-placeholder) option in each contest in the ballot coding file the following for each decrypting trustee $T_i$.

	(F) The given value $v_i$ is in the set of $Z_q$

	(G) The given values $a_i$ and $b_i$ are both in the set $Z_q^r$.

	(H) The challenge value $c_i$ satisfies 
	
	$$
	c_i=H(Q ̅,(A,B),(a_i,b_i ),M_i )
	$$

	(I) The equation 
	
	$$
	g^{v_i} \bmod p=(a_i K_i^{c_i} )  \bmod p
	$$
	
	is satisfied.

	(J) The equation 
	
	$$
	A^{v_i}  \bmod p=(b_i M_i^{c_i} )  \bmod p
	$$ 
	
	is satisfied.

| Variable | Meaning | Folder | File | Level |
| -------  | ------- | ------ | ---- | ----- |
| $(A,B)$ | encrypted aggregate total of votes in contest	root | tally.json | [prefix] $\rightarrow$ message $\rightarrow$ pad, data |
| $M_i$ | partial decryption of $(A,B)$ by guardian $T_i$ | root | tally.json | [prefix] $\rightarrow$ shares $\rightarrow$ [Item] $\rightarrow$ share |
| $(a_i,b_i)$ | commitment by guardian $T_i$ to partial decryption of $(A,B)$ | root | tally.json | [prefix] $\rightarrow$ shares $\rightarrow$ [Item] $\rightarrow$ proof $\rightarrow$ pad, data |
| $c_i$ | challenge to partial decryption of guardian $T_i$  | root | tally.json | [prefix] $\rightarrow$ shares $\rightarrow$ [Item] $\rightarrow$ proof $\rightarrow$ challenge |
| $v_i$ | response to challenge of guardian $T_i$ | root	tally.json | [prefix] $\rightarrow$ shares $\rightarrow$ [Item] $\rightarrow$ proof $\rightarrow$ response |

## Correctness of Substitute Data for Missing Guardians

!!! note
	This is only necessary if some guardians are missing during tallying

!!! important
	An election verifier must confirm for each (non-placeholder) option in each contest in the ballot coding file the following for each missing trustee $T_i$ and for each surrogate trustee $T_\ell$.

	(A) The given value $v_{i,l}$ is in the set $Z_q$.

	(B) The given values $a_{i,l}$ and $b_{i,l}$ are both in the set $Z_q^r$.

	(C) The challenge value $c_{i,l}$ satisfies 
	
	$$
	c_(i,l)=H(Q ̅,(A,B),(a_(i,l),b_(i,l) ),M_(i,l) )
	$$

	(D) The equation 
	
	$$
	g^{v_{i,l}}  \bmod p=\left(a_{i,l}\cdot \left(\prod_{j=0}^{k-1} K_{i,j}^{l^j} \right)^{c_{i,l} } \right)  \bmod p
	$$
	
	is satisfied.

	(E) The equation 
	
	$$
	A^{v_{i,\ell}}  \bmod p= \left( b_{i,\ell} M_{i,l}^{c_{i,l}} \right)  \bmod p
	$$
	
	is satisfied.

| Variable | Meaning | Folder | File | Level |
| -------  | ------- | ------ | ---- | ----- |
| $(A,B)$ | encrypted aggregate total of votes in contest | root | tally.json | [prefix] $\rightarrow$ message $\rightarrow$ pad, data |
| $M_(i,\ell)$ | share of guardian $T_\ell$ of missing partial decryption of $(A,B)$ by guardian $T_i$ | root | tally.json | [prefix] $\rightarrow$ shares $\rightarrow$ [Item] $\rightarrow$ substitute_proof $\rightarrow$ [item] $\rightarrow$ share |
| $(a_{i,l},b_{i,l})$ | commitment by guardian $T_\ell$ to share of partial decryption for missing guardian $T_i$ | root | tally.json | [prefix] $\rightarrow$ shares $\rightarrow$ [Item] $\rightarrow$ substitute_proof $\rightarrow$ [item] $\rightarrow$ pad, data |
| $c_{i,\ell}$ | challenge to guardian $T_\ell$ share of missing partial decryption of guardian $T_i$ | root | tally.json | [prefix] $\rightarrow$ shares $\rightarrow$ [Item] $\rightarrow$ substitute_proof $\rightarrow$ [item] $\rightarrow$ challenge |
| $v_{i,l}$ | response to challenge of guardian $T_\ell$ share of partial decryption of guardian $T_i$ | root | tally.json | [prefix] $\rightarrow$ shares $\rightarrow$ [Item] $\rightarrow$ substitute_proof $\rightarrow$ [item] $\rightarrow$ response |

## Correctness of Construction of Replacement Partial Decryptions

!!! note
	This is only necessary if some guardians are missing during tallying

!!! important
	An election verifier should confirm that for each trustee $T_\ell$ serving to help compute a missing share of a tally, that its Lagrange coefficient $w_\ell$ is correctly computed by confirming the equation

	$$
	\left(\prod_{j\in(U-{\ell})}j\right)  \bmod q=\left(w_l⋅\left(\prod_{j\in (U-{l})} (j-\ell) \right)\right)  \bmod q
	$$

	An election verifier should then confirm the correct missing tally share for each (non-placeholder) option in each contest in the ballot coding file for each missing trustee $T_i$ as

	$$
	M_i=\prod_{\ell \in U}\left(M_{i,\ell}\right)^{w_\ell}  \bmod p
	$$

| Variable | Meaning | Folder | File | Level |
| -------  | ------- | ------ | ---- | ----- |
| $w_\ell$ | coefficient for use with shares of guardian $T_\ell$ | root | tally.json | [prefix] $\rightarrow$ shares $\rightarrow$ [item] $\rightarrow$ coefficient |
| $M_{i,\ell}$ | share of guardian $T_\ell$ of missing partial decryption of $(A,B)$ by guardian $T_i$ | root | tally.json | [prefix] $\rightarrow$ shares $\rightarrow$ [Item] $\rightarrow$ substitute_proof $\rightarrow$ [item] $\rightarrow$ share |
| $M_i$ | partial decryption of $(A,B)$ by guardian $T_i$ | root | tally.json | [prefix] $\rightarrow$ shares $\rightarrow$ [Item] $\rightarrow$ share |

## Validation of Correct Decryption of Tallies

!!! important
	An election verifier should confirm the following equations for each (non-placeholder) option in each contest in the ballot coding file.

	(C) 

	$$
	B=\left(M \cdot \left(\prod_{i=1}^n M_i \right)\right)  \bmod p
	$$

	(D) 	
	
	$$
	M=g^t  \bmod p
	$$

	An election verifier should also confirm that the text labels listed in the election record match the corresponding text labels in the ballot coding file.

| Variable | Meaning | Folder | File | Level |
| -------  | ------- | ------ | ---- | ----- |
| $M_i$ | partial decryption of $(A,B)$ by guardian $T_i$ | root | tally.json | [prefix] $\rightarrow$ shares $\rightarrow$ [Item] $\rightarrow$ share |
| (M) | full decryption of $(A,B)$ | root | tally.json | [prefix] $\rightarrow$ value |
| $t$ | tally value | root | tally.json | [prefix] $\rightarrow$ tally |


# Validation of Correct Decryption of Spoiled Ballots

!!! important
	An election verifier should confirm the correct decryption of each spoiled ballot using the same process that was used to confirm the election tallies.

	An election verifier should also confirm that for each decrypted spoiled ballot, the selections listed in text match the corresponding text in the ballot coding file.


Validation of Correct Decryption of Spoiled Ballots is a repeat of verification steps 8 through 11 for each spoiled ballot instead of for the aggregate ballot that contains encrypted tallies


[^23]: Special thanks to Rainbow Huang (@rainbowhuanguw) for her help in producing this mapping.

[^24]: In general, if $n$ is prime, one can compute $a^b \bmod n$ as $(a \bmod n)^{(b \bmod (n-1)} )  \bmod n$.  But within this application, the efficiency benefits of performing a modular reduction on an exponent are limited, and the risk of confusion or error from doing so likely exceeds the benefit.  In the particular instance of this specification, if $a \in Z_p^r$, then one can compute $a^b  \bmod p$ as $a^{(b mod q)} \bmod p$.  This has greater efficiency benefits, but the risk of confusion or error still likely exceed the efficiency benefit.

[^25]: If alternative parameters are allowed, election verifiers must confirm that $p$, $q$, $r$, $g$, and $\bar{g} are such that both $p$ and $q$ are prime (this may be done probabilistically using the Miller-Rabin algorithm), that $p-1=qr$ is satisfied, that $q$ is not a divisor of $r$, and $1 \lt g \lt p$, that $g^q  \bmod p=1$, that $g \bar{g} \bmod p=1$, and that generation of the parameters is consistent with the cited standard.
