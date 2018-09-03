# coala

## 基本介绍

[coala][1] 是一个 Python 实现的命令行 linter，提供一个统一的命令行接口，用于代码分析和修复，无论你使用的是哪种开发语言。官方的一句话介绍是：linting and fixing code for all languages。同时，coala支持多种IDE/编辑器的扩展。coala也可以用在Continuous Integration上，比如自动检查github上的Pull Request，并自动生成修复的patch。

以下内容节选自[开源项目哪里找？ - 高策的回答 - 知乎][2](有改动)，主要是推荐coala社区的理由：

> 1. 社区有完整的贡献指南和从newcomer到developer再到maintainer的贡献路线，对新人非常友好;
> 2. 社区有完善的CI/CD 流程，以及文档，基础设施完整且实用; 
> 3. 社区完全由爱好者组成，没有公司参与，比较单纯，社区成员也相对比较友好; 
> 4. 每年都是GSoC的org，在未来有拿Google 的资助为coala 贡献代码的可能; (补充: coala之前是在Python Software Foundation组织下参加的GSoC，2017年第一次作为独立组织参加，拿到9个slots，2018年拿到19个slots，相比总共的申请人数30+来说，算是成功率比较高的org）
> 5. coala 社区的贡献难度低。(补充：因为coala是用python编写的，并且项目规模并不很大；GSoC的project多数都和core无关，一般是coala周边的project，不读核心代码也没什么关系）

[1]: https://coala.io
[2]: https://www.zhihu.com/question/270443389/answer/354203261

## 申请指南

coala有一个[projects][3]页面，上面有历年以及最新的projects/ideas列表。coala也欢迎申请者自己提出idea。

coala开发者主要的交流平台是[Gitter][4]，其中有专门用来讨论GSoC相关内容的[频道][5]。

[3]: https://projects.coala.io
[4]: https://gitter.im/coala/
[5]: https://gitter.im/coala/coala/gsoc

## Case Study - GSoC 2018 项目

[@li-boxuan][6]在 GSoC 2018 申请了两个项目, 其中[coala Language Server][7]是我想做的项目，另一个是最后时刻提交的一个backup proposal，没想到前者没中，而后者中了。所以，如果有时间的话（我就是最后熬夜赶工出来的，质量比较差就不好意思放上来了），最好不要孤注一掷只交一份proposal。还有一点：org获得的slot数目，与学生提交的proposal质量和数量有关，所以org的管理员会比较希望大家尽量能多提交proposal。

这里简单讲一下coala Language Server这个项目。[Language Server Protocol][8]是微软提出的一套协议，简单来说就是将IDE/编辑器与语言服务器解耦。

> The Language Server protocol is used between a tool (the client) and a language smartness provider (the server) to integrate features like auto complete, go to definition, find all references and alike into the tool

举个例子，coala现在有vim, emacs, sublime, Eclipse等IDE & 编辑器的插件，但每个插件都要用不同的语言/规则编写。Language Server的作用就是不再需要这些插件，而由一个统一的server + IDE/client的client取代。

现在coala已经有一个基本可以用的[coala Language Server][9], 是由[@gaocegege][10]写的，他也会是今年这个项目的mentor。但是还有很多bug，以及一些待实现的feature，待补充的测试、文档等。这个project就是基于已有的Language Server做重构/开发。

这里需要注意的是，每个org的人选最后是由管理员来决定的，不一定完全按照mentor的preference。所以和导师套词固然重要，但是管理员的决定权也是很重要的。

如果最后没有选上也不要灰心，不一定是你的实力问题，也可能只是运气不够好，最后的结果会受到很多场外因素的影响：比如可能slot紧张，而你的project比起其他的没有那么重要，即使你的proposal写得很好，贡献在社区里很多；也可能有的候选人有其他public relation，就像申请国外大学，推荐信有时候比三维更重要。

[6]: https://github.com/li-boxuan
[7]: https://github.com/gsoc-cn/gsoc-cn/blob/master/resources/proposals/2018/coala/coala%20GSoC%202018%20Application%20-%20Boxuan%20Li%20-%20coala%20Language%20Server.pdf
[8]: https://langserver.org/
[9]: https://github.com/coala/coala-vs-code
[10]: https://github.com/gaocegege

## 历年项目

- [2017](https://summerofcode.withgoogle.com/archive/2017/organizations/5817061024464896/)
- [2016](https://summerofcode.withgoogle.com/archive/2016/organizations/5597862805110784/)
