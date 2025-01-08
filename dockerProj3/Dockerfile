# use the latest version of ubuntu linux as a base
FROM ubuntu:latest

# update the package index of the ubuntu image, and upgrades any installed packages to the latest version
RUN apt-get update && apt-get upgrade -y

# install nginx
RUN apt-get install -y nginx

# copy myapp folder and contents to container
COPY myapp /var/www/html

# expose port 8080 on the container, allowing it to accept incoming requests
EXPOSE 8080

# default command when the container starts (CMD). Starts nginx in the foreground (ie, not as a daemon), and keeps the container running in the background
CMD [ "nginx", "-g", "daemon off;" ]
