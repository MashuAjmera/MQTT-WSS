const connectb = document.getElementById("connect");
const subscribeb = document.getElementById("subscribe");
const publishb = document.getElementById("publish");
const disconnectb = document.getElementById("disconnect");

//Using the HiveMQ public Broker, with a random client Id
var client = new Messaging.Client(
  "localhost",
  9001,
  "myclientid_" + parseInt(Math.random() * 100, 10)
);

//Gets  called if the websocket/mqtt connection gets disconnected for any reason
client.onConnectionLost = function (responseObject) {
  //Depending on your scenario you could implement a reconnect logic here
  alert("connection lost: " + responseObject.errorMessage);
};

//Gets called whenever you receive a message for your subscriptions
client.onMessageArrived = function (message) {
  //Do something with the push message you received
  document
    .getElementById("messages")
    .append(
      "<span>Topic: " +
        message.destinationName +
        "  | " +
        message.payloadString +
        "</span><br/>"
    );
};


//Creates a new Messaging.Message Object and sends it to the HiveMQ MQTT Broker
var publish = function (payload, topic, qos) {
  //Send your message (also possible to serialize it as JSON or protobuf or just use a string, no limitations)
  var message = new Messaging.Message(payload);
  message.destinationName = topic;
  message.qos = qos;
  client.send(message);
};

function connect(){

//Connect Options
var options = {
  timeout: 3,
  useSSL: true,
  //Gets Called if the connection has sucessfully been established
  onSuccess: function () {
    alert("Connected");
  },
  //Gets Called if the connection could not be established
  onFailure: function (message) {
    alert("Connection failed: " + message.errorMessage);
  },
};
client.connect(options);
}

connectb.addEventListener("click", connect);

