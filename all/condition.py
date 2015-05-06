#coding=utf-8
#!/usr/bin/env python
  
import threading  
import time  
   
condition1 = threading.Condition()  

condition2 = threading.Condition()  
products1 = 0  
products2 = 0  
N = 10

class Producer1(threading.Thread):  
    def __init__(self):  
        threading.Thread.__init__(self)  
          
    def run(self):  
        global condition1, products1 
        while True:  
            if condition1.acquire():  
                if products1 < N - 1:  
                    products1 += 1;  
                    print "Producer1(%s):deliver one1, now products:%s" %(self.name, products1) 
                    print "" 
                    condition1.notify()  
                else:  
                    print "Producer1(%s):already 9, stop deliver, now products:%s" %(self.name, products1)  
                    condition1.wait();  
                condition1.release()  
                time.sleep(2)  

class Producer2(threading.Thread):  
    def __init__(self):  
        threading.Thread.__init__(self)  
          
    def run(self):  
        global condition2, products2  
        while True:  
            if condition2.acquire():  
                if products2 < N-2:  
                    products2 += 1;  
                    print "Producer2(%s):deliver one2, now products:%s" %(self.name, products2)  
                    print ""
                    condition2.notify()  
                else:  
                    print "Producer2(%s):already 8, stop deliver, now products:%s" %(self.name, products2)  
                    condition2.wait();  
                condition2.release()  
                time.sleep(2)           
class Consumer(threading.Thread):  
    def __init__(self):  
        threading.Thread.__init__(self)  
          
    def run(self):  
        global condition1, condition2, products1,products2
        while True:  
            if condition1.acquire():  
                if products1 > 1:  
                    products1 -= 1 
                    print "!!!!!!!!!!!Consumer(%s):consume frame, now products1:%s, products2:%s" %(self.name, products1,products2)  
                    condition1.notify()
                else:
                    print "Consumer(%s): stop consume frame, products1:%s,products2:%s" %(self.name, products1,products2)  
                    condition1.wait();  
                condition1.release()
                time.sleep(2) 
            if condition2.acquire():
                if products2 > 2:
                    products2-=2
                    print "$$$$$$$$$$$Consumer(%s):consume wheels and create a car, now products1:%s, products2:%s" %(self.name, products1,products2)  
                    condition2.notify()
                else:
                    print "Consumer(%s): stop consume wheels, products1:%s,products2:%s" %(self.name, products1,products2)  
                    condition2.wait();  
                condition2.release() 
                time.sleep(2)  
                  
if __name__ == "__main__":  
    p1 = Producer1()
    p1.start()
    p2 = Producer2()
    p2.start()
    c = Consumer()
    c.start()