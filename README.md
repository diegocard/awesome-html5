Awesome HTML5 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) [![Build Status](https://api.travis-ci.org/diegocard/awesome-html5.svg?branch=master)](https://travis-ci.org/diegocard/awesome-html5)
=============

A curated list of awesome HTML5 resources. Inspired by [awesome-php](https://github.com/ziadoz/awesome-php) and [awesome-python](https://github.com/vinta/awesome-python)

## Table of Contents
- [Articles and standards](#articles-and-standards)
- [Multimedia capabilities](#multimedia-capabilities)
  - [Audio](#audio)
  - [Media capture](#media-capture)
  - [Picture in Picture](#picture-in-picture)
  - [Speech synthesis](#speech-synthesis)
  - [Voice recognition](#voice-recognition)
  - [Virtual Reality (VR)](#virtual-reality)
  - [Web animations](#web-animations)
- [Elements](#elements)
  - [Canvas](#canvas)
  - [Head](#head)
  - [Sectioning](#sectioning)
  - [Media Elements](#media-elements)
  - [Forms](#forms)
  - [Time](#time)
  - [WebVTT](#webtt)
  - [HTML Imports](#html-imports)
- [Development APIs](#development-apis)
  - [Permissions](#permissions)
  - [Geolocation](#geolocation)
  - [Cryptography](#cryptography)
  - [File](#file)
  - [Frame timing](#frame-timing)
  - [requestIdleCallback](#requestidlecallback)
  - [requestAnimationFrame](#requestanimationframe)
  - [Web payments](#web-payments)
- [Semantics](#semantics)
- [Accessibility](#accessibility)
- [DOM management](#dom-management)
  - [Shadow DOM](#shadow-dom)
  - [Data Binding](#data-binding)
  - [Web Components](#web-components)
- [Progressive web apps](#progressive-web-apps)
  - [Service Workers](#service-workers)
  - [Offline caching](#offline-caching)
  - [Push Notifications](#push-notifications)
- [Client side storage](#client-side-storage)
- [Performance](#performance)
- [Mobile](#mobile)
- [Communications and interoperability](#communications-and-interoperability)
  - [Web Sockets](#web-sockets)
  - [WebRTC](#webrtc)
- [Web Workers](#web-workers)
- [WebGL](#webgl)
- [Browser compatibility](#browser-compatibility)
- [Books](#books)
- [Game development](#game-development)
- [Videos and Keynotes](#videos-and-keynotes)
- [Websites and resources](#websites-and-resources)
  - [Websites](#websites)
  - [Weekly news](#weekly-news)
  - [Twitter](#twitter)
- [Contributing](#contributing)

## Articles and standards

* [HTML 5.3](https://w3c.github.io/html/) - Current HTML5 spec
* [Progressive enhancement](https://www.smashingmagazine.com/2009/04/progressive-enhancement-what-it-is-and-how-to-use-it/)
* [The extensible web manifesto](https://extensiblewebmanifesto.org/)
* [Differences between HTML5 and HTML4 from W3C](https://www.w3.org/TR/html5-diff/)

## Multimedia capabilities

### Audio

* [Getting started with the Web Audio API](https://www.html5rocks.com/en/tutorials/webaudio/intro/?redirect_from_locale=es)
* [Web Audio API at MDN](https://developer.mozilla.org/es/docs/Web_Audio_API)
* [Making a Guitar Tuner with HTML5](https://jonathan.bergknoff.com/journal/making-a-guitar-tuner-html5)
* [Audio visualisation with the Web Audio API and React](https://www.twilio.com/blog/audio-visualisation-web-audio-api--react)

### Media Capture

* [Capturing Audio & Video in HTML5](https://www.html5rocks.com/es/tutorials/getusermedia/intro/)
* [Using the media capture API](https://www.sitepoint.com/using-the-media-capture-api/)

### Picture in Picture

* [Chrome's new Picture in Picture API](https://developers.google.com/web/updates/2018/10/watch-video-using-picture-in-picture)

### Speech Synthesis

* [Intro to the HTML5 Speech Synthesis API](http://creative-punch.net/2014/10/intro-html5-speech-synthesis-api/)
* [Another useful intro](https://shapeshed.com/html5-speech-recognition-api/)

### Voice Recognition

* [Web speech API demo](https://www.google.com/intl/en/chrome/demos/speech.html)
* [Using the Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API/Using_the_Web_Speech_API)
* [Experimenting with the Web Speech API](https://www.sitepoint.com/experimenting-web-speech-api/)
* [Free voice recognition library (annyang)](https://www.talater.com/annyang/)

### Virtual Reality

* [Firefox Reality now available](https://blog.mozilla.org/blog/2018/09/18/firefox-reality-now-available/)

### Web animations

* [Intro to web animations](http://danielcwilson.com/blog/2015/07/animations-intro/)
* [When to Use the Web Animations API](http://danielcwilson.com/blog/2016/08/why-waapi/)

## Elements

### Canvas

* [Brief description from W3 Schools](https://www.w3schools.com/tags/tag_canvas.asp)
* [Tutorial from MDN](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial)
* [Various Tutorials](https://www.html5canvastutorials.com/)
* [Cheat Sheet](https://simon.html5.org/dump/html5-canvas-cheat-sheet.html)

### Head

* [A list of things that go in your pages' HEAD element](https://gethead.info/)

### Sectioning

* [How to Use The HTML5 Sectioning Elements](https://blog.teamtreehouse.com/use-html5-sectioning-elements)

### Media Elements

* Audio and Video
  - [audio tag from W3Schools](https://www.w3schools.com/tags/tag_audio.asp)
  - [video tag from W3 Schools](https://www.w3schools.com/tags/tag_video.asp)
  - [Tutorial from MDN](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Video_and_audio_content)
  - [Capturing audio and video in HTML5](https://www.html5rocks.com/en/tutorials/getusermedia/intro/)
* embed tag
  - [Brief description from W3 Schools](https://www.w3schools.com/tags/tag_embed.asp)
* source tag
  - [Brief description from W3 Schools](https://www.w3schools.com/tags/tag_source.asp)
* track tag
  - [Brief description from W3 Schools](https://www.w3schools.com/tags/tag_track.asp)

### Forms

* [Changes to forms in HTML5 from MDN](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms)

### Details

* [How to Use the Details and Summary Elements](https://blog.teamtreehouse.com/use-details-summary-elements)
* [Details element polyfill](https://www.smashingmagazine.com/2014/11/complete-polyfill-html5-details-element/)

### Time

* [Time element guide](https://www.sitepoint.com/html5-time-element-guide/)

### WebVTT

* [First draft from W3C](http://www.w3.org/TR/2014/WD-webvtt1-20141113/)

### HTML Imports

* [Introduction to HTML imports](https://www.webcomponents.org/community/articles/introduction-to-html-imports)

## Development APIs

### Permissions

* [Permissions API for the Web by Google](https://developers.google.com/web/updates/2015/04/permissions-api-for-the-web)

### Geolocation

* [Using Geolocation](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API)
* [HTML5 Apps: Positioning with Geolocation](https://code.tutsplus.com/tutorials/html5-apps-positioning-with-geolocation--mobile-456)

### Cryptography

* [Web Cryptography API draft](http://www.w3.org/TR/WebCryptoAPI/)
* [Table of web cryptography support](http://diafygi.github.io/webcrypto-examples/)
* [Window.crypto](https://developer.mozilla.org/en-US/docs/Web/API/Window/crypto)
* [Cryptography next steps from W3C](http://www.w3.org/2012/webcrypto/webcrypto-next-workshop/report.html)

### File

* [Using files from web applications (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/File/Using_files_from_web_applications)
* [Reading local files in JavaScript](https://www.html5rocks.com/en/tutorials/file/dndfiles/)
* [File API Draft](https://w3c.github.io/FileAPI/)
* [File system API](http://www.w3.org/TR/file-system-api/)

### Frame timing

* [Video from google developers](https://www.youtube.com/watch?v=4zoC3eaa9z0)
* [Draft from W3C](https://w3c.github.io/frame-timing/)

### requestIdleCallback

* [On Google developers](https://developers.google.com/web/updates/2015/08/using-requestidlecallback)

### requestAnimationFrame

* [Using requestAnimationFrame (CSS Tricks)](https://css-tricks.com/using-requestanimationframe/)
* [Great article by Paul Irish](https://medium.com/@paul_irish/requestanimationframe-scheduling-for-nerds-9c57f7438ef4#.9gev5fdub)

### Web payments

* [Web payments API overview](https://developers.google.com/web/fundamentals/payments/)

## Semantics

* [Semantic elements from W3Schools](https://www.w3schools.com/html/html5_semantic_elements.asp)
* [Sections and Outlines of an HTML5 from MDN Document](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Using_HTML_sections_and_outlines)
* [HTML5 Semantics from Smashing Magazine](https://www.smashingmagazine.com/2011/11/html5-semantics/)
* [Lesser known semantics element from W3C & Opera](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Advanced_text_formatting)

## Accessibility

* [Excellent intro to accessibility from Google's fundamentals](https://developers.google.com/web/fundamentals/accessibility/)
* [Accessibility checklist for web developers](https://webaim.org/standards/wcag/checklist)
* [ARIA from MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)
* [Great Accessibility Style Guide](https://a11y-style-guide.com/style-guide/)
* [Designing for Cognitive Differences](https://alistapart.com/article/designing-for-cognitive-differences)
* [Guide on how HTML elements are supported by screen readers](https://thepaciellogroup.github.io/AT-browser-tests/)
* [Top 25 Accessibility Testing Tools for Website](https://dynomapper.com/blog/27-accessibility-testing/246-top-25-awesome-accessibility-testing-tools-for-websites)
* [Web Accessibility Evaluation Tools List from W3](http://www.w3.org/WAI/ER/tools/)
* [Pa11y - automated accessibility testing](http://pa11y.org/)
* [Aria in HTML](https://developer.paciellogroup.com/blog/2014/10/aria-in-html-there-goes-the-neighborhood/)
* [Accessible and Responsive HTML5 Video Player](https://2017.ind.ie/blog/accessible-video-player/)

## DOM Management

### Shadow DOM

* [Shadow DOM v1: self-contained web components](https://developers.google.com/web/fundamentals/web-components/shadowdom)
* [What's New in Shadow DOM v1 (by examples)](https://hayato.io/2016/shadowdomv1/)

### Data Binding

* [Data-binding Revolutions with Object.observe()](https://www.html5rocks.com/en/tutorials/es7/observe/)

### Web Components

* [Custom elements v1: reusable web components](https://developers.google.com/web/fundamentals/web-components/customelements)
* [The power of web components](https://hacks.mozilla.org/2018/11/the-power-of-web-components/)
* [Polymer project](https://github.com/polymer)
* [A Quick Introduction To Polymer](https://www.webcomponents.org/community/articles/a-quick-polymer-introduction)
* [Building web components using Polymer and ES6 classes](https://www.polymer-project.org/blog/es6)
* [Demythstifying Web Components](http://www.backalleycoder.com/2016/08/26/demythstifying-web-components/)
* [HTML imports](https://www.html5rocks.com/en/tutorials/webcomponents/imports/)
* [Building Webapps with Yeoman and Polymer](https://www.html5rocks.com/en/tutorials/webcomponents/yeoman/)

## Progressive web apps

* [Intro to PWAs](https://developers.google.com/web/progressive-web-apps/)
* [An Extensive Guide To Progressive Web Applications](https://www.smashingmagazine.com/2018/11/guide-pwa-progressive-web-applications/)
* [The Business Case for Progressive Web Apps](https://cloudfour.com/thinks/the-business-case-for-progressive-web-apps/)

### Service Workers

* [Service Worker fundamentals](https://developers.google.com/web/fundamentals/primers/service-workers/)
* [ServiceWorkies - Learn SWs playing a game](https://serviceworkies.com/)
* [The Service Worker Cookbook](https://serviceworke.rs/)
* [Offline content with service workers](https://www.madebymike.com.au/writing/service-workers/)
* [Making a Service Worker: a case study (Smashing Magazine)](https://www.smashingmagazine.com/2016/02/making-a-service-worker/)
* [Service workers explained](https://github.com/w3c/ServiceWorker/blob/master/explainer.md)
* [Service Worker Libraries, Totally Tooling Tips](https://www.youtube.com/watch?v=IIRj8DftkqE)
* [ServiceWorker: Revolution of the Web Platform](https://ponyfoo.com/articles/serviceworker-revolution)

### Offline caching

* [The Offline Cookbook](https://developers.google.com/web/fundamentals/instant-and-offline/offline-cookbook/)
* [Instant-loading Offline-first (Progressive Web App Summit 2016)](https://www.youtube.com/watch?v=qDJAz3IIq18)
* [Offline Storage for Progressive Web Apps (article by Addy Osmani)](https://medium.com/dev-channel/offline-storage-for-progressive-web-apps-70d52695513c#.jsbxgywzz)
* [A Beginner's Guide to Using the Application Cache](https://www.html5rocks.com/en/tutorials/appcache/beginner/)

### Push Notifications

* [Web Push Notifications (Google's Web fundamentals)](https://developers.google.com/web/fundamentals/push-notifications/)
* [Push API W3C draft](http://w3c.github.io/push-api/)
* [Notifications API spec](https://notifications.spec.whatwg.org/)

## Client side storage

* [Client-Side Storage](https://www.html5rocks.com/en/tutorials/offline/storage/)
* [Offline Cookbook](https://jakearchibald.com/2014/offline-cookbook/)
* [Introduction to IndexedDB](https://www.codemag.com/Article/1411041)
* [Real-World Off-Line Data Storage](https://code.tutsplus.com/tutorials/real-world-off-line-data-storage--net-34063)
* [Local storage tutorial](https://developer.mozilla.org/en-US/docs/Archive/Add-ons/Overlay_Extensions/XUL_School/Local_Storage)

## Performance

* [Accelerated Mobile Pages (AMP)](https://www.ampproject.org/learn/overview/)
* [Google developers best practices](https://developers.google.com/speed/docs/insights/rules)
* [Optimizing performance from Google Web Fundamentals](https://developers.google.com/web/fundamentals/performance/why-performance-matters/)
* [Resource hints draft (preconnect and preload)](http://www.w3.org/TR/2014/WD-resource-hints-20141021/)
* [Prefetching and prerendeding](https://medium.com/@luisvieira_gmr/html5-prefetch-1e54f6dda15d)
* [Image compression](https://www.html5rocks.com/en/tutorials/speed/img-compression/)
* [Text compression](https://www.html5rocks.com/en/tutorials/speed/txt-compression/)
* [Resource timing spec](http://www.w3.org/TR/resource-timing/)

## Mobile

* [The Web App Manifest (Google's fundamentals)](https://developers.google.com/web/fundamentals/web-app-manifest/)
* [Field guide to web applications](https://www.html5rocks.com/webappfieldguide/toc/index/)
* [Apache Cordova tutorial](http://ccoenraets.github.io/cordova-tutorial/)
* [PhoneGap from Scratch](https://code.tutsplus.com/tutorials/phonegap-from-scratch-introduction--mobile-9171)
* [Best practices for mobile web apps](https://www.html5rocks.com/en/tutorials/speed/quick/)
* [Build mobile apps with Kendo UI]https://docs.telerik.com/kendo-ui/controls/hybrid/introduction)
* [HTML5 Vibration API](https://code.tutsplus.com/tutorials/html5-vibration-api--mobile-22585)
* [HTML5 Battery Status API](https://code.tutsplus.com/tutorials/html5-battery-status-api--mobile-22795)
* [Privacy analysis of the HTML5 Battery Status API](https://eprint.iacr.org/2015/616.pdf)
* [HTML5 Network Information API](https://code.tutsplus.com/tutorials/html5-network-information-api--cms-21598)
* [Sencha Touch tutorials](https://docs.sencha.com/)

## Communications and interoperability

### Web Sockets

* [Introducing Websockets](https://www.html5rocks.com/en/tutorials/websockets/basics/)

### WebRTC

* [What is WebRTC and how does it work](https://www.innoarchitech.com/what-is-webrtc-and-how-does-it-work/)
* [WebRTC made simple](https://blog.carbonfive.com/2014/10/16/webrtc-made-simple/)
* [WebRTC data channels tutorial](https://www.html5rocks.com/en/tutorials/webrtc/datachannels/)
* [WebRTC data channels from MDN](https://developer.mozilla.org/en-US/docs/Games/Techniques/WebRTC_data_channels)

## Web Workers

* [Web Worker Basics](https://www.html5rocks.com/en/tutorials/workers/basics/)
* [How fast are web workers?](https://hacks.mozilla.org/2015/07/how-fast-are-web-workers/)
* [Web Workers in MDN](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers)
* [Getting started with Web Workers](https://code.tutsplus.com/tutorials/getting-started-with-web-workers--net-27667)

## WebGL

* [WebGL Fundamentals](https://www.html5rocks.com/en/tutorials/webgl/webgl_fundamentals/)

## Browser compatibility

* [I want to use](http://www.iwanttouse.com/)
* [Can I use...](https://caniuse.com/)
* [W3C quality tools](http://w3c.github.io/developers/tools/)
* [HTML5 test](http://beta.html5test.com/)
* [HTML5 demos](https://bestvpn.org/html5demos/)

## Books

* [Dive Into HTML5](http://diveinto.html5doctor.com/)
* [HTML5: Up and Running](https://www.amazon.com/HTML5-Running-Dive-Future-Development/dp/0596806027)
* [Using the HTML5 Filesystem API](http://shop.oreilly.com/product/0636920021360.do)
* [HTML5 Game Development Insights](https://www.apress.com/us/book/9781430266976)
* [Web Design Playground: HTML & CSS The Interactive Way](https://www.manning.com/books/web-design-playground)

## Game development

* [Getting started with HTML5 Game Development from Mozilla Hacks](https://hacks.mozilla.org/2013/09/getting-started-with-html5-game-development/)
* [HTML 5 game development video series by Mozilla](https://hacks.mozilla.org/2016/02/html-5-game-development-video-series/)
* [Info, news and tutorials](http://html5gamedevelopment.com/)
* [Over 380 resources on HTML5 game development](https://html5-game-development.zeef.com/andre.antonio.schmitz)
* Opensource JavaScript game engines
  - [Pixi.js](https://github.com/pixijs/pixi.js)
  - [phaser](https://github.com/photonstorm/phaser)
  - [MelonJS](https://github.com/melonjs/melonJS)
  - [kiwi.js](https://github.com/gamelab/kiwi.js)
  - [Crafty](https://github.com/craftyjs/Crafty)
  - [PhysicsJS](https://github.com/wellcaffeinated/PhysicsJS)
  - [Stage.js](https://github.com/shakiba/stage.js)
  - [cocos2d](https://github.com/cocos2d/cocos2d-html5)

## Videos and Keynotes

* [HTML5 Developer Conference](https://html5devconf.com/videos.html)
* [Polymer: declarative, encapsulated, reusable components](https://www.youtube.com/watch?v=DH1vTVkqCDQ)
* [Making the mobile web fast, feature-rich, and beautiful](https://www.youtube.com/watch?v=EXjPsvwIDwU)
* [Dart: HTML of the Future, Today!](https://www.youtube.com/watch?v=euCNWhs7ivQ)

## Websites and resources

### Websites

* [HTML official reference](https://webplatform.github.io/docs/Main_Page/index.html) (allows collaborative modification of content like wiki)
* [HTML5 Rocks](https://www.html5rocks.com/en/) (news, tutorials and updates)
* [HTML5 Gallery](http://html5gallery.com/) (a showcase of sites using HTML5 markup and API's)
* [HTML5 development guide from MDN](https://developer.mozilla.org/en-US/docs/Learn/HTML)
* [W3C Highlights form June 2014](http://www.w3.org/2014/06/w3c-highlights/)
* [HTML5 Please](https://html5please.com/) (Know when HTML5 feature are ready to use)
* [Keen HTML](https://keenhtml.com) (Free interactive lessons to learn HTML)

### Weekly news

* [HTML5 Weekly](https://frontendfoc.us/)
* [Mozilla Hacks Weekly Articles](https://hacks.mozilla.org/category/mozilla-hacks-weekly/)
* [Responsive Design Newsletter](http://responsivedesignweekly.com/)

### Twitter

* [@html5](https://twitter.com/html5)
* [@html5rock](https://twitter.com/html5rock)
* [@html5gallery](https://twitter.com/html5gallery)
* [@html5doctor](https://twitter.com/html5doctor)
* [@GameDevHTML5](https://twitter.com/GameDevHTML5)
* [@mozhacks](https://twitter.com/mozhacks)
* [@googlechrome](https://twitter.com/googlechrome)

## Other awesome lists

* [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness)
* [lists](https://github.com/jnv/lists)
* [Community Curated Resources](https://hackr.io/tutorials/learn-html-5)

## Contributing

Your contributions are always welcome!
