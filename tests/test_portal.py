# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(scope="function")
def portal():
    from ipc.portal import Portal
    return Portal()


def test_neutralized_portal_level_is_1(portal):
    assert portal.level == 1


@pytest.mark.parametrize("input,expected", [
    ([8, 7, 6, 6, 5, 5, 4, 4], 5),
    ([8, 7, 1, None, None, None, None, None], 2),
    ([None] * 8, 1)
])
def test_portal_level(portal, input, expected):
    portal.resonators = input
    assert portal.level == expected


def test_set_resonator(portal):
    portal.resonators[0] = 1
    assert portal.resonators == [1, None, None, None, None, None, None, None]