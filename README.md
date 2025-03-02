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
    task-01-system-health
### Steps Taken
        Created a working program and split it into separate functions."
### How To Run
        write here
## TASK 2:
### Description
# TASK 3:
### Description
    - Ansible Playbook for Web Application Deployment
    - Objective:Automate the deployment of a simple web application using Ansible.
    - Requirements:
        1) Install Nginx on the remote server.
        2) Configure Nginx to serve an HTML file from a specified directory.
        3) Ensure Nginx service is started and enabled on boot.
    - STEPS TAKEN:
        HTML
            1 - Created web_app.html with the content to be served by Nginx.
        INVENTORY
            1 - Created inventory.ini to define the target machines or groups.
            2 - Verify your inventory with: ansible-inventory -i inventory.ini --list
            3 - Ping the local group in your inventory to test connectivity: ansible local -m ping -i inventory.ini
        PLAYBOOK
            1 - Find the Nginx configuration file to copy the path inside the server block configuration for a static HTML website:
                nginx -V (look for the --conf-path=/etc/nginx/nginx.conf)
            2 - Created playbook.yml for the deployment tasks.
            3 - Run Ansible with the inventory and playbook: ansible-playbook -i inventory.ini playbook.yml

TASK 4:
    - Write an Ansible Playbook to Perform a System Backup
    - Objective:Automate system backups using Ansible.
    - Requirements:
        - Archive the /var/log directory into a .tar.gz file.
        - Store the backup on a remote server or S3 bucket.
        - Add a timestamp to the backup filename.
        - Verify the backup by checking:
        - File existence
        - File size (to confirm it's not empty)
    - STEPS TAKEN:
        1) backup path into tar file
            tar -czf compress-dir.tar dir1
        2) put timestamps
        3) check backup (existance and size)
        4) send to remote server

ssh -i ~/.ssh/id_rsa cherryrina@10.100.102.10


