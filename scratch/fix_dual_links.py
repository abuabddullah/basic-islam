# -*- coding: utf-8 -*-
import re
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

file_path = "মৃত্যু/মৃত্যু_জানাযা_ও_অনন্ত_জীবন_সম্পূর্ণ_বই.md"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix the single Quran link
content = content.replace(
    "(সূরা আল-আ'রাফ, ৭:৩৪; সূরা ইউনুস, ১০:৪৯) — [quran.com/7/34](https://quran.com/7/34)",
    "— [সূরা আল-আ'রাফ, ৭:৩৪](https://quran.com/7/34); [সূরা ইউনুস, ১০:৪৯](https://quran.com/10/49)"
)

# Fix dual hadith links like:
# [সহীহ বুখারী, হাদীস নং XXX](...) | **মান:** মুত্তাফাকুন আলাইহি। | [মুসলিম হাদীস YYY](...)
# ->
# [সহীহ বুখারী, হাদীস নং XXX](...); [সহীহ মুসলিম, হাদীস নং YYY](...) | **মান:** মুত্তাফাকুন আলাইহি (সহীহ বুখারী ও সহীহ মুসলিম)।
def fix_dual(m):
    bukhari_part = m.group(1).strip()
    m_num = m.group(2).strip()
    m_url = m.group(3).strip()
    return f"{bukhari_part}; [সহীহ মুসলিম, হাদীস নং {m_num}]({m_url}) | **মান:** মুত্তাফাকুন আলাইহি (সহীহ বুখারী ও সহীহ মুসলিম)।"

content = re.sub(
    r'(\[সহীহ বুখারী, হাদীস নং [^\]]+\]\([^\)]+\))\s*\|\s*\*\*মান:\*\*\s*মুত্তাফাকুন আলাইহি[।.]?\s*\|\s*\[মুসলিম হাদীস ([^\]]+)\]\((https?://www\.hadithbd\.com/hadith/filter/\?book=2&hadith=\d+)\)',
    fix_dual,
    content
)

# Fix other dual links:
# | [বুখারী হাদীস ১৩৮০](...)
content = re.sub(
    r'(\[সহীহ বুখারী, হাদীস নং ১৩১৪\]\([^\)]+\))\s*\|\s*\*\*মান:\*\*\s*সহীহ[।.]?\s*\|\s*\[বুখারী হাদীস ১৩৮০\]\((https?://www\.hadithbd\.com/hadith/filter/\?book=1&hadith=1380)\)',
    r'\1; [সহীহ বুখারী, হাদীস নং ১৩৮০](\2) | **মান:** সহীহ।',
    content
)

# Fix | [তিরমিযী হাদীস ৯৭৯](...)
content = re.sub(
    r'(\[[^\]]+\]\([^\)]+\))\s*\|\s*\*\*মান:\*\*\s*সহীহ[।.]?\s*\|\s*\[তিরমিযী হাদীস ৯৭৯\]\((https?://www\.hadithbd\.com/hadith/filter/\?book=3&hadith=979)\)',
    r'\1; [জামে‘ আত-তিরমিযী, হাদীস নং ৯৭৯](\2) | **মান:** সহীহ।',
    content
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Dual links standardized successfully!")
