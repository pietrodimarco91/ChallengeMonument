__author__='Pietro Di Marco'

import subprocess
import time

if __name__ == '__main__':

    commands = [
        'sleep 3',
        'ls -l /',
        'find /',
        'sleep 4',
        'find /usr',
        'date',
        'sleep 5',
        'uptime'
    ]

    # instantiate and run the different processes
    procs = [subprocess.Popen(i.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE) for i in commands]
    res = list()
    start_time = time.time()

    # when the process terminates it saves the time elapsed
    while True:
        for p in procs:
            if p.poll() is not None:
                res.append(float(time.time()-start_time))
                procs.remove(p)
        if not procs:
            break

    # display the report
    print("minimum execution time: " + str(min(res))+" s")
    print("maximum execution time: " + str(max(res))+" s")
    print("average execution time: " + str(sum(res)/len(res))+" s")
    print("total elapsed time: " + str(sum(res))+" s")