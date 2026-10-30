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

def to_bengali_digits(s):
    bn_digits = {'0': '০', '1': '১', '2': '২', '3': '৩', '4': '৪', '5': '৫', '6': '৬', '7': '৭', '8': '৮', '9': '৯'}
    return ''.join(bn_digits.get(c, c) for c in str(s))

def clean_ref_and_link(c_type, raw_ref, link):
    if c_type == 'কুরআন':
        m_s = re.search(r'\(?(সূরা [^,\)\—\[\]]+),\s*([0-9০-৯]+:[0-9০-৯]+(?:-[0-9০-৯]+)?)\)?', raw_ref)
        if m_s:
            s_name = m_s.group(1).strip()
            s_ayah = to_bengali_digits(m_s.group(2).strip())
            ref_label = f"{s_name}, {s_ayah}"
        else:
            ref_label = to_bengali_digits(raw_ref.strip('[]() '))
        return ref_label, link
    else:
        m_url = re.search(r'book=(\d+)&hadith=(\d+)', link)
        if m_url:
            b_id = m_url.group(1)
            h_num = m_url.group(2)
            b_name = HADITH_BOOKS.get(b_id, 'হাদীস গ্রন্থ')
            ref_label = f"{b_name}, হাদীস নং {to_bengali_digits(h_num)}"
            return ref_label, link
        else:
            return to_bengali_digits(raw_ref.strip('[]() ')), link

def build_presentation(batch_num, ch_range, start_id, end_id, json_path, out_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        items = json.load(f)
        
    print(f"Generating Batch {batch_num} presentation: {len(items)} citations ({start_id} to {end_id})")
    
    with open(out_path, 'w', encoding='utf-8') as f_out:
        f_out.write(f"# বই ০২: মৃত্যু, জানাযা ও অনন্ত জীবন\n")
        f_out.write(f"## ব্যাচ {batch_num:02d}: তাহক্বীক্ব ও রেফারেন্স যাচাই ({ch_range}: উদ্ধৃতি {start_id} হতে {end_id})\n\n---\n\n")
        
        for it in items:
            cid = it['id']
            ctype = it['type']
            ch = it['chapter']
            ar = it['arabic'].strip()
            tr = it['bengali'].strip()
            raw_ref = it['reference']
            link = it['link']
            tahqiq = it['tahqiq']
            
            clean_ref, clean_url = clean_ref_and_link(ctype, raw_ref, link)
            
            f_out.write(f"### [উদ্ধৃতি {cid:02d}] {ctype} — {ch}\n")
            f_out.write(f"* **আরবী মতন:**  \n  {ar}\n")
            f_out.write(f"* **বাংলা অনুবাদ:** \"{tr}\"\n")
            f_out.write(f"* **রেফারেন্স:** [{clean_ref}]({clean_url})\n")
            f_out.write(f"* **তাহক্বীক্ব ও মান:** {tahqiq}\n\n---\n\n")

    print(f"Saved to {out_path}")

if __name__ == '__main__':
    build_presentation(2, "অধ্যায় ০৩ হতে ০৬", 55, 115, 'scratch/batch2_cleaned_list.json', 'scratch/mrittu_batch2_presentation.txt')
    build_presentation(3, "অধ্যায় ০৭ হতে ১০", 116, 162, 'scratch/batch3_cleaned_list.json', 'scratch/mrittu_batch3_presentation.txt')
