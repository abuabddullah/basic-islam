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

original_len = len(content)
print(f"Original file length: {original_len} characters")

# 1. Fix Abu Dawud hadith 3213 typo
old_str_1 = "> — [সুনান আবু দাউদ, হাদিস: ৩২১২, ৩২-১৩](https://www.hadithbd.com/hadith/filter/?book=4&hadith=13); শায়খ আলবানী হাদিসটিকে সহীহ বলেছেন।"
new_str_1 = "> — **গ্রন্থ:** [সুনান আবূ দাঊদ, হাদীস নং ৩২১৩](https://www.hadithbd.com/hadith/filter/?book=4&hadith=3213) | **মান:** সহীহ (আলবানী)।"
if old_str_1 in content:
    content = content.replace(old_str_1, new_str_1)
    print("Fixed Abu Dawud 3213 typo.")

# 2. Fix Bengali যَوْمِ in Surah Al-Mu'minun 23:100
old_str_2 = "وَمِن وَرَائِهِم بَرْزَخٌ إِلَىٰ যَوْمِ يُبْعَثُونَ"
new_str_2 = "وَمِن وَرَائِهِم بَرْزَخٌ إِلَىٰ يَوْمِ يُبْعَثُونَ"
if old_str_2 in content:
    content = content.replace(old_str_2, new_str_2)
    print("Fixed Bengali character in Surah Al-Mu'minun 23:100.")

# 3. Add link to Surah Al-Imran 3:8 in Ch 3
old_str_3 = """> **«رَبَّنَا لَا تُزِغْ قُلُوبَنَا بَعْدَ إِذْ هَدَيْتَنَا وَهَبْ لَنَا مِن لَّدُنكَ رَحْمَةً ۚ إِنَّكَ أَنتَ الْوَهَّابُ»**  
>  (সূরা আলে ইমরান, ৩:৮)"""
new_str_3 = """> **رَبَّنَا لَا تُزِغْ قُلُوبَنَا بَعْدَ إِذْ هَدَيْتَنَا وَهَبْ لَنَا مِن لَّدُنكَ رَحْمَةً ۚ إِنَّكَ أَنتَ الْوَهَّابُ**  
>
> **অনুবাদ:** "হে আমাদের রব! সরল পথ প্রদর্শনের পর আপনি আমাদের অন্তরসমূহকে সত্যচ্যুত করবেন না এবং আপনার নিকট থেকে আমাদেরকে অনুগ্রহ দান করুন; নিশ্চয় আপনিই মহাদাতা।"  
> — [সূরা আলে ইমরান, ৩:৮](https://quran.com/3/8)"""
if old_str_3 in content:
    content = content.replace(old_str_3, new_str_3)
    print("Added translation and link for Surah Al-Imran 3:8.")

# 4. Add link and translation to Bukhari 5671 in Ch 4
old_str_4 = """> **«اللَّهُمَّ أَحْيِنِي مَا كَانَتِ الْحَيَاةُ خَيْرًا لِي، وَتَوَفَّنِي إِذَا كَانَتِ الْوَفَاةُ خَيْرًا لِي»**  
>  (সহীহ বুখারী: ৫৬৭১)"""
new_str_4 = """> **«اللَّهُمَّ أَحْيِنِي مَا كَانَتِ الْحَيَاةُ خَيْرًا لِي، وَتَوَفَّنِي إِذَا كَانَتِ الْوَفَاةُ خَيْرًا لِي»**  
>
> **অনুবাদ:** "হে আল্লাহ! আমাকে সে পর্যন্ত জীবিত রাখুন যতক্ষণ জীবিত থাকাটা আমার জন্য কল্যাণকর হয়, আর আমাকে তখনই মৃত্যু দিন যখন মৃত্যুটা আমার জন্য কল্যাণকর হয়।"  
> — **গ্রন্থ:** [সহীহ বুখারী, হাদীস নং ৫৬৭১](https://www.hadithbd.com/hadith/filter/?book=1&hadith=5671) | **মান:** সহীহ।"""
if old_str_4 in content:
    content = content.replace(old_str_4, new_str_4)
    print("Added link and translation for Bukhari 5671.")

# 5. Add link and translation to Tirmidhi 2083 in Ch 4
old_str_5 = """> **«أَسْأَلُ اللَّهَ الْعَظِيمَ رَبَّ الْعَرْشِ الْعَظِيمِ أَنْ يَشْفِيَكَ»**  
>  (আসআলুল্লাহাল 'আযীম, রাব্বাল 'আরশিল 'আযীম, আই-য়াশফিয়াক — তিরমিযী ২০৮৩)"""
new_str_5 = """> **«أَسْأَلُ اللَّهَ الْعَظِيمَ رَبَّ الْعَرْشِ الْعَظِيمِ أَنْ يَشْفِيَكَ»**  
>
> **অনুবাদ:** "আমি মহান আরশের অধিপতি মহান আল্লাহর নিকট প্রার্থনা করছি, তিনি যেন আপনাকে আরোগ্য দান করেন।"  
> — **গ্রন্থ:** [জামে‘ আত-তিরমিযী, হাদীস নং ২০৮৩](https://www.hadithbd.com/hadith/filter/?book=3&hadith=2083) | **মান:** সহীহ।"""
if old_str_5 in content:
    content = content.replace(old_str_5, new_str_5)
    print("Added link and translation for Tirmidhi 2083.")

# 6. Add translation for Muslim 2759 in Ch 4
old_str_6 = """> **«إِنَّ اللَّهَ تَعَالَى يَبْسُطُ يَدَهُ بِاللَّيْلِ لِيَتُوبَ مُسِيءُ النَّهَارِ، وَيَبْسُطُ يَدَهُ بِالنَّهَارِ لِيَتُوبَ مُسِيءُ اللَّيْلِ، حَتَّى تَطْلُعَ الشَّمْسُ مِنْ مَغْرِبِهَا»**  
> (সহীহ মুসলিম: ২৭৫৯) — [মুসলিম হাদীস ২৭৫৯](https://www.hadithbd.com/hadith/filter/?book=2&hadith=2759)"""
new_str_6 = """> **«إِنَّ اللَّهَ تَعَالَى يَبْسُطُ يَدَهُ بِاللَّيْلِ لِيَتُوبَ مُسِيءُ النَّهَارِ، وَيَبْسُطُ يَدَهُ بِالنَّهَارِ لِيَتُوبَ مُسِيءُ اللَّيْلِ، حَتَّى تَطْلُعَ الشَّمْسُ مِنْ مَغْرِبِهَا»**  
>
> **অনুবাদ:** "নিশ্চয় আল্লাহ তা‘আলা রাতে তাঁর হাত প্রসারিত করেন যেন দিনে পাপকারী ব্যক্তি তাওবা করে; এবং দিনে তাঁর হাত প্রসারিত করেন যেন রাতে পাপকারী ব্যক্তি তাওবা করে—যতক্ষণ না পশ্চিম দিক থেকে সূর্য উদিত হয়।"  
> — **গ্রন্থ:** [সহীহ মুসলিম, হাদীস নং ২৭৫৯](https://www.hadithbd.com/hadith/filter/?book=2&hadith=2759) | **মান:** সহীহ।"""
if old_str_6 in content:
    content = content.replace(old_str_6, new_str_6)
    print("Added translation for Muslim 2759.")

# 7. Add link and translation for Bukhari 792 in Ch 5
old_str_7 = """> **«سُبْحَانَكَ اللَّهُمَّ رَبَّنَا وَبِحَمْدِكَ اللَّهُمَّ اغْفِرْ لِي»**  
>  (সহীহ বুখারী: ৭৯২)"""
new_str_7 = """> **«سُبْحَانَكَ اللَّهُمَّ رَبَّنَا وَبِحَمْدِكَ اللَّهُمَّ اغْفِرْ لِي»**  
>
> **অনুবাদ:** "হে আমাদের রব আল্লাহ! আপনার পবিত্রতা ও প্রশংসা সহকারে গুণগান করছি; হে আল্লাহ! আপনি আমাকে ক্ষমা করে দিন।"  
> — **গ্রন্থ:** [সহীহ বুখারী, হাদীস নং ৭৯২](https://www.hadithbd.com/hadith/filter/?book=1&hadith=792) | **মান:** মুত্তাফাকুন আলাইহি (সহীহ বুখারী ও সহীহ মুসলিম)"""
if old_str_7 in content:
    content = content.replace(old_str_7, new_str_7)
    print("Added link for Bukhari 792.")

# 8. Add translation for Muslim 918 in Ch 6
old_str_8 = """> **«إِنَّا لِلَّهِ وَإِنَّا إِلَيْهِ رَاجِعُونَ، اللَّهُمَّ أْجُرْنِي فِي مُصِيبَتِي، وَأَخْلِفْ لِي خَيْرًا مِنْهَا»**  
> (সহীহ মুসলিম: ৯১৮) — [মুসলিম হাদীস ৯১৮](https://www.hadithbd.com/hadith/filter/?book=2&hadith=918)"""
new_str_8 = """> **«إِنَّا لِلَّهِ وَإِنَّا إِلَيْهِ رَاجِعُونَ، اللَّهُمَّ أْجُرْنِي فِي مُصِيبَتِي، وَأَخْلِفْ لِي خَيْرًا مِنْهَا»**  
>
> **অনুবাদ:** "নিশ্চয় আমরা সবাই আল্লাহর জন্য এবং নিশ্চিতভাবেই আমরা সবাই তাঁরই দিকে প্রত্যাবর্তনকারী। হে আল্লাহ! আমার এই বিপদে আমাকে প্রতিদান দিন এবং এর বিনিময়ে আমাকে এর চেয়ে উত্তম কিছু দান করুন।"  
> — **গ্রন্থ:** [সহীহ মুসলিম, হাদীস নং ৯১৮](https://www.hadithbd.com/hadith/filter/?book=2&hadith=918) | **মান:** সহীহ।"""
if old_str_8 in content:
    content = content.replace(old_str_8, new_str_8)
    print("Added translation for Muslim 918.")

# 9. Add link and translation to Muslim 920 in Ch 6 summary
old_str_9 = """> **«اللَّهُمَّ اغْفِرْ لَهُ، وَارْفَعْ دَرَجَتَهُ فِي الْمَهْدِيِّينَ، وَاخْلُفْهُ فِي عَقِبِهِ فِي الْغَابِرِينَ، وَاغْفِرْ لَنَا وَلَهُ يَا رَبَّ الْعَالَمِينَ، وَافْسَحْ لَهُ فِي قَبْرِهِ، وَنَوِّرْ لَهُ فِيهِ»**  
>  (সহীহ মুসলিম: ৯২০)"""
new_str_9 = """> **«اللَّهُمَّ اغْفِرْ لَهُ، وَارْفَعْ دَرَجَتَهُ فِي الْمَهْدِيِّينَ، وَاخْلُفْهُ فِي عَقِبِهِ فِي الْغَابِرِينَ، وَاغْفِرْ لَنَا وَلَهُ يَا رَبَّ الْعَالَمِينَ، وَافْسَحْ لَهُ فِي قَبْرِهِ، وَنَوِّرْ لَهُ فِيهِ»**  
>
> **অনুবাদ:** "হে আল্লাহ! আপনি তাকে ক্ষমা করে দিন, হেদায়েতপ্রাপ্তদের মাঝে তার মর্যাদা সমুন্নত করুন এবং তার পশ্চাতে রেখে যাওয়া পরিবারের জন্য আপনি উত্তম অভিভাবক হয়ে যান। আর হে রব্বুল আলামীন! আমাদের এবং তাকে ক্ষমা করুন, তার কবরকে তার জন্য প্রশস্ত করে দিন এবং তাতে নূর দান করুন।"  
> — **গ্রন্থ:** [সহীহ মুসলিম, হাদীস নং ৯২০](https://www.hadithbd.com/hadith/filter/?book=2&hadith=920) | **মান:** সহীহ।"""
if old_str_9 in content:
    content = content.replace(old_str_9, new_str_9)
    print("Added link and translation for Muslim 920 summary.")

# 10. Add link to Surah Al-Baqarah 2:156 in Ch 10
old_str_10 = """> «إِنَّا لِلَّهِ وَإِنَّا إِلَيْهِ رَاجِعُونَ»  
> **অর্থ:** "নিশ্চয় আমরা সবাই আল্লাহরই জন্য এবং নিশ্চিতভাবেই আমরা সবাই তাঁরই দিকে প্রত্যাবর্তনকারী।" """
new_str_10 = """> **﴿إِنَّا لِلَّهِ وَإِنَّا إِلَيْهِ رَاجِعُونَ﴾**  
>
> **অনুবাদ:** "নিশ্চয় আমরা সবাই আল্লাহরই জন্য এবং নিশ্চিতভাবেই আমরা সবাই তাঁরই দিকে প্রত্যাবর্তনকারী।"  
> — [সূরা আল-বাক্বারা, ২:১৫৬](https://quran.com/2/156)"""
if old_str_10.strip() in content:
    content = content.replace(old_str_10.strip(), new_str_10)
    print("Added link for Surah Al-Baqarah 2:156 in Ch 10.")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Master file updated successfully! New length: {len(content)} characters.")
