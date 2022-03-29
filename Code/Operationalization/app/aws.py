import json
import time
from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder 

class Aws():

    def __init__(self, settings):
        self.settings = settings
        self.connect_aws_iot_core()

    def connect_aws_iot_core(self):
        event_loop_group= io.EventLoopGroup(1)
        host_resolver = io.DefaultHostResolver(event_loop_group)
        client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
        
        self.mqtt_connection = mqtt_connection_builder.mtls_from_path(
            endpoint = self.settings["ENDPOINT"],
            cert_filepath = self.settings["PATH_TO_CERTIFICATE"],
            pri_key_filepath = self.settings["PATH_TO_PRIVATE_KEY"],
            ca_filepath = self.settings["PATH_TO_AMAZON_ROOT_CA_1"],
            client_bootstrap = client_bootstrap,
            client_id = self.settings["CLIENT_ID"],
            clean_session = False,
            keep_alive_secs = 6
        )

        self.connection_feature = self.mqtt_connection.connect()
        self.connection_feature.result()
        
        return self.mqtt_connection, self.connection_feature

    def publish(self, message="", t=1):
        print(f"Sending Message {message}")
        self.mqtt_connection.publish(
            topic=self.settings["TOPIC"],
            payload=json.dumps(message),
            qos=mqtt.QoS.AT_LEAST_ONCE
        )
        print(F"Message Send")
        time.sleep(t)
        disconnect_future = self.mqtt_connection.disconnect()
        disconnect_future.result()
