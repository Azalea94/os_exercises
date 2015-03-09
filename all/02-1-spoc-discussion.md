#lec 3 SPOC Discussion

## 第三讲 启动、中断、异常和系统调用-思考题

## 3.1 BIOS
 1. 比较UEFI和BIOS的区别。
 
 >
UEFI，全称Unified Extensible Firmware Interface，即“统一的可扩展固件接口”，是一种详细描述全新类型接口的标准，这种接口用于操作系统自动从预启动的操作环境，加载到一种操作系统上，UEFI抛去了传统BIOS需要长时间自检的问题，让硬件初始化以及引导系统变得简洁快速.主要带来的便利有：
>
>1）UEFI已具备文件系统的支持，它能够直接读取FAT分区中的文件,同时，可直接在其中运行的应用程序。
>
>2）不再需要主引导记录，不再需要活动分区，不需要任何工具，只要复制安装文件到一个FAT32（主）分区/U盘中，然后从这个分区/U盘启动
>
>3)UEFI是用模块化、C语言风格的参数堆栈传递方式、动态链接的形式构建系统，它比BIOS更易于实现，容错和纠错特性也更强，从而缩短了系统研发的时间。
>

 2. 描述PXE的大致启动流程。
 >
 PXE即 “preboot execute environment”,工作于Client/Server的网络模式，支持工作站通过网络从远端服务器下载映像，并由此支持通过网络启动操作系统。在启动过程中，终端要求服务器分配IP地址，再用TFTP（trivial file transfer protocol）或MTFTP(multicast trivial file transfer protocol)协议下载一个启动软件包到本机内存中执行，由这个启动软件包完成终端基本软件设置，从而引导预先安装在服务器中的终端操作系统。
>



## 3.2 系统启动流程
 1. 了解NTLDR的启动流程。
>
> NTLDR启动流程：
1、电源自检程序开始运行
2、主引导记录被装入内存，并且程序开始执行
3、活动分区的引导扇区被装入内存
4、NTLDR从引导扇区被装入并初始化
5、将处理器的实模式改为32位平滑内存模式
6、NTLDR开始运行适当的小文件系统驱动程序。
7、NTLDR读boot.ini文件
8、NTLDR装载所选操作系统
如果windows NT/windows 2000/windows XP/windows server 2003这些操作系统被选择，NTLDR运行Ntdetect。
对于其他的操作系统，NTLDR装载并运行Bootsect.dos然后向它传递控制。
windows NT过程结束。
9.Ntdetect搜索计算机硬件并将列表传送给NTLDR，以便将这些信息写进\\HKE Y_LOCAL_MACHINE\HARDWARE中。
10.然后NTLDR装载Ntoskrnl.exe，Hal.dll和系统信息集合。
11.Ntldr搜索系统信息集合，并装载设备驱动配置以便设备在启动时开始工作
12.Ntldr把控制权交给Ntoskrnl.exe，这时,启动程序结束,装载阶段开始


 2. 了解GRUB的启动流程。
  >
> grub启动过程中用到几个重要的文件,stage1,stage2,有的时候需要stage1.5.这些文件一般都在/boot/grub文件夹下面.grub被载入通常包括以下几个步骤:
    1. 装载基本的引导装载程序(stage1),stage1通常位于主引导扇区里面,对于硬盘就是MBR了,stage1的   主要功能就是装载第二引导程序(stage2).这主要是归结于在主引导扇区中没有足够的空间用于其他东西。
    2. 装载第二引导装载程序(stage2),这第二引导装载程序实际上是引出更高级的功能,　
     以允许用户装载入一个特定的操作系统。在GRUB中，这步是让用户显示一个菜单或
     是输入命令。由于stage2很大,所以它一般位于文件系统之中(通常是boot所在的根
     分区).
    3.stage1.5和文件系统有关系: 有时候基本引导装载程序(stage1)不能识别stage2所在的文件系统分区,那么这
    时候就需要stage1.5来连接stage1和stage2了.

 3. 比较NTLDR和GRUB的功能有差异。
 
 4. 了解u-boot的功能。
 >
>uboot就是一个复杂的bootloader程序。它支持嵌入式操作系统的引导(NetBSD, VxWorks, QNX, RTEMS, ARTOS, LynxOS, android,linux等）和 嵌入式处理器。
>
>主要功能：u-boot启动内核的过程主要分两个阶段，两个阶段的功能分别如下：
>
>1)第一阶段：
>
>> 硬件设备初始化 - 加载u-boot第二阶段代码到ram空间 - 设置栈 - 跳转到第二阶段入口
>
>2)第二阶段：
>
>> 初始化本阶段使用过的硬件设备 - 检测系统内存映射 - 将内核从Flash读到ram - 为内核设置启动参数 - 调用内核


## 3.3 中断、异常和系统调用比较
 1. 举例说明Linux中有哪些中断，哪些异常？
 ----
中断是由硬件产生的异步中断，比如键盘中断；
>
>异常是处理器产生的同步中断，比如系统调用。

 2. Linux的系统调用有哪些？大致的功能分类有哪些？  (w2l1)

---
>
>linux 系统调用传统意义上有二百多个，但以C语言库函数的形式实现的系统调用更多，且因为Linux版本不同数量也会有差异，但基础的类型变化不大，比如write、read的文件读写操作；fork、clone等进程管理；getpriority等读取内核数据操作。从功能上分类，主要有：
>
>1）进程控制（fork，exit） 2）文件系统与文件操作（open，create，close） 3）内存管理（brk，sync） 4）系统控制（time, sysinfo) 5）网络管理(getdomainname,gethostname) 6）用户管理(getuid, setuid) 7）进程间通讯(ipc)
```
  + 采分点：说明了Linux的大致数量（上百个），说明了Linux系统调用的主要分类（文件操作，进程管理，内存管理等）
  - 答案没有涉及上述两个要点；（0分）
  - 答案对上述两个要点中的某一个要点进行了正确阐述（1分）
  - 答案对上述两个要点进行了正确阐述（2分）
  - 答案除了对上述两个要点都进行了正确阐述外，还进行了扩展和更丰富的说明（3分）
 ```
 
 3. 以ucore lab8的answer为例，uCore的系统调用有哪些？大致的功能分类有哪些？(w2l1)
 ---
>
>lab8有22个系统调用，主要分类有：
>
>> 1. 文件操作（sys_read,sys_write等)；
>> 2. 进程管理（sys_exit, sys_wait,sys_lab6_set_priority等）；
>> 3. 文件系统操作 （sys_fstat等）；
>> 4. 系统控制 （sys_gettime等）；
 ```
  + 采分点：说明了ucore的大致数量（二十几个），说明了ucore系统调用的主要分类（文件操作，进程管理，内存管理等）
  - 答案没有涉及上述两个要点；（0分）
  - 答案对上述两个要点中的某一个要点进行了正确阐述（1分）
  - 答案对上述两个要点进行了正确阐述（2分）
  - 答案除了对上述两个要点都进行了正确阐述外，还进行了扩展和更丰富的说明（3分）
 ```
 
## 3.4 linux系统调用分析
 1. 通过分析[lab1_ex0](https://github.com/chyyuu/ucore_lab/blob/master/related_info/lab1/lab1-ex0.md)了解Linux应用的系统调用编写和含义。(w2l1)
 
---
“file lab1-ex0.exe " 输出信息为 " ELF 64-bit LSB  executable, x86-64, version 1(SYSV),dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID..., not stripped"
>
>说明 此文件是个可执行文件（executable），为 x86-64 平台编译，保存为 ELF(Executable and Linking Format) 文件格式，并且包含着符号表（not stripped）。
>
>objdump 可以显示更多二进制文件的信息。比如 "objdump -hrt lab1-ex0.exe"
可以显示出Sections（段的信息），可以看到有30个sections，例如其中 .text: 这是编译生成的可执行代码。
>
>还可以显示了一个符号表（symbol table).
>
>nm指令可以显示目标文件的符号清单，"nm lab1-ex0.exe" 输出信息可以看到此执行文件用到的符号：
除了看到'd'类型的hello 和 'D'的main， 还有很多'a'类型的 系统调用的符号 如：STDOUT，SYS_close等。
>
>通过分析可以得到，此程序在实现系统调用时，首先将系统调用号（SYS_write）放到eax寄存器中，然后将参数放到ebx，ecx中，之后以int中断形式执行，最后返回ret.

 ```
  + 采分点：说明了objdump，nm，file的大致用途，说明了系统调用的具体含义
  - 答案没有涉及上述两个要点；（0分）
  - 答案对上述两个要点中的某一个要点进行了正确阐述（1分）
  - 答案对上述两个要点进行了正确阐述（2分）
  - 答案除了对上述两个要点都进行了正确阐述外，还进行了扩展和更丰富的说明（3分）
 
 ```
 
 2. 通过调试[lab1_ex1](https://github.com/chyyuu/ucore_lab/blob/master/related_info/lab1/lab1-ex1.md)了解Linux应用的系统调用执行过程。(w2l1)

 ---
>
>实际上使用 strace可以清楚的看到执行过程中对系统函数的调用过程。 输入"strace ./lab1-ex1.exe"可以看到：
>
>首先是brk 和 mmap2等进行动态加载的分配空间和检查（access);
>
>然后是搜索检查标准库（open read fstat);
>
>接着是标准库加载并初始化（mmap,arch_prctl,mprotect)
>
>最后执行write函数并退出。

 ```
  + 采分点：说明了strace的大致用途，说明了系统调用的具体执行过程（包括应用，CPU硬件，操作系统的执行过程）
  - 答案没有涉及上述两个要点；（0分）
  - 答案对上述两个要点中的某一个要点进行了正确阐述（1分）
  - 答案对上述两个要点进行了正确阐述（2分）
  - 答案除了对上述两个要点都进行了正确阐述外，还进行了扩展和更丰富的说明（3分）
 ```
 
## 3.5 ucore系统调用分析
 1. ucore的系统调用中参数传递代码分析。
 1. ucore的系统调用中返回结果的传递代码分析。
 1. 以ucore lab8的answer为例，分析ucore 应用的系统调用编写和含义。
 1. 以ucore lab8的answer为例，尝试修改并运行代码，分析ucore应用的系统调用执行过程。
 
## 3.6 请分析函数调用和系统调用的区别
 1. 请从代码编写和执行过程来说明。
   1. 说明`int`、`iret`、`call`和`ret`的指令准确功能
 ---

 >
>int :产生需要马上处理的中断信息,引发中断过程.
>
>iret :从中断中恢复中断前的状态,中断服务程序的最后一条指令。IRET指令将推入堆栈的段地址和偏移地址弹出，使程序返回到原来发生中断的地方。
>
>call: 进行跳转，跳转之前保存返回地址（下一条指令的地址），以便在跳转目标代码
>
>ret: 子程序的返回，当前堆栈指针减2,返回之前的指令地址。
>
int iret 用于系统调用 ，堆栈切换和特权级的转换
call和ret 常规调用 ，没有堆栈切换
 
