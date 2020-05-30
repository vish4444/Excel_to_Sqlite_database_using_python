# Excel_to_Sqlite_database_using_python
* When you want to analyze large excel files and do not have SQL server or any other database, use this code to create your own Sqlite local database with "DB Browser for SQLite" to start querying.
* This code uses pandas and sqlite3 python libraries, so they need to be installed as prerequisites.
* You can directly write a single large excel file with multiple sheets into the database at one go. 
* New table will be created for each sheet.
* You can query directly using Sqlite3 library via python or alternatively install the https://sqlitebrowser.org/dl/#macos to access your newly created database from a GUI. Thanks to sqlitebrowser.org for this utility.
