# Red Hen Lab

## 关键词
语音识别 自然语言处理 深度学习  中文项目 高校教授 

## 基本介绍
[Red Hen Lab](http://www.redhenlab.org/home) 是一个致力于研究语音识别（ASR）、自然语言处理（NLP）以及一些视频处理的开源组织，其创始人及负责人为UCLA教授 [Francis Steen](http://cogweb.ucla.edu/steen/)和CASE教授[Mark Turner](http://markturner.org/)，组织内部有来自全球各地高校、组织的志愿者，拥有十分强大的数据资源。这个组织的主要工作是研究开发各种适用于上述技术的开源工具、数据挖掘以及对于其中核心技术的探讨。可以说，在这个组织里，你不仅仅是在码代码，也会有做学术的成分在里面（当然，要看具体的项目）。2018年1月，Red Hen Lab与湖南师范大学联合创办了[认知科学研究中心](http://cognitivescience.hunnu.edu.cn)。

## Case Study - Chinese Pipeline

本次（2018）GSOC 我申请到的项目为Chinese Pipeline，它要求我能够从很多的中文视频里（大部分为新闻联播、晚间新闻等）识别出新闻中的文字，然后再对文字进行NLP的各种工作的处理，包括但不限于分词、命名实体识别、POS tagging等，之后如果还有时间，可以用这些数据进行一些文本分析。这个项目今年总共收了两位申请者，一位专攻语音识别部分，一位专攻自然语言处理部分，我是后者，但同时我也要参与到前者里去。我们这个项目的地址介绍在[这里](http://www.redhenlab.org/home/the-cognitive-core-research-topics-in-red-hen/chinese-pipeline)，会随着项目的进行实时更新，可以说是一个趣味和挑战并存的项目了。虽然说明年应该不会再有类似的项目，但是因为Lab里的中国人很多，明年很可能还会有中文的项目，大家可以提前关注。


## 申请指南

作为一个刚刚申请到这个项目的萌新，我尝试以我的视角还原本次申请。

首先我想说，这个组织相对来说比较好申，作为一个第四次参加的强org，这个组织今年收取了12个人，除了coala等少数几个大组织，这个组织招收名额还是十分可观的。其次，这个组织不需要你提交pr，不需要你提前几个月联系。我最开始是想申 CLIPS 或是CLTK，但是它们的名额都太少而且竞争还超级激烈，因此在还有十几天就要截止时我才开始跟Red Hen Lab邮件联系。 Prof. Steen 超级负责任，几乎每信必回，而且对你提到的问题都乐于解答，给我的印象非常好。在申请日期截止前，我做的事情就是把教授提到的开源软件熟悉了一遍，然后写了一个pre-proposal，修改之后再提交了一个proposal最终版。在我后几次发邮件时，Prof.Steen说我们给你一个视频，如果你能够用deepspeech(百度的一个工具)把它转化为文字，will be a plus. 因此在截止日期到了之后，我开始在网上查相关攻略，最后用Paddlepaddle简单实现了一下，发了过去，最终就申请到了。另一个小伙伴更甚，她离结束三四天才开始联系Red Hen Lab，用了一个下午加一个晚上就写完了proposal，之后就收到了offer。所以说可能是由于中国申请者太少，我们两个就很幸运的、难度较低地收到了录取。

那么申请这个项目究竟有没有什么背景呢？一定要说的话，首先我觉得一定要有搜寻工具和资料的能力，就像他们主页上说的，它们不希望招什么都要问他们的人。再就是要有Tensorflow或其他机器学习库的使用经历，因为据我观察他们主要还是使用的Tensorflow。其他我觉得都不重要，编码能力也没见他们考察，我和另一个小伙伴甚至都不是CS或是软工的，我们一个是电子，一个是电气专业。所以，大家放宽心，加油申请！

至于申请时如何联系的问题，我觉得发邮件就可以，直接发给redhenlab@gmail.com，之后我收到了Prof. Steen的回复，然后就一直跟他联系了。Red Hen Lab 还会让你填一个mail list，你可以详细填一下你的技能等，帮助社区更好的了解自己。
## Summer 体验
	> 待续

## Proposal(s)
我的放在了 [resources/proposals/2018/red-hen-lab](../proposals/2018/red-hen-lab) 下面。

## 历年项目
[GSOC-2015](https://www.google-melange.com/archive/gsoc/2015/orgs/redhenlab)               
[GSOC-2016](https://summerofcode.withgoogle.com/archive/2016/organizations/5973353810624512/#projects)         
[GSOC-2017](https://summerofcode.withgoogle.com/archive/2017/organizations/6645492838563840/)   

