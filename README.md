El presente repositorio muestra un proyecto que busca analizar el trafico IRC de un servidor y un cliente, para ello se realizaran diversos test, para lograr un analisis completo.

En este se presentan dos carpetas, cada una contiene un dockerfile. Estas aplicaciones son para poder realizar un analisis sobre el protocolo IRC, ademas de estos archivos, tenemos un informe en PDF sobre el mismo, un video y una captura de wireshark.

Guia de uso:

Primero clonamos:
```sh
$ git clone https://github.com/Oscurt/IRC_Analysis
```

Luego correr los dockerfile:

```sh
$ docker build -t server IRC_Analysis/server
$ docker build -t client IRC_Analysis/client
$ docker build -t client IRC_Analysis/polymorph
```

Creamos una red con docker:

```sh
$ docker network create IRC
```

Luego montamos el servidor:

```sh
$ docker run --net=IRC -it server
```

Ahora el cliente: 

```sh
$ docker run --net=IRC -it client
```

Ahora polymorph 

```sh
$ docker run --privileged --net=IRC -it poly
```

Para conectarse al servidor se debe verificar la IP del server, esto debe ser una vez el server este corriendo, pues le asignara una IP, esta la podemos consultar con el siguiente comando:

```sh
$ docker network inspect IRC
```

Dentro del cliente para conectarse debemos agregar el server, por ende una vez en weechat usar:

```sh
\server add "nombre" "ipserver"
\connect "nombre"
```

Video con la captura:

[![IRC Analysis](https://img.youtube.com/vi/TTblLelks9E/hqdefault.jpg)](https://youtu.be/TTblLelks9E)

Video con el trafico modificado:

[![Manipulacion de trafico IRC](https://img.youtube.com/vi/QhbpBZOFHFI/hqdefault.jpg)](https://youtu.be/QhbpBZOFHFI)

