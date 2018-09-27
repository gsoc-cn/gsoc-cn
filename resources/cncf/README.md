# Cloud Native Computing Foundation

## 关键词

`Kubernetes`,  `Docker`, `Prometheus`,`Golang`, `Service Mesh`

## 基本介绍

[CNCF](https://www.cncf.io/)，全称Cloud Native Computing Foundation（云原生计算基金会），口号是**坚持和整合开源技术来让编排容器作为微服务架构的一部分**。

CNCF作为一个厂商中立的基金会，致力于Github上的快速成长的开源技术的推广，如Kubernetes、Prometheus、Envoy等，帮助开发人员更快更好的构建出色的产品。

下图是CNCF的全景图:

<p align="center">
  <img width="100%" height="100%" src="https://raw.githubusercontent.com/cncf/landscape/master/landscape/CloudNativeLandscape_latest.png" alt="logo" />
</p>

关于CNCF的使命与组织方式请参考[CNCF宪章](https://www.cncf.io/about/charter/)，概括的讲CNCF的使命包括以下三点：

- 容器化包装。
- 通过中心编排系统的动态资源管理。
- 面向微服务。

CNCF这个角色的作用是推广技术，形成社区，开源项目管理与推进生态系统健康发展。



PS: 上面的介绍是取自于[https://jimmysong.io/kubernetes-handbook/cloud-native/cncf.html](https://jimmysong.io/kubernetes-handbook/cloud-native/cncf.html)。宋净超是CNCF的Ambassador，圈内知名人士，如果大家想深入了解CNCF基金会及旗下组织，可以翻一翻他的blog。

## 申请指南

### Idea

CNCF基金会自己维护了一个GSoC的[repo](https://github.com/cncf/soc) ，里面含有历年的Project Ideas，包括没有成功入选的idea。如果对某个idea感兴趣的话，可以去slack上直接联系相应的mentor。

### Tips

1. 关于slots。CNCF是Google联合其他很多家公司宣布成立的开源组织，Kubernetes又是Google在主导推进的，GSoC是Google家的就不必多说了，所以CNCF在slots上面的问题就不言而喻了。这样就避免了像OpenCV今年没有slots的情况。
2. 关于idea的优先级。社区拿到了slots后，可能每个idea都有人申请，在不同idea申请人的实力差不多时，社区肯定是选取重要的idea。所以，选取idea的时候，也要注意主次，比如，如果某个idea是在已有的issue中未解决的，那么它的优先级肯定是靠前的。

## Case Study

### Integrate Containerd with Katacontainers - Containerd
今年我做的项目是`Integrate Containerd with Katacontainers`。

在一月份的时候，CNCF就在soc的repo下持续更新了今年的idea。扫了一遍后，对两个idea蛮感兴趣的。

一个是Prometheus里的某个idea，这个idea和我当时手上的项目正好相关，于是就去slack上联系了那个idea的mentor，聊的还蛮愉快的。之后一个礼拜，看了他给的资料后，发现这个idea不难。

另一个是Containerd的idea，因为本身在搞容器领域的东西，所以自然就感兴趣了。

在考虑了两三天后，决定还是选容器相关的idea。原因有两个：

1. 仔细研究了下两个idea的背景后，发现Prometheus的这个idea，相比于其他几个Prometheus的idea，不够核心，很有可能选不上。而Containerd的这个idea则是挺核心，并且对于Containerd和Kubernetes这两个社区而言这个feature是比较紧急的，很大可能性会被选中。
2. 做容器相关的idea更符合我的发展路线。而Prometheus，则只是刚好手上项目用到。并不打算深入监控领域。

选好idea后，就该写Proposal了。

我在写Proposal的时候，与mentor沟通的比较多，因为要了解清楚这个项目到底要实现哪些东西，这样才不至于文不对题。竞争这个idea的人还是有很多的，对于被选上的原因，感觉大概是之前就做了半年多Kubernetes及Docker相关的项目，积累了不少经验，使mentor和社区能信任我。当然，自己也觉得蛮幸运的了。



PS: 这里我用slack的原因，一是用slack私信时，可以看到对方那边是几点以及是否在线，这样对沟通的时间比较好掌握；二是用slack就和用微信一样，交流起来更加便捷，能够及时解决疑问。

### Conditional Name Server Identifier - CoreDNS
我今年做的项目是`Conditional Name Server Identifier`, 其实是一个CoreDNS的external plugin。

[CoreDNS](https://coredns.io/) 是一个plugin-based的轻量级DNS服务器，之所以说它是plugin-based，是因为所有的DNS功能都是通过plugin实现的，而且CoreDNS扩展性高，可定制性强，用户可以根据自己的需求enable/disable plugin，而且也可以根据需求添加自己的plugin。CoreDNS 现在已经被Kubernetes接受，成为Kubernetes cluster的DNS服务器。

至于我项目的具体内容的话，大家可以参考我的代码仓库[idetcd](https://github.com/jiachengxu/idetcd), 里面有详细的介绍，主要是给减轻DevOps配置服务器的工作量提供了一个解决方案，可以做到服务器nodes使用相同configuration，动态配置服务器，实现一步到位。而不需要针对各个node进行配置。

至于申请的要点的话我认为有两点：
- **积极和mentor沟通联系。** 我当时其实是三月份开始准备的，当时在GSoC网站上一个组织一个组织看，找到CNCF感觉很对自己的胃口，就去CNCF自己维护的GSoC仓库去看今年的项目了，然后发现这个项目挺感兴趣，就赶紧和mentor联系。我是通过邮件联系的，基本上的流程是这样的：第一封邮件先向mentor表明自己的兴趣，然后项目所提供的信息有限，就顺便向mentor了解具体项目信息；第二封的话就是提出自己的一些看法，包括一些自己没看明白的问题，然后尽量提出自己的解决方案；第三封的话就是开始询问一些细节，开始准备写proposal。

- **一篇很好的proposal。** 我个人认为只要你做好了第一点，proposal是水到渠成。比较重要的是proposal尽量边和mentor沟通边写，最后deadline之前记得发给mentor review一下。如果mentor看过之后都觉得没问题，或者给你提出修改意见之后你积极修改，我相信被拒掉的几率也很小吧？最后国内的同学如果英语不是很好的话，记得用语法检测工具（比如Grammarly)记得修正一下语法错误。

至于accept之后的日子就好过了，就是按照计划，逐步完成，记得多和mentor交流，我觉得GSoC最重要的不是你写了多少代码，而是你对项目宏观把握的提升，而且从和mentor的交流之中你也可以对项目管理以及解决问题的方式有一个清晰的认识，我觉得这是单纯写代码学不到的。

至于和mentor的交流方式，我比较喜欢视频会议，我和mentor大概是每周一次，最后两周是每周三次，期间如果遇到问题也会发邮件沟通。视频通话最好的点就是便于交流，写邮件发消息我觉得还是不如直接说话来的快。

## Proposals

见 [resources/proposals/2018/cncf](../proposals/2018/cncf)

## 历年项目

- [2017](https://summerofcode.withgoogle.com/archive/2017/organizations/6018829461225472/)
- [2018](https://summerofcode.withgoogle.com/organizations/6453865516367872/#4718187841585152/)
