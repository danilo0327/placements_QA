# Dependencies
import pandas as pd
import streamlit as st 
import plotly.express as px 
from PIL import Image 

st.set_page_config(page_title='Coty QAs')
st.header('Coty QAs 2023s')
st.subheader('Pre trafficking QA')
st.caption('1. Traffic Sheet (TS)')
st.write('En esta sección del pre trafficking QA podras realizar un analisis exploratorio del TS')

### --- Load Dataframe 1 (Traffic sheet)
excel_file = r"C:\Users\danduart2\Desktop\Tickets\Open\COTY-11257\TS URL SWAP\ID~GLB00057IY_YQ~24FY_BS~PUBUSLOC_MK~us_AR~ZEN_CH~MULTI_MB~covrgrl_CN~FY24 2H Cleantopia_CP~4300006115_CI~TBD_OB~AWA_IO~CP2F0SM.xlsx"
df1 = pd.read_excel(excel_file, header=10)
df1.dropna(subset=['SITE'], inplace=True)

st.dataframe(df1)

st.caption('1. DCM Export (Legacy Export)')
st.write('En esta sección del pre trafficking QA podras realizar un analisis exploratorio del Legacy de DCM')


### --- Load Dataframe 2 (DCM Export)
export_file = r"C:\Users\danduart2\Downloads\CampaignSpreadsheet-31209116-2024-01-04.xls"
df2 = pd.read_excel(export_file)
df2.drop(['Error Message'], axis=1, inplace=True)
df2.dropna(subset=['Site Name'], inplace=True)


st.dataframe(df2)
