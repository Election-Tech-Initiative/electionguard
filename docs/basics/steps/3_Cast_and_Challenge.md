# Cast and Challenge

Each ballot that is completed by a voter must be either cast or challenged. A cast ballot is a ballot that the voter accepts as valid and wishes to include in the official election tally. A challenge ballot, also referred to as a spoiled ballot, is a ballot that the voter does not accept as valid and wishes to exclude from the official election tally.

![Encrypt][encrypt-image]

<!-- Links -->
[encrypt-image]: ../../images/undraw/voting.svg ""

ElectionGuard includes a mechanism to mark a specific ballot as either cast or spoiled. Cast ballots are included in the tally record, while spoiled ballots are not. Spoiled ballots are decrypted into plaintext and published along with the rest of the election record.
