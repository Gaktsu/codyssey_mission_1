FROM ubuntu:24.04

RUN apt-get update -y && apt-get install nginx -y

ENV codyssey=minseong

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:80/ || exit 1

COPY ./index.html /var/www/html/index.html
    
CMD ["/bin/bash"]