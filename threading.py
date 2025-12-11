import threading
import time

def print_1():
    print("starting a thread",threading.current_thread().name)
    
    time.sleep(0.02)
    
    print("finishing a thread",threading.current_thread().name)
    
def print_2():
        print("starting a thread",threading.current_thread().name)
             
        print("finishing a thread",threading.current_thread().name)
        
a=threading.Thread(target=print_1, name="thread1") 
b=threading.Thread(target=print_2, name="thread2") 

a.start()
b.start()