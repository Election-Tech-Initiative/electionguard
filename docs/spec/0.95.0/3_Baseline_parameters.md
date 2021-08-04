# Baseline Election Parameters

*ElectionGuard* uses integer ElGamal rather than elliptic-curve ElGamal in order to make construction of election verifiers as simple as possible without requiring special tools and dependencies. The exponential ElGamal used to encrypt votes is defined by a 4096-bit prime $p$ and a 256-bit prime $q$ which divides $(p − 1)$. We use $r=\frac{p-1}{q}$ to denote the cofactor of $q$, and a generator $g$ of the order $q$ subgroup $Z_p^r$ is fixed.

Another parameter of an election should be a public ballot coding file. This file should list all the contests in an election, the number of selections allowed for each contest, and the options for each contest together with associations between each option and its representation on a virtual ballot. It is assumed that each contest in the ballot coding file has a unique label and that within each contest, each option also has a unique label. For instance, if Alice, Bob, and Carol are running for governor, and David and Ellen are running for senator, the ballot coding file could enable the vector $\langle0,1,0; 0,1\rangle$ to be recognized as a ballot with votes for Bob as governor and Ellen as senator. The detailed format of a ballot coding file will not be specified in this document. But the contents of this file are hashed together with the prime modulus $(p)$, subgroup order $(q)$, generator $(g)$, number of guardians $(n)$, decryption quorum threshold value $(k)$, date, and jurisdictional information to form a base hash code $(Q)$ which will be incorporated into every subsequent hash computation in the election.

Standard parameters for ElectionGuard begin with the largest 256-bit prime $q = 2^{256} − 189$. The hexadecimal representation of $q$ is as follows.

``` text
FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFF43
```

The modulus $p$ is then set to be a 4096-bit prime with the following properties:

* The first 256 bits of $p$ are all ones
* The last 256 bits of $p$ are all ones
* $p-1$ is a multiple of $q$
* $\frac{p-1}{2q}$ is also prime

The middle 3,584 bits of $p$ are chosen by starting with the first 3,584 bits of the Euler-Mascheroni constant $(\gamma)$, pre-pending and appending 256 ones, and finding the smallest prime larger than this number that satisfies the above properties.

This works out to $p=2^{4096}-2^{3840} - 1 + 2^{256}(\lfloor2^{3584}\gamma\rfloor + \delta)$ where the value of
$\delta = 495448529856135475846147600290107731951815687842437876083937612367400355133042233301$
[^12]
The hexadecimal representation of $p$ is as follows:

``` text
FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF 93C467E3 7DB0C7A4 D1BE3F81 0152CB56 A1CECC3A F65CC019 0C03DF34 709AFFBD 8E4B59FA 03A9F0EE D0649CCB 621057D1 1056AE91 32135A08 E43B4673 D74BAFEA 58DEB878 CC86D733 DBE7BF38 154B36CF 8A96D156 7899AAAE 0C09D4C8 B6B7B86F D2A1EA1D E62FF864 3EC7C271 82797722 5E6AC2F0 BD61C746 961542A3 CE3BEA5D B54FE70E 63E6D09F 8FC28658 E80567A4 7CFDE60E E741E5D8 5A7BD469 31CED822 03655949 64B83989 6FCAABCC C9B31959 C083F22A D3EE591C 32FAB2C7 448F2A05 7DB2DB49 EE52E018 2741E538 65F004CC 8E704B7C 5C40BF30 4C4D8C4F 13EDF604 7C555302 D2238D8C E11DF242 4F1B66C2 C5D238D0 744DB679 AF289048 7031F9C0 AEA1C4BB 6FE9554E E528FDF1 B05E5B25 6223B2F0 9215F371 9F9C7CCC 69DDF172 D0D62342 17FCC003 7F18B93E F5389130 B7A661E5 C26E5421 4068BBCA FEA32A67 818BD307 5AD1F5C7 E9CC3D17 37FB2817 1BAF84DB B6612B78 81C1A48E 439CD03A 92BF5222 5A2B38E6 542E9F72 2BCE15A3 81B5753E A8427633 81CCAE83 512B3051 1B32E5E8 D8036214 9AD030AA BA5F3A57 98BB22AA 7EC1B6D0 F17903F4 E234EA60 34AA8597 3F79A93F FB82A75C 47C03D43 D2F9CA02 D03199BA CEDDD453 34DBC6B5 FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF
```

The hexadecimal representation of the cofactor $r=p-1$ is as follows:

```text
00000000 00000000 00000000 00000000 00000000 00000000 00000000 000000BC 93C467E3 7DB0C7A4 D1BE3F81 0152CB56 A1CECC3A F65CC019 0C03DF34 709B8AF6 A64C0CED CF2D559D A9D97F09 5C3076C6 86037619 148D2C86 C317102A FA214803 1F04440A C0FF0C9A 417A8921 2512E760 7B2501DA A4D38A2C 1410C483 6149E2BD B8C8260E 627C4646 963EFFE9 E16E495D 48BD215C 6D8EC9D1 667657A2 A1C8506F 2113FFAD 19A6B2BC 7C457604 56719183 309F874B C9ACE570 FFDA877A A2B23A2D 6F291C15 54CA2EB1 2F12CD00 9B8B8734 A64AD51E B893BD89 1750B851 62241D90 8F0C9709 879758E7 E8233EAB 3BF2D6AB 53AFA32A A153AD66 82E5A064 8897C9BE 18A0D50B ECE030C3 432336AD 9163E33F 8E7DAF49 8F14BB28 52AFFA81 4841EB18 DD5F0E89 516D5577 76285C16 071D2111 94EE1C3F 34642036 AB886E3E C28882CE 4003DEA3 35B4D935 BAE4B582 35B9FB2B AB713C8F 705A1C7D E4222020 9D6BBCAC C4673186 01565272 E4A63E38 E2499754 AE493AC1 A8E83469 EEF35CA2 7C271BC7 92EEE211 56E617B9 22EA8F71 3C22CF28 2DC5D638 5BB12868 EB781278 FA0AB2A8 958FCCB5 FFE2E5C3 61FC1744 20122B01 63CA4A46 308C8C46 C91EA745 7C1AD0D6 9FD4A7F5 29FD4A7F 529FD4A7 F529FD4A 7F529FD4 A7F529FD 4A7F529F D4A7F52A
```

Finally, the generator $g$ is chosen to be $g=2r \bmod p$ and has the following hexadecimal representation

``` text
037DE384 F98F6E03 8D2A3141 825B33D5 D45EC4CC 64CFD15E 750D6798 F5196CF2 A142CDF3 3F6EF853 840EC7D4 EC804794 CFB0CFB6 5363B256 6387B98E E0E3DEF1 B706FA55 D5038FFB 4A62DCBB 93B1DDD8 D3B308DA 86D1C3A5 25EF356F E5BB5931 4E656334 80B396E1 DD4B795F 78DE07D8 6B0E2A05 BE6AF78F D7F736FC BA6C032E 26E050AF 50A03C65 FA7B6C87 F4554CB5 7F3DABCB AD8EB9D8 FDEBEEF5 8570669A CC3EDA17 DBFC47B8 B3C39AA0 8B829B28 872E62B5 D1B13A98 F09D40AC 20C2AB74 A6750E7C 8750B514 1E221C41 F55BBA31 D8E41422 B64D2CBA 7AAA0E9F D8785702 F6932825 BF45DE83 86D24900 742062C1 322B37C5 0AF18215 8090C35D A9355E6C F7F72DA3 9A2284FD FB1918B2 A2A30E69 501FA234 2B728263 DF23F1DB 8355BDE1 EB276FB3 685F3716 72CEB313 FDAB069C C9B11AB6 C59BCE62 BAAD96AA C96B0DBE 0C7E71FC B2255254 5A5D1CED EEE01E4B C0CDBDB7 6B6AD45F 09AF5E71 114A005F 93AD97B8 FE09274E 76C94B20 08926B38 CAEC94C9 5E96D628 F6BC8066 2BA06207 801328B2 C6A60526 BF7CD02D 9661385A C3B1CBDB 50F759D0 E9F61C11 A07BF421 8F299BCB 29005200 76EBD2D9 5A3DEE96 D4809EF3 4ABEB83F DBA8A12C 5CA82757 288A89C9 31CF564F 00E8A317 AE1E1D82 8E61369B A0DDBADB 10C136F8 691101AD 82DC5477 5AB83538 40D99921 97D80A6E 94B38AC4 17CDDF40 B0C73ABF 03E8E0AA
```

!!! info
    Alternative parameter sets are possible. A good source for parameter generation is appendix A of FIPS 186-4[^13] . However, allowing alternate parameters would force election verifiers to recognize and check that parameters are correctly generated. Since these checks would be very different from other checks that are required of a verifier, allowing alternate parameters would add substantial complexity to election verifiers. For this reason, this version of *ElectionGuard* fixes the parameters as above.

!!! important
    An *ElectionGuard* version 1 election verifier may assume that the baseline parameters match the parameters provided above. However, it is recommended that the above parameters be checked against the parameters of each election to accommodate the possibility of different parameters in future versions of *ElectionGuard*[^14].

[^12]: Discovering this value $\delta$ required a search through roughly 42 million values satisfying the first three of the above properties to find one for which both $p$ and $\frac{(p-1)}{2q}$ are both prime.

[^13]: NIST (2013) Digital Signature Standard (DSS). In: FIPS 186-4. [https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-4.pdf](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-4.pdf)

[^14]: If alternative parameters are allowed, election verifiers must confirm that $p$, $q,$ $r$, and $g$ are such that both $p$ and $q$ are prime (this may be done probabilistically using the Miller-Rabin algorithm), that $p-1=qr$ is satisfied, that $q$ is not a divisor of $r$, that $1 \lt g \lt p$, that $g^q  \bmod p=1$, and that generation of the parameters is consistent with the cited standard.
