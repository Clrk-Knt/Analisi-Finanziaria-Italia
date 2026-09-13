import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import yfinance as yf

df_mib = yf.download("FTSEMIB.MI", start="2020-01-01")["Close"]
df_isp = yf.download("ISP.MI", start="2020-01-01")["Close"]

if isinstance(df_mib, pd.DataFrame):
  df_mib = df_mib.iloc[:, 0]
if isinstance(df_isp, pd.DataFrame):
  df_isp = df_isp.iloc[:, 0]

df = pd.DataFrame({"FTSE_MIB": df_mib, "Intesa_Sanpaolo": df_isp}).dropna()
df.index.name = "Data"

df_norm = (df / df.iloc[0]) * 100

plt.figure(figsize=(12, 6))
plt.plot(
    df_norm.index,
    df_norm["FTSE_MIB"],
    label="FTSE MIB (Indice)",
    color="royalblue",
)
plt.plot(
    df_norm.index,
    df_norm["Intesa_Sanpaolo"],
    label="Intesa Sanpaolo (Banca/Tassi)",
    color="darkorange",
)
plt.title("Confronto Indice di Borsa vs Settore Bancario (Base 100 = 2020)")
plt.xlabel("Data")
plt.ylabel("Valore Indicizzato")
plt.legend()
plt.grid(True)
plt.show()

correlazione = df.corr()
print("\nMatrice di Correlazione:")
print(correlazione)

plt.figure(figsize=(6, 5))
sns.heatmap(correlazione, annot=True, cmap="coolwarm", vmin=-1, vmax=1, fmt=".2f")
plt.title("Matrice di Correlazione: FTSE MIB vs Intesa Sanpaolo")
plt.tight_layout()
plt.show()