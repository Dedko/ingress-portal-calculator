# -*- coding: utf-8 -*-
from enum import IntEnum

RESONATOR_ENERGY = {1: 1000, 2: 1500, 3: 2000, 4: 2500, 5: 3000, 6: 4000, 7: 5000, 8: 6000}  # Lv: XM


class MultiHack(IntEnum):
    common = 4
    rare = 8
    very_rare = 12
