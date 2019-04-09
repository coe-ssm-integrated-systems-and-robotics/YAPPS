#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Dice(object):
    """
    This class is used to store information about
    a dice that is detected on the grid.
    """

    def __init__(self, x, y, top_face):
        """
        This initializes the values of a detected dice.

        :param row: The where the dice
        """
        self.x = x
        self.y = y
        self.top_face = top_face


class Grid(object):
    def __init__(self, dice):
        self.dice = dice
