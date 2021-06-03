# MQTT-WSS

Install Chrome: `sudo dpkg -i google-chrome-stable_current_amd64.deb`

Install MQTTBox MQTT Client chrome extension

Username password in broker: https://stackoverflow.com/questions/63078589/im-able-to-connect-to-mqtt-broker-running-in-a-container-with-any-client-certif

## Brokers
### Use Public Broker
MQTT Brokers with Websockets to check: http://www.steves-internet-guide.com/mqtt-websockets/

Installing Broker on Docker

Install docker: `sudo apt install snapd \n sudo snap install docker`

Check all Docker container status: `sudo docker ps -a`

Copy file from pc to docker: `sudo docker cp mosquitto.conf 836e6b60e113:/mosquitto/config`

Know IP of docker container: `sudo docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' 836e6b60e113`

Install MQTT Broker on docker: `sudo docker run -it -d -p 1883:1883 eclipse-mosquitto:1.6`

Remove containers: `sudo docker rm 69382c66b297 e5941c21f7c6`

See docker container images: `sudo docker images`

Remove docker images: `sudo docker rmi 0a64a2b6149a`

Setup eclipse mosquito image along with WebSockets: `sudo docker run -it  -d  -p 1883:1883 -p 9001:9001 eclipse-mosquitto`

Execute container: `sudo docker exec -it f320e517eeb9 sh`

Install Vim tex editor in docker: `apk add vim`

Open file: `vim /mosquitto/config/mosquitto.conf`

Edit file: `i`

Under Listerners: `listener 9001` and `protocol websockets`

Under Security: `allow_anonymous true`

Close editing: `Esc` key

Save: `:wq`

Exit: `exit`

`apk add openssl`

`mkdir /mosquitto/certs`

First create a key pair for the CA: `sudo openssl genrsa -des3 -out ca.key 2048`
Password: 12345678
 
Now Create a certificate for the CA using the CA key that we created in step 1: `sudo openssl req -new -x509 -days 1826 -key ca.key -out ca.crt`

Password: 12345678

Common Name: mashuajmera
 
Now we create a server key pair that will be used by the broker
Command is: sudo openssl genrsa -out server.key 2048
 
Now we create a certificate request .csr. When filling out the form the common name is important and is usually the domain name of the server.Because I’m using Windows on a local network I used the Windows name for the computer that is running the Mosquitto broker which is ws4.
Command is: sudo openssl req -new -out server.csr -key server.key
Common Name: localhost
 
Now we use the CA key to verify and sign the server certificate. This creates the server.crt file
Command is:  sudo openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 360
 
listener 9002
protocol websockets
#require_certifiates true
cafile /mosquitto/certs/ca.crt
keyfile /mosquitto/certs/server.key
certfile /mosquitto/certs/server.crt
tls_version tlsv1.2
Allow_anonymous true

Stop docker: sudo docker stop f320e517eeb9
Start docker: sudo docker start f320e517eeb9
Restart docker: sudo docker restart f320e517eeb9
Installing Broker on Ubuntu
Install Mosquitto Broker: sudo install mosquitto
Mosquitto SSL Configuration -MQTT TLS Security (steves-internet-guide.com)
Restart Mosquitto: sudo systemctl restart mosquitto
Allow port: sudo ufw allow 9001

## Clients

### Web Client
Javascript client mosquitto: Using The JavaScript MQTT Client With Websockets
Create MQTT Client: MQTT Web Applications: How to build your own! (hivemq.com)
To enable client certificate: http://www.steves-internet-guide.com/creating-and-using-client-certificates-with-mqtt-and-mosquitto/
In the script file of the client: options.useSSL=true
Change the host and port to the one desired

Firefox Fix: MQTT (wss) Not Connecting in Firefox, Works in Other Browsers

### Terminal Client
It only supports MQTT and MQTT over SSL. It doesn’t support websockets.

sudo apt install mosquitto-clients

Publish with only CA Certificate when require_certificate false
mosquitto_pub --cafile ABB/ca.crt -d -h localhost -p 9005 -t test -m "hello there"
 
Publish with CA and Client certificates when require_certificate true
mosquitto_pub --cafile ABB/ca.crt --cert ABB/client.crt --key ABB/client.key -d -h localhost -p 9005 -t testing -m "hello there588"
 
Subscribe with only CA Certificate when require_certificate false
mosquitto_sub --cafile ABB/ca.crt -h localhost -p 9005 -t test
 
Subscribe with CA and Client certificates when require_certificate true
mosquitto_sub --cafile ABB/ca.crt --cert ABB/client.crt --key ABB/client.key -h localhost -p 9005 -t testing

### Python Client
Make MQTT Client: How to use MQTT in Python (Paho) | EMQ (emqx.io)
Make MQTT with SSL: Mosquitto SSL Configuration -MQTT TLS Security
Websockets with SSL: Using MQTT Over WebSockets with Mosquitto
