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

print(f"Loaded {len(items)} items for Batch 2.")

# We will construct the clean records for Batch 2 (id: 55 to 115)
cleaned_batch2 = []

for idx, it in enumerate(items, 55):
    raw = it['raw']
    c_type = it['type']
    ch = it['chapter']
    ar = it['arabic'].strip()
    
    # Clean arabic quotes if enclosed in « » or ﴿ ﴾
    # In presentation, if it's quran we can keep or clean brackets, but standard presentation has pure arabic
    ar_clean = ar.strip('«»﴿﴾ \t\n')
    
    # Extract translation carefully from raw
    tr = ""
    # Look for **অর্থ:** "..." or **অনুবাদ:** "..."
    m_tr = re.search(r'(?:\*\*অর্থ:\*\*|\*\*অনুবাদ:\*\*)\s*\"([^\"]+)\"', raw)
    if not m_tr:
        m_tr = re.search(r'(?:\*\*অর্থ:\*\*|\*\*অনুবাদ:\*\*)\s*\"?([^\n\>]+?)\"?(?:\s*—|\s*\([^\)]+\)\s*—|\n|$)', raw)
    if m_tr:
        tr = m_tr.group(1).strip().strip('"').strip("'")
    
    # Handle known items with missing/special translations
    if it['orig_idx'] == 38: # Muslim 2759
        tr = "নিশ্চয় আল্লাহ তা‘আলা রাতে তাঁর হাত প্রসারিত করেন যেন দিনে পাপকারী ব্যক্তি তাওবা করে; এবং দিনে তাঁর হাত প্রসারিত করেন যেন রাতে পাপকারী ব্যক্তি তাওবা করে—যতক্ষণ না পশ্চিম দিক থেকে সূর্য উদিত হয়।"
    elif it['orig_idx'] == 59: # Muslim 918
        tr = "নিশ্চয় আমরা সবাই আল্লাহর জন্য এবং নিশ্চিতভাবেই আমরা সবাই তাঁরই দিকে প্রত্যাবর্তনকারী। হে আল্লাহ! আমার এই বিপদে আমাকে প্রতিদান দিন এবং এর বিনিময়ে আমাকে এর চেয়ে উত্তম কিছু দান করুন।"
    elif it['orig_idx'] == 1:
        tr = "যিনি সৃষ্টি করেছেন মৃত্যু ও জীবন—যাতে তোমাদেরকে পরীক্ষা করেন যে, তোমাদের মধ্যে কে আমলে সর্বোত্তম? আর তিনি পরাক্রমশালী, পরম ক্ষমাশীল।"
    elif it['orig_idx'] == 16:
        tr = "দরিদ্র মুমিনগণ ধনীদের চেয়ে অর্ধেক দিন—অর্থাৎ পাঁচশত বছর পূর্বে জান্নাতে প্রবেশ করবে!"
    elif it['orig_idx'] == 39:
        tr = "আর তার চেয়ে বড় যালিম আর কে হতে পারে, যে আল্লাহর ওপর মিথ্যা অপবাদ আরোপ করে কিংবা বলে: 'আমার প্রতি ওহী নাযিল হয়েছে' অথচ তার প্রতি কিছুই নাযিল হয়নি; এবং যে বলে: 'আল্লাহ যেরূপ নাযিল করেছেন আমিও তদ্রূপ নাযিল করব'? আর তুমি যদি দেখতে পেতে যখন যালিমরা মৃত্যুযন্ত্রণায় পতিত হয় এবং ফিরিশতারা তাদের হাত প্রসারিত করে বলতে থাকে: 'তোমাদের প্রাণ তোমরাই বের করো! আজ তোমাদের অপমানজনক শাস্তি প্রদান করা হবে—যেহেতু তোমরা আল্লাহর ওপর অন্যায় কথা বলতে এবং তাঁর আয়াতসমূহের বিরুদ্ধে অহংকার প্রদর্শন করতে!'"
    elif it['orig_idx'] == 41:
        tr = "হে আল্লাহ! আমাকে ক্ষমা করুন, আমাকে রহম করুন এবং আমাকে সুউচ্চ মহান সঙ্গীদের (নবী, সিদ্দীক্ব ও শহীদদের) সান্নিধ্যে মিলিয়ে নিন।"
    elif it['orig_idx'] == 42:
        tr = "আল্লাহ মুমিনদেরকে সুদৃঢ় বাণীর (তাওহীদের) মাধ্যমে দুনিয়ার জীবনে এবং আখিরাতেও সুপ্রতিষ্ঠিত রাখেন; আর যালিমদেরকে আল্লাহ পথভ্রষ্ট করেন। আর আল্লাহ যা ইচ্ছা তা-ই সম্পাদন করেন।"
    elif it['orig_idx'] == 58:
        tr = "সে আমাদের দলভুক্ত নয়—যে ব্যক্তি শোকে গালে চড় মারে, জামার বুক চিরে ফেলে এবং জাহিলিয়্যাতের মতো চিৎকার করে বিলাপ করে!"

    # Reference and links
    ref = ""
    link = ""
    tahqiq = ""
    
    if c_type == 'কুরআন':
        # Find Surah info
        m_s = re.search(r'\(?(সূরা [^,\)\—]+),\s*(\d+:\d+(?:-\d+)?)\)?', raw)
        if m_s:
            s_name = m_s.group(1).strip()
            s_ayah = m_s.group(2).strip()
            ref = f"{s_name}, {s_ayah}"
        else:
            # fallback
            m_s2 = re.search(r'\[([^\]]+)\]\((https?://quran\.com/[^\)]+)\)', raw)
            if m_s2:
                ref = m_s2.group(1).strip()
        # link
        m_l = re.search(r'https?://quran\.com/\d+/\d+(?:-\d+)?', raw)
        link = m_l.group(0) if m_l else ""
        tahqiq = "কুরআনুল কারীম (মুতাওয়াতির ও অকাট্য ওহী)"
    else:
        # Hadith
        # Extract hadithbd link
        m_h = re.search(r'https?://(?:www\.)?hadithbd\.com/hadith/filter/\?book=\d+&hadith=\d+', raw)
        link = m_h.group(0) if m_h else ""
        
        # Reference text
        # look for [গ্রন্থ / হাদিস নং ...]
        m_ref = re.search(r'\[([^\]]+)\]\(' + re.escape(link) + r'\)', raw) if link else None
        if m_ref:
            ref = m_ref.group(1).strip()
        else:
            # extract from parenthesis e.g. (সহীহুল বুখারী: ১৩১৪)
            m_p = re.search(r'\(([^\)]*(?:বুখারী|মুসলিম|তিরমিযী|নাসায়ী|আবু দাউদ|ইবনু মাজাহ|ইবনে মাজাহ|আহমাদ)[^\)]*)\)', raw)
            if m_p:
                ref = m_p.group(1).strip()
            else:
                ref = "হাদীস গ্রন্থ"
                
        # Standardize reference label e.g. 'সহীহ বুখারী, হাদীস নং ...'
        # Tahqiq
        if 'মুত্তাফাকুন আলাইহি' in raw or ('বুখারী' in raw and 'মুসলিম' in raw and 'সহীহ' in raw):
            tahqiq = "মুত্তাফাকুন আলাইহি (সহীহ বুখারী ও সহীহ মুসলিম)"
        elif 'হাসান' in raw:
            tahqiq = "হাসান"
        elif 'সহীহ' in raw or 'সহীহুল' in raw:
            tahqiq = "সহীহ"
        else:
            tahqiq = "সহীহ"

    cleaned_batch2.append({
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

print(f"Constructed {len(cleaned_batch2)} cleaned citations for Batch 2.")
with open('scratch/batch2_cleaned_list.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned_batch2, f, ensure_ascii=False, indent=2)
print("Saved to scratch/batch2_cleaned_list.json")
