# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(scope="module")
def portal():
    from ipc.portal import Portal
    return Portal()


def test_neutralized_portal_level_is_1(portal):
    assert portal.level == 1