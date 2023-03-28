#!/usr/bin/python3
"""
0-lockboxes
"""

import pprint


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened
    """
    if not len(boxes):
        return True
    boxes = list(map(lambda box: {'locked': True, 'keys': box}, boxes))
    unlockBoxes(boxes, 0)
    return len(list(filter(lambda box: box.get('locked'), boxes))) == 0


def unlockBoxes(boxes, key):
    """
    unlocks boxes recursively
    """
    isLocked = boxes[key].get('locked')
    if isLocked:
        boxes[key].update({'locked': False})
        pprint.pprint(boxes)
        keys = boxes[key].get('keys')
        for _key in keys:
            unlockBoxes(boxes, _key)
