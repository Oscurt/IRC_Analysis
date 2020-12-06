FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y\
&& apt-get upgrade -y\
&& apt-get install build-essential python-dev libnetfilter-queue-dev tshark tcpdump python3-pip wireshark git net-tools iptables vim gedit nano linux-modules-5.4.0-53-generic kmod -y\
&& pip3 install git+https://github.com/kti/python-netfilterqueue\
&& pip3 install polymorph 
# RUN modprobe ip6table_filter

#COPY utils.py /usr/local/lib/python3.8/dist-packages/polymorph/
COPY functions /usr/local/lib/python3.8/dist-packages/polymorph/functions/

ENTRYPOINT [ "polymorph" ]

# sudo docker run --privileged --net=IRC -it poly
# spoof -t 172.18.0.2 -g 172.18.0.3 // la primera es la IP del server, la otra del cliente.
# capture -f irc