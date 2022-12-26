#!/bin/bash -e

udevadm control --reload-rules
udevadm trigger --subsystem-match=usb --attr-match=idVendor=06a3 --action=add
