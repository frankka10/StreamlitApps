import pandas as pd
import numpy as np
import streamlit as st

def main():
  df = pd.read_excel("Produits_dopants_20160317.xlsx")
  
  st.dataframe(df.head())
  
if __name__ == '__main__':
  main()

  
