# Hashing

A hash function is used to generate the new value according to a mathematical algorithm. The result of a hash function is known as a hash value or simply, a hash. ElectionGuard uses hashing in its cryptographic context, This is done for a variety of reasons, including preventing discovery of election ballot contents, but also to verify certain information. For example, a hash of the manifest is added to the ballot which can verify the ballot is using the correct manifest.

## Hashing Function

The hashing function takes zero or more elements and calculates their cryptographic hash using SHA256 allowed element types are the integers, strings, lists, and specialty classes. The function takes all the elements and hashes them to form an integer that is `mod q - 1` or modulus of the small prime minus one.

The hash should be encoded using `utf-8`. When the bytes converted to an integer, it should use `big` byte order where the most significant byte is at the beginning of the byte array. A separator `|` is used between each of the properties of an object. 


!!! Note
    Whenever **[sequence order]** is present, items should be hashed in [sequence order]. 

- **Strings**: Same string representation
- **Integers**: String representation of integer
- **Large Integers:** String representation of integer as hex
- **Lists:** Lists recursively call the hashing function and then are treated as a large integer
- **Classes:** See [Classes](#classes) below

------------------------------------------------------

## Classes

The hashing function is used for manifests and ballots and their internal classes to generate a unique hash that can be used for verification. 

### Manifest

_Elements are hashed in the following order:_

1. Election Scope Id
2. Name of Election Type
3. Start Date and Time as ISO
4. End Date and Time as ISO
5. Name
6. Contact Information
7. Geopolitical Units
8. Parties
9. Contests
10. Ballot Styles

The following are classes that are hashed related to the manifest. Some of these are reused within the ballots.

#### Annotated String

_Elements are hashed in the following order:_

1. Annotation
2. Value

#### Language

_Elements are hashed in the following order:_

1. Value
2. Language

#### Internationalized Text

_Elements are hashed in the following order:_

1. Text

#### Contact Information

_Elements are hashed in the following order:_

1. Name
2. Address Line
3. Email
4. Phone

### Geopolitical Unit

_Elements are hashed in the following order:_

1. Object Id
2. Name
3. Name of Reporting Unit Type
3. Contact Information

#### Ballot Style

_Elements are hashed in the following order:_

1. Object Id
2. Geopolitical Unit Ids
3. Party Ids
4. Image URI

#### Party

_Elements are hashed in the following order:_

1. Object Id
2. Name
3. Abbreviation
4. Color
5. Logo URI

#### Candidate

_Elements are hashed in the following order:_

1. Object Id
2. Name
3. Party Id
4. Image URI

#### Selection Description

_Elements are hashed in the following order:_

1. Object Id
2. Sequence Order
3. Candidate Id

#### Contest Description

_Elements are hashed in the following order:_

1. Object id
2. Sequence Order
3. Electoral District Id
4. Name of Vote Variation
5. Ballot Title
6. Ballot Subtitle
7. Name
8. Number Elected
9. Votes Allowed
10. Ballot Selections

### Ballot

The following are classes that are hashed related to the ballot. 

#### Ciphertext Ballot

_For a **nonce seed**, elements are hashed in the following order:_

1. Manifest Hash
2. Object Id
3. Nonce

_For a **cryptography hash**, elements are hashed in the following order:_

1. Object Id
2. Encryption Seed (ie: Manifest Hash)
3. Hash of Contests in sequence order

#### Ciphertext Contest

_Elements are hashed in the following order:_

1. Object Id
2. Encryption Seed (ie: Manifest Hash)
3. Hash of Selections in sequence order

#### Ciphertext Selection

_Elements are hashed in the following order:_

1. Object Id
2. Encryption Seed (ie: Manifest Hash)
3. Hash of ElGamal Ciphertext


### ElGamal Ciphertext

_Elements are hashed in the following order:_

1. Pad
2. Data

------------------------------------------------------

## Codes

The hashing function is used for devices and ballots to create unique codes for identification.  

### Encryption Device

_Elements are hashed in the following order:_

1. Device Id
2. Session Id
3. Launch Code
4. Location

### Ballot

_Elements are hashed in the following order:_

1. Previous Code
2. Timestamp
3. Ballot Hash

------------------------------------------------------

## Commitments

Hashes of commitments are used often during the verification process. These still use the same function. 

### Encryption Key

For the ballot [encryption key], each coefficient commitment for each guardian's public key from their[ election key pair] should be hashed in [sequence order]. 

_Example of elements in hashing order:_

1. Guardian A (Sequence Order: 1) - Coefficient 1 Commitment
2. Guardian A (Sequence Order: 1) - Coefficient 2 Commitment
3. Guardian B (Sequence Order: 2) - Coefficient 1 Commitment
4. Guardian B (Sequence Order: 2) - Coefficient 2 Commitment

[sequence order]: ../overview/Glossary/#sequence-order
[encryption key]: ../overview/Glossary/#encryption-key
[election key pair]: ../overview/Glossary/#election-key-pair