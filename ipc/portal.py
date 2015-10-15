# -*- coding: utf-8 -*-
from statistics import mean

from .items import RESONATOR_ENERGY


class Portal(object):

    def __init__(self):
        self.resonators = [None] * 8
        self.mods = [None] * 4
        self._installed_multi_hacks = []
        self._installed_heat_sinks = []

    @property
    def level(self):
        """ Portal Level
        """
        resonators = [r for r in self.resonators if r]
        if not resonators:
            return 1
        return sum(resonators) // 8

    @property
    def energy(self):
        """ Portal Energy
        """
        return sum(RESONATOR_ENERGY[r] for r in self.resonators if r)

    @property
    def linkable_range(self):
        """ Link linkable_range

        Portal Link Range = 160 m * (Average Resonators Level ^ 4)
        """
        resonators = [r for r in self.resonators if r]
        if not resonators:
            return 0
        return int(160 * (mean(resonators) ** 4))

    def _calc_influence_value_by_mods(self, mods):
        """ Calculate the influence value by MODs
        """
        mods = sorted(mods, reverse=True)
        if not mods:
            return []
        most_rare = mods[:1]
        rest_of_mods = [mod / 2 for mod in mods[1:]]
        return most_rare + rest_of_mods

    def hacks_before_burnout(self):
        """ Return the hack possible number of portal.
        """
        count = 4
        for mh in self._calc_influence_value_by_mods(self._installed_multi_hacks):
            count += mh
        return count

    def cooldown(self):
        """ Return Cooldown decrease.
        """
        seconds = 300
        for hs in self._calc_influence_value_by_mods(self._installed_heat_sinks):
            seconds *= (100 - hs) / 100
        return int(seconds)

