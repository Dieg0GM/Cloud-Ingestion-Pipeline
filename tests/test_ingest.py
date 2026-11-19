import unittest
from ingest import is_valid_event


class EventValidationTests(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(is_valid_event({"device_id": "sim-1", "severity": "INFO", "message": "ok"}))

    def test_invalid(self):
        self.assertFalse(is_valid_event({"device_id": "", "severity": "INFO", "message": "ok"}))
        self.assertFalse(is_valid_event([]))


if __name__ == "__main__":
    unittest.main()
