from pymysql import connect
import pandas as pd
from sqlalchemy import create_engine
from sklearn.feature_selection import SelectKBest, f_classif

def clean(t_name):
    
    df = connect(host='localhost', user='root', password='Nivash@03',database = 'Nivash_C')
    cur = df.cursor()
    query = "select * from "+t_name
    cur.execute(query)
    df1 = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    df_1 = pd.DataFrame(df1, columns=columns)
    print("Before cleaning the data, the shape of the dataset is ",df_1.shape)

    df_1.drop_duplicates(inplace=True)
    
    print("After dropping duplicates,the shape od dataset is ",df_1.shape)
    
    count_isnull = df_1.isnull().sum().sum()
    
    if count_isnull == 0:
        pass
    else:
        df_1.dropna(inplace=True,how='any')
        print("After dropping NULL values,the shape od dataset is ",df_1.shape)
    
    x = df_1.iloc[:,4:12]
    y = df_1[' loan_status']

    select = SelectKBest(score_func=f_classif,k=2)
    fit = select.fit(x,y)
    features = x.columns[fit.get_support()]
    print("The most correlated columns for loan_status are ",features[0]," and ",features[1])
      
    query = "drop table "+t_name
    cur.execute(query)
    df.commit()
    cur.close()
    df.close()
    path = "mysql://root:Nivash%4003@localhost/Nivash_c"
    engine = create_engine(path)
    df_1.to_sql(t_name,con = engine, index = False)
    print("File cleaned and appended in SQL")
    return df_1