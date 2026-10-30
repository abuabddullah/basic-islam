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
    print(f"================ {name} ================")
    for it in items:
        print(f"[{it['id']:03d}] {it['type']:6s} | Ref: {it['reference']:<35} | Link: {it['link']:<55} | Tahqiq: {it['tahqiq']}")
