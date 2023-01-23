import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

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

def path_proportion_per_class(classe, substance):
  df = {}
  l = []
  for voie in data[(data['Classe'] == classe) & (data['Substance'] == substance)]['Voie'].unique():
    l.append(len(data[(data['Classe'] == classe) & (data['Substance'] == substance) & (data['Voie'] == voie)]))
  df['Voie'] = data[(data['Classe'] == classe) & (data['Substance'] == substance)]['Voie'].unique()
  df['Repartition'] = np.array(l)
  return pd.DataFrame(df)

def most_substances_classes(n):
  df = substances_derivates_per_class()
  df = df.sort_values(by='Number of Substances', ascending=False)
  return df.head(n)

def most_derivates_classes(n):
  df = substances_derivates_per_class()
  df = df.sort_values(by='Number of DenomSpe', ascending=False)
  return df.head(n)

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
  
  selected_columns = st.multiselect("Select the columns you want to see the length ", data.columns, default = data.columns[7])
  if selected_columns:
    tabs = []
    for i in range(len(selected_columns)):
      tabs.append("tab_{}".format(i))
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
  
  
  st.subheader("Overview of the quantity of substances and devirates per classes")
  df = substances_derivates_per_class()
  st.area_chart(df.set_index('Classe'))  
  with st.expander("Explanation"):
    st.write("This figure describes on the same graph the number of substances per class "
             "and the number of deviations of substances per class found in our dataset")
  
  # Classes with the n-highest number of substances
  tab1, tab2 = st.tabs(['K- Classes with the highest number of Substances','K- Classes with the highest number of Derivates'])
  with tab1:
    k1 = st.slider('Choose the number of classes with the highest number of substances you want to display', 0, 20, 10)
    df = most_substances_classes(k1)
    fig, ax = plt.subplots()
    ax.stem(df['Classe'], df['Number of Substances'], orientation='horizontal')
    st.pyplot(fig)
  with tab2:
    k2 = st.slider('Choose the number of classes with the highest number of substances you want to display', 0, 20, 10, key='k2')
    df = most_derivates_classes(k2)
    fig2, ax = plt.subplots()
    ax.scatter(df['Number of DenomSpe'], df['Classe'])
    st.pyplot(fig2)
    
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
      
   # Proportion of paths per substance
  st.subheader("Proportion of paths consumption per class")
  st.write("About the acquisition process, they concern the acquisition of these"
           "doping substances, whether you may have an authorization or not.")
  
  col1, col2 = st.columns(2)
  with col1:
    classe = st.selectbox(
    'Select a class among the list :', data['Classe'].unique(), key='option1')
  with col2:
    substance = st.selectbox(
    'Select a substance of the chosen class :', data[data['Classe'] == classe]['Substance'].unique(), key='option2')
  
  if substance:
    df2 = path_proportion_per_class(classe, substance)
    st.dataframe(df2)
    fig2 = px.pie(df2, values = 'Repartition', names = 'Voie', title = 'Proportion of path consumption ')
    st.plotly_chart(fig2)  
    with st.expander("Explanation"):
      st.write("This figure describes on the same graph the number of substances per class "
               "and the number of deviations of substances per class found in our dataset")
  
  # Informations about the use of the derivates
  st.subheader('What is the specific information about their use ?')
  col4, col5, col6 = st.columns(3)
  with col4:
    classe1 = st.selectbox(
    'Select a class among the list :', data['Classe'].unique(), key='k1')
  with col5:
    substance1 = st.selectbox(
    'Select a substance of the chosen class', data[data['Classe'] == classe1]['Substance'].unique(), key='sub')
  with col6:
    derivate = st.selectbox(
    'Select a derivate of the substance', data[(data['Classe'] == classe1) & (data['Substance'] == substance1)]['DenomSpe'].unique(), key='der')
  
  col7, col8 = st.columns(2)
  with col7:
    st.write('Complemantary informations about the selected substance or derivate')
    st.write('{}',.format(data[(data['Classe'] == classe1) & (data['Substance'] == substance1) & (data['DenomSpe'] == derivate)]['Informations complémentaires']))
  with col8:
    st.write('Other complemantary informations about the selected substance or derivate')
    st.write(data[(data['Classe'] == classe1) & (data['Substance'] == substance1) & (data['DenomSpe'] == derivate)]['Informations complémentaires bis'])
   
    
    
    
if __name__ == '__main__':
  main()

  
