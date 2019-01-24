import threading

class MyMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x = MyMessenger(name ='Send Messages')
y = MyMessenger(name ='Receive Messages')
x.start()
y.start()


