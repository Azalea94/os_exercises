# 操作系统概述思考题

## 个人思考题

---

分析你所认识的操作系统（Windows、Linux、FreeBSD、Android、iOS）所具有的独特和共性的功能？
- [x]  

>  
>共性功能：
>>操作系统的功能包括管理计算机系统的硬件、软件及数据资源；控制程序运行；改善人机界面；为其它应用软件提供支持等，使计算机系统所有资源最大限度地发挥作用，为用户提供方便的、有效的、友善的服务界面。
>
>特性：
 >> 1）windows：图形界面非常友好，易于使用；
 >
  >>2）Linux：源代码公开的自由及开放源码，可以自由传播；
  >
  >>3）FreeBSD：高性能和高可靠性；
  >
  >>4）Android：主要用于手机、平板等便携设备，与IOS相比，具有全开放性和以及丰富廉价的应用资源；
  >
  >>5）IOS：流畅简单的操作体验、精美的用户界面、丰富的应用程序以及较高的安全性，是一个商业系统。
  

请总结你认为操作系统应该具有的特征有什么？并对其特征进行简要阐述。
- [x]  

>   应具有的基本特征有4个：
  >>1）并发性
  >
   >>此特征是指可以处理在同一时间间隔内发生的两个或多个事件：对于单处理机，用微观上分时交替处理实现，对于多处理机，可分配到每个处理机上进行同时执行。
   >
   >>这一特征有效地改善了系统资源的利用率和提高了系统的吞吐量，但它使系统复杂化，操作系统必须具有控制和管理各种并发活动的能力
   >
  >>2）共享 
  >
   >>此特征是指在操作系统环境下，系统中的资源可供内存中多个并发执行的进程(线程)共同使用。
   >
   >>由于资源属性的不同，进程对资源共享的方式也不同，主要有两种：互斥共享方式和同时访问方式。
   >
   >>并发和共享是操作系统两个最基本的特征，这两者之间又是互为存在条件的。
   >
  >>3）虚拟
  >
   >>此特征是指操作系统通过某种技术将一个物理实体（实际存在的）变为若干个逻辑上的对应物（用户感觉到的），比如xunit处理机、xunit内存等的实现。
   >
  >>4）异步性
  >
  >>由于资源的限制和程序的并发，每个程序在何时执行，多个程序间的执行顺序以及完成每道程序所需的时间都是不确定的，因而也是不可预知的。

请给出你觉得的更准确的操作系统的定义？
- [x]  

> 操作系统是一段管理计算机硬件与软件资源的计算机程序，保证计算机程序运行的提供基本的服务和环境，任何其他软件都必须在操作系统的支持下才能运行。从层次结构上说，操作系统是用户和计算机的接口，也是计算机硬件和软件的接口。

你希望从操作系统课学到什么知识？
- [x]  

> 理论上：操作系统的基本功能的实现方式和原理，如何利用操作系统知识提高自己的计算机应用能力；
>
  实践上：通过认真完成实验对操作系统的实现有更深刻的了解和体会，提高实践能力。

---

## 小组讨论题

---

目前的台式PC机标准配置和价格？
- [x]  

> 不同的品牌型号有不同的价格，相应也有不同的性能。下面的一个例子是大众都能接受的三四千的价位：
>
>1.CPU ：AMD速龙II X4 641（盒）              ¥425
>
>2.主板：翔升A75T-S                          ¥379
>
3.内存：威刚8GB DDR3 1600G（游戏威龙双通道）¥259
>
4.硬盘：希捷Barracuda 1TB 7200转 64MB 单碟  ¥540
>
5.显卡：精影HD5850 1G精镭版                 ¥698
>
6.机箱：先马刺客                            ¥199
>
7.显示器：现代N231                          ¥809
>
8.键鼠装：义宏KM-7200键鼠套装               ¥29
>
9.光驱：先锋BDC-207BK                       ¥299

你理解的命令行接口和GUI接口具有哪些共性和不同的特征？
- [x]  

> 共性：
>
>> 都是为用户提供的调用操作系统功能、请求操作系统为其服务的手段，是用不同形式表现的命令接口。
>
> 不同：
>> 命令行：具有规定的词法、语法和语义，以命令为基本单位； 不支持鼠标，通过键盘输入指令； 需要用户记忆操作的命令；
>
>>但好处是节约计算机系统的资源；同时对于有经验的用户，更加方便快捷；同时，支持批处理命令，可以高效、正确地处理命令。
>>
>>GUI : 具有图形化的操作界面，对于用户来说更加直观和形象；通过事件驱动的控制方式，即用户通过动作产生事件以驱动程序工作；
>
>> 但GUI也有其缺点，比如对于多客户端计算机，或者是全天运作的服务器计算机，图形化操作方式有时会力有未逮。需要不断增强命令行界面的脚本语言和宏语言来提供丰富的控制与自动化的系统管理能力。

为什么现在的操作系统基本上用C语言来实现？
- [x]  

>  原因主要有：
>
>>从历史角度说，现在常见的操作系统内核主要有Linux, Unix, Darwin（Mac OSX的内核）以及NT(windows的内核)。Linux, Unix, Darwin本质上都是unix/类unix操作系统，而Unix操作系统的实现语言就是C语言（以及汇编）实现的，所以从效率上讲没必要用另一种新的语言重写。
>
>>从开发角度说，C语言具有开发成本低、工具齐全的巨大优势:目前所有的语言的开发环境里，C语言能做到编译成不依赖操作系统的形式二进制代码，C语言的各种脱离系统的库最丰富，最完整，C语言用来开发操作系统的工具最多,C 语言可以进行方便的内存管理，生成代码尺寸可控。

为什么没有人用python，java来实现操作系统？
- [x]  

>  因为编程语言只是工具，java和python也可以实现操作系统，但是因为其本身的限制因素，其作为工具要付出的成本太大了。比如说，操作系统一个很重要的功能是进行内存管理，Java, Python之类的不能直接操纵内存的语言要做内存管理是很困难的事情，所以如果用java或者python实现会相当麻烦且笨拙，效率不高，相比之下，C语言的优势是非常明显的（见上一题），所以基本上不用python和java实现操作系统。

请评价用C++来实现操作系统的利弊？
- [x]  

>  C++对于操作系统的内核开发有一定的优点：
>
>>1）C++的template模板功能可以方便的实现高效率的代码重用。
>
>>2) 操作系统的内核部分有一部分工作实际上是面向对象的，而C++本身就是一种面向对象的语言。
>
>>3) C++ 编译器执行的某些规则比标准 C 编译器更加严格，而且提供一些能够在驱动程序上下文中安全使用的附加特性
>
> 同时C++开发OS存在的缺点有：
>
>>1)代码分页问题：C++ 编译器为非 POD 类和模板生成代码的方式使得很难确定执行一个函数所需的所有代码的去向，因此很难将代码安全地分页。
>
>>2)堆栈：由于C++具有额外的机制通常会导致更多的函数调用，所以 C++ 使用的堆栈总数常常会比C更多,而堆栈空间往往是有限的。
>
>>3)动态内存：C++中如new 和delete函数的调用会影响内存跟踪工具检测驱动程序代码中的内存泄漏和其他问题的能力。
>
>>4)库：不是所有的库函数都可以在内核模式下使用，且导出的 C++ 函数的名称可能因版本不同而异；
>
>>5）编译器：C++版本引发的不兼容问题。

---

## 开放思考题

---

请评价微内核、单体内核、外核（exo-kernel）架构的操作系统的利弊？
- [x]  

>  1） 微内核：
>
>>优点：
>  
>>1.提高可扩展性：因为微内核OS许多功能是由相对独立的服务器软件实现的，大大改善了系统的灵活性。
>
>>2.增强可靠性：微内核是经过严格测试的，同时提供了规范精简的API；同时，服务器出现错误时不会影响内核和其他服务器.
>
>>3. 增强可移植性：微内核OS中绝大部分（各种服务器）与硬件平台无关。
>
>>4. 提供了对分布式系统的支持.
>
>>5. 融入了面向对象技术。
>
>>缺点：
>
>>主要是运行效率较低，因为在微内核OS中完成一次服务请求会引起比其他OS更多的上下文切换。
>
>  2） 单体内核：
>
>>优点：操作系统内的各软件组件因具有高度紧密性，如此在系统的低级运作上将格外有效率。
>
>>缺点：其操作系统的代码依然是高度紧密的，很难修改成其他类型的操作系统架构。此外，所有的模块也都在同一块寻址空间内运行，倘若某个模块有错误、瑕疵（Bug），运行时就会损及整个操作系统运作。
>
>  3)外核：
>
>>优点：实现了应用级资源管理，由应用程序而不是操作系统管理硬件资源。
>
>>另外，外核将资源保护及其管理分割开来。由于进程间通信、虚拟内存管理等传统概念都是在应用层实现的，所以可以很容易对他们进行扩展、专业化和替换。



请评价用LISP,OCcaml, GO, D，RUST等实现操作系统的利弊？
- [x]  

>  这些语言实现操作系统，优点：可以利用语言各自的特点，比如lips良好的交互性、GO天然的并发性等； 但也存在缺点：效率低下；另外由于实现的底层操作系统，很多库函数可能无法使用，也可能会导致一定的安全隐患。

进程切换的可能实现思路？
- [x]  

>  先触发中断，然后保存当前进程的数据到堆栈中，之后进行另一个进程的处理，当需要返回的时候恢复保存过的数据即可。

计算机与终端间通过串口通信的可能实现思路？
- [x]  

>  串口按位发送和接收字节，同时进行串->并的转换。另外为了保证不出错，可能还要加上校验的操作。

为什么微软的Windows没有在手机终端领域取得领先地位？
- [x]  

>  1.APP应用匮乏、明星机型短缺以及和Windows Mobile应用断层等因素，一直难以在市场上打开有效缺口;
2.微软的移动终端战略很模糊：微软在移动领域的品牌变化过多次，从最早的Windows Mobile再到Windows Phone，最终又回归Windows。这样造成时机的贻误和竞争对手的领先。
3.竞争对手的压制：iPhone横空出世和Android大行其道。微软的中心一直在功能，而iPhone出世后用户思路更趋向于体验大于功能。


你认为未来（10年内）的操作系统应该具有什么样的特征和功能？
- [x]  

>  轻捷；可移植性好；或许可以更方便地增加用户的个人特征。

---
