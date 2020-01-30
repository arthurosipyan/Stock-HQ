from alpha_vantage.sectorperformance import SectorPerformances

key = '4FMVG5XEDEI2HNO3'

sp = SectorPerformances(key)

sector_data, meta = sp.get_sector()
ranks = []

for rank in sector_data:
    ranks.append(rank)

# ---

for i in ranks:
    print("-------------------------------------\n", i, "\n-------------------------------------\n")
    for j in sector_data[i]:
        print(j)
    print("")
