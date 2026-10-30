# -*- coding: utf-8 -*-
import json
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('scratch/batch2_parsed.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for it in items:
    print(f"=== ITEM {it['orig_idx']} (Ch {it['ch_idx']}) ===")
    print(it['raw'])
    print("-" * 50)
