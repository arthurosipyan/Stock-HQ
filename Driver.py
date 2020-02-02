import SectorPerformance as Sectors
import StockTimeSeries as Stocks

api_key = '4FMVG5XEDEI2HNO3'

if __name__ == '__main__':
    while True:
        try:
            choice = int(input("What would you like to see?\n\n 1. Stock Dividend \n 2. Sector Performance\n\n"))
            if choice == 1:
                stock = input("Please enter the Stock's Symbol: ")
                Stocks.get_dividends(api_key, stock)
                break
            elif choice == 2:
                Sectors.get_sector_performances(api_key)
                break
        except ValueError:
            print("\nPlease enter a valid option...\n")
