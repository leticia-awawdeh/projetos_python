import pandas as pd

pd.read_csv(r"C:\Users\Letícia\Desktop\ava.csv")

df = pd.read_csv(r"C:\Users\Letícia\Desktop\ava.csv", sep=';')

df.sort_values(by='S-rank')

def formatar_colunas(df):
    df['Liquidez'] = df['Liquidez (estimativa via GFinance)']
    df.drop('Liquidez', axis=1, inplace=True)
    df['Posição'] = df['Posição'].astype(int)
    df['FII'] = df['FII'].astype(str)
    df['Mediana Mensal 12M'] = df['Mediana Mensal 12M'].astype(float)
    df['P/VPA'] = df['P/VPA'].astype(float)
    df['Preço da cota'] = df['Preço da cota'].astype(float)
    df['Liquidez'] = df['Liquidez'].astype(float)
    return df

df.rename(columns={'Liquidez (estimativa via GFinance)': 'Liquidez'}, inplace=True)

print(df)
