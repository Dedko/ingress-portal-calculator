# -*- coding: utf-8 -*-
import pytest

from ipc.items import MultiHack as MH


@pytest.fixture(scope="function")
def portal():
    from ipc.portal import Portal
    return Portal()


def test_neutralized_portal_level_is_1(portal):
    assert portal.level == 1


@pytest.mark.parametrize("resonators,expected", [
    ([8, 7, 6, 6, 5, 5, 4, 4], 5),
    ([8, 7, 1, None, None, None, None, None], 2),
    ([None] * 8, 1)
])
def test_portal_level(portal, resonators, expected):
    portal.resonators = resonators
    assert portal.level == expected


def test_set_resonator(portal):
    portal.resonators[0] = 1
    assert portal.resonators == [1, None, None, None, None, None, None, None]

@pytest.mark.parametrize("resonators,expected", [
    ([8, 7, 6, 6, 5, 5, 4, 4], 30000),
    ([8] * 8, 48000),
    ([None] * 8, 0)
])
def test_portal_energy(portal, resonators, expected):
    portal.resonators = resonators
    assert portal.energy == expected


@pytest.mark.parametrize("resonators,expected", [
    ([8] * 8, 655360),
    ([1] * 8, 160),
    ([8, 7, 6, 6, 5, 5, 4, 4], 160180),
    ([None] * 8, 0)
])
def test_portal_range(portal, resonators, expected):
    portal.resonators = resonators
    assert portal.range == expected


@pytest.mark.parametrize("mods,expected", [
    ([MH.very_rare] * 4, 34),
    ([MH.very_rare, MH.rare, MH.rare, MH.common], 26),
    ([MH.very_rare, None, None, None], 16),
    ([None] * 4, 4)
])
def test_portal_hacks_befor_burnout(portal, mods, expected):
    portal.mods = mods
    assert portal.hacks_before_burnout() == expected