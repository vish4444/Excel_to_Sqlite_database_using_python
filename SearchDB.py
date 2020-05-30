import sqlite3
import csv
import pandas as pd

####Code to query the local table####
con = sqlite3.connect('MY_SAMPLE_SQLITE.db')
db_df = pd.read_sql_query('SELECT distinct M.MEMBER_ID, \
    C.PaidAmt, C.billedamt, C.AllowedAmt, C.PcpProvNbr, C.VendorNumber, \
        P.ProviderName, \
            V.VendorNumber, V.VendorName \
    FROM Claims as C LEFT JOIN Members as M ON C.Member_Id=M.MEMBER_ID \
        LEFT JOIN Providers as P ON C.PcpProvNbr=P.ProviderID \
            LEFT JOIN Vendors as V ON C.VendorNumber=V.VendorNumber \
            where C.MEMBER_ID= "88C783D6-88FD-88B4-88F3-8865875A6A54" \
        ', con)
print (db_df)
#db_df.to_csv('database.csv', index=False)  #write the query results to a csv
con.close()

#Alternatively you can also use https://sqlitebrowser.org/dl/#macos 
# to access this locally created Sqlite DB using a GUI for querying and other database operations.