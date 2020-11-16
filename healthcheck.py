import shutil
import psutil

# check update

def check_disk_usage(disk):
    #This function will check disk usage
    du=shutil.disk_usage(disk)
    free=du.free/du.total*100
    return free>20

def check_cpu_usage():
    #This function will check cpu usage
    usage=psutil.cpu_percent(0.5)
    return usage>75

#Output messages after completed checks
if not check_disk_usage("/"):
    print("Error in Disk!")
elif not check_cpu_usage():
    print("Error in CPU!")
else:
    print("Everything OK!")
