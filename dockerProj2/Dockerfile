# Use the official Apache HTTP Server image
FROM httpd:2.4

# Copy custom configuration file (if any)
# COPY ./my-httpd.conf /usr/local/apache2/conf/httpd.conf

# Copy website files into the container
COPY ./htdocs/ /usr/local/apache2/htdocs/

# Expose port 80
EXPOSE 80
