# finbot_rpc_server
========================

## Requirements

To run finbot_rpc_server you'll need `pika` and other libraries,
install the requirements using:

    pip install -r requirements.txt


## finbot_rpc_server

finbot_rpc_server needs [rabbitMQ] up and running:

Instruction on how to install rabbitMQ here:
    
    https://www.rabbitmq.com/download.html

Them to start rabbitMQ run:
    
    rabbitmq-server

To finally start finbot_rpc_server run:

    python finbot_rpc_server.py