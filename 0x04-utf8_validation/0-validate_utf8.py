#!/usr/bin/python3
"""
utf 8 validation module
"""


def num_bytes_required(num):
    """
    returns the number of bytes required to represent the number in utf-8
    """
    if num <= 127:
        return 1
    elif num <= 223:
        return 2
    elif num <= 239:
        return 3
    return 4


def get_next_char_seq(sequence, value):
    """
    returns the next bytes in the sequence
    """
    num_bytes = num_bytes_required(value)
    char_seq = []
    for _ in range(num_bytes):
        if len(sequence) == 0:
            return None
        char = sequence[0]
        sequence = sequence[1:]
        char_seq.append(char)
    return char_seq


def is_seq_valid_utf8(sequence):
    """
    returns True if the sequence is a valid utf-8 encoding
    """
    if len(sequence) == 1:
        return sequence[0] <= 127

    return all([bin(num >> 6)[2:] == "10" for num in sequence[1:]])


def validUTF8(data):
    """
    validates a given data set represents a valid utf-8 encoding
    the data set contains list of integers
    """
    if data is None:
        return False

    while len(data) > 0:
        seq = get_next_char_seq(data, data[0])
        if seq is None or not is_seq_valid_utf8(seq):
            return False
        data = data[len(seq):]
    return True
