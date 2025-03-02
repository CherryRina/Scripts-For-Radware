"""
Script checks services abailability and restarts it if it's down,
when finished, logs the actions and outcome (success or failure) to a log file.
"""

import subprocess
import logging

def create_new_file():
    """ creates a new file """
    # TODO: create new function that check if file exist
    with open("service_availability_logs.log", 'a') as file:
        file.write("System Health Logs\n")
        file.write("===================\n")

def setup_logger():
    """ sets the logger for the script """
    # logger
    logger = logging.getLogger('service_availability_logs')
    logger.setLevel(logging.INFO)
    # handler
    file_handler = logging.FileHandler('service_availability_logs.log')
    file_handler.setLevel(logging.INFO)
    # formatter
    formater = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formater)
    # add handler to logger 
    logger.addHandler(file_handler)
    return logger

logger = setup_logger() # global access to the logger

def restart_service(service_name):
    """ checks services abailability and restarts it if the it's down
        when finished, sends a log to the logger file """
    result = subprocess.run(['systemctl', 'is-active' , service_name], stdout=subprocess.PIPE, text=True)
    # TODO: process all systemctl statuses
    if result.stdout.strip() == 'inactive':
        logger.info(f"service named '{service_name}' is down")
        subprocess.run(['sudo', 'systemctl' , 'start' , service_name])
        logger.info(f"service named '{service_name}' was restarted")
    elif result.stdout.strip() == 'active':
        logger.info(f"service named '{service_name}' is up")
    else:
        logger.error(f"service named '{service_name}' unexpected service status: {result.stdout.strip()}")

def main():
    """ main function """
    create_new_file()
    service_name = "nginx"
    restart_service(service_name)

if __name__ == "__main__":
    main()
