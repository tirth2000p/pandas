from sqlalchemy import create_engine
import pymysql
import pandas as pd


pymysql.connect('database-cn.cmzprpz4vkmr.us-east-1.rds.amazonaws.com','Drag', 'jibZav-7mikje-qoztyz')
#my_conn = create_engine("mysql+mysqldb://Drag:jibZav-7mikje-qoztyz@database-cn.cmzprpz4vkmr.us-east-1.rds.amazonaws.com/CM")

my_dict = {
    'class':['five', 'six', 'seven'],
    'No':[5,6,7]
}

df = pd.DataFrame(data=my_dict)

print(df)

df.to_sql(con=my_conn, name='student2', if_exists='overwrite', index=False)