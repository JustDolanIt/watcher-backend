#!/usr/bin/env python3
# ex: ts=4 sw=4 et

import psutil
import os
import datetime


# Functions part
def getData(avmem=True, usgmem=True, avg=True, uptime=True, frdsk=True, usgdsk=True):
    'Used to get required data. Possilbe flags: Available memory (avmem == True), Memory usage percent (usgmem == True), Average load (avg == True), Uptime (uptime == True), Free disk space (frdsk == True), Disk usage (usgdsk == True)'

    data = dict()
    FORMAT = 1024 * 1024.0

    if avmem:
        data.update({"avMem": psutil.virtual_memory().available/FORMAT})
    if usgmem:
        data.update({"memUsage": psutil.virtual_memory().percent})
    if avg:
        data.update({"avg": os.getloadavg()}) # Used direct system call. psutil.cpu_percent gives kinda another info
    if uptime:
        utime = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
        data.update({"uptime": utime.days})
    if frdsk:
        data.update({"freeDisk": psutil.disk_usage('/').free/FORMAT})
    if usgdsk:
        data.update({"diskUsage": psutil.disk_usage('/').percent})
    return(data)

if __name__ == "__main__":
    print(getData())
