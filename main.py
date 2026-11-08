"""Compare DNS zone serials across name servers.

Usage: python3 main.py serials.csv
CSV columns: server,zone,serial.
A zone is IN SYNC when every server reports the same serial,
otherwise MISMATCH, with the differing servers listed.
"""
import argparse, csv, sys
from collections import defaultdict

def check(rows):
    by_zone = defaultdict(list)
    for row in rows:
        by_zone[row["zone"].strip()].append((row["server"], row["serial"].strip()))
    out = []
    for zone in sorted(by_zone):
        servers = by_zone[zone]
        serials = {s for _, s in servers}
        verdict = "IN SYNC" if len(serials) == 1 else "MISMATCH"
        out.append((zone, verdict, servers))
    return sorted(out, key=lambda r: r[1] == "IN SYNC")

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        for zone, verdict, servers in check(list(csv.DictReader(f))):
            detail = ", ".join(f"{s}={ser}" for s, ser in servers)
            print(f"{zone}: {verdict} ({detail})")
    return 0

if __name__ == "__main__":
    sys.exit(main())
