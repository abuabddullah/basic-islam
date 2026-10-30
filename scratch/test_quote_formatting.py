# -*- coding: utf-8 -*-
import json
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

def clean_ref_and_link(c_type, raw_ref, link):
    if c_type == 'কুরআন':
        m_s = re.search(r'\(?(সূরা [^,\)\—\[\]]+),\s*(\d+:\d+(?:-\d+)?)\)?', raw_ref)
        if m_s:
            s_name = m_s.group(1).strip()
            s_ayah = m_s.group(2).strip()
            return f"{s_name}, {s_ayah}", link
        else:
            return raw_ref.strip('[]() '), link
    else:
        m_url = re.search(r'book=(\d+)&hadith=(\d+)', link)
        if m_url:
            b_id = m_url.group(1)
            h_num = m_url.group(2)
            b_name = HADITH_BOOKS.get(b_id, 'হাদীস গ্রন্থ')
            return f"{b_name}, হাদীস নং {h_num}", link
        else:
            return raw_ref.strip('[]() '), link

def format_master_quote(item):
    c_type = item['type']
    ar = item['arabic'].strip()
    tr = item['bengali'].strip()
    link = item['link'].strip()
    tahqiq = item['tahqiq'].strip()
    clean_ref, clean_url = clean_ref_and_link(c_type, item['reference'], link)
    
    # Standard format matching Chapters 1 and 2
    if c_type == 'কুরআন':
        return f'> **{ar}**\n>\n> **অনুবাদ:** "{tr}"  \n> — [{clean_ref}]({clean_url})'
    else:
        return f'> **{ar}**\n>\n> **অনুবাদ:** "{tr}"  \n> — **গ্রন্থ:** [{clean_ref}]({clean_url}) | **মান:** {tahqiq}।'

# Test formatting on a couple items
with open('scratch/batch2_cleaned_list.json', 'r', encoding='utf-8') as f:
    b2 = json.load(f)

print("Sample Batch 2 formatted block:")
print(format_master_quote(b2[0]))
print("---")
print(format_master_quote(b2[1]))
