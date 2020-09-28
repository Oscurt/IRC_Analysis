GUIA ACTUAL PARA CORRERLO:<br/>
<br/>

cd server<br/>
sudo docker build -t server .<br/>

cd ..<br/>

cd client<br/>
sudo docker build -t client .<br/>

sudo docker network create IRC<br/>
sudo docker run --net=IRC -it server<br/>
(chequear la IP del servidor)<br/>
sudo docker run --net=IRC -it client<br/>
(en el cliente ejecutar lo siguiente)<br/>
/server add local IPSERVER<br/>
/connect local<br/>
