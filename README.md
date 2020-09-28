GUIA ACTUAL PARA CORRERLO:

sudo docker network create IRC
sudo docker run --net=IRC -it server
(chequear la IP del servidor)
sudo docker run --net=IRC -it client
(en el cliente ejecutar lo siguiente)
/server add local IPSERVER
/connect local