# Apache SystemML

## 关键词

`Java`, `Deep learning`, `Apache Spark`, `Compiler`, `Data management`

## 基本介绍

[Apache SystemML](https://systemml.apache.org/) 是一个致力于处理大规模机器学习的平台。它提供了一种类似R的领域特有语言（或者用 Python）给数据科学家去实现机器学习的算法，然后将算法运行在 Apache Spark 集群上。

## 申请指南

建议想申请的同学具备一定的 Java 基础，涉及 Runtime 技术的主题最好熟悉 Apache Spark。最好能有一些 Machine Learning 的知识，不过没有也没关系，关键要表达出对其学习的热情。SystemML 社区比较注重代码实践能力，因此写proposal的同时最好能提交至少一个PR。我在18年参加的项目是在 JIRA 上公布[主题](https://issues.apache.org/jira/browse/SYSTEMML-2083)的，我在上面和导师进行交流，同时我也利用 [Mailing List](https://www.mail-archive.com/dev@systemml.apache.org/maillist.html) 提出我的问题和看法和社区里的人进行讨论。

## Case Study

### Language and runtime for parameter servers

我参加的是2018年的[Language and runtime for parameter servers](https://summerofcode.withgoogle.com/archive/2018/projects/5148916517437440/)。我个人建议的是越早接触社区并能和导师沟通，越能表现你的积极性，开源的其中一个目的就是集各方意见，所以合格的 GSOC 学生是一个有能力和社区沟通的人。当然刚刚接触这个主题的时候我也不知道具体要实现什么，没关系，要敢于提问，导师会很乐意给出指示，例如要看的论文。在理解主题的同时，为了要展示我的代码能力，我选了一个 JIRA 的issue尝试着做一个PR。在将近两个月的准备工作中，我完成了两个PR和proposal。

关于项目： idea 源于最新的一种 deep learning model training 的并行架构叫 Parameter Server。我的proposal是引入 Data Parallel Parameter Server 到 SystemML当中，需要完成的工作包括 Compiler 的语言扩展和 基于 Apache Spark 的 Runtime 扩展。


## Proposals

| Year | Project | Idea | Student | Mentor | Proposal |
| ---- | ------- | ---- | ------- | ------ | -------- |
|  2018    |   Apache SystemML      |   [Language and runtime for parameter servers](https://issues.apache.org/jira/browse/SYSTEMML-2083)   |   [Guobao Li](https://github.com/EdgarLGB)      |   [Matthias Boehm](https://github.com/mboehm7)     |       [Proposal][2018-proposal]   |

## 总结文章

| Year | Project | Idea | Student | Mentor |  Report  |
| ---- | ------- | ---- | ------- | ------ | -------- |
| 2018 |  Apache SystemML  |  [Language and runtime for parameter servers](https://issues.apache.org/jira/browse/SYSTEMML-2083)    |     [Guobao Li](https://github.com/EdgarLGB)    |    [Matthias Boehm](https://github.com/mboehm7)    |   [Report][report]       |

## 历年项目

* [2018][2018-proposal]

[2018-proposal]: proposals/2018/apache-systemml-parameter-server.pdf
[report]: http://edgarlgb.github.io/Gsoc-project/
