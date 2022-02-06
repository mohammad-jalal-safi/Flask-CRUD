import os
#1. Database Configuration for slqserver
ServerName = 'LAPTOP-TLDPAMUB'
DatabaseName = 'PRMIS'
DBURL = 'mssql+pyodbc://' + ServerName + '/' + DatabaseName + '?driver=SQL+Server+Native+Client+11.0'

#2. secret key
SECRET_KEY =os.urandom(32) # 'AwSy!2@#4z?xyzNaMe'