# Examples of integration of MQTT and Hecuba
In this repository, we are storing a few examples of how to integrate Hecuba and MQTT.
The code in this repository uses [Hecuba](github.com/bsc-dd/hecuba) to store the 
messages received into Cassandra. 
We use paho-mqtt as python driver to connect to the mosquitto server. In this example,
we will use the test server provided by  Mosquitto, https://test.mosquitto.org. 
To serialize objects, we use pydantic, that allows defining a schema of the object to 
serialize using Python3's hint system. 


## Requirements and installation
The code has been tested with Python 3. To install, you can type:
```bash
pip3 install -r requirements.txt
python3 setup.py install --user
```
The code requires to connect to an Apache Cassandra cluster. You can either configure the 
entry point by setting the system variable "CONTACT_NAMES", or run Cassandra locally. 


## Bank example 
In this example, we are simulating a producer (bank_producer) that emits log information 
about possible bank activities performed by users. 
The receiver (bank_receiver), receives the message, validate its format and store it in 
Cassandra
### How to run the example:

```bash
#To start the producer
python3 hecuba_mqtt/bank_example/bank_producer.py 

#To start the consumer, open a new terminal and type. 
python3 hecuba_mqtt/bank_example/bank_receiver.py 

# Check options with --help
python hecuba_mqtt/bank_example/bank_receiver.py  --help # same options for bank_producter.py
Usage: bank_receiver.py [OPTIONS]

Options:
  --password TEXT  MQTT password
  --username TEXT  MQTT username
  --hostname TEXT  MQTT server hostname
  --port INTEGER   MQTT server port
  --help           Show this message and exit.

```

