FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y\
&& apt-get upgrade -y\
&& apt-get install build-essential python-dev libnetfilter-queue-dev tshark tcpdump python3-pip wireshark git -y\
&& pip3 install git+https://github.com/kti/python-netfilterqueue\
&& pip3 install polymorph

ENTRYPOINT ["polymorph"]


#sudo docker run --net=IRC -it poly