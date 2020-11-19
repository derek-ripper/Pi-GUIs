"""
Code illustration: 7.04
    Threading with Queue Simple Demo
Tkinter GUI Application Development Blueprints
"""

import queue
import threading


class Consumer(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            job = self.queue.get()
            self.do_task(job)

    def do_task(self, task):
        print ('doing task{}'.format(task))
        self.queue.task_done()


def producer(tasks):
    mqueue = queue.Queue()
    # populate queue with tasks
    for task in tasks:
        mqueue.put(task)
    # create 6 threads and pass the queue as its argument
    for i in range(6):
        mythread = Consumer(mqueue)
        mythread.daemon = True
        mythread.start()

    # wait for the queue to finish
    mqueue.join()
    print ('all tasks completed')

if __name__ == "__main__":
    tasks = 'A B C D E F'.split()
    producer(tasks)
