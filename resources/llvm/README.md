# The LLVM Compiler Infrastructure

## 关键词
`llvm`, `clang`, `milr`

## 基本介绍

LLVM是一个自由软件项目，它是一种编译器基础设施，以C++写成，包含一系列模块化的编译器组件和工具链。
发展多年的LLVM组织有着的成熟的社区，也多次参加过GSOC项目，每年的LLVM都会针对其各个子项目提供多种多样的idea（其难度包含低中高不同档次），且每年的LLVM都能有不少的slot。

以下都是官方描述:

The LLVM Project is a collection of modular and reusable compiler and toolchain technologies. Despite its name, LLVM has little to do with traditional virtual machines. LLVM began as a research project at the University of Illinois, with the goal of providing a modern, SSA-based compilation strategy capable of supporting both static and dynamic compilation of arbitrary programming languages. Since then, LLVM has grown to be an umbrella project consisting of a number of different subprojects, many of which are being used in production by a wide variety of commercial and open source projects as well as being widely used in academic research.

The primary sub-projects of LLVM are:

* The LLVM Core libraries provide a modern source- and target-independent optimizer, along with code generation support for many popular CPUs. These libraries are built around a well specified code representation known as the LLVM intermediate representation ("LLVM IR").
* Clang is an "LLVM native" C/C++/Objective-C compiler, which aims to deliver amazingly fast compiles, extremely useful error and warning messages and to provide a platform for building great source level tools. The Clang Static Analyzer is a clang-based tool that automatically finds bugs in your code.
* The LLDB project builds on libraries provided by LLVM and Clang to provide a great native debugger on top of Clang and LLVM libraries.
* The libc++ and libc++ ABI projects provide a standard conformant and high-performance implementation of the C++ Standard Library.
* The MLIR subproject aims to address software fragmentation, compilation for heterogeneous hardware, significantly reduce the cost of building domain specific compilers, and aid in connecting existing compilers.
* The lld project aims to be the built-in linker for clang/llvm. Currently, clang must invoke the system linker to produce executables.
* In addition to official subprojects of LLVM, there are a broad variety of projects that use components of LLVM for various tasks.

## 申请指南

* 在参选组织名单公布后尽早与项目导师联系(通常是邮件和IRC）。
* 在LLVM社区有过提交的有额外加分，如果申请时没有可以尝试询问有没有当前可以尝试的工作。

## Case Study

## Proposals
| Year | Project | Idea | Student | Mentor | Proposal |
| ---- | ------- | ---- | ------- | ------ | -------- |
| 2020 | LLDB    | Implement the missing tab completions for LLDB's command line | [@MrHate](https://github.com/MrHate) | [@Teemperor](https://github.com/Teemperor), [@JDevlieghere](https://github.com/JDevlieghere) | [proposal](https://docs.google.com/document/d/15sWN27KR6I25hJsYRkg8GJwgc1t0skhfvNf2a9PFOFM/edit?usp=sharing) |

## 总结文章
| Year | Project | Idea | Student | Mentor |  Report  |
| ---- | ------- | ---- | ------- | ------ | -------- |
| 2020 | LLDB    | Implement the missing tab completions for LLDB's command line | [@MrHate](https://github.com/MrHate) | [@Teemperor](https://github.com/Teemperor), [@JDevlieghere](https://github.com/JDevlieghere) | [report](https://docs.google.com/document/d/1iZ4ZzGMhAwFYqFByd0mrj_K8E9qwlvT3HcikiU5WrJU/edit?usp=sharing) |

## 历年项目
* [Open LLVM Projects](http://llvm.org/OpenProjects.html)
* [GSOC'16](https://summerofcode.withgoogle.com/archive/2016/organizations/5806108052553728/)
* [GSOC'17](https://summerofcode.withgoogle.com/archive/2017/organizations/6215410651234304/)
* [GSOC'18](https://summerofcode.withgoogle.com/archive/2018/organizations/5263452624912384/)
* [GSOC'19](https://summerofcode.withgoogle.com/archive/2019/organizations/5682474363912192/)
* [GSOC'20](https://summerofcode.withgoogle.com/archive/2020/organizations/5902726635978752/)
