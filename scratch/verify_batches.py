# -*- coding: utf-8 -*-
import json
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

for name, path in [('Batch 2', 'scratch/batch2_cleaned_list.json'), ('Batch 3', 'scratch/batch3_cleaned_list.json')]:
    with open(path, 'r', encoding='utf-8') as f:
        items = json.load(f)
    print(f"=== Verifying {name} ({len(items)} items) ===")
    missing_cnt = 0
    for it in items:
        missing = [k for k in ['arabic', 'bengali', 'reference', 'link', 'tahqiq'] if not it[k].strip()]
        if missing:
            missing_cnt += 1
            print(f"Item {it['id']}: Missing {missing}")
            print(f"  Orig {it['orig_idx']}: {it}")
    if missing_cnt == 0:
        print("All items have non-empty arabic, bengali, reference, link, and tahqiq!")
