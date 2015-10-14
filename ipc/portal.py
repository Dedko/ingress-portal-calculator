# -*- coding: utf-8 -*-
from statistics import mean

RESONATOR_ENERGY = {1: 1000, 2: 1500, 3: 2000, 4: 2500, 5: 3000, 6: 4000, 7: 5000, 8: 6000}  # Lv: XM


class Portal(object):

    def __init__(self):
        self.resonators = [None] * 8

    @property
    def level(self):
        resonators = [r for r in self.resonators if r]
        if not resonators:
            return 1
        return sum(resonators) // 8

    @property
    def energy(self):
        return sum(RESONATOR_ENERGY[r] for r in self.resonators if r)

    @property
    def range(self):
        """
        Portal Range = 160 m * (Average Resonators Level ^ 4)
        """
        resonators = [r for r in self.resonators if r]
        if not resonators:
            return 0
        return int(160 * (mean(resonators) ** 4))