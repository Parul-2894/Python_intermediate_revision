from multiprocessing import Process
import os 
import time

processes = []

num_processes = os.cpu_count()


def square_nums():
    for i in range(100):
        sqr = i*i
        print(sqr)
        time.sleep(0.1)

# create process
for i in range(num_processes-2):
    p = Process(target=square_nums)
    processes.append(p)


if __name__ == '__main__': #Note:: this is very important, otherwise you will
    #get runtime errors. 

    # start
    for p in processes:
        p.start()

    for p in processes:
        p.join()  #  The join() method is used to block the main process (i.e., the script that initiated the new process) until the target process completes its execution. This is useful for synchronizing processes and ensuring that the main process waits for all child processes to finish before continuing.

    #without join the main process can complete without the completion of the join process. 
    print("All are dones")


