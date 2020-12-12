FROM nginx:1.11.7

ADD ./web/nginx.conf /etc/nginx/nginx.conf
ADD ./web/default.conf /etc/nginx/sites-available/default
ADD ./web/default.conf /etc/nginx/sites-enabled/default
ADD ./web/uwsgi_params /etc/nginx/uwsgi_params

RUN mkdir /var/www
RUN mkdir /var/www/front
RUN mkdir /var/www/static