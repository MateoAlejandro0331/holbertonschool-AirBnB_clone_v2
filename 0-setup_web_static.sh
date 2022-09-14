#!/usr/bin/env bash
<<<<<<< HEAD
# write a Bash script that sets up your web servers for the deployment of web_static. It must:
apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
service nginx restart
=======
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
>>>>>>> b60c011d18793dc71de41a02e5f8828f488dfd70
