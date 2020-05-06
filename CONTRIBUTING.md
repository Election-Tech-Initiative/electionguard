# Contributing

* [Getting Started](#getting-started)
* [Pull Requests](#pull-requests)
* [Contributor License Agreement](#contributor-license-agreement)
* [Code of Conduct](#code-of-conduct)
* [Developer's Certificate of Origin 1.1](#developers-certificate-of-origin-11)


## Getting Started

### C-Implementation Submodule
For each platform, the C-Implementation in the submodule must be built first.
The instructions vary per platform.

1. Initialize the submodule
2. Navigate to `libs\ElectionGuard-SDK-C-Implementation`
3. Follow platform specific instructions

#### Linux

1. Install cmake and gmp (`sudo apt-get install cmake libgmp3-dev`)
2. `cmake -S . -B build -DBUILD_SHARED_LIBS=ON`
3. `cmake --build build`
4. `libelectionguard.so` should be created

#### MacOS (.dylib)

1. Install cmake and gmp (`brew install cmake gmp`)
2. `cmake -S . -B build -DBUILD_SHARED_LIBS=ON`
3. `cmake --build build`
4. `libelectionguard.dylib` is created

#### Windows (.dll)

1. Install cmake and gmp ([Use Step 1 from Windows Instructions for C-Implementation](https://github.com/microsoft/ElectionGuard-SDK-C-Implementation/blob/master/README-windows.md))
2. `cmake -S . -B build -G "MSYS Makefiles" -DBUILD_SHARED_LIBS=ON`
3. `cmake --build build`
4. `electionguard.dll` is created

### C# Library Solution
_Note: This build will copy the library created by the submodule build._

Use Visual Studio or `dotnet build` to build.


### Testing

_Warning: Prior to testing, the submodule and the solution must be built in correct order._

Use `dotnet test` to start unit tests or Visual Studio Test Explorer.

## Pull Requests

Before submitting a pull request, [rebase](https://www.atlassian.com/git/tutorials/merging-vs-rebasing) your branch from master. 

⚠ **Do not** use ``git merge`` or the *merge* button provided by Github.

Ensure your pull request is [referencing at least one issue](https://help.github.com/en/github/managing-your-work-on-github/closing-issues-using-keywords) and following PR template.

## [Contributor License Agreement](https://cla.opensource.microsoft.com)

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

## [Code of Conduct](CODE_OF_CONDUCT.md)

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

* (a) The contribution was created in whole or in part by me and I
  have the right to submit it under the open source license
  indicated in the file; or

* (b) The contribution is based upon previous work that, to the best
  of my knowledge, is covered under an appropriate open source
  license and I have the right under that license to submit that
  work with modifications, whether created in whole or in part
  by me, under the same open source license (unless I am
  permitted to submit under a different license), as indicated
  in the file; or

* (c) The contribution was provided directly to me by some other
  person who certified (a), (b) or (c) and I have not modified
  it.

* (d) I understand and agree that this project and the contribution
  are public and that a record of the contribution (including all
  personal information I submit with it, including my sign-off) is
  maintained indefinitely and may be redistributed consistent with
  this project or the open source license(s) involved.