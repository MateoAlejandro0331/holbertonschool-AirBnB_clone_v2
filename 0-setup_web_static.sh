#!/usr/bin/env bash
#Write a Bash script that sets up your web servers for the deployment of web_static. It must:
if ! command -v nginx -v &> /dev/null
then
    sudo apt-get update
    sudo apt -y install nginx
fi
print="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
ubuntu@89-web-01:~/$ curl localhost/hbnb_static/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
#Create directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
#Create html file and write into it
sudo touch /data/web_static/releases/test/index.html
sudo chmod 777 /data/web_static/releases/test/index.html
echo "$print" > /data/web_static/releases/test/index.html
#Create a symbolic link: 1=referenced           2=copy
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
#Change owner and group to data folder
sudo chown -R ubuntu:ubuntu /data/
#Changes nginx config
sudo sed -i "/listen 80 default_server/ a location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default
sudo service nginx restart
