import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Bird Species EDA Dashboard",
    layout="wide"
)

st.title("🦜 Bird Species Monitoring Dashboard")

forest_sheets = pd.read_excel(
    "Bird_Monitoring_Data_FOREST.XLSX",
    sheet_name=None
)

grass_sheets = pd.read_excel(
    "Bird_Monitoring_Data_GRASSLAND.XLSX",
    sheet_name=None
)

forest_df = pd.concat(
    forest_sheets.values(),
    ignore_index=True
)

grass_df = pd.concat(
    grass_sheets.values(),
    ignore_index=True
)

forest_df["Habitat"] = "Forest"
grass_df["Habitat"] = "Grassland"

df = pd.concat(
    [forest_df, grass_df],
    ignore_index=True
)

st.success("Dataset Loaded Successfully")

col1, col2 = st.columns(2)

with col1:
    st.metric("Rows", df.shape[0])

with col2:
    st.metric("Columns", df.shape[1])

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Columns")
st.write(df.columns.tolist())