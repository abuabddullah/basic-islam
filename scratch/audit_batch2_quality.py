# -*- coding: utf-8 -*-
import json
import re
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('scratch/batch2_parsed.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for it in items:
    idx = it['orig_idx']
    raw = it['raw']
    c_type = it['type']
    ch_idx = it['ch_idx']
    
    # Check harakat: tashkeel chars are \u064B to \u0652, plus dagger alif \u0670
    tashkeel_count = len(re.findall(r'[\u064B-\u0652\u0670]', it['arabic']))
    has_tashkeel = tashkeel_count > 5
    
    # Check translation
    has_tr = len(it['translation']) > 5
    
    # Check links
    links = it['links']
    has_link = len(links) > 0
    
    # Check tahqiq mention in raw
    has_tahqiq = any(w in raw for w in ['মুত্তাফাকুন', 'সহীহ', 'হাসান', 'য‘ঈফ', 'যইফ', 'দুর্বল', 'সনদ', 'মান:'])
    
    issues = []
    if not has_tashkeel:
        issues.append("Low/No Tashkeel")
    if not has_tr:
        issues.append("Missing Translation")
    if not has_link:
        issues.append("Missing Link")
    if not has_tahqiq and c_type == 'হাদিস':
        issues.append("Missing Tahqiq")
        
    status = "OK" if not issues else "CHECK: " + ", ".join(issues)
    print(f"[{idx:02d}] Ch {ch_idx} {c_type:6s} -> {status}")
    if issues:
        print(f"     AR: {it['arabic'][:60]}")
        print(f"     RAW: {raw[:150]}...")
