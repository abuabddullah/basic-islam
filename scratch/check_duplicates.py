# -*- coding: utf-8 -*-
import json
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

for b_name, f_path in [('Batch 2', 'scratch/batch2_parsed.json'), ('Batch 3', 'scratch/batch3_parsed.json')]:
    with open(f_path, 'r', encoding='utf-8') as f:
        items = json.load(f)
    print(f"=== {b_name} Duplicate Check ===")
    seen_links = {}
    for it in items:
        for l_text, l_url in it['links']:
            if l_url in seen_links:
                print(f"Duplicate URL {l_url}: Item {seen_links[l_url]} and Item {it['orig_idx']} (Ch {it['ch_idx']})")
            else:
                seen_links[l_url] = it['orig_idx']
