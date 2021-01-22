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

!!! important ""
	(A) The challenge $c_{i,j}$ is correctly computed as 

$$
c_{i,j}=H(Q,K_{i,j},h_{i,j} )  \bmod q
$$

!!! important ""
	(B) The equation 

$$
g^{u_{i,j} }  \bmod p=h_{i,j} K_{i,j}^{c_{i,j} }  \bmod p 
$$

!!! important ""
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

!!! important ""
    (A) Joint election public key

$$
K=\prod_{i=1}^n K_i  \bmod p
$$

!!! important ""
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

!!! important ""
    (I)The given values $\alpha$, $\beta$, $a_0$, $b_0$, $a_1$, and $b_1$ are all in the set $Z_p^r$.  (A value $x$ is in $Z_p^r$ if and only if $x$ is an integer such that $0 \le x \lt p$ and $x^q  \bmod p=1$ is satisfied.)

!!! important ""
	(J) The challenge $c$ is correctly computed as 

$$
c=H(\bar{Q},(\alpha,\beta),(a_0,b_0 ),(a_1,b_1 ))
$$

!!! important ""
	(K) The given values $c_0$, $c_1$, $v_0$, and $v_1$ are each in the set $Z_q$.  (A value $x$ is in $Z_q$ if and only if $x$ is an integer such that 0 \le x \lt q.)

!!! important ""
	(L) The equation 
    
$$
c=(c_0+c_1 )  \bmod q
$$

!!! important ""
    is satisfied.

!!! important ""
    (M) The equation 

$$
g^{v_0}  \bmod p= a_0 \alpha^{c_0}  \bmod p
$$

!!! important ""
    is satisfied.

!!! important ""
	(N) The equation 

$$
g^{v_1}  \bmod p=a_1 \alpha^{c_1}  \bmod p
$$

!!! important ""
    is satisfied.

!!! important ""
	(O) The equation 

$$
K^{v_0}  \bmod p=b_0 \beta^{c_0}  \bmod p
$$

!!! important ""
    is satisfied.

!!! important ""
	(P) The equation 

$$
g^{c_1} K^{v_1}  \bmod p=b_1 \beta^{c_1}  \bmod p
$$

!!! important ""
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

!!! important ""
	(H) The number of placeholder positions matches the contest’s selection limit $L$.

!!! important ""
	(I) The contest total $(A,B)$ satisfies $A=\prod_i \alpha_i  \bmod p$ and $B=\prod_i \beta_i  \bmod p$ where the $(\alpha_i,\beta_i ) represent all possible selections (including placeholder selections) for the contest.

!!! important ""
	(J) The given value $V$ is in $Z_q$.

!!! important ""
	(K) The given values a and b are each in $Z_p^r$.

!!! important ""
	(L) The challenge value $C$ is correctly computed as $C=H(\bar{Q},(A,B),(a,b))$.

!!! important ""
	(M) The equation $g^V  \bmod p=(aA^C )  \bmod p$ is satisfied.

!!! important ""
	(N) The equation $((g^{LC} K)^V )  \bmod p=(bB^C )  \bmod p$ is satisfied.

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

!!! important ""
	(D) The equation $H_0=H(\bar{Q})$ is satisfied.

!!! important ""
	(E) For each ballot $B_i, H_i=H(H_{i-1},D,T,B_i)$ is satisfied.

!!! important ""
	(F) The closing hash $\bar{H} =H(H_l,\text{“CLOSE"}$ is correctly computed from the final tracking code H_l.

| Variable | Meaning | Folder | File | Level |
| -------  | ------- | ------ | ---- | ----- |
| $H_i$  | running hash of ballots produced | encrypted_ballots | every file in this folder | tracking_hash (also previous_tracking_hash) |

## Correctness of Ballot Aggregation

!!! important
    An election verifier must confirm for each (non-placeholder) option in each contest in the ballot coding file that the aggregate encryption $(A,B)$ satisfies $A=∏_j▒α_j  and B=∏_j▒β_j$ where the $(\alpha_j,\beta_j )$ are the corresponding encryptions on all cast ballots in the election record.

| Variable | Meaning | Folder | File | Level |
| -------  | ------- | ------ | ---- | ----- |
| $(\alpha_j,\beta_j)$ | encryption of vote | encrypted_ballots | every file in this folder	 | contests $\rightarrow$ [Item] $\rightarrow$ ballot_selections $\rightarrow$ [Item] $\rightarrow$ ciphertext $\rightarrow$ pad, data |
| $(A,B)$ | encrypted aggregate total of votes in contest | root | tally.json | [prefix] $\rightarrow$ message $\rightarrow$ pad, data |

## Correctness of Partial Decryptions

!!! important
    An election verifier must then confirm for each (non-placeholder) option in each contest in the ballot coding file the following for each decrypting trustee $T_i$.

!!! important ""
	The given value $v_i$ is in the set $Z_q$.

!!! important ""
	The given values $a_i$ and $b_i$ are both in the set $Z_q^r$.

!!! important ""
	The challenge value $c_i$ satisfies $c_i=H(\bar{Q},(A,B),(a_i,b_i ),M_i )$.

!!! important "" 
	The equation 

$$
g^{v_i}  \bmod p=(a_i K_i^{c_i} )  \bmod p
$$

!!! important "" 
    is satisfied.

!!! important "" 
    The equation $A^{v_i}  \bmod p=(b_i M_i^{c_i} )  \bmod p$ is satisfied.


[^23]: Special thanks to Rainbow Huang (@rainbowhuanguw) for her help in producing this mapping.

[^24]: In general, if $n$ is prime, one can compute $a^b \bmod n$ as $(a \bmod n)^{(b \bmod (n-1)} )  \bmod n$.  But within this application, the efficiency benefits of performing a modular reduction on an exponent are limited, and the risk of confusion or error from doing so likely exceeds the benefit.  In the particular instance of this specification, if $a \in Z_p^r$, then one can compute $a^b  \bmod p$ as $a^{(b mod q)} \bmod p$.  This has greater efficiency benefits, but the risk of confusion or error still likely exceed the efficiency benefit.

[^25]: If alternative parameters are allowed, election verifiers must confirm that $p$, $q$, $r$, $g$, and $\bar{g} are such that both $p$ and $q$ are prime (this may be done probabilistically using the Miller-Rabin algorithm), that $p-1=qr$ is satisfied, that $q$ is not a divisor of $r$, and $1 \lt g \lt p$, that $g^q  \bmod p=1$, that $g \bar{g} \bmod p=1$, and that generation of the parameters is consistent with the cited standard.
