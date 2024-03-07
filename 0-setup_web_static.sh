#!/usr/bin/env bash
# Configure nginx as web server
if ! command -v nginx &> /dev/null;
then
	sudo apt-get update
	sudo apt-get -y nginx
fi

mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo "<html><head></head><body><h1>Hello Lawan!</h1></body></html>" > /data/web_static/releases/test/index.html

rm -f /data/web_static/current && ln -s /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data

cat << EOF > /etc/nginx/sites-available/default
server {
	listen 80;
	server_name localhost;
	
	location /hbnb_static {
		alias /data/web_static/current/;
	}
}
EOF

#sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
sudo service nginx restart
exit 0
