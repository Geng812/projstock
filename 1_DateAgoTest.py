import datetime
import time

def Get_nday_ageo(date, n)

  nDayList = []

  t = time.strptime(date, "%Y-%m-%d")
  y, m, d = t[0:3]
  
  while n > 0:
  
    D = str(datetime.datetime(y, m, d) - datetime.time
    
    sDate = D[0].split('-')
    week = datetime.datetime(int(sDate[0], int(sDate[1]), int(sDate[2])).weekday()
    
    if week != 6 and week != 5 :
    
      nDayList.append(D[0])
      
    n -= 1
      
  return nDayList
