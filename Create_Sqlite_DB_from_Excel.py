#!/usr/bin/env python
import sqlite3
import pandas as pd

    
con = sqlite3.connect('//Users//mymac//AnacondaProjects//Create_Sqlite_DB_from_Excel//MY_SAMPLE_SQLITE.db', uri=True)
wb = pd.read_excel('//Users//mymac//AnacondaProjects//Create_Sqlite_DB_from_Excel//Sample_Claims_File.xlsx',sheet_name = ['Vendors', 'Members', 'Claims', 'Providers'])

#print (wb)  #test whether the file is read correctly

#Code to write the excel to the Sqlite DB
for sheet in wb:
    wb[sheet].to_sql(sheet,con,index=False)
con.commit()
con.close()
