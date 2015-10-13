# -*- coding: utf-8 -*-


class Portal(object):

    def __init__(self):
        self.resonators = [None] * 8

    @property
    def level(self):
        if not all(self.resonators):
            return 1
        return sum(filter(lambda r: r is not None, self.resonators)) // 8
