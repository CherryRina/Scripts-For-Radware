"""
This script monitors the health of a system - CPU ussage, RAM ussage and Disk space percentages
The script will write logs about those components based on a threshold:
    - INGO log - when the utilization percentage is lower than 80%
    - WARNING log  - when the utilization percentage is between 80% and 90%
    - CRITICAL log - when the utilization percentage is higher than 90%
"""

import psutil 
import os
import re
import logging

def create_new_file():
    """ creates a new file """
    # TODO: create newfunction that check if file exist
    with open("system_health_logs.log", 'a') as file:
        file.write("System Health Logs\n")
        file.write("===================\n")

def setup_logger():
    """ sets the logger for the script """
    # logger
    logger = logging.getLogger('system_health_logger')
    logger.setLevel(logging.INFO)
    # handler
    file_handler = logging.FileHandler('system_health_logs.log')
    file_handler.setLevel(logging.INFO)
    # formatter
    formater = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formater)
    # add handler to logger 
    logger.addHandler(file_handler)
    return logger

logger = setup_logger() # global access to the logger

def log_by_threshold(component, percent):
    """ function that raises a log by the threshold """
    if 80 <= percent <= 90:
        logger.warning(f"{component} is at {percent}%")
    elif percent >= 90:
        logger.critical(f"{component} is at {percent}% !")
    else:
        logger.info(f"{component} is at {percent}%")

def CPU_utilization():
    """ montor the CPU utilization in percentages """
    utilization = psutil.cpu_percent(1)
    log_by_threshold("CPU", utilization)

def RAM_utilization():
    """ montor the RAM utilization in percentages """
    total_memory, used_memory, free_memory = map(int,os.popen('free -t -m').readlines()[-1].split()[1:])
    utilization = round((used_memory/total_memory)*100,2)
    log_by_threshold("RAM", utilization)

def disk_utilization():
    """ montor the disk utilization in percentages """
    disk_regix = re.compile(r'/dev/sd.*') # finds all sd devices
    disk_usage_percent = {}
    for partition in psutil.disk_partitions(all=False):
        if disk_regix.match(partition.device): # with regix match only the sd.* devices
            try:
                usage = psutil.disk_usage(partition.mountpoint) # ountpoint - where device is mounted and accessed
                disk_usage_percent[partition.device] = usage.percent 
            except:
                # skips the partition whre permission is denied
                continue
    for disk, percent in disk_usage_percent.items():
        log_by_threshold(disk, percent)

def main():
    """ main function """
    create_new_file()
    CPU_utilization()
    RAM_utilization()
    disk_utilization()
    
if __name__ == "__main__":
    main()