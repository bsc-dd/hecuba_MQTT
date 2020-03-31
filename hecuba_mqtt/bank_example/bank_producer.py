import paho.mqtt.publish as publish
import time
from random import randint
from datetime import date
from hecuba_mqtt.bank_example.data_model import IPlogJSON

OPERATIONS = ['LOGIN', 'LOGOUT', 'DEPOSIT', 'TRANSFER']


def produce():
    while True:
        time.sleep(randint(0, 10))
        log = IPlogJSON(
            FK_NUMPERSO=randint(0, 10000),
            PK_ANYOMESDIA=str(date.today()),
            IP_TERMINAL='%d.%d.%d.%d' % (randint(0, 254), randint(0, 254), randint(0, 254), randint(0, 254)),
            FK_COD_OPERACION=OPERATIONS[randint(0, len(OPERATIONS) - 1)]
        )

        publish.single("hecuba/bank_case", log.json(), port=1883, hostname="test.mosquitto.org")
        print("published %s" % (str(log)))


if __name__ == "__main__":
    produce()
