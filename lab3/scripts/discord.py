#!/usr/bin/env python3
import zlib
import json
import datetime
from utils import *

# Filter for capturing websocket traffic
WS_CAPTURE_FILTER = f'websocket && ip.dst == 194.210.61.136 && http.proxy_connect_host == "gateway.discord.gg"'
EXTRACT_FIELDS = ['data.data']

# Suffix used for zlib synchronization
DECOMPRESS_SUFFIX = b'\x00\x00\xff\xff'
# Initialize byte array to accumulate data chunks
data_buffer = bytearray()

captured_data = run_tshark(WS_CAPTURE_FILTER, EXTRACT_FIELDS, extra_flags="-E occurrence=a")

for record in captured_data:
    for hex_chunk in record.split(","):
        byte_chunk = bytes.fromhex(hex_chunk)
        data_buffer += byte_chunk

        # Detect the start of a new compressed data stream
        if byte_chunk.startswith(b"\x78\xda"):
            decompressor = zlib.decompressobj()

        # Process and decompress when a chunk ends with the zlib suffix
        if byte_chunk.endswith(DECOMPRESS_SUFFIX):
            decompressed_data = json.loads(decompressor.decompress(data_buffer))
            if decompressed_data["t"] == "MESSAGE_CREATE":
                message_payload = decompressed_data["d"]
                message_time = datetime.datetime.strptime(message_payload["timestamp"], "%Y-%m-%dT%H:%M:%S.%f%z")
                adjusted_time = message_time - datetime.timedelta(weeks=4.71428571)
                formatted_time = adjusted_time.strftime("%Y-%m-%d %H:%M:%S")
                print(f"{formatted_time} {message_payload['author']['username']}: {message_payload['content']}")
            # Clear buffer for the next data chunk
            data_buffer.clear()

