import pandas as pd
import numpy as np
import streamlit as st


  
def main():
  data = pd.read_excel("Produits_dopants_20160317.xlsx")
  
  
  
  st.title('Drops Substances Analysis')
  st.subheader('')
  # st.dataframe(data.head(10))
  
  df = {}
  l = []
  l2 = []
  for classe in data['Classe'].unique():
      l.append(len(data[data['Classe'] == classe]['Substance'].unique()))
      l2.append(len(data[data['Classe'] == classe]['DenomSpe'].unique()))

  df['Classe'] = data['Classe'].unique()
  df['Number of Substances'] = np.array(l)
  df['Number of DenomSpe'] = np.array(l2)
  df = pd.DataFrame(df)
  
  import seaborn as sns
  import matplotlib.pyplot as plt

  # Initialize the matplotlib figure
  f, ax = plt.subplots(figsize=(6, 15))

  # Plot the total crashes
  sns.set_color_codes("pastel")
  sns.barplot(x="Number of DenomSpe", y="Classe", data=df,
              label="Total deviratives", color="b")

  # Plot the crashes where alcohol was involved
  sns.set_color_codes("muted")
  sns.barplot(x="Number of Substances", y="Classe", data=df,
              label="Number of Substances", color="b")

  # Add a legend and informative axis label
  ax.legend(ncol=2, loc="lower right", frameon=True)
  ax.set(xlim=(0, 24), ylabel="",
         xlabel="Distribution of doping substances")
  sns.despine(left=True, bottom=True)
  
  
if __name__ == '__main__':
  main()

  
