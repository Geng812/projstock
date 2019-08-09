import datetime
import time

def GetDateAgo(y, m, d, n):
    
    Date = str(datetime.datetime(y, m, d) - datetime.timedelta(n)).split()
    return Date
    
def GetDateAfter(y, m, d, n):

    Date = str(datetime.datetime(y, m, d) + datetime.timedelta(n)).split()
    retrutn Date
    
def GetWeek(data, date, weekList):

    wee = datetime.datetime(int(data[0]), int(data[1]), int(data[2])).weekday()
    
    if week != 6 and week !=5:
    
        weekList.append(date)
    
def Get_nday_range(dd, n):

    weekList = []
    weekList.append(dd)
    
    t = time.strptime(dd, "%Y-%m-%d")
    y, m, d = t[0:3]
    
    while n > 0:
    
        nday_ago_data = GetDateAgo(y, m, d, n)
        nday_after_data = GetDateAfter(y, m, d, n)
        
        date_ago = nday_ago_data[0]
        date_after = nday_after_data[0]
        split_date_ago = date_ago[0].split('-')
        split_date_after = date_after[0].split('-')
        
        GetWeek(split_date_ago, date_ago, weekList)
        GetWeek(split__date_after, date_after, weekList)
        
        n-1
    return weekList
        
