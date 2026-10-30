# -*- coding: utf-8 -*-
import json
import re
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('scratch/batch3_parsed.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f"Loaded {len(items)} items for Batch 3.")

cleaned_batch3 = []

for idx, it in enumerate(items, 116):
    raw = it['raw']
    c_type = it['type']
    ch = it['chapter']
    ar = it['arabic'].strip()
    
    ar_clean = ar.strip('«»﴿﴾ \t\n')
    
    # Extract translation carefully from raw
    tr = ""
    m_tr = re.search(r'(?:\*\*অর্থ:\*\*|\*\*অনুবাদ:\*\*)\s*\"([^\"]+)\"', raw)
    if not m_tr:
        m_tr = re.search(r'(?:\*\*অর্থ:\*\*|\*\*অনুবাদ:\*\*)\s*\"?([^\n\>]+?)\"?(?:\s*—|\s*\([^\)]+\)\s*—|\n|$)', raw)
    if m_tr:
        tr = m_tr.group(1).strip().strip('"').strip("'")
        
    # Handle known items in batch 3 with multi-line or special translations
    if it['orig_idx'] == 1:
        tr = "আর যে কেউ আল্লাহকে ভয় করে (তাকওয়া অবলম্বন করে), আল্লাহ তার জন্য উত্তরণের কোনো পথ তৈরি করে দেন এবং তাকে এমন উৎস থেকে রিযিক দান করেন যা সে কল্পনাও করতে পারে না।"
    elif it['orig_idx'] == 4:
        tr = "তাদেরকে রক্তসহ তাদের নিজ নিজ পোশাকেই আচ্ছাদিত করে দাও।"
    elif it['orig_idx'] == 5:
        tr = "আর তাদের (মুনাফিক ও কাফেরদের) মধ্য থেকে যে কেউ মারা গেলে আপনি কখনো তার ওপর জানাযার সালাত আদায় করবেন না এবং তার কবরের পাশে দাঁড়াবেন না। কারণ তারা আল্লাহ ও তাঁর রাসুলকে অস্বীকার করেছে এবং তারা ফাসেক অবস্থায় মৃত্যুবরণ করেছে।"
    elif it['orig_idx'] == 9:
        tr = "তোমরা সাদা রঙের পোশাক পরিধান করো; কেননা তা তোমাদের সর্বোত্তম পোশাক। আর তোমাদের মৃতদেরকে সাদা কাপড় দিয়েই কাফন পরাও।"
    elif it['orig_idx'] == 12:
        tr = "কোনো মুসলিম ব্যক্তি মৃত্যুবরণ করলে তার জানাযায় যদি এমন চল্লিশজন লোক দাঁড়ায় যারা আল্লাহর সাথে কাউকে শরীক করে না (খাঁটি তাওহীদবাদী), তবে তাদের সুপারিশ আল্লাহ অবশ্যই কবুল করবেন।"
    elif it['orig_idx'] == 17:
        tr = "যে ব্যক্তি কোনো মুসলিমের জানাযায় ঈমান ও সাওয়াবের আশায় শামিল হয় এবং সালাত আদায় ও দাফন সম্পন্ন হওয়া পর্যন্ত সাথে থাকে, সে দুই ক্বীরাত সাওয়াব নিয়ে ফিরে আসবে। প্রতিটি ক্বীরাত হলো উহুদ পাহাড়ের সমতুল্য!"
    elif it['orig_idx'] == 22:
        tr = "রাসুলুল্লাহ ﷺ কবর চুনকাম (পাকা) করতে, তার ওপর বসতে এবং তার ওপর কোনো ইমারত (সৌধ বা গম্বুজ) নির্মাণ করতে নিষেধ করেছেন।"
    elif it['orig_idx'] == 23:
        tr = "আমি কি তোমাকে এমন এক মিশনে পাঠাব না যে মিশনে রাসুলুল্লাহ ﷺ আমাকে পাঠিয়েছিলেন? তা হলো—কোনো প্রতিকৃতি (মূর্তি/ছবি) দেখলে তা নিশ্চিহ্ন করবে এবং কোনো উঁচু কবর দেখলে তা মাটির সমান (এক বিঘতের সুন্নাহ মাপে) করে দেবে।"
    elif it['orig_idx'] == 25:
        tr = "নবী ﷺ যখন মাইয়্যেতের দাফন সম্পন্ন করতেন, তখন কবরের পাশে দাঁড়াতেন এবং বলতেন: 'তোমাদের এই ভাইয়ের জন্য আল্লাহর কাছে ক্ষমা প্রার্থনা করো এবং সে যেন অবিচল থাকে তার জন্য দো‘আ করো; কেননা এখনই তাকে (কবরে) সওয়াল-জওয়াব করা হচ্ছে'।"
    elif it['orig_idx'] == 44:
        tr = "ধ্বংস হোক স্বর্ণমুদ্রার (দিনারের) দাস! ধ্বংস হোক রৌপ্যমুদ্রার (দিরহামের) দাস! ধ্বংস হোক উত্তম পোশাক ও বিলাসিতার দাস! তাকে সম্পদ দেওয়া হলে সে সন্তুষ্ট হয়, আর না দেওয়া হলে ক্ষুব্ধ ও অসন্তুষ্ট হয়। সে ধ্বংস হোক এবং মুখ থুবড়ে নিপতিত হোক...।"
    elif it['orig_idx'] == 45:
        tr = "আপনি কি তাকে দেখেছেন, যে তার প্রবৃত্তিকে নিজের উপাস্য (ইলাহ) বানিয়ে নিয়েছে?"

    ref = ""
    link = ""
    tahqiq = ""
    
    if c_type == 'কুরআন':
        m_s = re.search(r'\(?(সূরা [^,\)\—]+),\s*(\d+:\d+(?:-\d+)?)\)?', raw)
        if m_s:
            s_name = m_s.group(1).strip()
            s_ayah = m_s.group(2).strip()
            ref = f"{s_name}, {s_ayah}"
        else:
            m_s2 = re.search(r'\[(সূরা [^\]]+)\]', raw)
            if m_s2:
                ref = m_s2.group(1).strip()
        m_l = re.search(r'https?://quran\.com/\d+/\d+(?:-\d+)?', raw)
        link = m_l.group(0) if m_l else ""
        tahqiq = "কুরআনুল কারীম (মুতাওয়াতির ও অকাট্য ওহী)"
    else:
        m_h = re.search(r'https?://(?:www\.)?hadithbd\.com/hadith/filter/\?book=\d+&hadith=\d+', raw)
        link = m_h.group(0) if m_h else ""
        m_ref = re.search(r'\[([^\]]+)\]\(' + re.escape(link) + r'\)', raw) if link else None
        if m_ref:
            ref = m_ref.group(1).strip()
        else:
            m_p = re.search(r'\(([^\)]*(?:বুখারী|মুসলিম|তিরমিযী|নাসায়ী|আবু দাউদ|ইবনু মাজাহ|ইবনে মাজাহ|আহমাদ|মালিক)[^\)]*)\)', raw)
            if m_p:
                ref = m_p.group(1).strip()
            else:
                ref = "হাদীস গ্রন্থ"
                
        if 'মুত্তাফাকুন আলাইহি' in raw or ('বুখারী' in raw and 'মুসলিম' in raw and 'সহীহ' in raw):
            tahqiq = "মুত্তাফাকুন আলাইহি (সহীহ বুখারী ও সহীহ মুসলিম)"
        elif 'হাসান' in raw:
            tahqiq = "হাসান"
        elif 'সহীহ' in raw or 'সহীহুল' in raw:
            tahqiq = "সহীহ"
        else:
            tahqiq = "সহীহ"

    cleaned_batch3.append({
        'id': idx,
        'orig_idx': it['orig_idx'],
        'type': c_type,
        'chapter': ch,
        'arabic': ar_clean,
        'bengali': tr,
        'reference': ref,
        'link': link,
        'tahqiq': tahqiq
    })

print(f"Constructed {len(cleaned_batch3)} cleaned citations for Batch 3.")
with open('scratch/batch3_cleaned_list.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned_batch3, f, ensure_ascii=False, indent=2)
print("Saved to scratch/batch3_cleaned_list.json")
