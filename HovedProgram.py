import datamaaler
from time import sleep
import threading
import queue


class myThread (threading.Thread):
    def __init__(self, threadID, name, read, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.read = read
        self.delay = delay

    def run(self):
        print("Starting " + self.name)
        if self.read:
            while self.read:
                data.append(datamaaler.generate_data())
                sleep(self.delay)
        else:
            while not self.read:
                sleep(self.delay)
                #lock
                datamaaler.avg_data(data)
                del data[:]
                #unlock
 
        print("Exiting " + self.name)


data = []
queueLock = threading.Lock()
workQueue = queue.Queue(10)

thread1 = myThread(1, "Thread-1", 1, 1)
thread2 = myThread(2, "Thread-2", 0, 60)

thread1.start()
thread2.start()

print("Exiting main thread")