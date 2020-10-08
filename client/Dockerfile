FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y\
&& apt-get upgrade -y\
&& apt-get install build-essential -y\
&& apt-get install wget -y\
&& apt-get install clang -y\
&& apt-get install cmake -y\
&& apt-get install pkg-config -y\
&& apt-get install libncursesw5-dev -y\
&& apt-get install libcurl4-gnutls-dev -y\
&& apt-get install clang -y\
&& apt-get install clang -y\
&& apt-get install zlib1g-dev -y\
&& apt-get install libgcrypt20-dev -y\
&& apt-get install libgnutls28-dev -y\
&& apt-get install gettext -y\
&& apt-get install ca-certificates -y\
&& apt-get install libaspell-dev -y\
&& apt-get install python3-dev -y\
&& apt-get install libperl-dev -y\
&& apt-get install ruby -y\
&& apt-get install ruby-dev -y\
&& apt-get install liblua5.3-dev -y\
&& apt-get install tcl-dev -y\
&& apt-get install guile-2.0-dev -y\
&& apt-get install libv8-dev -y\
&& apt-get install php-dev -y\
&& apt-get install libphp-embed -y\
&& apt-get install libxml2-dev -y\
&& apt-get install libargon2-0-dev -y\
&& apt-get install libsodium-dev -y\
&& apt-get install asciidoctor -y\
&& apt-get install libcpputest-dev -y\
&& wget https://github.com/weechat/weechat/archive/v2.9.tar.gz\
&& tar -xzf v2.9.tar.gz\
&& cd weechat-2.9\
&& mkdir build\
&& cd build\
&& cmake ..\
&& make\
&& make install

EXPOSE 6666/tcp 6667/tcp 6697/tcp

ENTRYPOINT ["weechat"]

# sudo docker run --net=IRC -it client