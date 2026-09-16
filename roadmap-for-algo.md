# Algoritmlash rivojlanish yo‘l xaritasi

> **Maqsad:** algoritmik fikrlashni mustahkamlash, masala yechish tezligi va aniqligini oshirish, yechimlarni toza/umumiy/optimal kodga aylantirish.
>
> **Boshlang‘ich nuqta:** `samirbekjs/Algorithm` repository tahliliga ko‘ra sizda Python asoslari va ko‘p masala yechish tajribasi yaxshi shakllangan. Keyingi asosiy qadam — yechimni shunchaki ishlaydigan kod emas, balki isbotlangan, optimal va o‘qilishi oson algoritm sifatida qurish.

---

## 1. Hozirgi holat va asosiy maqsadlar

### Kuchli tomonlar

- 391 ta masala yechimi orqali katta amaliy mashq bazasi yaratilgan.
- `if/else`, `for`, `while`, funksiyalar, list va stringlar bilan ishlash shakllangan.
- Sonlar nazariyasi, matematika, satrlar, vaqt, shartlar va oddiy o‘yin masalalariga duch kelgansiz.
- `EKUB/EKUK`, Fibonacci, tub sonlar, Paskal uchburchagi, kodlash va matritsa kabi mavzularda tajriba bor.
- RoboContest kabi platformada real testlardan o‘tgan yechimlar yozilgan.

### Rivojlantirilishi kerak bo‘lgan tomonlar

- Masala yechishdan oldin algoritmni aniq rejalashtirish.
- Vaqt va xotira murakkabligini (`Big-O`) muntazam tahlil qilish.
- Hardcode va maxsus holatlarga haddan tashqari tayanmaslik.
- Takrorlanuvchi kodni funksiyalarga ajratish.
- Chegaraviy holatlar va katta inputlar bilan ishlash.
- Ma’lumotlar tuzilmalari va klassik algoritmlarni chuqur o‘rganish.
- Kod nomlari, formatlash, testlash va hujjatlashtirishni yaxshilash.

### 12 oylik yakuniy maqsad

Quyidagi darajaga chiqish:

1. O‘rta darajadagi masalani 20–40 daqiqada tahlil qilish.
2. Kamida ikkita yechim variantini taqqoslash.
3. Murakkablikni oldindan aytish va optimallashtirish.
4. `array`, `hash map`, `stack`, `queue`, `tree`, `graph`, `heap` kabi tuzilmalarni mustaqil qo‘llash.
5. Yechimning to‘g‘riligini qisqa isbotlay olish.
6. Kodni boshqa dasturchi bemalol o‘qiy oladigan darajada yozish.

---

## 2. O‘rganish tartibi

## Bosqich 0 — Kod sifati va masala yechish intizomi

**Davomiyligi:** 1 hafta

Har bir yangi masala uchun quyidagi shablondan foydalaning:

```text
1. Masala nimani so‘rayapti?
2. Input va output qanday?
3. Cheklovlar qanday?
4. Oddiy (brute-force) yechim nima?
5. Uni qaysi qism optimallashtiradi?
6. Algoritmning invarianti yoki asosiy g‘oyasi nima?
7. Vaqt murakkabligi: O(?)
8. Xotira murakkabligi: O(?)
9. Qaysi edge case’lar bor?
10. Qo‘lda kamida 3 ta test.
```

### Qat’iy qoidalar

- Masala shartini o‘qimasdan kod yozmang.
- Avval algoritmni oddiy tilda yozing, keyin kodga o‘ting.
- `print()` orqali tasodifiy tekshirishni yakuniy kodda qoldirmang.
- Bir xil hisoblashni bir necha joyda takrorlamang.
- O‘zgaruvchi nomini ma’noli tanlang: `n`, `k` kabi nomlar faqat kontekst aniq bo‘lsa ishlatilsin.
- Har bir yechimdan keyin: “Bu kod eng yomon holatda qancha ishlaydi?” deb so‘rang.

---

## Bosqich 1 — Python poydevorini mustahkamlash

**Davomiyligi:** 2–3 hafta

### Mavzular

- Funksiya, parametr, `return`.
- Scope va lokal o‘zgaruvchilar.
- List, tuple, set, dictionary.
- Slicing va string metodlari.
- `sorted`, `key`, `lambda`.
- `enumerate`, `zip`, `any`, `all`.
- Rekursiya asoslari.
- Python input/output tezligi.
- `sys.stdin.buffer.readline` bilan tezkor input.

### Amaliy vazifalar

- Repository’dagi takrorlanuvchi sonlar va string masalalarini funksiyalar bilan qayta yozish.
- Har bir masalani `solve()` funksiyasiga o‘tkazish.
- `if __name__ == "__main__":` ishlatishni odat qilish.
- Kamida 20 ta eski yechimni PEP 8 uslubida refaktor qilish.

### Maqsad

Kod faqat ishlashi emas, balki boshqa inputlar uchun ham umumiy ishlashi kerak.

---

## Bosqich 2 — Murakkablik va asosiy patternlar

**Davomiyligi:** 3–4 hafta

### O‘rganiladigan patternlar

- Bir martalik yurish: `O(n)`.
- Ikki ko‘rsatkich: two pointers.
- Sliding window.
- Prefix sum.
- Difference array.
- Frequency map.
- Sorting + greedy.
- Binary search.
- Coordinate compression asoslari.

### Har bir pattern uchun

1. Pattern qaysi turdagi masalalarda ishlashini aniqlang.
2. Brute-force yechim yozing.
3. Optimal yechimga o‘ting.
4. Murakkablikni yozing.
5. Kamida 5 ta edge case bilan tekshiring.

### Portfolio vazifasi

Repository’da alohida katalog yarating:

```text
patterns/
  two_pointers/
  sliding_window/
  prefix_sum/
  binary_search/
  greedy/
```

Har bir katalogda:

- `README.md` — pattern tushuntirishi;
- kamida 5 ta masala;
- har bir faylda murakkablik izohi bo‘lishi kerak.

---

## Bosqich 3 — Ma’lumotlar tuzilmalari

**Davomiyligi:** 6–8 hafta

### 3.1. Linear tuzilmalar

- Stack.
- Queue va deque.
- Linked list tushunchasi.
- Hash table ishlash prinsipi.
- Set orqali tezkor qidirish.

**Masalalar:** qavslar balansi, monotonic stack, navbat simulyatsiyasi, eng yaqin katta/kichik element.

### 3.2. Daraxtlar

- Binary tree.
- Binary search tree.
- DFS: preorder, inorder, postorder.
- BFS va level-order traversal.
- Rekursiv va iterativ traversal.
- Heap va priority queue.

**Masalalar:** daraxt balandligi, yo‘l yig‘indisi, eng past umumiy ajdod, `k`-chi katta element.

### 3.3. Graflar

- Adjacency list va matrix.
- BFS, DFS.
- Connected components.
- Cycle detection.
- Topological sort.
- Weighted graph.
- Dijkstra algoritmi.
- Disjoint Set Union (DSU).

**Masalalar:** labirint, orollar soni, shaharlar orasidagi yo‘l, bog‘langan komponentalar, minimal ulanish.

### Maqsad

Graph yoki tree masalasini ko‘rganingizda, uni qaysi traversal va qaysi data structure bilan yechish kerakligini tez aniqlash.

---

## Bosqich 4 — Sonlar nazariyasi va kombinatorika

**Davomiyligi:** 3–4 hafta

### Mavzular

- EKUB va EKUK.
- Euclid algoritmi.
- Tub sonlar va Eratosthenes sieve.
- Tub ko‘paytuvchilarga ajratish.
- Bo‘luvchilar soni va yig‘indisi.
- Modular arithmetic.
- Modular exponentiation.
- Fermat va modular inverse asoslari.
- Kombinatorika.
- Binomial coefficients.
- Pigeonhole principle.
- Invariant va parity.

### Siz uchun alohida e’tibor

Repository’da EKUB/EKUK, tub sonlar va raqamlar bilan ishlash masalalari ko‘p. Endi ularni faqat sikl bilan emas, quyidagi savollar asosida qayta ko‘rib chiqing:

- `O(n)` o‘rniga `O(sqrt(n))` qilish mumkinmi?
- Sieve kerakmi?
- Formula mavjudmi?
- Modular hisoblashda overflow yoki katta son muammosi bormi?

---

## Bosqich 5 — Rekursiya, backtracking va dynamic programming

**Davomiyligi:** 6–8 hafta

### Rekursiya va backtracking

- State va choice tushunchasi.
- Base case.
- Permutation va combination.
- Subset generation.
- Constraint pruning.
- N-Queens va Sudoku kabi klassik masalalar.

### Dynamic Programming

Avval quyidagi to‘rt savolni yozing:

1. State nimani anglatadi?
2. Transition qanday?
3. Base case nima?
4. Javob qaysi state’da joylashgan?

### DP mavzulari

- 1D DP.
- 2D/grid DP.
- Knapsack.
- Coin change.
- Longest common subsequence.
- Longest increasing subsequence.
- Interval DP asoslari.
- Bitmask DP bilan tanishuv.

### Maqsad

DP formulani yodlash emas, holatni to‘g‘ri modellashtirishni o‘rganish.

---

## Bosqich 6 — Kuchli algoritmlar va contest tayyorgarligi

**Davomiyligi:** 8–12 hafta

- Greedy proof.
- Divide and conquer.
- Merge sort va inversion count.
- Quickselect.
- Fenwick tree.
- Segment tree.
- Shortest paths.
- Minimum spanning tree: Kruskal, Prim.
- Strongly connected components bilan tanishuv.
- String algoritmlari: KMP, Z-function, trie.
- Bit manipulation.
- Meet-in-the-middle.
- Amortized analysis.

Bu bosqichga faqat avvalgi mavzular bo‘yicha masalalarni mustaqil yecha olganingizdan keyin o‘ting.

---

## 3. Haftalik o‘qish rejasi

### Minimal rejim: haftasiga 10 soat

| Kun | Vazifa | Vaqt |
|---|---|---:|
| Dushanba | Nazariya va 2 ta oson masala | 1.5 soat |
| Seshanba | 3 ta oson/o‘rta masala | 1.5 soat |
| Chorshanba | Pattern yoki data structure implementatsiyasi | 1.5 soat |
| Payshanba | 2 ta o‘rta masala | 1.5 soat |
| Juma | Eski kodni refaktor qilish | 1 soat |
| Shanba | Virtual contest yoki 4–5 ta masala | 2.5 soat |
| Yakshanba | Tahlil, xatolar jurnali, takrorlash | 0.5 soat |

### 30–30–30 qoidasi

Har bir o‘rta masala uchun:

- **30 daqiqa** — mustaqil tahlil;
- **30 daqiqa** — kodlash va testlash;
- **30 daqiqa** — editorial/optimal yechimni o‘rganish va qayta yozish.

Yechimni darhol ko‘chirmang. Avval o‘zingizning xatongizni tushuning.

---

## 4. Kod sifati standarti

Har bir yangi fayl quyidagi ko‘rinishga yaqin bo‘lsin:

```python
import sys


def solve() -> None:
    data = sys.stdin.buffer.readline
    n = int(data())

    # Algoritmning asosiy qismi
    answer = n
    print(answer)


if __name__ == "__main__":
    solve()
```

### Pull request yoki o‘z-o‘zini tekshirish checklist’i

- [ ] Masala nomi va fayl nomi tushunarli.
- [ ] Kod umumiy yechimga ega, hardcode qilinmagan.
- [ ] Funksiyalar bitta vazifani bajaradi.
- [ ] O‘zgaruvchi nomlari mazmunli.
- [ ] Edge case’lar tekshirilgan.
- [ ] `O(?)` vaqt murakkabligi yozilgan.
- [ ] `O(?)` xotira murakkabligi yozilgan.
- [ ] Keraksiz import va o‘zgaruvchilar yo‘q.
- [ ] Input katta bo‘lganda yechim ishlaydi.
- [ ] Kodni boshqa odam o‘qiganda algoritm g‘oyasi tushunarli.

### Hozirgi repository uchun to‘g‘rilashlar

- 391 ta faylni yagona kataloglarga ajratish.
- Fayl nomlaridagi apostrof, bo‘shliq va maxsus belgilarni standartlashtirish.
- Har bir masalani `solve()` funksiyasiga o‘tkazish.
- `README.md` ni mavzular bo‘yicha indeks bilan kengaytirish.
- `attempt_*.py` kabi vaqtinchalik fayllarni `archive/` ga ko‘chirish.
- Murakkab yechimlarga qisqa izoh va complexity yozish.
- Hardcoded maxsus holatlarni umumiy matematik yoki algoritmik yechim bilan almashtirish.

Masalan, `0424_Snake_game.py` kabi yechimlarda maxsus massivlar va alohida `if` bloklari ko‘payib ketmasligi kerak. Bunday vaziyatda avval holat modeli, invariant va barcha harakatlar qoidasi aniqlanib, keyin umumiy simulyatsiya yoziladi.

---

## 5. Xatolar jurnali

Har bir noto‘g‘ri urinishni o‘chirib yubormang. `mistakes.md` faylida quyidagi formatdan foydalaning:

```markdown
## 2026-09-16 — R032A Labirint

- **Xato turi:** BFS o‘rniga noto‘g‘ri greedy tanlandi
- **Sabab:** masala grafiga aylantirilmadi
- **Noto‘g‘ri taxmin:** eng yaqin katak har doim optimal yo‘l beradi
- **To‘g‘ri g‘oya:** BFS barcha qadamlarni qatlamma-qatlam ko‘radi
- **O‘rganganim:** vaznlar teng bo‘lsa, shortest path uchun BFS
- **Keyingi mashq:** 3 ta grid BFS masalasi
```

Xatolarni quyidagi kategoriyalarga ajrating:

- Noto‘g‘ri tushunilgan shart.
- Boundary error.
- Index error.
- Integer division yoki rounding xatosi.
- Noto‘g‘ri murakkablik.
- Overflow yoki katta input.
- Noto‘g‘ri data structure.
- Hardcode.
- Fikrni kodga noto‘g‘ri o‘tkazish.

---

## 6. O‘lchab boriladigan ko‘rsatkichlar

Har hafta quyidagilarni yozib boring:

| Ko‘rsatkich | Maqsad |
|---|---:|
| Mustaqil yechilgan masalalar | 8–12 ta |
| O‘rta darajadagi masalalar | 3–5 ta |
| Qayta yozilgan eski yechimlar | 2 ta |
| O‘rganilgan pattern | 1–2 ta |
| Complexity tahlil qilingan kodlar | 100% |
| Xatolar jurnaliga yozuv | Har bir WA’dan keyin |
| Virtual contest | Har 2 haftada 1 ta |

Sonni ko‘paytirishdan ko‘ra, tushunilgan masalalar soni muhimroq.

---

## 7. Bosqichdan bosqichga o‘tish mezonlari

### 1-bosqichdan o‘tish

- 20 ta oddiy masalani `solve()` bilan yozish.
- List, dict, set va string metodlarini mustaqil qo‘llash.
- Kodni xatosiz formatlash.

### 2-bosqichdan o‘tish

- Two pointers, sliding window, prefix sum va binary search’ni tushuntira olish.
- 10 ta o‘rta masalada `O(n^2)` dan `O(n)` yoki `O(n log n)` ga o‘tish.

### 3-bosqichdan o‘tish

- Stack, queue, heap, tree va graph’ni noldan implementatsiya qilish.
- BFS/DFS masalalarini mustaqil yechish.

### 4-bosqichdan o‘tish

- EKUB/EKUK, sieve, modular arithmetic va kombinatorikani qo‘llash.
- Formula va brute-force orasidagi farqni izohlash.

### 5-bosqichdan o‘tish

- Kamida 20 ta DP/backtracking masalasi.
- Har bir DP yechimida state, transition va base case’ni yozish.

### 8/10 darajaga chiqish

- O‘rta masalalarning kamida 70 foizini mustaqil yechish.
- Murakkablikni koddan oldin aniqlash.
- Bir masala uchun brute-force va optimal yechimni taqqoslash.
- Hardcoded istisnolarni umumiy yechim bilan almashtirish.
- 3–5 ta virtual contest’da barqaror natija ko‘rsatish.

### 9–10/10 daraja

- Qiyin masalalarda yangi g‘oyani tez topish.
- Isbot, optimallik va implementatsiya birgalikda shakllangan bo‘lishi.
- Murakkab data structure va advanced algoritmlarni mustaqil qo‘llash.
- Boshqa odamning yechimini tahlil qilib, yaxshilash.

---

## 8. 90 kunlik aniq reja

### 1–30-kun: poydevor

- 20 ta eski faylni refaktor qilish.
- Big-O notatsiyasini amalda qo‘llash.
- 10 ta two pointers/sliding window masalasi.
- 10 ta prefix sum/frequency map masalasi.
- `mistakes.md` yuritishni boshlash.

### 31–60-kun: data structures

- Stack, queue, deque, heap’ni noldan yozish.
- 10 ta BFS/DFS masalasi.
- 5 ta binary search masalasi.
- 5 ta greedy masala va har biri uchun qisqa proof.
- Har hafta bitta mini-contest.

### 61–90-kun: chuqur algoritmlar

- 10 ta sonlar nazariyasi masalasi.
- 10 ta recursion/backtracking masalasi.
- 10 ta 1D/2D DP masalasi.
- 3 ta to‘liq virtual contest.
- Repository’ni mavzular bo‘yicha tartiblash.
- O‘zingiz uchun 20–30 ta masaladan iborat yakuniy test.

---

## 9. Yakuniy baholash mezoni

| Yo‘nalish | Ulush |
|---|---:|
| Masalani tushunish va model qurish | 20% |
| Algoritm tanlash | 25% |
| Data structure’dan foydalanish | 15% |
| Complexity va optimallik | 15% |
| Edge case va correctness | 10% |
| Kod sifati va readability | 10% |
| Tahlil va xatolardan o‘rganish | 5% |

Hozirgi taxminiy holatingiz: **6.5/10**.

90 kunlik reja muntazam bajarilsa, realistik maqsad — **7.5–8/10**. Keyingi 6–12 oy davomida data structures, graph, DP va complexity ustida ishlash orqali **8.5–9/10** darajaga chiqish mumkin.

---

## Yakuniy tavsiya

Sizga hozir ko‘proq masala soni emas, **masala sifatini tahlil qilish** kerak. Har bir yechimdan keyin uchta savolni odat qiling:

1. Buni qanday qilib umumiyroq yozish mumkin?
2. Buni qanday qilib tezroq yozish mumkin?
3. Men nima uchun bu yechim to‘g‘ri ekanini isbotlay olamanmi?

Shu uchta savolni muntazam qo‘llasangiz, sizning hozirgi “ko‘p masala yechgan boshlang‘ich/o‘rta daraja” holatingizdan “tizimli va kuchli algoritmchi” darajasiga o‘tishingiz tezlashadi.
