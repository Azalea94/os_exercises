#include<iostream.h > 
#include<stdio.h> 
#include<stdlib.h>  
#include "queue.h" 

void main () { 
  LinkQueue* x;   int n,i; 
  int timing=0;//时刻 
  Job *jobing;//任务数组（动态分配） 
  x = (LinkQueue*)malloc(sizeof(LinkQueue)*5);   for(i=1; i<=4; i++)//初始化所有队列  
 
  InitQueue(x[i]); 
  cout<<"请输入任务个数："<<endl;   
cin>>n;   
if(n==0){  
  cout<<"没有任务，请重新输入"<<endl; 
  cin>>n; 
} 
  jobing = new Job[n];//动态空间分配   
cout<<"请输入各个任务信息："<<endl;   
cout<<"任务号 到达时间 运行时间"<<endl;   
for(i=0;i<n;i++)  
  cin>>jobing[i].jobnum>>jobing[i].arrivetime>>jobing[i].burst; 
  i=0; 
  
while(i!=n||!(EmptyQueue(x[1])&&EmptyQueue(x[2])   
 && EmptyQueue(x[3])&& EmptyQueue(x[4])))
{ 
   while(timing==jobing[i].arrivetime)    
{    
	create(x,jobing[i]);//创建任务    
	i++; 
   } 
   function(x,timing);//任务运行    timing++; 
 } 
  for(i=1; i<=4; i++)   
	ClearQueue(x[i]);//清空队列
 }  
