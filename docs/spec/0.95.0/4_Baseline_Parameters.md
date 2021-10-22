# Baseline Parameters
_ElectionGuard_ uses integer ElGamal rather than elliptic-curve ElGamal in order to make construction of election verifiers as simple as possible without requiring special tools and dependencies. The exponential ElGamal used to encrypt votes is defined by a 4096-bit prime $p$ and a 256-bit prime $q$ which divides $(p − 1)$. We use $r = \frac{p-1}{q}$ to denote cofactor of $q$, and a generator $g$ of the order $q$ subgroup $\mathbb{Z}^{r}_{p}$ is fixed.

Another parameter of an election should be a public ballot coding file. This file should list all the contests in an election, the number of selections allowed for each contest, and the options for each contest together with associations between each option and its representation on a virtual ballot. It is assumed that each contest in the ballot coding file has a unique label and that within each contest, each option also has a unique label. For instance, if Alice, Bob, and Carol are running for governor, and David and Ellen are running for senator, the ballot coding file could enable the vector$〈0,1,0; 0,1〉$ to be recognized as a ballot with votes for Bob as governor and Ellen as senator. The detailed format of a ballot coding file will not be specified in this document. But the contents of this file are hashed together with the prime modulus $(p)$, subgroup order $(q)$, generator $(g)$, number of guardians $(n)$, decryption quorum threshold value $(k)$, date, and jurisdictional information to form a base hash code $(Q)$ which will be incorporated into every subsequent hash computation in the election.

Standard parameters for ElectionGuard begin with the largest 256-bit prime $q = 2^{256} − 189$. The hexadecimal representation of q is as follows.

```
FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFF43
```
The modulus $p$ is then set to be a 4096-bit prime with the following properties.

- The first 256 bits of $p$ are all ones.
- The last 256 bits of $p$ are all ones.
- $p − 1$ is a multiple of $q$.
- $\frac{p−1}{2q}$ is also prime.

The middle 3584 bits of $p$ are chosen by starting with the first 3584 bits of the Euler–Mascheroni constant ($\gamma$), pre-pending and appending 256 ones, and finding the smallest prime larger than this value that satisfies the above properties.

This works out to $p = 2^{4096} − 2^{3840} − 1 + 2^{256}(⌊2^{3584}\gamma⌋ + \delta)$ where the value of $\delta$ is given by

$$
\delta = 495448529856135475846147600290107731951815687842437876083937612367400355133042233301 .^{12}
$$

The hexadecimal representation of q is as follows.
```
FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF
93C467E3 7DB0C7A4 D1BE3F81 0152CB56 A1CECC3A F65CC019 0C03DF34 709AFFBD
8E4B59FA 03A9F0EE D0649CCB 621057D1 1056AE91 32135A08 E43B4673 D74BAFEA
58DEB878 CC86D733 DBE7BF38 154B36CF 8A96D156 7899AAAE 0C09D4C8 B6B7B86F
D2A1EA1D E62FF864 3EC7C271 82797722 5E6AC2F0 BD61C746 961542A3 CE3BEA5D
B54FE70E 63E6D09F 8FC28658 E80567A4 7CFDE60E E741E5D8 5A7BD469 31CED822
03655949 64B83989 6FCAABCC C9B31959 C083F22A D3EE591C 32FAB2C7 448F2A05
7DB2DB49 EE52E018 2741E538 65F004CC 8E704B7C 5C40BF30 4C4D8C4F 13EDF604
7C555302 D2238D8C E11DF242 4F1B66C2 C5D238D0 744DB679 AF289048 7031F9C0
AEA1C4BB 6FE9554E E528FDF1 B05E5B25 6223B2F0 9215F371 9F9C7CCC 69DDF172
D0D62342 17FCC003 7F18B93E F5389130 B7A661E5 C26E5421 4068BBCA FEA32A67
818BD307 5AD1F5C7 E9CC3D17 37FB2817 1BAF84DB B6612B78 81C1A48E 439CD03A
92BF5222 5A2B38E6 542E9F72 2BCE15A3 81B5753E A8427633 81CCAE83 512B3051
1B32E5E8 D8036214 9AD030AA BA5F3A57 98BB22AA 7EC1B6D0 F17903F4 E234EA60
34AA8597 3F79A93F FB82A75C 47C03D43 D2F9CA02 D03199BA CEDDD453 34DBC6B5
FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF
```

The hexadecimal representation of the cofactor $r = \frac{p−1}{q}$ is as follows.
```
1 00000000 00000000 00000000 00000000 00000000 00000000 00000000 000000BC
93C467E3 7DB0C7A4 D1BE3F81 0152CB56 A1CECC3A F65CC019 0C03DF34 709B8AF6
A64C0CED CF2D559D A9D97F09 5C3076C6 86037619 148D2C86 C317102A FA214803
1F04440A C0FF0C9A 417A8921 2512E760 7B2501DA A4D38A2C 1410C483 6149E2BD
B8C8260E 627C4646 963EFFE9 E16E495D 48BD215C 6D8EC9D1 667657A2 A1C8506F
2113FFAD 19A6B2BC 7C457604 56719183 309F874B C9ACE570 FFDA877A A2B23A2D
6F291C15 54CA2EB1 2F12CD00 9B8B8734 A64AD51E B893BD89 1750B851 62241D90
8F0C9709 879758E7 E8233EAB 3BF2D6AB 53AFA32A A153AD66 82E5A064 8897C9BE
18A0D50B ECE030C3 432336AD 9163E33F 8E7DAF49 8F14BB28 52AFFA81 4841EB18
DD5F0E89 516D5577 76285C16 071D2111 94EE1C3F 34642036 AB886E3E C28882CE
4003DEA3 35B4D935 BAE4B582 35B9FB2B AB713C8F 705A1C7D E4222020 9D6BBCAC
C4673186 01565272 E4A63E38 E2499754 AE493AC1 A8E83469 EEF35CA2 7C271BC7
92EEE211 56E617B9 22EA8F71 3C22CF28 2DC5D638 5BB12868 EB781278 FA0AB2A8
958FCCB5 FFE2E5C3 61FC1744 20122B01 63CA4A46 308C8C46 C91EA745 7C1AD0D6
9FD4A7F5 29FD4A7F 529FD4A7 F529FD4A 7F529FD4 A7F529FD 4A7F529F D4A7F52A
```

Finally, the generator $g$ is chosen to be $g = 2^r\bmod p$ and has the following hexadecimal representation.
```
037DE384 F98F6E03 8D2A3141 825B33D5 D45EC4CC 64CFD15E 750D6798 F5196CF2
A142CDF3 3F6EF853 840EC7D4 EC804794 CFB0CFB6 5363B256 6387B98E E0E3DEF1
B706FA55 D5038FFB 4A62DCBB 93B1DDD8 D3B308DA 86D1C3A5 25EF356F E5BB5931
4E656334 80B396E1 DD4B795F 78DE07D8 6B0E2A05 BE6AF78F D7F736FC BA6C032E
26E050AF 50A03C65 FA7B6C87 F4554CB5 7F3DABCB AD8EB9D8 FDEBEEF5 8570669A
CC3EDA17 DBFC47B8 B3C39AA0 8B829B28 872E62B5 D1B13A98 F09D40AC 20C2AB74
A6750E7C 8750B514 1E221C41 F55BBA31 D8E41422 B64D2CBA 7AAA0E9F D8785702
F6932825 BF45DE83 86D24900 742062C1 322B37C5 0AF18215 8090C35D A9355E6C
F7F72DA3 9A2284FD FB1918B2 A2A30E69 501FA234 2B728263 DF23F1DB 8355BDE1
EB276FB3 685F3716 72CEB313 FDAB069C C9B11AB6 C59BCE62 BAAD96AA C96B0DBE
0C7E71FC B2255254 5A5D1CED EEE01E4B C0CDBDB7 6B6AD45F 09AF5E71 114A005F
93AD97B8 FE09274E 76C94B20 08926B38 CAEC94C9 5E96D628 F6BC8066 2BA06207
801328B2 C6A60526 BF7CD02D 9661385A C3B1CBDB 50F759D0 E9F61C11 A07BF421
8F299BCB 29005200 76EBD2D9 5A3DEE96 D4809EF3 4ABEB83F DBA8A12C 5CA82757
288A89C9 31CF564F 00E8A317 AE1E1D82 8E61369B A0DDBADB 10C136F8 691101AD
82DC5477 5AB83538 40D99921 97D80A6E 94B38AC4 17CDDF40 B0C73ABF 03E8E0AA
```

> Alternative parameter sets are possible. A good source for parameter generation is appendix A of FIPS $186-4^{13}$ . However, allowing alternate parameters would force election verifiers to recognize and check that parameters are correctly generated. Since these checks would be very different from other checks that are required of a verifier, allowing alternate parameters would add substantial complexity to election verifiers. For this reason, this version of ElectionGuard fixes the parameters as above.  

> An ElectionGuard version 1 election verifier may assume that the baseline parameters match the parameters provided above. However, it is recommended that the above parameters be checked against the parameters of each election to accommodate the possibility of different parameters in future versions of ElectionGuard.

## Key Generation
Before an election, the number of guardians ($n$) is fixed together with a quorum value ($k$) that describes the number of guardians necessary to decrypt tallies and produce election verification data. The values $n$ and $k$ are integers subject to the constraint that $1 ≤ k ≤ n$. Canvassing board members can often serve the role of election guardians, and typical values for $n$ and $k$ could be 5 and 3 – indicating that 3 of 5 canvassing board members must cooperate to produce the artifacts that enable election verification. The reason for not setting the quorum value $k$ too low is that it will also be possible for $k$ guardians to decrypt individual ballots.  

> Note that decryption of individual ballots does not directly compromise voter privacy since links between encrypted ballots and the voters who cast them are not retained by the system. However, voters receive verification codes that can be associated with individual encrypted ballots, so any group that has the ability to decrypt individual ballots can also coerce voters by demanding to see their tracking codes.  

Threshold ElGamal encryption is used for encryption of ballots. This form of encryption makes it very easy to combine individual guardian public keys into a single public key for encrypting votes and ballots. It also offers a homomorphic property that allows individual encrypted votes to be combined to form encrypted tallies.  

The guardians of an election will each generate a public-private key pair. The public keys will then be combined (as described in the following section) into a single election public key which is used to encrypt all selections made by voters in the election.  

Ideally, at the conclusion of the election, each guardian will use its private key to form a verifiable partial decryption of each tally. These partial decryptions will then be combined to form full verifiable decryptions of the election tallies.  

To accommodate the possibility that one or more of the guardians will not be available at the conclusion of the election to form their partial decryptions, the guardians will cryptographically share 15 their private keys amongst each other during key generation in a manner to be detailed in the next section. A pre-determined threshold value ($k$) out of the ($n$) guardians will be necessary to produce a full decryption.  

Additionally, each guardian will also generate an auxiliary public-private key pair. These auxiliary keys will be used by the guardians to exchange fragments of their principal vote-encryption keys and for other scenarios in which non-vote data may need to be encrypted.  

### Overview of key generation
The $n$ guardians of an election are denoted by $T_1 , T_2 , ... , T_n$ . Each guardian $T_i$ generates an independent ElGamal public-private key pair by generating a random integer secret $s_i \in \mathbb{Z}_q$ and forming the public key $K_i = g^{s_i}\bmod p$. Each of these public keys will be published in the election record together with a non-interactive zero-knowledge Schnorr proof of knowledge of possession of the associated private key.  

The joint election public key will be

$$
K = \prod_{i=1}^{n} K_i\bmod p
$$

To enable robustness and allow for the possibility of missing guardians at the conclusion of an election, the ElectionGuard key generation includes a sharing of private keys between guardians to enable decryption by any $k$ guardians. This sharing is verifiable, so that receiving guardians can confirm that the shares they receive are meaningful; and the process allows for decryption without explicitly reconstructing private keys of missing guardians.  

Each guardian $T_i$ generates $k − 1$ random polynomial coefficients $a_{i,j}$ such that $0 < j < k$ and $0 ≤ a i,j < q$ and forms the polynomial

$$
P_i(x) = \sum_{j=0}^{k-1} a_{i,j}x^j\bmod q
$$

by setting $a_{i,0}$ equal to its secret value $s_i$ . Guardian $T_i$ then publishes commitments $K_{i,j} = g^{a_{i,j}}\bmod p$ to each of its random polynomial coefficients. As with the primary secret keys, each guardian should provide a Schnorr proof of knowledge of the secret coefficient value $a_{ij}$, associated with each published commitment $K_{i,j}$ . Since polynomial coefficients will be generated and managed in precisely the same fashion as secret keys, they will be treated together in a single step below.  

At the conclusion of the election, individual encrypted ballots will be homomorphically combined into a single encrypted aggregate ballot – consisting of an encryption of the tally for each option offered to voters. Each guardian will use its secret key to generate a partial decryption of each encrypted tally value, and these partial decryptions will be combined into full decryptions. If any election guardians are missing during tallying, any set of $k$ guardians who are available can cooperate to reconstruct the missing partial decryption.  

All spoiled ballots are individually decrypted in precisely the same fashion.

### Details of key generation
Each guardian $T_i$ in an election with a decryption threshold of $k$ generates $k$ secret polynomial coefficients $a_{i,j}$ such that $0 ≤ j < k$ and $0 ≤ a_{i,j} < q$ and forms the polynomial

$$
P_i(x) = \sum_{j=0}^{k-1} a_{i, j} x^j \bmod q.
$$

Guardian $T_i$ then publishes commitments $K_{i,j} = g^{a_{i,j}} \bmod p$ for each of its random polynomial coefficients. The constant term $a_{i,0}$ of this polynomial will serve as the private key for guardian $T_i$ , and for convenience we denote $s_i = a_{i,0}$ , and its commitment $K_{i,0}$ will serve as the public key for guardian $T_i$ and will also be denoted as $K_i = K_{i,0}$ .  

In order to prove possession of the coefficient associated with each public commitment, for each $K_{i,j}$ with $0 ≤ j < k$, guardian $T_i$ generates a Schnorr proof of knowledge for each of its coefficients as follows.  

This Non-Interactive Zero-Knowledge (NIZK) proof proceeds as follows.  

__NIZK Proof by Guardian $T_i$ of its knowledge of secrets $a_{i,j}$ such that $K_{i,j} = g^{a_{i,j}} \bmod p$__

For each $0 ≤ j < k$, Guardian $T_i$ generates random integer values $R_{i,j}$ in $\mathbb{Z}_q$ and computes $h_{i,j} = g^{R_{i,j}} \bmod p$. Then, using the hash function SHA-256 (as defined in NIST PUB FIPS 180- $4^16$ ), guardian $T_i$ then performs a single hash computation $c_{i,j} = H(Q, K_{i,j} , h_{i,j} ) \bmod q$ and publishes the values $K_{i,j} , h_{i,j} , c_{i,j}$ , and $u_{i,j} = \(R_{i,j} + c_{i,j} a_{i,j} ) \bmod q.

> An election verifier must confirm the following for each guardian $T_i$ and for each $j \in \mathbb{Z}_k$ :  

> 1. The challenge $c_{i,j}$ is correctly computed as $c_{i,j} = H(Q, K_{i,j} , h_{i,j} ) \bmod q$.
> 2. The equation $g^{u_{i,j}} \bmod p = h_{i,j} K_{i,j}^{c_{i,j}} \bmod p$ is satisfied.

It is worth noting here that for any fixed constant $\alpha$, the value $g^{P_i (\alpha)} \bmod p$ can be computed entirely from the published commitments as

$$
g^{P_i(\alpha)} = g^{\sum_{j=0}^{k-1}a_{i,j}\alpha^{j}}\bmod p = \prod_{j=0}^{k-1}g^{a_{i,j}\alpha^{j}}\bmod p = \prod_{j=0}^{k-1}(g^{a_{i,j}})^{\alpha^j}\bmod p = \prod_{j=0}^{k-1}K_{i, j}^{\alpha^j}\bmod p.
$$

> Although this formula includes double exponentiation – raising a given value to the power $\alpha^j$ – in what follows, $\alpha$ and $j$ will always be small values (bounded by $n$). This can also be reduced if desired since the same result will be achieved if the exponents $\alpha^j$ are reduced to $\alpha^j \bmod q$.  

To share secret values amongst each other, it is assumed that each guardian $T_i$ has previously shared an auxiliary public encryption function $E_i$ with the group. Each guardian $T_i$ then publishes the encryption $E_{\ell} (R_{i,\ell} , P_i (\ell))$ for every other guardian $T_{\ell}$ – where $R_{i,\ell}$ is a random nonce.  

Guardian $T_\ell$ can now decrypt each $P_i(\ell)$ encrypted to its public key and verify its validity against the commitments made by $T_i$ to its coefficients $K_{i,0} , K_{i,1} , ... , K_{i,k−1}$ by confirming that the following equation holds:

$$
g^{P_i\ell} \bmod p = \prod_{j=0}^{k-1}(K_{i,j})^{\ell^j} \bmod p.
$$

Guardians then publicly report having confirmed or failed to confirm this computation. If the recipient guardian $T_\ell$ reports not receiving a suitable value $P_i (\ell)$, it becomes incumbent on the sending guardian $T_i$ to publish this $P_i (\ell)$ together with the nonce $R_{i,\ell}$ it used to encrypt $P_i (\ell)$ under the public key $E_\ell$ of recipient guardian $T_l$ . If guardian $T_i$ fails to produce a suitable $P_i (\ell)$ and nonce $R_{i,l}$ that match both the published encryption and the above equation, it should be excluded from the election and the key generation process should be restarted with an alternate guardian. If, however, the published $P_i (\ell)$ and $R_{i,\ell}$ satisfy both the published encryption and the equation above, the claim of malfeasance is dismissed and the key generation process continues undeterred.  

Once the baseline parameters have been produced and confirmed, all of the public commitments $K_{i,j}$ are hashed together with the base hash $Q$ to form an extended base hash $\overline{Q}$ that will form the basis of subsequent hash computations. The hash function SHA-256 will be used here and for all hash computations for the remainder of this document.  

> An election verifier must verify the correct computation of the joint election public key and extended base hash.

>1. $\overline{Q} = H(Q, K_{1,0} , K_{1,1} , K_{1,2} , ... , K_{1,k−1} , K_{2,0} , K_{2,1} , K_{2,2} , ... , K_{2,k−1} , ... , K_{n,0} , K_{n,1} , K_{n,2} , ... , K_{n,k−1} )$
>2. $K = \prod_{i=i}^n K_i \bmod p$.

