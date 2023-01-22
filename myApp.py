import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

data = pd.read_excel("Produits_dopants_20160317.xlsx")

def substances_derivates_per_class():
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
  return pd.DataFrame(df)

def status_proportion_per_class(classe):
  l = []
  df = {}
  for status in data['Statut'].unique():
    l.append(len(data[(data['Classe'] == classe) & (data['Statut'] == status)]['DenomSpe'].unique()))
  df['Statut'] = data['Statut'].unique()
  df['Proportion'] = np.array(l)
  return pd.DataFrame(df)


def main():
  
  # Display the header
  st.title("Doping Substances Analysis")
  
  st.subheader("Introduction")
  st.write("This project presents a statistical analysis of data on doping products" 
            "recorded in March 2016 on the website of the French Ministry of Health ")
 
  # Display the dataframe
  st.subheader("What does our dataset look like?")
  st.write("Our dataset contains 2238 rows and 8 columns(features)")
  st.dataframe(data)
  st.write("There are the repartitions of the most relevant columns :")
  #with st.expander("Classes"):
   # st.write()
  
  selected_columns = st.multiselect("Select the columns you want to see the length ", data.columns, default = data.columns[7])
  if selected_columns:
    tabs = []
    for i in range(len(selected_columns)):
      tabs.append("tab{}".format(i))
    tabs = st.tabs(selected_columns)
    for i in range(len(tabs)):
      with tabs[i]:
        st.write("There are {} unique elements in this column".format(len(data[selected_columns[i]].unique())))
  
  
  # Substances and derivates per classes
  st.subheader("Overview of the quantity of substances and devirates per classes")
  df = substances_derivates_per_class()
  st.bar_chart(df.set_index('Classe'))  
  with st.expander("Explanation"):
    st.write("This figure describes on the same graph the number of substances per class "
             "and the number of deviations of substances per class found in our dataset")
  
  # Classes with the n-highest number of substances
  st.subheader("Overview of the quantity of substances and devirates per classes")
  df = substances_derivates_per_class()
  st.area_chart(df.set_index('Classe'))  
  with st.expander("Explanation"):
    st.write("This figure describes on the same graph the number of substances per class "
             "and the number of deviations of substances per class found in our dataset")
    
  # Proportion of statut 
  st.subheader("Proportion of statut")
  st.write("About the statutes, they concern the consumption of these"
           "doping substances during and outside competition")
  option = st.selectbox(
    'Select a class among the following ones :', data['Classe'].unique())
  if option:
    df = status_proportion_per_class(option)
    st.dataframe(df)
    fig = px.pie(df, values = 'Proportion', names = 'Statut', title = 'Proportion of statut')
    st.plotly_chart(fig)  
    with st.expander("Explanation"):
      st.write("This figure describes on the same graph the number of substances per class "
               "and the number of deviations of substances per class found in our dataset")
  
  
if __name__ == '__main__':
  main()

  
