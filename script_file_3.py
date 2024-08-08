from pymysql import connect
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


def visual(t_name):
    
    df = connect(host='localhost', user='root', password='Nivash@03',database = 'Nivash_C')
    cur = df.cursor()
    query = "select * from "+t_name
    cur.execute(query)
    df1 = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    df_1 = pd.DataFrame(df1, columns=columns)

    
    print("Line Plot")
    sns.lineplot(x=' no_of_dependents',y=' loan_amount',data=df_1)
    plt.title("Loan amount based on no. of dependents")
    plt.xlabel("No_of_dependents")
    plt.ylabel('Loan_amount')
    plt.show()
    
    print("Histogram")
    sns.histplot(df_1[' loan_amount'],bins=10,kde=True)
    plt.xlabel('Loan_Amount')
    plt.ylabel('Count')
    plt.show()
    
    print("Pie Chart")
    _count = df_1[' no_of_dependents'].value_counts()
    plt.pie(_count, labels=_count.index,autopct='%1.1f%%')
    plt.title('No_of_dependencies')
    plt.show()