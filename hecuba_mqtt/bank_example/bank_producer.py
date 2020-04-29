import paho.mqtt.publish as publish
import time
from random import randint
from datetime import date
from hecuba_mqtt.bank_example.data_model import IPlogJSON
import click

OPERATIONS = ['LOGIN', 'LOGOUT', 'DEPOSIT', 'TRANSFER']


@click.command()
@click.option('--password', default=None, help='MQTT password')
@click.option('--username', default=None, help='MQTT username')
@click.option('--hostname', default="test.mosquitto.org", help='MQTT server hostname')
@click.option('--port', default=1883, help='MQTT server port')
def produce(password, username, hostname, port):
    while True:
        time.sleep(randint(0, 10))
        log = IPlogJSON(
            FK_NUMPERSO=randint(0, 10000),
            PK_ANYOMESDIA=str(date.today()),
            IP_TERMINAL='%d.%d.%d.%d' % (randint(0, 254), randint(0, 254), randint(0, 254), randint(0, 254)),
            FK_COD_OPERACION=OPERATIONS[randint(0, len(OPERATIONS) - 1)]
        )

        auth = None if username is None else {'username': username, 'password': password}
        publish.single("hecuba/bank_case", log.json(), port=port, hostname=hostname, auth=auth)
        print("published %s" % (str(log)))


if __name__ == "__main__":
    produce()
