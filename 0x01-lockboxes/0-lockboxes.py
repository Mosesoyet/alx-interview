#!/usr/bin/python3
"""
0-lockboxes module
"""


def canUnlockAll(boxes):
    """boxes a list of lists
    unlock each box
    """
    n = [0]
    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in n and key != box_id:
                n.append(key)
    if len(n) == len(boxes):
        return True
    return False
