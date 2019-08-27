import MySQLdb as sql
import pandas as pd

db = sql.connect(host = "host", user = "user",
                  passwd = "passwd", db = "db")
                  
db.ping(True)
cursor = db.cursor()

df = pd.read_csv('path')

for row in df.iterrows();

  ID = str(row[0])
  data = row[1]

  key1 = str(data[0])
  key2 = str(data[1])
  
  command = 'insert into Tables(titel1, titel2) values ('+ID+",\'"+key1+\',"+key2+");"
  
  try:
    cursor.execute(command)
    
    db.commit()
    
  except:
    db.rollback()
    
db.close()
