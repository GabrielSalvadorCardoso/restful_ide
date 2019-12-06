# restful_ide
restful_ide uses python3 and pip

## intall project python dependencies
pip install -r requirements.txt

## restful_ide uses mapnik, to install it
https://github.com/mapnik/mapnik/wiki/UbuntuInstallation

## in the case of errors involving the C++ compiler
https://github.com/mapnik/mapnik/issues/3769

## install mapnik python bidings
pip3 install mapnik

## if the previous command doesn't work
https://github.com/mapnik/python-mapnik

restful_ide uses PostgreSQL with spatial extansion PostGIS. Feel free to use whatever database with spatial extansion you want

## restful_ide spatial data
ftp://geoftp.ibge.gov.br/cartas_e_mapas/bases_cartograficas_continuas/bcim/versao2016/shapefile/

## using shp2pgsql to transfer shapefiles to postgres/postgis
https://www.bostongis.com/pgsql2shp_shp2pgsql_quickguide.bqg
