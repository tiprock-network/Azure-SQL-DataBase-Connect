import pyodbc as pyo
import pandas as pd
print("Fetching Azure SQL Database...")

#connection string
conn=pyo.connect(
    r"Driver={SQL Server};Server=tcp:<hostname>,1433;Database=<dbname>;Uid=<adminName>;Pwd={<yourpassword_here>};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
    
    ) 

print('Successfully logged in...')

#use default database provided
print('Inserting new data into <tablename>...')
#inserting data into database
insQuery=r"<Put INSERT INTO SQL Command of your Choice>"

#create a cursor
cs=conn.cursor();
#execute query with cursor
cs.execute(insQuery)
cs.commit()

#do SELECT statement
print('Execution Done, Collecting data.../n')
query=r"<Do a SELECT of your choice>"
df=pd.read_sql(query,conn)

#close the connection
print('Closing Connection...')
conn.close()
print('\nConnection Closed')
print(df.head(10))
print('Data Successfully retrieved.')

