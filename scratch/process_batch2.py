# -*- coding: utf-8 -*-
import json
import re
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('scratch/batch2_raw_extracted.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f"Total items: {len(items)}")

parsed_citations = []

for i, it in enumerate(items, 1):
    raw = it['raw']
    ch = it['ch_title']
    ch_idx = it['ch_idx']
    
    # Quran vs Hadith
    is_quran = 'quran.com' in raw or ('সূরা' in raw and 'হাদিস' not in raw and 'হাদীস' not in raw)
    c_type = "কুরআন" if is_quran else "হাদিস"
    
    # Links
    links = re.findall(r'\[([^\]]+)\]\((https?://[^\)]+)\)', raw)
    
    # Arabic text extraction
    ar_lines = []
    for line in raw.split('\n'):
        line_clean = line.strip().lstrip('> ').strip('*_ ')
        # check if line contains arabic
        if re.search(r'[\u0600-\u06FF]{4,}', line_clean):
            # check if it is not an explanation line
            if not any(k in line_clean for k in ['অনুবাদ:', 'অর্থ:', 'গ্রন্থ:', 'মান:', 'হাদীস নং', 'হাদিস:', 'সূরা ']):
                # clean enclosing brackets if needed
                ar_lines.append(line_clean)
    arabic = " ".join(ar_lines).strip()
    # clean leading or trailing symbols like « » ﴿ ﴾
    arabic = arabic.strip()
    
    # Translation extraction
    # patterns: **অর্থ:** "..." or **অনুবাদ:** "..."
    tr = ""
    tr_match = re.search(r'(?:\*\*অনুবাদ:\*\*|\*\*অর্থ:\*\*)\s*\"?([^\n\>]+?)\"?(?:\s*—|\s*\(|\n|$)', raw)
    if tr_match:
        tr = tr_match.group(1).strip().strip('"').strip("'")
    
    parsed_citations.append({
        'orig_idx': i,
        'ch_idx': ch_idx,
        'chapter': ch,
        'type': c_type,
        'arabic': arabic,
        'translation': tr,
        'links': links,
        'raw': raw
    })

print(f"Parsed {len(parsed_citations)} citations.")
with open('scratch/batch2_parsed.json', 'w', encoding='utf-8') as f:
    json.dump(parsed_citations, f, ensure_ascii=False, indent=2)

for c in parsed_citations:
    print(f"[{c['orig_idx']}] Ch {c['ch_idx']} [{c['type']}]")
    print(f"  AR: {c['arabic'][:70]}...")
    print(f"  TR: {c['translation'][:70]}...")
    print(f"  LN: {c['links']}")
    print("-" * 40)
