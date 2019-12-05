FROM kotaimen/mapnik:3.0.18-ubuntu

RUN pip3 install Django==2.2.3
RUN pip3 install django-cors-headers==3.1.0
RUN pip3 install django-rest-framework==0.1.0
RUN pip3 install djangorestframework==3.10.1
RUN pip3 install djangorestframework-gis==0.14
RUN pip3 install djangorestframework-jwt==1.11.0
RUN pip3 install geobuf==1.1.1
RUN pip3 install Pillow==5.1.0
RUN pip3 install protobuf==3.0.0
RUN pip3 install psycopg2==2.7.4
RUN pip3 install psycopg2-binary==2.8.3
RUN pip3 install PyJWT==1.7.1
RUN pip3 install pyproj==1.9.5.1
RUN pip3 install requests==2.21.0
RUN pip3 install six==1.12.0
RUN pip3 install sqlparse==0.3.0
RUN pip3 install virtualenv==16.0.0
RUN pip3 install uwsgi

RUN mkdir /code

# sudo docker run -p 35000:2000 -v /home/gabriel/Documentos/UNICARIOCA/TCC/producao/python/restful_ide/:/code --name restful-ide --network network_prod restful-ide:1.0.0 uwsgi --ini /code/uwsgi.ini
