modal_awal = 100000000
total_laba = 0

print()

for bulan in range(1, 9):
    if bulan == 1 or bulan == 2:
        laba = 0
    elif bulan == 3 or bulan == 4:
        laba = modal_awal * 0.01  # 1%
    elif bulan == 5 or bulan == 6 or bulan == 7:
        laba = modal_awal * 0.05  # 5%
    elif bulan == 8:
        laba = modal_awal * 0.03  # 3%

    total_laba += laba
    print("laba bulan ke-", bulan, "sebesar:", laba)

print("Total laba adalah:", total_laba)