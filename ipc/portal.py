# -*- coding: utf-8 -*-

RESONATOR_ENERGY = {1: 1000, 2: 1500, 3: 2000, 4: 2500, 5: 3000, 6: 4000, 7: 5000, 8: 6000}  # Lv: XM


class Portal(object):

    def __init__(self):
        self.resonators = [None] * 8

    @property
    def level(self):
        resonators = [r for r in self.resonators if r]
        if not resonators:
            return 1
        return sum(filter(lambda r: r is not None, self.resonators)) // 8

    @property
    def energy(self):
        return sum(RESONATOR_ENERGY[r] for r in self.resonators if r)