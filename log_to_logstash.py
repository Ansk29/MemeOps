import logging
import socket
import json
import time

# GELF format log handler
class GELFHandler(logging.Handler):
    def __init__(self, host, port):
        logging.Handler.__init__(self)
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def emit(self, record):
        log_message = self.format(record)
        gelf_message = {
            "short_message": log_message,
            "level": record.levelno,
            "host": record.name,
            "_id": "random_id_12345",  # You can change this or make it unique
            "version": "1.1",
            "source_host": "192.168.16.1"  # Replace with your actual host IP
        }
        self.socket.sendto(json.dumps(gelf_message).encode(), (self.host, self.port))

# Set up logging
logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)

# Configure the GELF handler to send logs to Logstash
gelf_handler = GELFHandler("localhost", 12201)  # Logstash running on localhost and port 12201
gelf_handler.setFormatter(logging.Formatter('%(message)s'))
logger.addHandler(gelf_handler)

# Example logging loop (could be based on actual events in your application)
while True:
    logger.info("This is an info message.")
    logger.error("This is an error message.")
    time.sleep(5)  # Log every 5 seconds
