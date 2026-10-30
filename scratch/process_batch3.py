# -*- coding: utf-8 -*-
import json
import re
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('scratch/batch3_raw_extracted.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f"Total items in Batch 3: {len(items)}")

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
        line_clean = line.strip().lstrip('> -*#').strip()
        if re.search(r'[\u0600-\u06FF]{4,}', line_clean):
            if not any(k in line_clean for k in ['অনুবাদ:', 'অর্থ:', 'গ্রন্থ:', 'মান:', 'হাদীস নং', 'হাদিস:', 'সূরা ']):
                ar_lines.append(line_clean)
    arabic = " ".join(ar_lines).strip()
    
    # Translation extraction
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

print(f"Parsed {len(parsed_citations)} citations in Batch 3.")
with open('scratch/batch3_parsed.json', 'w', encoding='utf-8') as f:
    json.dump(parsed_citations, f, ensure_ascii=False, indent=2)

with open('scratch/batch3_audit_dump.txt', 'w', encoding='utf-8') as f_out:
    for it in parsed_citations:
        f_out.write(f"=== ITEM {it['orig_idx']} (Ch {it['ch_idx']}) ===\n")
        f_out.write(it['raw'] + "\n")
        f_out.write("-" * 50 + "\n")

print("Dumped to scratch/batch3_audit_dump.txt")
