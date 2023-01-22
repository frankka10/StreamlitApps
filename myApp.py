import pandas as pd
import numpy as np
import streamlit as st


  
def main():
  data = pd.read_excel("Produits_dopants_20160317.xlsx")
  st.dataframe(data)
  
  
if __name__ == '__main__':
  main()

  
