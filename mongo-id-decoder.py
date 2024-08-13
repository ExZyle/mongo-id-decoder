#!/usr/bin/env python3
import bson
import sys

def decode_object_id(oid_str):
    # Convert the string ObjectId to a BSON ObjectId
    try:
        oid = bson.ObjectId(oid_str)
    except bson.errors.InvalidId:
        print("Invalid ObjectId format. Please provide a valid 24-character hexadecimal string.")
        return

    # Extract the timestamp (first 4 bytes)
    timestamp = oid.generation_time

    # Extract the machine identifier (next 3 bytes)
    machine_id = oid.binary[4:7].hex()

    # Extract the process identifier (next 2 bytes)
    process_id = int.from_bytes(oid.binary[7:9], byteorder='big')

    # Extract the counter (last 3 bytes)
    counter = int.from_bytes(oid.binary[9:12], byteorder='big')

    # Print the details
    print(f"ObjectId: {oid_str}")
    print(f"Timestamp: {timestamp} (UTC)")
    print(f"Machine Identifier: {machine_id}")
    print(f"Process Identifier: {process_id}")
    print(f"Counter: {counter}")

def main():
    if len(sys.argv) > 1:
        object_id_str = sys.argv[1]
    else:
        object_id_str = input("Enter a MongoDB ObjectId: ")
    
    decode_object_id(object_id_str)

if __name__ == "__main__":
    main()
