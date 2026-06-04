'''
13 tadan 4-dars
txns = [(1500, 'approved'), (2300, 'declined'), (890, 'approved'), (15000, 'approved')]

total = 0
for amount, status in txns:
    if status == 'approved':
        total += amount

print(total)
'''

'''
13 tadan 5-dars
1. ZCA
2. Python-da satrlar o'zgarmas
3. strip
4. "1,500"

card = '8600123456781234'
print(f"{card[:4]}********{card[-4:]}")
'''

'''
13 tadan 6-dars
1. None
2. append bitta element qo'shadi, extend — iterabldan birma-bir
3. [4, 6]
4. -1

txns = [1500, 2300, 890, 15000, 500, 7200, 3400]
txns.sort(reverse=True)
print(*txns[:3])
'''

'''
13 tadan 7-dars
1. Bo'sh dict
2. Kalit yo'q bo'lsa xato qilmaydi
3. U o'zgaruvchan (hashlanmaydi)
4. {2, 3}

txns = [
    {'amount': 1500, 'currency': 'UZS'},
    {'amount': 50,   'currency': 'USD'},
    {'amount': 890,  'currency': 'UZS'},
    {'amount': 25,   'currency': 'EUR'},
    {'amount': 60,   'currency': 'RUB'},
    {'amount': 45,   'currency': 'USD'},
]

print(','.join(sorted(set(t['currency'] for t in txns))))
'''

'''
13 tadan 8-dars
1. None
2. Default ro'yxat barcha chaqiruvlar uchun umumiy
3. Local -> Enclosing -> Global -> Builtin

def commission(amount, rate=0.01):
    return amount * rate

print(commission(150000), commission(150000, 0.015))
'''

'''
13 tadan 9-dars
1. tuple
2. *lst paketni ochadi, lst — bitta argument
3. `return` bilan ko'p qatorli blok

customers = [
    {'name': 'Ali', 'balance': 1500},
    {'name': 'Dilnoza', 'balance': 23000},
    {'name': 'Bobur', 'balance': 890},
]

print(','.join(c['name'] for c in sorted(customers, key=lambda c: c['balance'], reverse=True)))
'''

'''
13 tadan 10-dars
1. Loyiha bog'liqliklarini izolyatsiya qilish
2. Joriy versiyalarni faylga yozadi
3. Nomlar qayerdan kelganligi noma'lum, konfliktlar
4. requirements.txt
'''

'''
13 tadan 11-dars
1. Xato bo'lsa ham faylni yopishini kafolatlaydi
2. w qaytadan yozadi, a oxiriga qo'shadi
3. for line in f:
4. utf-8

text = 'Ali | 1500 | approved\nBobur | 5000 | declined\nAli | 23000 | approved\nDilnoza | 890 | approved'

total = 0
for line in text.strip().split('\n'):
    parts = [p.strip() for p in line.split('|')]
    if parts[2] == 'approved':
        total += int(parts[1])
print(total)
'''

'''
13 tadan 12-dars
1. dumps satr qaytaradi, dump faylga yozadi
2. Kirill/o'zbek harflarni buzmaslik
3. datetime
4. true

import json
raw = '[{"customer":"Ali","amount":1500},{"customer":"Bobur","amount":23000},{"customer":"Dilnoza","amount":890}]'

data = json.loads(raw)
print(max(data, key=lambda x: x['amount'])['customer'])
'''

'''
13 tadan 13-dars
1. Barchani ushlaydi, shu jumladan KeyboardInterrupt
2. Har doim — xato bor yoki yo'q
3. Joriy istisnoni qayta ko'taradi
4. Exception

def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'error'

print(safe_div(10, 2), safe_div(5, 0))
'''
