
TASK 3:
    - Ansible Playbook for Web Application Deployment
    - Objective:Automate the deployment of a simple web application using Ansible.
    - Tasks:
        1) Install Nginx on the remote server.
        2) Configure Nginx to serve an HTML file from a specified directory.
        3) Ensure Nginx service is started and enabled on boot.
    - Outcome:
        The remote server will automatically install, configure, and run Nginx to serve the web application without manual intervention.
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
        Archive the /var/log directory into a .tar.gz file.
        Store the backup on a remote server or S3 bucket.
        Add a timestamp to the backup filename.
        Verify the backup by checking:
        File existence
        File size (to confirm it's not empty)
        This task aims to ensure automated, consistent, and verifiable backups of critical system data.
    - STEPS TAKEN:
    1) backup path into tar file
        tar -czf compress-dir.tar dir1
    2) put timestamps
    3) check backup (existance and size)
    4) send to remote server

ssh -i ~/.ssh/id_rsa cherryrina@10.100.102.10


