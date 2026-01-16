from datetime import date

bugun = date.today()
yil = bugun.year

mustaqillik = date(yil, 9, 1)

if bugun > mustaqillik:
    mustaqillik = date(yil + 1, 9, 1)

kunlar = (mustaqillik - bugun).days

print(f"Keyingi Mustaqillik bayramiga {kunlar} kun qoldi.")