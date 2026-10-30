# -*- coding: utf-8 -*-
import json
import re
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

for name, path in [('Batch 2', 'scratch/batch2_cleaned_list.json'), ('Batch 3', 'scratch/batch3_cleaned_list.json')]:
    items = json.load(open(path, encoding='utf-8'))
    print(f"=== {name} ===")
    for it in items:
        ar = it['arabic']
        bn_chars = re.findall(r'[\u0980-\u09FF]', ar)
        if bn_chars:
            print(f"Item {it['id']} has Bengali in Arabic ({len(bn_chars)} bn chars):")
            print("  AR:", ar[:120])
