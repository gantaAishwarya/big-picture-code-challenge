FROM alpine:latest

ENV DEBIAN_FRONTEND=noninteractive

#copy application
RUN mkdir -p /etc/nginx/sites-available
RUN mkdir -p /home/application-user/application/data
COPY ./resources/application /etc/nginx/sites-available/application
COPY ./resources/application.ini /home/application-user/application/
COPY ./src/ /home/application-user/application/src/
COPY ./resources/ /home/application-user/application/resources/
COPY ./model/ /home/application-user/application/model/
COPY ./wsgi.py /home/application-user/application/


#installing requied libraries
RUN adduser -D -G www-data application-user
RUN apk update
RUN apk add python3 py3-pip nginx python3-dev build-base linux-headers pcre-dev libffi-dev openssl git


#setup Virtual environment
RUN python3 -m venv /home/application-user/application/venv
RUN /home/application-user/application/venv/bin/python3 -m pip install --upgrade pip
RUN /home/application-user/application/venv/bin/pip install uwsgi flask wheel pip-upgrader
RUN /home/application-user/application/venv/bin/pip install -r /home/application-user/application/resources/requirements.txt
RUN /home/application-user/application/venv/bin/pip freeze > /home/application-user/application/resources/requirements.txt
RUN /home/application-user/application/venv/bin/pip-upgrade /home/application-user/application/resources/requirements.txt -p all
RUN /home/application-user/application/venv/bin/pip freeze > /home/application-user/application/resources/requirements.txt


RUN chmod 777 /home/application-user/application/application.ini
#link nginx config
RUN mkdir /etc/nginx/sites-enabled/
RUN ln -s /etc/nginx/sites-available/application /etc/nginx/sites-enabled/default

COPY ./resources/nginx.conf /etc/nginx/nginx.conf
WORKDIR /home/application-user/application
CMD nginx;/home/application-user/application/venv/bin/uwsgi --ini /home/application-user/application/application.ini;

#TODO: manually adjust application.sock permissions
#Expose port for <usecase>
EXPOSE 80
EXPOSE 443