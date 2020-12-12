FROM nginx:1.11.7

ADD ./nginx.conf /etc/nginx/nginx.conf
ADD ./default.conf /etc/nginx/sites-available/default
ADD ./default.conf /etc/nginx/sites-enabled/default
ADD ./uwsgi_params /etc/nginx/uwsgi_params

RUN mkdir /var/www
RUN mkdir /var/www/front
RUN mkdir /var/www/static