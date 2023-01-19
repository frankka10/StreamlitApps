import pandas as pd
import numpy as np
import streamlit as st

def load_data(data):
  return pd.read_excel(data)

def main():
  data = load_data('Produits_dopants_20160317.xlsx')
  st.title("Drop products")
  st.dataframe(data.head(10))
  
  
if __name__ == '__main__':
  main()
