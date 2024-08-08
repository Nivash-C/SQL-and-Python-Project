import pandas as pd
from sqlalchemy import create_engine

def append_to_sql(file):
    df = pd.read_csv(file)
    path = "mysql://root:Nivash%4003@localhost/Nivash_c"
    engine = create_engine(path)
    
    
    print("Appending to SQL...")
    
    while True:
        table_name = input("Enter table name")
        try:
            df.to_sql(table_name,con = engine, index = False)
            print("Function completed")
            print("Table created in SQL")
            print("Table Name: ",table_name)
            break
            
        except ValueError:
            print("Table name already exists.Try different table name")
        
