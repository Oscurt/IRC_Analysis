FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y\
&& apt-get upgrade -y\
&& apt-get install build-essential python-dev libnetfilter-queue-dev tshark tcpdump python3-pip wireshark git net-tools iptables vim -y\
&& pip3 install git+https://github.com/kti/python-netfilterqueue\
&& pip3 install polymorph==1.0.3

COPY utils.patch /usr/local/lib/python3.8/dist-packages/polymorph/
RUN cd /usr/local/lib/python3.8/dist-packages/polymorph/; patch < utils.patch

COPY preconditions /usr/local/lib/python3.8/dist-packages/polymorph/conditions/preconditions/
COPY postconditions /usr/local/lib/python3.8/dist-packages/polymorph/conditions/postconditions/

ENTRYPOINT [ "polymorph" ]

# sudo docker run --net=IRC -it poly
# spoof -t 172.18.0.2 -g 172.18.0.3 // la primera es la IP del server, la otra del cliente.
# capture -f irc