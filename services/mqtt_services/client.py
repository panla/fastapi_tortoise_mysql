"""
pip install paho-mqtt
"""

import json
import ssl
from typing import Any

from paho.mqtt.client import Client, MQTTv311, MQTTv5
from paho.mqtt.subscribeoptions import SubscribeOptions
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes

from extensions import logger


class MqttClient:
    def __init__(
            self,
            host: str,
            port: int,
            client_id: str,
            username: str,
            password: str,
            keep_alive: int = 600,
            version: int = MQTTv311,
            properties: Properties = None,
            ca_cert: str = None,
            cert_path: str = None,
            key_path: str = None,
            keyfile_passwd: str = None
    ) -> None:
        """__init__

        Args:
            host (str): MQTT Server Host.
            port (int): MQTT Server Port.
            client_id (str): Client ClienID.
            username (str): Client UserName.
            password (str): Client Password.
            keep_alive (int, optional): MQTT Connect KeepAlive.
            version (int, optional): MQTT Version. Defaults to MQTTv311.
            properties (Properties, optional): when MQTTv5 use this. Defaults to None.
            ca_cert (str, optional): TLS CA cert file. Defaults to None.
            cert_path (str, optional): TLS Client cert path. Defaults to None.
            key_path (str, optional): TLS Client key path. Defaults to None.
            keyfile_passwd (str, optional): TLS Client key password. Defaults to None.
        """

        self._host = host
        self._port = port
        self.client_id = client_id
        self.username = username
        self.password = password
        self._keep_alive = keep_alive
        self.version = version
        self.properties = properties
        self._ca_cert = ca_cert
        self._cert_path = cert_path
        self._key_path = key_path
        self._keyfile_passwd = keyfile_passwd

        self.unique = self.client_id or self.username

        self.client = Client(client_id=self.client_id, protocol=version)
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_subscribe = self.on_subscribe
        self.client.on_unsubscribe = self.on_unsubscribe
        # self.client.on_publish = self.on_publish
        self.client.on_message = self.on_message

    def set_ssl_context(self):
        """set SSL context to use SSL"""

        if self.ca_cert and self.client_cert and self.client_key:
            context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS)
            context.check_hostname = False
            context.load_cert_chain(certfile=self.client_cert, keyfile=self.client_key, password=self.keyfile_passwd)
            context.load_verify_locations(self.ca_cert)
            context.verify_mode = ssl.CERT_REQUIRED

            self.client.tls_set_context(context=context)

    @staticmethod
    def set_properties(version: int, params: dict):

        if version in [MQTTv5]:
            properties = Properties(packetType=PacketTypes.CONNECT)
            for key, value in params.items():
                setattr(properties, key, value)
            return properties
        return None

    def connect(self):
        """Verify and Connect to a remote broker."""

        self.client.username_pw_set(self.username, self.password)
        self.set_ssl_context()

        return self.client.connect(self.host, self.port, self.keep_alive, properties=self.properties)

    def disconnect(self, rc: int = None):
        """Disconnect a connected client from the broker.
        rc: (MQTT v5.0 only) a ReasonCodes instance setting the MQTT v5.0
        rc to be sent with the disconnect.  It is optional, the receiver
        then assuming that 0 (success) is the value.
        """

        return self.client.disconnect(rc, properties=self.properties)

    def loop_start(self):
        """loop start"""

        self.client.loop_start()

    def loop_stop(self):
        """loop stop"""

        self.client.loop_stop()

    def loop_forever(self):
        """loop forever"""

        self.client.loop_forever()

    def add_callback(self, topic, callback):
        """Register a message callback for a specific topic."""

        self.client.message_callback_add(topic, callback)

    def subscribe(self, topic: str, qos: int = 0, options: SubscribeOptions = None):
        """Subscribe the client to one or more topics.

        options
            if MQTTv311 then None
            if MQTTv5 then example options=SubscribeOptions(qos=2)
        """

        return self.client.subscribe(topic, qos=qos, options=options, properties=self.properties)

    def unsubscribe(self, topic: str):
        """Unsubscribe the client to one or more topics."""

        return self.client.unsubscribe(topic=topic, properties=self.properties)

    def publish(self, topic, payload=None, qos: int = 0, retain: bool = False, flag: bool = True):
        """Publish a message on a topic."""

        logger.info(f'publish topic {topic}'.center(60, '*'))
        if flag:
            payload = json.dumps(payload, ensure_ascii=False)

        return self.client.publish(
            topic=topic, payload=payload, qos=qos, retain=retain, properties=self.properties
        )

    def on_connect(self, client: Client, userdata: Any, flags: dict, rc: int, properties: Properties = None):
        """Define the connected callback implementation."""

        logger.info(f'{self.unique} on_connect flags {flags} result code: {rc}'.center(60, '*'))

    def on_disconnect(self, client: Client, userdata: Any, rc: int, properties: Properties = None):
        """If implemented, called when the client disconnects from the broker."""

        logger.info(f'{self.unique} on_disconnected rc {rc}'.center(60, '*'))

    def on_subscribe(self, client: Client, userdata: Any, mid: int, granted_qos: tuple, properties: Properties = None):
        """Define the subscribed callback implementation."""

        logger.info(f'{self.unique} on_subscribe: mid {mid} granted_qos = {granted_qos}'.center(60, '*'))

    def on_unsubscribe(self, client: Client, userdata: Any, mid: int, properties: Properties = None):
        """Define the unsubscribe callback implementation."""

        logger.info(f'{self.unique} on_unsubscribe: mid = {mid}'.center(60, '*'))

    def on_publish(self, client: Client, userdata: Any, mid: int, properties: Properties = None):
        """Define the published message callback implementation."""

        logger.info(f'{self.unique} on_publish: mid = {mid}'.center(60, '*'))

    def on_message(self, client: Client, userdata: Any, msg, properties: Properties = None):
        """Define the message received callback implementation. use this when can`t match message_callback_add"""

        logger.info(f'{self.unique} on_message topic {msg.topic}'.center(60, '*'))
        payload = msg.payload.decode('utf-8')
        logger.info(payload)
