# -*- coding: utf-8 -*-


class Portal(object):

    def __init__(self):
        self.resonators = None

    @property
    def level(self):
        if not self.resonators:
            return 1
        return sum(self.resonators) // 8
