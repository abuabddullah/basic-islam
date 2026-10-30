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

# Pattern for: (সহীহ...: XXX) — [বুখারী হাদীস XXX](https://www.hadithbd.com/hadith/filter/?book=X&hadith=Y)
pattern = r'\(?([^\)\n]*(?:বুখারী|মুসলিম|তিরমিযী|নাসায়ী|আবু দাউদ|ইবনু মাজাহ|ইবনে মাজাহ)[^\)\n]*)\)?\s*—\s*\[([^\]]+)\]\((https?://www\.hadithbd\.com/hadith/filter/\?book=(\d+)&hadith=(\d+))\)'

matches = list(re.finditer(pattern, content))
print(f"Total Hadith link patterns to standardize: {len(matches)}")
for m in matches[:5]:
    parenthesis = m.group(1).strip()
    link_label = m.group(2).strip()
    url = m.group(3).strip()
    b_id = m.group(4)
    h_num = m.group(5)
    
    b_name = HADITH_BOOKS.get(b_id, 'হাদীস গ্রন্থ')
    clean_ref = f"{b_name}, হাদীস নং {to_bengali_digits(h_num)}"
    
    # check if tahqiq can be inferred from parenthesis
    tahqiq = ""
    if 'সহীহ' in parenthesis or 'সহীহ' in link_label:
        if 'মুত্তাফাকুন আলাইহি' in parenthesis or ('বুখারী' in parenthesis and 'মুসলিম' in parenthesis):
            tahqiq = "মুত্তাফাকুন আলাইহি"
        else:
            tahqiq = "সহীহ"
    elif 'হাসান' in parenthesis:
        tahqiq = "হাসান"
        
    print("BEFORE:", m.group(0))
    print("AFTER :", f"— **গ্রন্থ:** [{clean_ref}]({url})" + (f" | **মান:** {tahqiq}।" if tahqiq else ""))
    print()
