#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, with_statement,
    unicode_literals
)


class Yapps(object):
    """ Yahtzee Advanced Pick & Place System


    """

    def __init__(self, argumentName, anOptionalArg=None):
        """Initialization method.

        :param argumentName: an example argument.
        :type argumentName: string
        :param anOptionalArg: an optional argument.
        :type anOptionalArg: string
        :returns: New instance of :class:`Yapps`
        :rtype: Yapps

        """

        self.instanceVariable1 = argumentName

        if self.aClassVariable:
            print('Hello')

        if anOptionalArg:
            print('anOptionalArg: %s' % anOptionalArg)
