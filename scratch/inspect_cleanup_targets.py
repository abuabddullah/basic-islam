# -*- coding: utf-8 -*-
import json
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

b2 = json.load(open('scratch/batch2_cleaned_list.json', encoding='utf-8'))
b3 = json.load(open('scratch/batch3_cleaned_list.json', encoding='utf-8'))

print("=== Batch 2 Items needing Arabic cleanup ===")
for it in b2:
    if it['id'] in [79, 90, 108]:
        print(f"ID {it['id']}:")
        print("RAW:", it)
        print("-" * 40)

print("=== Batch 3 Items needing Arabic cleanup ===")
for it in b3:
    if it['id'] in [118, 119, 123, 125, 126, 133, 135, 144, 148, 152]:
        print(f"ID {it['id']}:")
        print("RAW:", it)
        print("-" * 40)
