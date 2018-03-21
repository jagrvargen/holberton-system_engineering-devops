#Web Server

0. 0-transfer_file - Transfers a file from our client to a server. Accepts 4 parameters: The path to the file to be transferred, the IP of the server we want to transfer the file to, the username scp connects with, and the path to the SSH private key that scp uses.

1. 1-install_nginx_web_server - A bash script which installs Nginx on the web server and configures the listening port to 80. When root is queried with a GET request using curl, it will return a page containing the string 'Holberton School'.
