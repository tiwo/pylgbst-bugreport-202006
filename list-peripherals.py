"""
liste-die-peripherie.py
"""

from pylgbst import get_connection_auto
from pylgbst.hub import MoveHub

import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

import os

hub_mac = os.environ.get("HUB_MAC", None)

conn = get_connection_auto(hub_mac=hub_mac)
log.info("===> get_connection_auto(hub_mac=%r) returned %r" % (hub_mac, conn))
hub = MoveHub(connection=conn)
log.info("===> Movehub instance: %r" % hub)

for device in hub.peripherals:
    print(device)
