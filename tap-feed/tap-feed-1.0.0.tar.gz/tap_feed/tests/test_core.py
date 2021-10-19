"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import get_standard_tap_tests

from tap_feed.tap import TapFeed

SAMPLE_CONFIG = {
    "feed_urls": ["http://feeds.feedburner.com/PythonSoftwareFoundationNews"],
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
}


# Run standard built-in tap tests from the SDK:
def test_standard_tap_tests():
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(TapFeed, config=SAMPLE_CONFIG)
    for test in tests:
        test()
