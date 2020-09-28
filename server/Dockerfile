FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y\
&& apt-get upgrade -y\
&& apt-get install build-essential -y\
&& apt-get install wget -y\
&& apt-get install golang-go -y\
&& wget https://github.com/oragono/oragono/archive/v2.3.0.tar.gz\
&& tar -xzf v2.3.0.tar.gz\
&& cd oragono-2.3.0\
&& mv default.yaml ircd.yaml\
&& sed -i 's/^\(\s*\)\"127.0.0.1:6667\":.*$/\1":6667":/' ircd.yaml\
&& sed -i 's/^\s*\"\[::1\]:6667\":.*$//' ircd.yaml\
&& make build\
&& ./oragono mkcerts

EXPOSE 6666/tcp 6667/tcp 6697/tcp

WORKDIR /oragono-2.3.0/

ENTRYPOINT ["./oragono", "run"]

# sudo docker run --net=IRC -it server