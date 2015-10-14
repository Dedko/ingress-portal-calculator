# -*- coding: utf-8 -*-
from statistics import mean
from .items import RESONATOR_ENERGY, MultiHack

class Portal(object):

    def __init__(self):
        self.resonators = [None] * 8
        self.mods = [None] * 4
        self._installed_multi_hacks = []

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

    def hacks_before_burnout(self):
        count = 4
        multi_hacks = sorted(self._installed_multi_hacks, reverse=True)
        if multi_hacks:
            count += multi_hacks[0]
            for mh in multi_hacks[1:]:
                count += mh // 2
        return count
