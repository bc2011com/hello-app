import streamlit as st

st.header("Hello World 👏")

st.write("This is my first app")

import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
df = pd.read_csv(url)
df2 = df.groupby('species')['body_mass_g'].mean()

st.bar_chart(df2)
st.line_chart(df2)
st.area_chart(df2)

genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

st.write(f"You selected {genre}")
