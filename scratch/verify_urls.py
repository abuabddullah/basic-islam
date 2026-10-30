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
    with open(path, 'r', encoding='utf-8') as f:
        items = json.load(f)
    print(f"=== Checking URLs in {name} ===")
    bengali_digits_in_url = 0
    for it in items:
        url = it['link']
        if re.search(r'[০-৯]', url):
            print(f"Item {it['id']} has Bengali digits in URL: {url}")
            bengali_digits_in_url += 1
        if not (url.startswith('https://quran.com/') or url.startswith('https://www.hadithbd.com/')):
            print(f"Item {it['id']} has suspicious URL: {url}")
    if bengali_digits_in_url == 0:
        print("All URLs are pure ASCII with NO Bengali digits!")
