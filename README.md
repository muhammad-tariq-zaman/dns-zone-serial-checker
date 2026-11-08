# dns-zone-serial-checker

Compare DNS zone serials across name servers: a zone is IN SYNC only when every server reports the same serial — mismatches first, so a stale secondary is spotted at a glance.

## How to run

```sh
python3 main.py serials.csv
```

## Example output

```
internal.example: MISMATCH (NS1=2026110501, NS2=2026110401)
example: IN SYNC (NS1=2026110501, NS2=2026110501)
```

Standard library only. Run the tests with `python3 -m unittest discover`.
