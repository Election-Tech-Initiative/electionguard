# Versioning

Versioning for ElectionGuard as the Software Development Kit (SDK) may seem complex, particularly between the Specification, the code repositories, and the serialized files in the sample data. To attempt to reduce the complexity, the versioning for ElectionGuard will be as the whole SDK including the serialization, instead of individual components. This is to help the users of ElectionGuard identify the pieces and parts that function together. As an example, a verifier will need to support the same version(s) of ElectionGuard as the election system it is verifying.

## How It Works

- **SDK** version will line up with a specification post 1.0. This is to allow contributors to develop following the ElectionGuard Specification of the SDK and utilize the badge system to indicate what their code supports.

- **Major** versions will indicate this top level version consistently across the repositories starting in 1.0. The goal is to keep the Election Record and other serialized files consistent outside of major versions changes. 

- **Minor** and smaller versions can differ to allow freedom within the code repositories. For example, the latest version python core could be v2.1.1 while the c++ core is at v2.48.0. 

## Current

### ElectionGuard 1.0

| Part           | Link          |    Release  |
|:---------------|:--------------| ------------|
| Specification  |[PDF][specs]   |    1.0      |
| Sample Data    | _Unreleased_  |    1.0      |
| Python Core    | _Unreleased_  |    1.4      |
| C++ Core       | _Unreleased_  |    1.0      |
| Python API     | _Unreleased_  |    1.1      |
| React UI       | _Unreleased_  |    1.0      |

## Future

### ElectionGuard 2.0

| Part           | Link          |    Release  |
|:---------------|:--------------| ------------|
| Specification  | _Unreleased_  |    2.0      |
| Sample Data    | _Unreleased_  |    2.0      |
| Python Core    | _Unreleased_  |    2.0      |
| C++ Core       | _Unreleased_  |    2.0      |
| Python API     | _Unreleased_  |    2.0      |
| React UI       | _Unreleased_  |    2.0      |


## Previous

### ElectionGuard 0.95

| Part           | Link          |    Release  |
|:---------------|:--------------| ------------|
| Specification  |[PDF][specs]   |    0.95     |
| Sample Data    |[Source][95-1] |    0.95     |
| Python Core    |[Source][95-2] |    1.2.2    |
| C++ Core       |[Source][95-3] |    0.1.6    |


### ElectionGuard 0.85

| Part          | Link          |    Release  |
|:--------------|:--------------| ------------|
| Specification |[PDF][specs]   |    0.85     |
| C Core        |  _Deprecated_ |    1.0      |
| C# Core       |  _Deprecated_ |    1.0      |


<!--Links--->
[specs]: ../spec/index.md
[95-1]: https://github.com/microsoft/electionguard-python/tree/1.2.2/data
[95-2]: https://github.com/microsoft/electionguard-python/tree/1.2.2
[95-3]: https://github.com/microsoft/electionguard-cpp/tree/0.1.6