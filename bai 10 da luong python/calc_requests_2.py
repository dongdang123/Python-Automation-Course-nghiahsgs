import threading
import time
import requests

global is_stop
is_stop=False

global count_rq
count_rq=0

global count_rq_success
count_rq_success=0



class myThread_request(threading.Thread):
    
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name=name
    def run(self):
        global is_stop
        global count_rq
        global count_rq_success

        while(not is_stop):
            # res=requests.get('http://google.com')
            res=requests.get('https://nha.chotot.com/toan-quoc/mua-ban-bat-dong-san?page=2')
            if res.status_code==200:
                count_rq_success+=1
            count_rq+=1

class myThread_time(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name=name
    def run(self):
        global is_stop

        time.sleep(60)#sleep 60s
        is_stop=True

print('is_stop',is_stop)

thread1=myThread_time('thread1')
thread2=myThread_request('thread2')
thread3=myThread_request('thread3')


thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print('is_stop',is_stop)
print('count_rq',count_rq)
print('count_rq_success',count_rq_success)
