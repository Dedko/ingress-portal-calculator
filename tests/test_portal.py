# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(scope="module")
def portal():
    from ipc.portal import Portal
    return Portal()


def test_neutralized_portal_level_is_1(portal):
    assert portal.level == 1


def test_portal_level(portal):
    portal.resonators = (8, 7, 6, 6, 5, 5, 4, 4)
    assert portal.level == 5