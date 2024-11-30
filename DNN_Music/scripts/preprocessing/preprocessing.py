def clean_df(df):
    df = df.drop(['filename', 'length'], axis=1)
    return df