#!/usr/bin/env bash
# Configure nginx as web server
if ! which nginx &> /dev/null;
then
	sudo apt-get update
	sudo apt-get -y nginx
fi

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared

echo "<html>
	<head></head>
	<body>
	<h1>Hello Lawan!</h1>
	</body>
	</html>" | sudo tee /data/web_static/releases/test/index.html

sudo rm -f /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

config_file="/etc/nginx/sites-available/default"
nginx_config="
server {
	listen 80;
	listen [::]:80;
	server_name _;
	
	location /hbnb_static {
		alias /data/web_static/current/;
	}
}
"

sudo cp $config_file $config_file.bak
echo "$nginx_config" | sudo tee $config_file > /dev/null
sudo service nginx restart
exit 0
