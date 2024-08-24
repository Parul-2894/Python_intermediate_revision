"""
    In threading or multiprocess yu can run code in parallel
    to speed up your code. 

    Difference between a process and a thread 

    Process: An instance of a program (e.g a Python interpreter)
    + Takes advantages of multiple cpus and cores.
    + separate memry space -> memory is not shared between processes
    + Great for CPu-bound processing. 
    + New Process is stated independently from other process
    + Processes are interruptable/killable
    + One GIL for each process -> avoids GIl limitations (Global Interpreter lock)

    - Heavyweight
    - more memory
    - Ipc (inter-process communication is more complicated)
    
"""

"""
Threads:
An entity within a process that can be scheduled fr execution.
A process can spawn multiple process

+ all threads within a process share the same memory
+ lightweight
+ Starting a thread is faster than starting a process. 
+ Great for I/O-bounud tasks.

-Threading is limited by GIL: only one thread at a time.GIl alows only one thread at a time
, so there is no actual parallel execution here.  
- no Effect for cpu-bounud tasks
- not intterruptable/killable
-Careful with race conditions.


"""

"""
Muliprocessing :
https://docs.python.org/2/library/multiprocessing.html
"""

"""

"""