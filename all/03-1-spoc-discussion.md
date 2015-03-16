# lec5 SPOC思考题


NOTICE
- 有"w3l1"标记的题是助教要提交到学堂在线上的。
- 有"w3l1"和"spoc"标记的题是要求拿清华学分的同学要在实体课上完成，并按时提交到学生对应的git repo上。
- 有"hard"标记的题有一定难度，鼓励实现。
- 有"easy"标记的题很容易实现，鼓励实现。
- 有"midd"标记的题是一般水平，鼓励实现。


## 个人思考题
---

请简要分析最优匹配，最差匹配，最先匹配，buddy systemm分配算法的优势和劣势，并尝试提出一种更有效的连续内存分配算法 (w3l1)
```
  + 采分点：说明四种算法的优点和缺点
  - 答案没有涉及如下3点；（0分）
  - 正确描述了二种分配算法的优势和劣势（1分）
  - 正确描述了四种分配算法的优势和劣势（2分）
  - 除上述两点外，进一步描述了一种更有效的分配算法（3分）
 ```
- [x]  

> 最先匹配：
-  优点：
>       * 简单
>       * 在高地址空间有大块的空闲分区
-   缺点：
>       * 会产生外部碎片
>       * 分配大块的时候较慢
>
> 最佳匹配：
-   优点：
>       条件：大部分分配的尺寸比较小的时候效果很好
>       * 可避免大的空闲分区被拆分
>       * 可减小外部碎片的大小
>       * 相对简单
-   缺点：
>       * 产生外部碎片
>       * 释放分区较慢，因为空闲分区是按照大小排列的，
>       需要查找并且合并临近的空闲分区
>       * 容易产生很多无用的小碎片
>
> 最差匹配：
-   优点：
>       * 条件：中等大小的分配较多的时候，效果最好
>       * 避免出现太多的小碎片（用的那块占用的不很大，剩下的空闲空间也可以
>       使用）
-   缺点：
>       * 释放分区比较慢
>       * 外部碎片
>       * 容易破坏大的空闲分区，因此后续难以分配大的分区
>
> buddy system
-   优点：
>       * 实现简单，分配和回收速度快。当一个大小为2K字节的块释放后，存储管理只需要搜索2K字节大小的块以判定是否需要合并。而那些允许以任意形式分割内存的策略的算法需要搜索整个空闲块表。
>       * 为动态分配和释放
-   缺点：
>       * 需要维护一个数据结构来记录使用情况，维护成本较大
>       * 都是2的幂次，分配时造成一定的浪费。比如原来是1024个块，申请了16个块，再申请600个块就申请不到了，因为已经被分割了。
>       * 一个很小的块往往会阻碍一个大块的合并，一个系统中，对内存块的分配，大小是随机的，一片内存中仅一个小的内存块没有释放，旁边两个大的就不能合并。
>       
> 更有效的分配方法：系统建立一个常用长度空闲区链表，链表表项分别指向对应长度的空闲区链表表头，查找时取相应长度的空闲区链表的第一项存放。




## 小组思考题

请参考ucore lab2代码，采用`struct pmm_manager` 根据你的`学号 mod 4`的结果值，选择四种（0:最优匹配，1:最差匹配，2:最先匹配，3:buddy systemm）分配算法中的一种，在应用程序层面来实现，并给出测试用例。 (spoc)

--- 
> C++ 实现：

```
#include <stdio.h>
#include <malloc.h>
#include <iostream>
using namespace std;
typedef struct node
{
    char* address;
    int size;
    struct node *next;
}node;

class bestmanage
{
private:
    char mem[1024];
    node * head= NULL;
    node freelist;
public:
    bestmanage()
    {
        head = new node;
        head->address = mem;
        head->size = 1024;
        head->next = NULL;
        freelist.next = head;
    }
    ~bestmanage(){};
    
    char* mng_malloc(int size)
    {
        cout<<"malloc! ths size is "<<size<<endl;
        size = size + sizeof(long long);
        int min = 1024;
        node* result = NULL;
        node* pre_result = NULL;
        node* pre = NULL;
        node*temp = freelist.next;
        while (temp!=NULL)
        {
            if (temp->size>=size && (temp->size-size<min))
            {
                min = temp->size-size;
                pre_result = pre;
                result = temp;
            }
            pre = temp;
            temp= temp->next;
        }
        if (result==NULL) 
        {cout<<"the memory is not fit for this operation :( "<<endl;return NULL;}

        char *address = result->address;
        if (    result->size == size)
        {
            pre_result = result->next;
            free(result);
        }
        else
        {
            result->size=result->size-size;
            result->address = result->address+size;
        }
        *(int *)address = size;
        address = address + sizeof(long long);
        cout<<"Malloc succeed :) "<<endl;
        return address;
    }
    void mng_merge()
    {
        node *temp = freelist.next;
        if (temp==NULL) return;
        node *pre = temp;
        temp = temp->next;
        while (temp!=NULL)
        {
            if ((long long)pre->address+pre->size==(long long)temp->address)
            {
                pre->size=pre->size+temp->size;
                pre->next = temp->next;
                free(temp);
                temp = pre->next;
            }
            else
            {
                pre=temp;
                temp=temp->next;
            }
        }
    }
    void mng_free(char*address)
    {
        int size = *(int *)(address-sizeof(long long));
        cout<<"free address "<<(long long)address-sizeof(long long)<<" size: "<<size<<endl;
        node *newnode = new node;
        newnode->address =address-sizeof(long long);
        newnode->next = NULL;
        newnode->size = size;
        node *temp = freelist.next;
        node *pre = &freelist;
        while (temp!=NULL)
        {
            if ((long long)temp->address>=(long long)address)
            {
                pre->next = newnode;
                newnode->next = temp;
                break;
            }
            pre = temp;
            temp= temp->next;
        }
        mng_merge();
    }
    void print()
    {
        cout<<"---------freelist info---------"<<endl;
        node *temp = freelist.next;
        int n=0;
        while (temp!=NULL)
        {
            n++;
            cout<<"node("<<n<<")  address: "<<(long long)temp->address<<" size:"<<temp->size<<endl;
            temp=temp->next;
        }
        cout<<"--------------end---------------"<<endl;
        cout<<endl;
    }
};

int main()
{
    bestmanage mng;
    char *m1 = mng.mng_malloc(20);
    char *m2 = mng.mng_malloc(200);
    char *m3 = mng.mng_malloc(600);
    mng.print();
    mng.mng_free(m2);
    mng.mng_free(m1);
    mng.print();
    char *m4 = mng.mng_malloc(210);
    mng.print();
    mng.mng_free(m3);
    mng.mng_free(m4);
    mng.print();
}
```
>运行结果：
```
malloc! ths size is 20
Malloc succeed :)
malloc! ths size is 200
Malloc succeed :)
malloc! ths size is 600
Malloc succeed :)
---------freelist info---------
node(1)  address: 2293068 size:180
--------------end---------------

free address 2292252 size: 208
free address 2292224 size: 28
---------freelist info---------
node(1)  address: 2292224 size:236
node(2)  address: 2293068 size:180
--------------end---------------

malloc! ths size is 100
Malloc succeed :)
---------freelist info---------
node(1)  address: 2292224 size:236
node(2)  address: 2293176 size:72
--------------end---------------

free address 2292460 size: 608
free address 2293068 size: 108
---------freelist info---------
node(1)  address: 2292224 size:1024
--------------end---------------
```
>解释：
```
    我的学号为2012011354，实现最优匹配算法。
    用类bestmanage作为管理者，用一个链表freelist来保存空闲分区，bestmanage中有malloc、free、merge等主要函数。
    由于简化释放时进行的内存合并操作，空闲分区按照地址大小进行排序。同时，如果要求分配大小为n的情况，实际会使用给它n+8字节大小，因为需要来存储使用的长度.
    因为在64位机上指针的大小为8，不是4，所以要用sizeof(long long),如果用sizeof(int)会报错 :(
```
## 扩展思考题

阅读[slab分配算法](http://en.wikipedia.org/wiki/Slab_allocation)，尝试在应用程序中实现slab分配算法，给出设计方案和测试用例。


