### Election Record

The Election Record are the files required at the end of the election to verify the election and are intended to be posted publicly. There should not be any sensitive data (eg: no guardian private keys) in the record. These include the following:

- Manifest
- Election Context
- Election Constants
- Encrypted Tally
- Decrypted Tally
- Guardian Records
- Lagrange Coefficients Record
- Encryption Device Information
- Encrypted Ballots
- Decrypted Spoiled Ballots

## Folder Structure

The Election Record should be expected to be a zip folder containing the following information. 

```
📂 record
--- 📄 manifest.json
--- 📄 context.json
--- 📄 constants.json
--- 📄 encrypted_tally.json
--- 📄 tally.json
--- 📁 guardians
------- 📄 guardian_id_1.json
------- 📄 guardian_id_2.json
------- 📄 lagrange_coefficients.json
------- ...
--- 📁 encryption_devices
------- 📄 device_id_1.json
------- 📄 device_id_2.json
------- ...
--- 📁 encrypted_ballots
------- 📄 encrypted_ballot_id_1.json
------- 📄 encrypted_ballot_id_2.json
------- ...
--- 📁 decrypted_ballots
------- 📄 decrypted_ballot_id_3.json
------- 📄 decrypted_ballot_id_4.json
------- ...
```