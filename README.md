# Tasks of Radware Home Exam 
## TASK 1
### Description
- Create a Python script that monitors CPU usage, memory usage, and disk space, with alerting features based on thresholds.
- Objective: Monitor system health metrics (CPU, memory, disk space) and log warnings or alerts when thresholds are exceeded.
- Requirements:
    1) Collect CPU load, memory usage, and disk space.
    2) Issue a warning log if usage exceeds 80%.
    3) Issue a major-level alert if usage exceeds 90%.
    Log entries when metrics exceed defined thresholds.
### Code Source
`/task-01-system-health`
### Steps Taken
Created a working program and split it into separate functions.
### How To Run
- Run Python script named `1-system_health.py`
- The script will create a log file named `system_health_logs.log` where you can watch the results
## TASK 2:
### Description
- Write a Python script to check if the nginx service is running and restart it if it is down, logging the results.
- Objective: Automate the check and restart of the nginx service if it is not running.
- Requirements:
    1) Check the status of nginx service.
    2) If the service is down, restart it.
    3) Log the success or failure of the restart operation.
### Code Source
    `/task-02-service-manager`
### Steps Taken
Created a working program and split it into separate functions.
### How To Run
- Run Python script named `2-service_managment.py`
- The script will create a log file named `service_availability_logs.log` where you can watch the results
## TASK 3:
### Description
- Ansible Playbook for Web Application Deployment
- Objective:Automate the deployment of a simple web application using Ansible.
- Requirements:
    1) Install Nginx on the remote server.
    2) Configure Nginx to serve an HTML file from a specified directory.
    3) Ensure Nginx service is started and enabled on boot.
### Code Source
`/task-03-web-app-deployment`
### Steps Taken
#### HTML
1) Created `web_app.html` with the content to be served by Nginx.
#### INVENTORY
1) Created inventory.ini to define the target machines or groups.
2) Verified my inventory with: 
`ansible-inventory -i inventory.ini --list`
3) Pinged the local group in my inventory to test connectivity: 
`ansible local -m ping -i inventory.ini`
#### PLAYBOOK
1) Found the Nginx configuration file to copy the path inside the server block configuration for a static HTML website:
    `nginx -V` (look for the --conf-path=/etc/nginx/nginx.conf)
2) Created `playbook.yml` for the deployment tasks.
3) Ran Ansible with the inventory and playbook: 
`ansible-playbook -i inventory.ini playbook.yml`
4) created a bash script named `run-mr.sh` to run everything at the right order.
### How To Run
- Run bash script named `run-me.sh` from shell
- The script executes Ansible and will return Nginx service status and results of web app connectivity
## TASK 4
### Description
- Automate the backup of critical directories (e.g., /var/log) using an Ansible playbook, including storing the backup remotely.
- Objective: Create an Ansible playbook that automates system backups and ensures backups are verified.
- Requirements:
    1) Archive the log directory (/var/log) into a .tar.gz file.
    2) Store the backup on a remote server or S3.
    3) Timestamp the backup file.
    4) Verify the backup by checking the file's existence and size.
### Code Source
`/task-04-system-log-backup`
### Steps Taken
#### INVENTORY
1) Created inventory.ini to define the target machines or groups.
2) Verified my inventory with: 
`ansible-inventory -i inventory.ini --list`
3) Pinged the local group in my inventory to test connectivity: 
`ansible local -m ping -i inventory.ini`
#### PLAYBOOK
1) Created two playbook files for the deployment tasks.
2) Ran Ansible with the inventory and playbooks.
3) Connected to the remote computer via SSH.
4) Created a bash script named `run-mr.sh` to run them one bu one. 
### How To Run
- Run bash script named `run-me.sh` from shell
- The script executes both of Ansible playbooks
## TASK 5
### Description
- Automate the periodic execution of a Python script using Jenkins.
- Objective: Create a Jenkins pipeline to execute the Python script from Task 2 on a scheduled basis.
- Requirements:
    1) Set up a Jenkins pipeline to execute the script from Task 2.
    2) Configure the job to run every 4 hours.
### Code Source
`/task-05-jenkins-pipline`
### Steps Taken
1) Downloaded a Jenkins Docker
2) Signed into the GUI at `http://localhost:8080`
3) Written a Jenkins pipeline
4) Created a new pipeline job inside the GUI
### How To Run



