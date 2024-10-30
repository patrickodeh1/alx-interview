#!/usr/bin/python3
"""
Function to validate UTF-8 encoding in a dataset
"""


def validUTF8(data):
    # Number of bytes remaining in the current UTF-8 character
    num_bytes = 0

    # Masks to check the leading bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Mask to get only the last 8 bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte & mask1) == 0:
                continue
            elif (byte & (mask1 >> 1)) == (mask1 >> 1):
                num_bytes = 1
            elif (byte & (mask1 >> 2)) == (mask1 >> 2):
                num_bytes = 2
            elif (byte & (mask1 >> 3)) == (mask1 >> 3):
                num_bytes = 3
            else:
                return False
        else:
            # Check if the byte is a valid continuation byte
            if (byte & mask1) != mask1 or (byte & mask2) == 0:
                return False
        num_bytes -= 1

    return num_bytes == 0
