# -*- coding: utf-8 -*-
import pytest


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
def test_portal_linkable_range(portal, resonators, expected):
    portal.resonators = resonators
    assert portal.linkable_range == expected


@pytest.mark.parametrize("multi_hacks,expected", [
    ([12] * 4, 34),       # VRMH * 4
    ([12, 8, 8, 4], 26),  # VRMH / RMH * 2 / CMH
    ([12], 16),           # VRMH * 1
    ([], 4)               # No MH
])
def test_portal_hacks_befor_burnout(portal, multi_hacks, expected):
    portal._installed_multi_hacks = multi_hacks
    assert portal.hacks_before_burnout() == expected
    
    
@pytest.mark.parametrize("heat_shinks,expected", [
    ([70] * 4, 24),       # VRHS * 4
    ([70, 50, 50, 20], 45),  # VRHS / RHS * 2 / CHS
    ([70], 90),           # VRHS * 1
    ([], 300)               # No HS
])
def test_portal_cool_down(portal, heat_shinks, expected):
    portal._installed_heat_sinks = heat_shinks
    assert portal.cooldown() == expected


@pytest.mark.parametrize("resonators,link_amps,expected", [
    ([1] * 8, [], 160),
    ([1] * 8, [2], 320),
    ([1] * 8, [2, 2], 400),
    ([1] * 8, [2, 2, 2], 440),
    ([1] * 8, [2, 2, 2, 2], 480),
    ([8] * 8, [], 655360),
    ([8] * 8, [7, 2, 2, 2], 5242880),
    ([8] * 8, [7, 7, 2, 2], 6062080),
    ([8] * 8, [7, 7, 7, 2], 6471680),
    ([8] * 8, [7, 7, 7, 7], 6881280),
])
def test_portal_linkable_range(portal, resonators, link_amps, expected):
    portal.resonators = resonators
    portal._installed_link_amps = link_amps
    assert portal.linkable_range == expected