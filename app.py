import streamlit as st
import pandas as pd
import duckdb

st.write("""
# SQL SRS
Spaced Repetition System SQL practice
""")

option = st.selectbox(

    "What would you like to review ?",
    ("Joins", "GroupBy", "Windows functions"),
    index=None,
    placeholder= "Select a thene ...",
)


st.write('You selected:',option)

data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)


tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    #st.header("A cat")
    #st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

    sql_querry = st.text_area(label="Entrez votre input")
    result = duckdb.query(sql_querry).df()
    st.write(f"Vous avez entré la query suivante:{sql_querry}")
    st.dataframe(result)



with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
