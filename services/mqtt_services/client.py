"""
pip install paho-mqtt
"""

import json

from paho.mqtt.client import Client

from extensions import logger


class MqttClient:
    def __init__(self) -> None:
        self.client = Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish
        self.client.on_disconnect = self.on_disconnect
        self.client.on_unsubscribe = self.on_unsubscribe
        self.client.on_subscribe = self.on_subscribe

    def connect(self, host: str, port: int, user: str, passwd: str, keepalive: int = 600):
        """connect server"""

        # set user passwd
        self.client.username_pw_set(user, passwd)
        # connect
        self.client.connect(host=host, port=port, keepalive=keepalive)

    def loop_start(self):
        """loop start"""

        self.client.loop_start()

    def loop_forever(self):
        """loop forever"""

        self.client.loop_forever()

    def subscribe(self, topic: str):
        """subscribe topic"""

        self.client.subscribe(topic)

    def publish(self, topic, msg, qos=0, retain=False, properties=None):
        """publish msg"""

        payload = json.dumps(msg, ensure_ascii=False)
        self.client.publish(topic=topic, payload=payload, qos=qos, retain=retain, properties=properties)

    def add_callback(self, topic, callback):
        """message_callback_add"""

        self.client.message_callback_add(topic, callback)

    def on_connect(self, client, userdata, flags, rc):
        """连接事件"""

        logger.info('on_connect'.center(40, '*'))
        logger.info(f'Connected with result code: {rc}')

    def on_disconnect(self, client, userdata, rc):
        """断开连接事件"""

        # logger.info('on_disconnect'.center(40, '*'))
        # logger.info('Unexpected disconnected rc = {rc}')
        pass

    def on_subscribe(self, client, userdata, mid, granted_qos):
        """订阅事件"""

        logger.info('on_subscribe'.center(40, '*'))
        logger.info(f'on_subscribe: qos = {granted_qos}')

    def on_unsubscribe(self, client, userdata, mid):
        """取消订阅事件"""

        # logger.info('on_unsubscribe'.center(40, '*'))
        # logger.info('on_unsubscribe: qos = {granted_qos}')
        pass

    def on_publish(self, client, userdata, mid):
        """发布消息事件"""

        logger.info('on_publish'.center(40, '*'))
        logger.info(f'on_publish: mid = {mid}')

    def on_message(self, client, userdata, msg):
        """获得消息事件，触发动作，匹配不到 message_callback_add 时使用这个"""

        logger.info('on_message'.center(40, '*'))
        payload = msg.payload.decode('utf-8')
        logger.info(f'on_message topic: {msg.topic}')
        logger.info(payload)
