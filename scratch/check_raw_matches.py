# -*- coding: utf-8 -*-
import json
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

content = open('মৃত্যু/মৃত্যু_জানাযা_ও_অনন্ত_জীবন_সম্পূর্ণ_বই.md', encoding='utf-8').read()

b2_raw = json.load(open('scratch/batch2_raw_extracted.json', encoding='utf-8'))
b3_raw = json.load(open('scratch/batch3_raw_extracted.json', encoding='utf-8'))

print("=== Checking match of Batch 2 raw blocks in master file ===")
b2_found = 0
for i, it in enumerate(b2_raw):
    raw = it['raw']
    if raw in content:
        b2_found += 1
    else:
        print(f"B2 [{i}] not found exactly in content: {raw[:60]}")

print(f"Batch 2: {b2_found}/{len(b2_raw)} matched exactly.")

print("=== Checking match of Batch 3 raw blocks in master file ===")
b3_found = 0
for i, it in enumerate(b3_raw):
    raw = it['raw']
    if raw in content:
        b3_found += 1
    else:
        print(f"B3 [{i}] not found exactly in content: {raw[:60]}")

print(f"Batch 3: {b3_found}/{len(b3_raw)} matched exactly.")
