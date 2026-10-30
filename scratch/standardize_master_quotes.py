# -*- coding: utf-8 -*-
import re
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

HADITH_BOOKS = {
    '1': 'সহীহ বুখারী',
    '2': 'সহীহ মুসলিম',
    '3': 'জামে‘ আত-তিরমিযী',
    '4': 'সুনান আবূ দাঊদ',
    '5': 'সুনান আন-নাসায়ী',
    '7': 'মুয়াত্তা মালিক',
    '14': 'সুনান ইবনু মাজাহ'
}

def to_bengali_digits(s):
    bn_digits = {'0': '০', '1': '১', '2': '২', '3': '৩', '4': '৪', '5': '৫', '6': '৬', '7': '৭', '8': '৮', '9': '৯'}
    return ''.join(bn_digits.get(c, c) for c in str(s))

file_path = "মৃত্যু/মৃত্যু_জানাযা_ও_অনন্ত_জীবন_সম্পূর্ণ_বই.md"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

original_len = len(content)
print(f"Reading {file_path} ({original_len} chars)")

# 1. Standardize Quran references:
# (সূরা ..., XX:YY) — [quran.com/...](https://quran.com/...)
def repl_quran(m):
    lead = m.group(1) # any leading '> ' or '   > '
    s_name = m.group(2).strip()
    s_ayah = to_bengali_digits(m.group(3).strip())
    url = m.group(4).strip()
    return f"{lead}— [{s_name}, {s_ayah}]({url})"

content = re.sub(
    r'(>[ \t]*)\(?(সূরা [^,\)\—\[\]\n]+),\s*([0-9০-৯]+:[0-9০-৯]+(?:-[0-9০-৯]+)?)\)?\s*—\s*\[quran\.com/[^\]]+\]\((https?://quran\.com/[^\)]+)\)',
    repl_quran,
    content
)

# 2. Standardize Hadith references:
# (সহীহ...: XXX) — [বুখারী হাদীস XXX](https://www.hadithbd.com/hadith/filter/?book=X&hadith=Y)
def repl_hadith(m):
    lead = m.group(1) # any leading '> '
    parenthesis = m.group(2).strip()
    link_label = m.group(3).strip()
    url = m.group(4).strip()
    b_id = m.group(5)
    h_num = m.group(6)
    
    b_name = HADITH_BOOKS.get(b_id, 'হাদীস গ্রন্থ')
    clean_ref = f"{b_name}, হাদীস নং {to_bengali_digits(h_num)}"
    
    # check tahqiq
    tahqiq = ""
    if 'মুত্তাফাকুন' in parenthesis or ('বুখারী' in parenthesis and 'মুসলিম' in parenthesis):
        tahqiq = "মুত্তাফাকুন আলাইহি"
    elif 'হাসান' in parenthesis:
        tahqiq = "হাসান"
    elif 'সহীহ' in parenthesis or 'সহীহ' in link_label:
        tahqiq = "সহীহ"
    else:
        tahqiq = "সহীহ"
        
    res = f"{lead}— **গ্রন্থ:** [{clean_ref}]({url})"
    if tahqiq:
        res += f" | **মান:** {tahqiq}।"
    return res

content = re.sub(
    r'(>[ \t]*)\(?([^\)\n]*(?:বুখারী|মুসলিম|তিরমিযী|নাসায়ী|আবু দাউদ|ইবনু মাজাহ|ইবনে মাজাহ)[^\)\n]*)\)?\s*—\s*\[([^\]]+)\]\((https?://www\.hadithbd\.com/hadith/filter/\?book=(\d+)&hadith=(\d+))\)',
    repl_hadith,
    content
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Standardized quotes successfully! New length: {len(content)} characters.")
