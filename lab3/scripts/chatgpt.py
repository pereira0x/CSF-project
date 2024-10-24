#!/usr/bin/env python3
from utils import *

FILTER_RULE = f'http.proxy_connect_host == "ab.chatgpt.com"'
CAPTURE_FIELDS = ['http2.data.data']

packet_data = run_tshark(FILTER_RULE, CAPTURE_FIELDS)

for entry in packet_data:
    for hex_str in entry.split(","):
        encoded_data = hex_str
        try:
            decoded_data = bytes.fromhex(encoded_data)
            print(decoded_data)
        except:
            pass
