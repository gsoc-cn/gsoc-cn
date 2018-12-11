# Checkstyle

## Technologies

Java, ANTLR

## 基本介绍

[Checkstyle](http://checkstyle.sourceforge.net/) 是一个 Java 代码静态分析工具，可以执行高度定制化且功能强大的静态分析和检查，在代码实时提示和持续集成（Continuous Integration）中有重要作用。一个典型的应用是使用 Checkstyle 来保证代码遵循 [Google Java Style](http://google.github.io/styleguide/javaguide.html) 规范。

Checkstyle 有一个团队负责维护该项目，其作为开源组织参与了 GSoC 2014 和 2017。作为一个代码质量控制工具，Checkstyle 对其项目本身的质量要求达到了近乎严苛的程度，有一套非常规范的贡献流程和多平台、多工具链的 CI 体系。参与项目可以深刻的锻炼一个人的代码质量和工程水平，100% coverage 的变态要求也将 TDD 思想（Test-Driven Development）发挥到了极致。

总而言之，即使在开源世界中，这也是一个对待新技术十分激进的组织，会在开发中积极尝试各种奇淫技巧。参与其中可以极大的提升对 CI 体系的认知，学习到如何从一个高屋建瓴的视角统观整个项目，是非常难得的体验。

## 申请指南

建议申请该项目的同学有基本的 Java 基础，且对自己的代码书写规范有较高要求（通俗而言，代码洁癖者佳）。

Checkstyle 每年会在 GitHub Wiki 中添加一个当年的 idea list，例如 [Checkstyle GSoC 2017 Project Ideas](https://github.com/checkstyle/checkstyle/wiki/Checkstyle-GSoC-2017-Project-Ideas)。基本上这就是当届 GSoC 可以申请的方向。根据个人体验，Checkstyle 接受自行提出的 idea 概率不大，因为组织的导师人手匮乏，而已经提出的 idea 多是他们一直想做或者 GSoC 几年来一直持续维护的，相对于学生自己的点子，我猜测导师们会更加倾向于已有的 idea。

Checkstyle 开发者主要的交流平台是 [Gitter](https://gitter.im/checkstyle/checkstyle) 和 [Google Group](https://groups.google.com/forum/#!forum/checkstyle-devel)，其中前者是 IM 聊天室，主要是用来做简单讨论（especially one-turn Q&A），后者主要用作较为正式和复杂内容的讨论。

通常来讲，大家在 GSoC 宣布组织名单后，可以到 Gitter 中进行套磁。Checkstyle 也会给出一个专门的 [GSoC 学生指南](https://github.com/checkstyle/checkstyle/wiki/To-student-of-GSoC-2017)，详细写出了申请当年 GSoC 的要求，大致包括要修复数个『功能级』的 issue，并给出的 proposal 的内容要求。

## Case Study

[Regression Testing Tool and HTML Report Generator for Pull Request](https://github.com/checkstyle/regression-tool) 是 [@Luolc](https://github.com/Luolc) 在 GSoC 2017 中参与的一个项目，当时曾撰文介绍 GSoC 并在文章中包含了很多 Checkstyle 项目申请过程和经验分享，可参见 [Google 编程之夏 (GSoC)：海量优质项目，丰厚报酬，你竟然还不知道？](https://zhuanlan.zhihu.com/p/27330699)。

这个项目是为了提升开发流程中的自动化。Checkstyle 在每次接收一个功能性的 Pull Request 时，都需要在数个知名 Java 项目上运行 Checkstyle 检查，进行回归测试，防止因为代码改动引发不希望的 bug。问题在于，因为每次修改的功能点各不相同，执行回归测试时的参数都需要人工配置。于是希望能通过每次 Pull Request 中的 git changes 自动化的提取出一些信息，辅助进行参数配置的工作。

我在 GSoC 2017 申请了两个项目，其中另一个 [Optimization of Distance Between Methods in Single Java Class](https://docs.google.com/document/d/1lWXpWhUN6cE06sjQANjWxamc_X3ddbSphTRSofChLyk/edit?usp=sharing) 才是我一直想做的项目。后来到了 proposal 提交截止前两天，导师找到我说人手不够，这个项目没有人带，让我赶紧再选个项目赶一份 proposal 出来，于是才有了前文介绍的项目。简而言之，proposal 重在精不在多，多修 issue，多和导师交流套磁比较重要。

## Proposals

PDF 版见该仓库 [resources/proposals/2017/checkstyle](../proposals/2017/checkstyle) 目录。

Google Docs 版见：
- [Optimization of Distance Between Methods in Single Java Class](https://docs.google.com/document/d/1lWXpWhUN6cE06sjQANjWxamc_X3ddbSphTRSofChLyk/edit?usp=sharing)
- [Regression Testing Tool and HTML Report Generator for Pull Request](https://docs.google.com/document/d/1xu6SE4qeKTRQ45R9FSLOQB-t5ExzBGyvU9FLGifvxY0/edit?usp=sharing)

## 历年项目

- [2017](https://summerofcode.withgoogle.com/archive/2017/organizations/5883569398349824/)
- [2014](https://www.google-melange.com/archive/gsoc/2014/orgs/checkstyle)
