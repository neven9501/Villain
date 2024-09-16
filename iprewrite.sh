#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <file_path> <ip_address>"
    exit 1
fi

file_path=$1
ip_address=$2

# Check if the file exists
if [ ! -f "$file_path" ]; then
    echo "The file $file_path does not exist."
    exit 1
fi

# Use sed to replace *LHOST* with the provided IP address
sed -i "s/\*LHOST\*/$ip_address/g" "$file_path"

echo "Replaced '*LHOST*' with '$ip_address' in $file_path."
