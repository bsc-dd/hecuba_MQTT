import paho.mqtt.client as mqtt
from hecuba_mqtt.bank_example.data_model import IPlogJSON, IPlogs


def receive():
    client = mqtt.Client()
    log_repository = IPlogs('test.iplogs')

    def on_connect(client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe("hecuba/bank_case")

    client.on_connect = on_connect

    def on_message(client, userdata, msg):
        log = IPlogJSON.parse_raw(msg.payload)
        log_repository[(log.FK_NUMPERSO, log.PK_ANYOMESDIA)] = [log.IP_TERMINAL, log.FK_COD_OPERACION]
        print("record for %s stored" % (log.FK_NUMPERSO))

    client.on_message = on_message

    client.connect("test.mosquitto.org", 1883, 60)

    client.loop_forever()


if __name__ == "__main__":
    receive()