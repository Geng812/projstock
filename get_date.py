#get date from 20100101 to now

import datetime
import calendar

dt = datetime.datetime.now()
year_list = range(2010, dt.year+1)
month_list = range(1, 13)

for year in year_list:
    for month in month_list:
        Cal = calendar.monthrange(year, month)
        day = int(Cal[1])
        day_list = range(1, day+1)

        if (year == dt.year and month > dt.month):
            break
        else:
            for dd in day_list:
                if dd == dt.day:
                    break
                date = str(year) + "{0:0=2d}".format(month) + "{0:0=2d}".format(dd)
                print(date)
