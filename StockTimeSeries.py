from alpha_vantage.timeseries import TimeSeries


def get_monthly(key, symbol):
    ts = TimeSeries(key)
    ts_data, meta = ts.get_monthly_adjusted(symbol)
    dates = []
    print("")

    for i in meta:
        print(i, meta[i])
    print("")

    for date in ts_data:
        dates.append(date)

    for i in dates:
        print("-------------------------------------\n", i, "\n-------------------------------------\n")
        for j in ts_data[i]:
            print("{} : {}".format(j, ts_data[i][j], 3))
        print("")


def get_dividends(key, symbol):
    ts = TimeSeries(key)
    ts_data, meta = ts.get_monthly_adjusted(symbol)
    dividend_dates = []
    print("")

    for i in meta:
        print(i[3::] + ": ", meta[i])
    print("")

    for date in ts_data:
        dividend_dates.append(date)

    for i in dividend_dates:
        print(i, " ",  end="")
        for j in ts_data[i]:
            if j == "7. dividend amount":
                print("{}: {}".format(j[3::].capitalize(), ts_data[i][j], 3))
        print("")
