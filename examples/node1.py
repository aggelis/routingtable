import json
import asyncio

from node import Node
from contact import Contact

# event loop
loop = asyncio.get_event_loop()

with open('node1.json', 'r') as f:
    node_config = json.load(f)

node = Node(
    loop,
    id = node_config['id'],
    listen_host = node_config['listen_host'],
    listen_port = node_config['listen_port'],
    bootstrap = node_config.get('bootstrap', False),
)

for cd in node_config['contacts']:
    c = Contact(**cd)
    node.rt.add_contacts.add(c)

# run loop
loop.run_forever()
loop.close()