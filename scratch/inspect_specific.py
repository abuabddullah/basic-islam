# -*- coding: utf-8 -*-
import json
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('scratch/batch2_parsed.json', 'r', encoding='utf-8') as f:
    b2 = json.load(f)
for it in b2:
    if it['orig_idx'] in [51, 52]:
        print(f"=== B2 Item {it['orig_idx']} ===")
        print(it['raw'])

with open('scratch/batch3_parsed.json', 'r', encoding='utf-8') as f:
    b3 = json.load(f)
for it in b3:
    if it['orig_idx'] in [6, 7]:
        print(f"=== B3 Item {it['orig_idx']} ===")
        print(it['raw'])
