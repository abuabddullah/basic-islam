# -*- coding: utf-8 -*-
import re
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def to_bengali_digits(s):
    bn_digits = {'0': '০', '1': '১', '2': '২', '3': '৩', '4': '৪', '5': '৫', '6': '৬', '7': '৭', '8': '৮', '9': '৯'}
    return ''.join(bn_digits.get(c, c) for c in str(s))

file_path = "মৃত্যু/মৃত্যু_জানাযা_ও_অনন্ত_জীবন_সম্পূর্ণ_বই.md"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Pattern for: (সূরা ..., XX:YY) — [quran.com/...](https://quran.com/...)
pattern = r'\(?(সূরা [^,\)\—\[\]]+),\s*([0-9০-৯]+:[0-9০-৯]+(?:-[0-9০-৯]+)?)\)?\s*—\s*\[quran\.com/[^\]]+\]\((https?://quran\.com/[^\)]+)\)'

matches = list(re.finditer(pattern, content))
print(f"Total Quran link patterns to standardize: {len(matches)}")
for m in matches[:5]:
    s_name = m.group(1).strip()
    s_ayah = to_bengali_digits(m.group(2).strip())
    url = m.group(3).strip()
    print("BEFORE:", m.group(0))
    print("AFTER :", f"— [{s_name}, {s_ayah}]({url})")
    print()
