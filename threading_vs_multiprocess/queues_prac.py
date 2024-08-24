from threading import Thread, Lock, current_thread
from queue import Queue
import time


def worker(q, lock):
   while True:
      value = q.get()
      with lock:
        print(f'we are in {current_thread().name} got {value}')
      q.task_done()

if __name__ == "__main__":
    q = Queue()
    lock = Lock()
    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon = True  #Daemon threads are background threads that automatically exit as soon as all non-daemon threads (typically the main program) have completed. This means that when the main server function (run_server) completes, the daemon thread (t) will automatically stop, and you won't have to manually stop it.
        thread.start()
    
    for i in range(1,21):
        q.put(i)

    q.join()

    print("end main")
    