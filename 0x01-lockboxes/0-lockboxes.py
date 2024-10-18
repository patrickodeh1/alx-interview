#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """ unlock all boxes """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    stack = [0]
    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if not opened[key]:
                opened[key] = True
                stack.append(key)

    return all(opened)
