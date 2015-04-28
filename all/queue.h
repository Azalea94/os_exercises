queue.h struct Job {  
     int  jobnum;     //任务号      
int  arrivetime;  //到达时间      
int  burst;    //运行时间      
int  retime;      //响应时间   int  leavetime;   
//离开时间   int  roundtime;   //周转时间   int  runtime;     //已运行时间 }; 
typedef Job ElemType; struct LNode{  ElemType data;  LNode* next; }; 
struct LinkQueue{  
	LNode* front; 
  LNode* rear; }; 
void InitQueue(LinkQueue& HQ) {  HQ.front=HQ.rear=NULL; } 
void EnQueue(LinkQueue& HQ,ElemType item) { 
  LNode* newptr=new LNode;   newptr->data=item;   newptr->next=NULL;   if (HQ.rear==NULL)     HQ.front=HQ.rear=newptr;   else     HQ.rear=HQ.rear->next=newptr; } 
ElemType OutQueue(LinkQueue& HQ) { 
 if (HQ.front==NULL) {   cerr<<"Queue NULL."<<endl;   exit(1);  } 
 ElemType temp=HQ.front->data;  LNode* p=HQ.front;  HQ.front=p->next;  if (HQ.front==NULL)    HQ.rear=NULL;  delete p;  return temp; }  
ElemType *PeekQueue(LinkQueue& HQ) { 
 if (HQ.front==NULL) {cerr<<"队列为空无首元素。"<<endl;exit(1);}  return &HQ.front->data;  } 
bool EmptyQueue(LinkQueue& HQ) {  
 return HQ.front==NULL; } 
void ClearQueue(LinkQueue& HQ) { 
 LNode* p=HQ.front;  while(p!=NULL) { 
    HQ.front=HQ.front->next; 









    delete p;     p=HQ.front;  } 
 HQ.rear=NULL; } 
void function(LinkQueue* x, int timing)//任务运行 { 
  int leatime[4];//时间片的大小   
leatime[0]=0;   leatime[1]=2;   leatime[2]=6;   leatime[3]=14;   
Job *t=NULL;   
int i=1;   
while(i<5)   
{    if(EmptyQueue(x[i])==false)//如果队列不为空    
	{        
            t=PeekQueue(x[i]);//读取队首元素       t->runtime++;//已运行时间+1       if(t->runtime==1&&timing>=t->arrivetime)     t->retime=timing - t->arrivetime;       if(t->runtime == t->burst)     {     t->leavetime=timing+1;  
              t->roundtime =t->leavetime - t->arrivetime;               
cout<<"任务号:"<<t->jobnum<<" "<<"响应时间:"<<t->retime<<" ";              
cout<<"离开时间:"<<t->leavetime<<" "<<"周转时间:"<<t->roundtime;              
cout<<endl; //输出信息     
OutQueue(x[i]);    
} 
            else if((t->runtime == leatime[i]) && (i<=3))    
{//调整优先级     
	EnQueue(x[i+1],OutQueue(x[i]));    } 
            break;    }    i++;   } } 
void create(LinkQueue* x,Job job) { 
   job.runtime=0; 









   EnQueue(x[1],job); }