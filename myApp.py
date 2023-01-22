import pandas as pd
import numpy as np
import streamlit as st


  
def main():
  
  # Display the header
  st.title("Doping Substances Analysis")
  st.subheader("Introduction")
  
  with st.beta_expander(st.subheader("Introduction")):
    st.text("This project presents a statistical analysis of data on doping products" 
            "recorded in March 2016 on the website of the French Ministry of Health ")
  
  # Display the dataframe
  data = pd.read_excel("Produits_dopants_20160317.xlsx")
  st.dataframe(data)
  
  
if __name__ == '__main__':
  main()

  
