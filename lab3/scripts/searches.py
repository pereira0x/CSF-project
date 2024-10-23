#!/usr/bin/env python3
from utils import *

# Define filter for tshark to capture specific HTTP traffic
HTTP_FILTER = f'http.path_segment == "/search" and ip.dst == {resolve_host("Router")}'
EXTRACTED_FIELDS = ['ip.src', 'frame.time_epoch', 'http2.headers.path']

# Run tshark to capture the filtered data
captured_data = run_tshark(HTTP_FILTER, EXTRACTED_FIELDS)

# Process each captured line
for record in captured_data:
    src_ip, timestamp, search_path = record.split('\t')
    
    # Extract search query parameter
    search_query = extract_urlencoded_parameter(search_path, 'q')
    
    # Convert the epoch timestamp to a formatted date
    message_time = datetime.datetime.fromtimestamp(float(timestamp))
    adjusted_time = message_time - datetime.timedelta(weeks=4.71428571)  # Same logic as in the original convert_time function
    formatted_time = adjusted_time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Output the result
    print(f"Source IP: {src_ip}, Search Query: {search_query}, Time: {formatted_time}")

