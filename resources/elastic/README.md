# Elastic

## 基本介绍

[Elastic][1] 是从 18 年开始参加 GSoC 的一个组织，它的主要项目包括 [Elasticsearch][2], [Logstash][3], [Kibana][4] 和 [Beats][5]，前三者组合在一起是工业界流行的 ELK stack，又称 Elastic stack

[1]: https://www.elastic.co/
[2]: https://www.elastic.co/products/elasticsearch
[3]: https://www.elastic.co/products/logstash
[4]: https://www.elastic.co/products/kibana
[5]: https://www.elastic.co/products/beats

以下是 Elastic 的 ecosystem:

<figure style="text-align: center">
  <img src="https://lh5.googleusercontent.com/mAnUZ0Eb05xJ0FfPLdZUYP2Y6lsoKkxTXXeWRkR90Q5fxt50Af9ee35Oygcz_TUZhWV31D1008C0-DVvC7VyjgRxEAp7x7yrGp_BZvL0hMiPSoSxQjtJXFG5r0qJrtU88XKxdkCx" />
  <figcaption>Elastic Ecosystem</figcaption>
</figure>

## 申请指南

每一个项目都有不同的技术栈，对于 Elasticsearch 需要熟练掌握 Java；对于 Logstash 需要掌握 Ruby 和 Java；对于 Kibana 需要熟练掌握 Javascript。Elastic 社区比较重视申请者的实际编程能力，所以申请者需要在写 proposal 之前提交至少一个 [Pull Request](https://help.github.com/articles/about-pull-requests/)，无论是修改和项目相关的 bug 还是写新 feature 都是对申请者的能力有用的背书。

Elastic 维护一个 [idea list][6]，不过他们也鼓励自己构想 idea 并实现。在 GSoC 的申请之前，你可以在 [Elastic 的 discuss 论坛][7] 上提前发布自己的想法，这样会收获到来自社区的评论，可以帮助你更好地完善你的 proposal。除此之外，你可以在论坛上找到之前的申请者都是如何与社区进行沟通和交流的。

Elastic 使用的交流平台主要是 Slack, IRC, Discuss, 平常的会议会使用 Zoom

我在 18 年参加的是 Kibana 的项目，具体的申请流程和体验参见 [你是怎么申请成功谷歌编程之夏（GSoC）项目？](https://www.zhihu.com/question/66687826/answer/375742767)

[6]: https://github.com/elastic/gsoc
[7]: https://discuss.elastic.co/c/elastic-community/elastic-gsoc

## Case Study

### Kibana Calendar Visualization and Filtering

我参加的是 2018 年的 [Kibana: Calendar Visualization and Filtering](https://summerofcode.withgoogle.com/archive/2018/projects/6162528463749120/)。因为 Elastic 的技术在工业界的知名度，申请项目的竞争非常激烈，不仅需要申请人很好的编程背景，还要有一份合格的 proposal。个人的建议是如果你对 Elastic 的技术非常感兴趣可以在对应 project 的 issue 上面多花一些时间，做一点有意义的 pull request，这样的话通过率会比较高。

关于项目: idea 的提出源于 Kibana 团队的 teacher 对于管理教学中日程表的使用。在项目之前，Kibana 基于索引文档只提供了基于横轴纵向分割的聚合操作，e.g. Date Histogram Aggregations on log data. 然而没有一个合适的根据日历显示格式排版的组件来展示现有的数据，于是就诞生了这个可视化插件，用来展示基于一天，一个月或者是一年的数据热点图。

未来有可能会成为 Kibana 的核心插件，现阶段还是作为一个 community plugin 来运作。感兴趣的同学 stay tuned: [Kibana Calendar Visualization](https://github.com/aaronoah/kibana_calendar_vis)

## Proposals

PDF 见 [resources/proposals/2018/elastic](../proposals/2018/elastic)

## 历年项目

- [2018](https://summerofcode.withgoogle.com/archive/2018/organizations/5469541127684096/)
