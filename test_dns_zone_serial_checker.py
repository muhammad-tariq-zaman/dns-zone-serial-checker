import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import check

def row(s, z, ser):
    return {"server": s, "zone": z, "serial": str(ser)}

class TestZoneSerial(unittest.TestCase):
    def test_in_sync(self):
        self.assertEqual(check([row("NS1", "example", 2026110501), row("NS2", "example", 2026110501)])[0][1], "IN SYNC")
    def test_mismatch(self):
        self.assertEqual(check([row("NS1", "example", 2026110501), row("NS2", "example", 2026110401)])[0][1], "MISMATCH")
    def test_mismatch_first(self):
        r = check([row("NS1", "a.example", 1), row("NS2", "a.example", 1), row("NS1", "b.example", 1), row("NS2", "b.example", 2)])
        self.assertEqual(r[0][0], "b.example")
    def test_single_server_sync(self):
        self.assertEqual(check([row("NS1", "example", 5)])[0][1], "IN SYNC")
