# netjsongraph.js: visualization of netjson data

## About me

> Note: I have droped my personal info.

- Blog: http://geekplux.com/
- GitHub: https://github.com/geekplux
- Twitter: https://twitter.com/geekplux
- Country: China

Please click on the links above to find more information about me.

*Who are you? What’s the focus of your studies? What makes you the best person to work on this project?*

> Note: There I provided my advantage.

## Experiences in Free Open Source Software

*What free and/or open source projects have you participated in? Please describe your contributions, provide us links to your features and commits.*

> Note: There I listed my projects worked before, especially open source project.


## Project Proposal

- Project Title: netjsongraph.js: visualization of netjson data
- Possible Mentor: Mentor Name

## Description

> netjsongraph.js has attracted quite some interest from around the world, but I couldn’t dedicate much time to it recently. It is also lacking automated tests and a modern build process. Probably it would be better to develop it using ES6 (which have some kind of built-in templating feature) and transpile it with babel.js.

> Our goals are the following:

> - make it faster with large numbers
> - make it more mobile friendly
> - use modern tools that are familiar to JS developers, so they can contribute more easily
> - add automated tests so we can be more confident of introducing changes
> - get rid of complex features
> - make it easy to extend, so users can experiment and build their own derivatives
> - make it easy to redraw/update the graph as new data comes in, at least at the library level we should support this
> - geographic visualization (like https://ninux.nodeshot.org/ (nodeshot project))


## Tasks and Schedule

- create a new branch: build the project with yarn, Webpack and Babel. *1 week*
- To build a (mostly) backward compatible version *1 week*
- draw a demo graph using canvas or WebGL. *2 week*
- make a example page to show visualization results. *1 week*
- add test(using Ava and XO) and CI. *1 week*
- discuss and design visualization view *1 week*
- import and integrate with OpenStreeMap or Mapbox to make a map. *1 week*
- visualization implemention. *8 weeks*
- beautify the visualization. *1 weeks*
- improve visualization and test. *4 weeks*
- design interface for plugin (to make this library extensible) *2 week*


## Project Details


- I recommend to use the http://sigmajs.org/ . If the performance is bottleneck, We can use canvas or WebGL directly to draw a graph.
- I think our implemention is data-driven, so we should design a data store for graph generation (a global Object (singleton pattern)). When the data store update, the graph will update, too. So we need to design a great interface and rerender mechanism (a function).
- Our map can use Mapbox or OpenStreeMap.



## My Availability

*school-related activities*

> Note: There should provide what other work you should finish during summer vacation.

I have at least 30 hours every week.

## After GSoC

*Do you have plans to continue with your project within the freifunk community after GSoC?*

> Note: Many organization needs a long time tech support.


Thanks.
