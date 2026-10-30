# -*- coding: utf-8 -*-
import json
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('scratch/batch3_parsed.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

def print_range(start, end):
    for it in items[start:end]:
        print(f"=== ITEM {it['orig_idx']} (Ch {it['ch_idx']}) ===")
        print("ARABIC:", it['arabic'])
        print("TRANS :", it['translation'])
        print("LINKS :", it['links'])
        print("RAW   :", it['raw'].split('\n')[-2:])
        print()

if __name__ == '__main__':
    arg = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    if arg == 1:
        print_range(0, 24)
    elif arg == 2:
        print_range(24, len(items))
