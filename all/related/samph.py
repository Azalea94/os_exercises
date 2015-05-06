#coding=utf-8
import threading  
import random  
import time  
frame = 0
wheel = 0
N = 10

class SemaphoreThread1(threading.Thread):  
    """class using semaphore"""  

    

    def __init__(self,threadName,semaphore,empty,frame):  
       """initialize thread"""  

       threading.Thread.__init__(self,name=threadName)  
       #self.sleepTime=2#random.randrange(1,6)  
       #set the semaphore as a data attribute of the class  
       self.s1=semaphore
       self.empty = empty
       self.frame = frame
    def run(self):  
      """Print message and release semaphore"""  
      global frame
       #acquire the semaphore
      while True:
        time.sleep(2)  
        self.s1.acquire()  
        self.empty.acquire()
         #remove a table from the list
        frame += 1 
        print "Producer1(%s):deliver frame, now frame:%s\n" %(self.name, frame)    
        self.frame.release()
      #self.threadSemaphore.release()  

class SemaphoreThread2(threading.Thread):  
    """class using semaphore"""  

    

    def __init__(self,threadName,semaphore,empty,wheel):  
       """initialize thread"""  

       threading.Thread.__init__(self,name=threadName)  
       #self.sleepTime=2#random.randrange(1,6)  
       #set the semaphore as a data attribute of the class  
       self.s2=semaphore
       self.empty = empty
       self.wheel = wheel
    def run(self):  
       """Print message and release semaphore"""  

       #acquire the semaphore
       global wheel
       while True:
         time.sleep(2)   
         self.s2.acquire() 
         self.empty.acquire() 
         #remove a table from the list

         wheel += 1 
         print "Producer2(%s):deliver wheels, now wheels:%s\n" %(self.name, wheel)    
         self.wheel.release()        
       #self.threadSemaphore.release()  

class SemaphoreThread3(threading.Thread):  
    """class using semaphore"""  

    

    def __init__(self,threadName,semaphore1,semaphore2,empty,frame,wheel):  
       """initialize thread"""  

       threading.Thread.__init__(self,name=threadName)  
       self.sleepTime=2#random.randrange(1,6)  
       #set the semaphore as a data attribute of the class  
       self.s1=semaphore1
       self.s2=semaphore2
       self.empty=empty
       self.frame=frame
       self.wheel = wheel
    def run(self):  
       """Print message and release semaphore"""  

       #acquire the semaphore 
       global frame, wheel 
       while True:
         self.frame.acquire() 
         frame -= 1
         print "Consumer(%s):consume frame, now frame:%s, wheels:%s\n" %(self.name, frame,wheel)      
         self.empty.release()
         self.s1.release()

         self.wheel.acquire()
         self.wheel.acquire()
         wheel -= 2
         print "Consumer(%s):consume wheels, now frame:%s, wheels:%s\n" %(self.name, frame,wheel)      
         self.empty.release()
         self.empty.release()
         self.s2.release()
         self.s2.release()
         time.sleep(2)         
         print "!!!!creat a car\n"      
        
#semaphore allows five threads to enter critical section  
s1=threading.Semaphore(9)  
s2=threading.Semaphore(8) 
Sempty=threading.Semaphore(10)
Sframe =  threading.Semaphore(0)
Swheel=threading.Semaphore(0)  
p1 = SemaphoreThread1("p1", s1,Sempty,Sframe)
p1.start()
p2 = SemaphoreThread2("p2", s2,Sempty,Swheel)
p2.start()
c = SemaphoreThread3("p3", s1,s2,Sempty,Sframe,Swheel)
c.start()
