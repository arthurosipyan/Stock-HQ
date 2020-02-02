from alpha_vantage.sectorperformance import SectorPerformances


def get_sector_performances(key):
    sp = SectorPerformances(key)
    sector_data, meta = sp.get_sector()
    ranks = []
    print("")

    for i in meta:
        print(i, meta[i], "\n")
    print("")

    for rank in sector_data:
        ranks.append(rank)

    for i in ranks:
        print("-------------------------------------\n", i, "\n-------------------------------------\n")
        for j in sector_data[i]:
            print("{}: {}".format(j, round(sector_data[i][j], 3)))
        print("")
