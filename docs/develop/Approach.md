# Approach

For the ElectionGuard repositories, these are the concepts that guide the approach for developers and writers. 

## ✅ Simplicity

Simplicity is the first and foremost goal of the code. The intent is for others to be able to easily transliterate the code to any other programming language with little more than structures and functions. This simplicity applies to all aspects of the code design, including naming.

## ✅ Transparency

ElectionGuard is open source first. Our code, our issues and even our Continuous Integration (CI) is designed to be visible to the public. This is to allow others to both be able to trust the code, learn, and hopefully help improve ElectionGuard. 

GitHub tools have been our primary tool to maintain transparency. Our cards are all GitHub issues. Our continuous integration uses GitHub Workflows to be out in the open. 

## ✅ Readability

Whether developing or writing for ElectionGuard, the goal is to create easy to read and understand text. We will always be improving in this area, but the goal is to make the system easy to grasp for not only developers, but for the public. This is the primary reason that Python was chosen as the primary reference implementation. Understanding the code and the written word is essential for confidence.

## ✅ Testability

The goal is to maximize code coverage and testing on the reference implementations. Tests are essential to the repositories for both providing proof the code functions but also to provide an understanding of how the code works. This means writing code that can be tested and writing the accompanying tests.

## ✅ Extendable and Interpretable

The reference implementations are intentionally general-purpose to support the different use cases of voting systems. Different projects may wish to use different pieces and parts of each repository. 
