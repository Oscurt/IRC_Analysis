GUIA ACTUAL PARA CORRERLO:<br/>
<br/>

cd server<br/>
sudo docker build -t server .<br/>

cd ..<br/>

cd client<br/>
sudo docker build -t client .<br/>

sudo docker network create IRC<br/>
sudo docker run --net=IRC -it server<br/>
(chequear la IP del servidor, por ejemplo con "sudo docker network inspect IRC)<br/>
sudo docker run --net=IRC -it client<br/>
(en el cliente ejecutar lo siguiente)<br/>
/server add local IPSERVER<br/>
/connect local<br/>

https://www.youtube.com/embed/TTblLelks9E
