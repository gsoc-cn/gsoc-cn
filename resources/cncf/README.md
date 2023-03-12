# Cloud Native Computing Foundation

## 关键词

`Kubernetes`,  `Docker`, `Prometheus`,`Golang`, `Service Mesh`

## 基本介绍

[CNCF](https://www.cncf.io/)，全称 Cloud Native Computing Foundation（云原生计算基金会），口号是**坚持和整合开源技术来让编排容器作为微服务架构的一部分**。

CNCF 作为一个厂商中立的基金会，致力于 Github 上的快速成长的开源技术的推广，如 Kubernetes、Prometheus、Envoy 等，帮助开发人员更快更好的构建出色的产品。

下图是 CNCF 的全景图:

<p align="center">
  <img width="100%" height="100%" src="https://landscape.cncf.io/images/landscape.png" alt="logo" />
</p>

关于 CNCF 的使命与组织方式请参考 [CNCF 宪章](https://www.cncf.io/about/charter/)，概括的讲 CNCF 的使命包括以下三点：

- 容器化包装。
- 通过中心编排系统的动态资源管理。
- 面向微服务。

CNCF 这个角色的作用是推广技术，形成社区，开源项目管理与推进生态系统健康发展。



PS: 上面的介绍是取自于 [https://jimmysong.io/kubernetes-handbook/cloud-native/cncf.html](https://jimmysong.io/kubernetes-handbook/cloud-native/cncf.html)。宋净超是 CNCF 的 Ambassador，圈内知名人士，如果大家想深入了解 CNCF 基金会及旗下组织，可以翻一翻他的 blog。

## 申请指南

### Idea

CNCF 基金会自己维护了一个 GSoC 的 [repo](https://github.com/cncf/soc) ，里面含有历年的 Project Ideas，包括没有成功入选的 idea。如果对某个 idea 感兴趣的话，可以去 slack 上直接联系相应的 mentor。

### Tips

1. 关于 slots。CNCF 是 Google 联合其他很多家公司宣布成立的开源组织，Kubernetes 又是 Google 在主导推进的，GSoC 是 Google 家的就不必多说了，所以 CNCF 在 slots 上面的问题就不言而喻了。这样就避免了像 OpenCV 今年没有 slots 的情况。
2. 关于 idea 的优先级。社区拿到了 slots 后，可能每个 idea 都有人申请，在不同 idea 申请人的实力差不多时，社区肯定是选取重要的 idea。所以，选取 idea 的时候，也要注意主次，比如，如果某个 idea 是在已有的 issue 中未解决的，那么它的优先级肯定是靠前的。

## Case Study

### Integrate Containerd with Katacontainers - Containerd
今年我做的项目是`Integrate Containerd with Katacontainers`。

在一月份的时候，CNCF 就在 soc 的 repo 下持续更新了今年的 idea。扫了一遍后，对两个 idea 蛮感兴趣的。

一个是 Prometheus 里的某个 idea，这个 idea 和我当时手上的项目正好相关，于是就去 slack 上联系了那个 idea 的 mentor，聊的还蛮愉快的。之后一个礼拜，看了他给的资料后，发现这个 idea 不难。

另一个是 Containerd 的 idea，因为本身在搞容器领域的东西，所以自然就感兴趣了。

在考虑了两三天后，决定还是选容器相关的 idea。原因有两个：

1. 仔细研究了下两个 idea 的背景后，发现 Prometheus 的这个 idea，相比于其他几个 Prometheus 的 idea，不够核心，很有可能选不上。而 Containerd 的这个 idea 则是挺核心，并且对于 Containerd 和 Kubernetes 这两个社区而言这个 feature 是比较紧急的，很大可能性会被选中。
2. 做容器相关的 idea 更符合我的发展路线。而 Prometheus，则只是刚好手上项目用到。并不打算深入监控领域。

选好 idea 后，就该写 Proposal 了。

我在写 Proposal 的时候，与 mentor 沟通的比较多，因为要了解清楚这个项目到底要实现哪些东西，这样才不至于文不对题。竞争这个 idea 的人还是有很多的，对于被选上的原因，感觉大概是之前就做了半年多 Kubernetes 及 Docker 相关的项目，积累了不少经验，使 mentor 和社区能信任我。当然，自己也觉得蛮幸运的了。



PS: 这里我用 slack 的原因，一是用 slack 私信时，可以看到对方那边是几点以及是否在线，这样对沟通的时间比较好掌握；二是用 slack 就和用微信一样，交流起来更加便捷，能够及时解决疑问。

### Conditional Name Server Identifier - CoreDNS
我今年做的项目是`Conditional Name Server Identifier`, 其实是一个 CoreDNS 的 external plugin。

[CoreDNS](https://coredns.io/) 是一个 plugin-based 的轻量级 DNS 服务器，之所以说它是 plugin-based，是因为所有的 DNS 功能都是通过 plugin 实现的，而且 CoreDNS 扩展性高，可定制性强，用户可以根据自己的需求 enable/disable plugin，而且也可以根据需求添加自己的 plugin。CoreDNS 现在已经被 Kubernetes 接受，成为 Kubernetes cluster 的 DNS 服务器。

至于我项目的具体内容的话，大家可以参考我的代码仓库 [idetcd](https://github.com/jiachengxu/idetcd), 里面有详细的介绍，主要是给减轻 DevOps 配置服务器的工作量提供了一个解决方案，可以做到服务器 nodes 使用相同 configuration，动态配置服务器，实现一步到位。而不需要针对各个 node 进行配置。

至于申请的要点的话我认为有两点：
- **积极和 mentor 沟通联系。** 我当时其实是三月份开始准备的，当时在 GSoC 网站上一个组织一个组织看，找到 CNCF 感觉很对自己的胃口，就去 CNCF 自己维护的 GSoC 仓库去看今年的项目了，然后发现这个项目挺感兴趣，就赶紧和 mentor 联系。我是通过邮件联系的，基本上的流程是这样的：第一封邮件先向 mentor 表明自己的兴趣，然后项目所提供的信息有限，就顺便向 mentor 了解具体项目信息；第二封的话就是提出自己的一些看法，包括一些自己没看明白的问题，然后尽量提出自己的解决方案；第三封的话就是开始询问一些细节，开始准备写 proposal。

- **一篇很好的 proposal。** 我个人认为只要你做好了第一点，proposal 是水到渠成。比较重要的是 proposal 尽量边和 mentor 沟通边写，最后 deadline 之前记得发给 mentor review 一下。如果 mentor 看过之后都觉得没问题，或者给你提出修改意见之后你积极修改，我相信被拒掉的几率也很小吧？最后国内的同学如果英语不是很好的话，记得用语法检测工具（比如 Grammarly) 记得修正一下语法错误。

至于 accept 之后的日子就好过了，就是按照计划，逐步完成，记得多和 mentor 交流，我觉得 GSoC 最重要的不是你写了多少代码，而是你对项目宏观把握的提升，而且从和 mentor 的交流之中你也可以对项目管理以及解决问题的方式有一个清晰的认识，我觉得这是单纯写代码学不到的。

至于和 mentor 的交流方式，我比较喜欢视频会议，我和 mentor 大概是每周一次，最后两周是每周三次，期间如果遇到问题也会发邮件沟通。视频通话最好的点就是便于交流，写邮件发消息我觉得还是不如直接说话来的快。

## Proposals

- [Proposals 2018](./proposals/2018/)
- [Proposals 2022](./proposals/2022/)
- 

## 历年项目

- [2017](https://summerofcode.withgoogle.com/archive/2017/organizations/6018829461225472/)
- [2018](https://summerofcode.withgoogle.com/organizations/6453865516367872/#4718187841585152/)
