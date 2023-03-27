#!/usr/bin/python3
"""
0-lockboxes
"""


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened given a list of boxes

    Args:
        boxes (list): list of boxes

    Returns:
        bool: True if all boxes can be opened, else False
    """
    keys = [0]
    for key in keys:
        for _key in boxes[key]:
            if _key not in keys and _key < len(boxes):
                keys.append(_key)

    if len(keys) == len(boxes):
        return True
    return False
