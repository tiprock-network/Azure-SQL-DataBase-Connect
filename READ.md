# Azure ODBC Connect SQL Database
Major Imports Required

* $ import pyodbc as pyo
* $ import pandas as pd

### Simple things to note in the code

The Strings with angle brackets should be replaced with the following fields according to your resource page:
e.g. <'hostname'> becomes myapplication.database.windows.net

r"Driver={SQL Server};Server=tcp:myapplication.database.windows.net,1433;Database=myDB;Uid=Admin_Name;Pwd={your_password_here};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"

### Note: Take Note of The Default Database Provided