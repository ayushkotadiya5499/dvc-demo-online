import pandas as pd
import numpy as np
import os

def load_data(url):
    df=pd.read_csv(url)
    return df

def drop_columns(df,column_name):
    df=df.drop(columns=[column_name],axis=0)
    return df

def main():
    df=load_data('https://raw.githubusercontent.com/araj2/customer-database/refs/heads/master/Ecommerce%20Customers.csv')
    df=df.iloc[:,3:]
    df=drop_columns(df,'Avg. Session Length')
    df=df[df['Length of Membership']>1]
    data='data'
    df.to_csv(os.path.join(data,'customer.csv'))

if __name__=='__main__':
    main()