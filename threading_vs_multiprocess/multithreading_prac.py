from threading import Thread
import time 

def square_nums():
    for i in range():
        print(i)

if __name__ == '__main__':
    threads = []
    num_threads = 8

    #creating threads 
    for i in range(num_threads):
        thread = Thread(target = square_nums)
        threads.append(thread)
    
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()