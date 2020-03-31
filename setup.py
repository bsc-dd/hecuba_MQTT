#!/usr/bin/env python3
from setuptools import setup


def setup_packages():
    # compute which libraries were built
    metadata = dict(name="Hecuba_MQTT",
                    version="0.0.1",
                    python_requires='>=3.6.10',
                    packages=['hecuba_mqtt', 'hecuba_mqtt.bank_example'],
                    zip_safe=False,
                    license="Apache License Version 2.0",
                    keywords="key-value, scientific computing",
                    description='Examples of MQTT and Hecuba integration',
                    author='Cesare Cugnasco',
                    author_email='cesare.cugnasco@bsc.es',
                    url='https://www.bsc.es',
                    long_description='''Example codes of the connection between Hecuba and MQTT.'''
                    )

    setup(**metadata)
    return


if __name__ == '__main__':
    setup_packages()
