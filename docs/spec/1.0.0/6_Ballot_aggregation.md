# Ballot Aggregation

At the conclusion of voting, all of the ballot encryptions are published in the election record together with the proofs that the ballots are well-formed.  Additionally, all of the encryptions of each option are homomorphically combined to form an encryption of the total number of times that option was selected.  The encryptions $(\alpha_i,\beta_i )$ of each individual option are combined by forming the product 

$$
(A,B)=\left(\prod_i \alpha_i\bmod p, \prod_i \beta_i  \bmod p\right)
$$

This aggregate encryption $(A,B)$, which represents an encryption of the tally of that option, is published in the election record for each option.

!!! important
    An election verifier must confirm for each (non-placeholder) option in each contest in the ballot coding file that the aggregate encryption (A,B) satisfies $A=\prod_j \alpha_j$ and $B=\prod_j \beta_j$ where the $(\alpha_j,\beta_j)$ are the corresponding encryptions on all cast ballots in the election record.


