import pytest
from .testLib import fullTest
from girderformindlogger.constants import REPROLIB_CANONICAL

activitySetUrl = ''.join([
    REPROLIB_CANONICAL,
    'activity-sets/ema-hbn/ema-hbn_schema'
])
act1 = ''.join([
    REPROLIB_CANONICAL,
    'activities/EmaHBNEvening/ema_evening_schema'
])
act2 = ''.join([
    REPROLIB_CANONICAL,
    'activities/EmaHBNMorning/ema_morning_schema'
])
act1Item = ''.join([
    REPROLIB_CANONICAL,
    'activities/EmaHBNEvening/items/good_bad_day'
])
act2Item = ''.join([
    REPROLIB_CANONICAL,
    'activities/EmaHBNMorning/items/sleeping_aids'
])

@pytest.mark.parametrize(
    "args",
    [(activitySetUrl, act1, act2, act1Item, act2Item)]
)
def test_1_HBN(args):
    activitySetUrl, act1, act2, act1Item, act2Item = args
    try:
        print('\n\n TEST 1: HBN')
        fullTest(activitySetUrl, act1, act2, act1Item, act2Item)
    except Exception as e:
        print('\n\n ERROR:', e)
        raise e

nestedActivitySet = ''.join([
    REPROLIB_CANONICAL,
    'activity-sets/pediatric-screener/pediatric-screener_schema'
])
nact1 = ''.join([
    REPROLIB_CANONICAL,
    'activities/PediatricScreener-Parent/pediatric_screener_parent_schema'
])
nact2 = ''.join([
    REPROLIB_CANONICAL,
    'activities/PediatricScreener-SelfReport/'
    'pediatric_screener_selfreport_schema'
])
nact1Item = ''.join([
    REPROLIB_CANONICAL,
    'activities/PediatricScreener-Parent/items/fidgety'
])
nact2Item = ''.join([
    REPROLIB_CANONICAL,
    'activities/PediatricScreener-SelfReport/items/having_less_fun'
])

@pytest.mark.parametrize(
    "args",
    [(nestedActivitySet, nact1, nact2, nact1Item, nact2Item)]
)
def test_2_pediatric_screener(args):
    nestedActivitySet, nact1, nact2, nact1Item, nact2Item = args

    try:
        print('\n\n TEST 2: Pediatric Screener')
        fullTest(
            nestedActivitySet,
            nact1,
            nact2,
            nact1Item,
            nact2Item
        )
    except Exception as e:
        print('\n\n ERROR:', e)
        raise e