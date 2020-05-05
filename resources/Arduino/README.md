# Arduino

## 关键词

`Arduino`, `electronics`, `robotics`, `interactivity`, `open-source electronics platform`

## 基本介绍

[Arduino](https://arduino.cc/) 是一款面向初学者的开源硬件，同时也有完全开源的软件社区。Arduino 被广泛用于单片机入门。

## 申请指南

Arduino 社区的很多内容是软件硬件相结合的，申请的同学需要有一定的硬件基础，部分涉及到编写驱动的 idea 需要你去翻芯片手册。此外， Arduino 有很多不同的开发板，主要涉及 AVR，ARM，Quark 三种主流架构，所以你还得有跨平台开发的相关知识。社区要求申请者需要向其官方库提交至少一个 PR，虽然没有明确难度要求，但是显然只改 typo 的话是很难让社区相信你有能力搞定项目的。。

关于 Slot：Arduino 今年是第一年参加 GSoC，所以只有两个名额，如果社区评价好的话后面应该会增加。

关于活跃度：就我个人的感受而言，负责 GSoC 的老哥似乎热情不高，写 Proposal 的时候没收到反馈，Github 上的留言也很死板(当然也可能是忙不过来)。但是其它部分还是不错的，即使是很久没有更新的官方 library，也能很快收到反馈。

沟通方式：在申请阶段通过 Github issue 沟通

工作方式：Github

版权：Arduino 社区有很多 contributor，如果你的代码中用到了他们的代码，请务必遵守许可证相关规定

## Case Study

### Port FreeRTOS to Portenta

2020 年的项目很有意思，可能是因为第一年参加没有经验，他们放出的项目都很简单，比如有给官方 lib 写例程，做分析。今年的重点在 Arduino 推出了它们的第一款工业级开发板：Portenta H7，很大一部分 idea 是为这块板子做配套工具的。

因为我对 OS 比较熟悉，看到这个 idea 就觉得有戏，然后就查查资料开始写 proposal，幸运的是在这个领域有很多成熟的方案，比如 FreeRTOS 官方就有 H7 用的 STM32H747 的移植说明。

这个芯片的亮点在于它有两个 core，一个 ARM Cortex-M4 和 ARM Cortex-M7，AMP 架构是本项目的难点，主要问题是两个 core 怎么合作。对于这一点 FreeRTOS 有一套 message buffer 的机制实现 core to core communication，甚至 ST 官方也有一套可以参考的东西。

所以其实这个项目的工作就是做一下整合+测试。。

对我来说最难的地方是提 PR，你说这么些个官方库，从发布到现在不知道迭代了多少遍，找 bug 那是千难万难，在一堆 issue 里面找了几天也没发现我能做的，最后干脆把它的[键盘库](https://github.com/arduino-libraries/Keyboard)重写了，重写后的 [lib](https://github.com/MRNIU/Keyboard) 可以支持更多的按键，添加不同的键盘布局也变得简单了(但是到今天结果公布我都没把这个坑填完QaQ)。

整个 proposal 大概花了三天时间完成，写 PR 花了一个多礼拜，期间很多时间都是在跟另外一位 contributor 沟通，因为我的代码里面用到了他的代码而没有注明版权信息。最后结果是把他的代码全删了自己重写一遍。。这花了很多时间，所以如果你使用了别人的代码，记得把版权写清楚。

重点：

- **写好 PR**

    PR 是社区了解你的直接方式，要注意代码风格，测试，社区版权规定，还有与相关人员良好的沟通。如果你实在找不到能下手的地方，那么也许开个新坑是个不错的主意，只要是对社区有益的 PR，mentor 在评估时也会有所考量的。建议：自己挖的坑要填完！！！

- **写好 proposal**

    proposal 越详细越好，比如我就给出了项目完成后的目录结构可能是什么样子的，几个关键宏如何定义，哪些硬件接口函数需要实现。Schedule 部分要留下足够的余地，对于硬件开发来说，经常会遇到莫名其妙的问题，尤其是一块新的开发板，很难保证不会遇到什么硬件级的 bug，如果在评估的时候进度相差太大，会影响你的 stipend。

## Proposals

| Year | Project | Idea | Student | Mentor | Proposal |
| ---- | ------- | ---- | ------- | ------ | -------- |
|  2020  | Port FreeRTOS to Portenta |   [GSoC @ Arduino: Ideas List](https://github.com/arduino/summer-of-code/blob/master/ideas.md)   |  [@MRNIU](https://github.com/MRNIU) | [@alranel](https://github.com/alranel) |   [PortFreeRTOS2Portenta](./proposals/2020/PortFreeRTOS2Portenta.pdf)   |

## 总结文章

| Year | Project | Idea | Student | Mentor | Report |
| ---- | ------- | ---- | ------- | ------ | -------- |
|  2020  | Port FreeRTOS to Portenta |   [GSoC @ Arduino: Ideas List](https://github.com/arduino/summer-of-code/blob/master/ideas.md)   |   [MRNIU](https://github.com/MRNIU) | [alranel](https://github.com/alranel) |   等我做完了再来写 (´･ω･`)   |

## 历年项目

* [2020](https://summerofcode.withgoogle.com/organizations/6251078376488960/#6482418854264832)

