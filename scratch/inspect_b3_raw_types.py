# -*- coding: utf-8 -*-
import json
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

b3_raw = json.load(open('scratch/batch3_raw_extracted.json', encoding='utf-8'))

for i, it in enumerate(b3_raw):
    raw = it['raw']
    is_quote = raw.startswith('>')
    first_line = raw.split('\n')[0][:60]
    print(f"[{i:02d}] Quote:{is_quote} :: {first_line}")
