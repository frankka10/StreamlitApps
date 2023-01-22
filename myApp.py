import pandas as pd
import numpy as np
import streamlit as st


  
def main():
  
  # Display the header
  st.title("Doping Substances Analysis")
  
  st.subheader("Introduction")
  st.write("This project presents a statistical analysis of data on doping products" 
            "recorded in March 2016 on the website of the French Ministry of Health ")
 
  # Display the dataframe
  st.subheader("What does our dataset look like?")
  st.write("Our dataset contains 2238 rows and 8 columns(features)")
  data = pd.read_excel("Produits_dopants_20160317.xlsx")
  st.dataframe(data)
  st.write("There are the repartitions of the most relevant columns :")
  #with st.expander("Classes"):
   # st.write()
  
  tab1, tab2, tab3, tab4 = st.tabs([data.columns[7],data.columns[0],data.columns[1],data.columns[2]])
  with tab1: 
    st.write("There are {} classes".format(len(data[data.columns[7]].unique())))
  with tab2: 
    st.write("There are {} substances".format(len(data[data.columns[0]].unique())))
  with tab3:
    st.write("There are {} devirates".format(len(data[data.columns[1]].unique())))
  with tab4:
    st.write("There are {} paths of consumption".format(len(data[data.columns[2]].unique())))
  
  
if __name__ == '__main__':
  main()

  
