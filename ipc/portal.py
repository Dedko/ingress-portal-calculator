# -*- coding: utf-8 -*-
from statistics import mean
from .items import RESONATOR_ENERGY, MultiHack

class Portal(object):

    def __init__(self):
        self.resonators = [None] * 8
        self.mods = [None] * 4
        self._installed_multi_hacks = []
        self._installed_heat_sinks = []

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

    def _get_effective_values(self, mods):
        """インストール済みMODの種類別での影響値を取得"""
        mods = sorted(mods, reverse=True)
        if not mods:
            return []
        most_rate = mods[:1]
        rest_of_mods = [mod / 2 for mod in mods[1:]]
        return most_rate + rest_of_mods

    def hacks_before_burnout(self):
        count = 4
        for mh in self._get_effective_values(self._installed_multi_hacks):
            count += mh
        return count

    def cool_down(self):
        cool_down_time = 300
        for hs in self._get_effective_values(self._installed_heat_sinks):
            cool_down_time *= (100 - hs) / 100
        return int(cool_down_time)

