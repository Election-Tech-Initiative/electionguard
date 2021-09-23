# Encryption

The primary function of ElectionGuard is to encrypt ballots. Ballots are encrypted on a uniquely identified device within the context of a specific election. The election public key is used to encrypt ballots. A master nonce value is generated for each ballot and the nonce is used to derive other nonce values for encrypting the selection on each ballot.

![Encrypt](../../images/undraw/encrypt.svg)
