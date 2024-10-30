import io

import duckdb
import pandas as pd
import streamlit as st
import ast

con=  duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review ?",
        ("cross_joins", "GroupBy", "Windows functions"),
        index=None,
        placeholder="Select a thene ...",
    )
    st.write("You selected:", theme)


    exercise=con.execute(f"SELECT * FROM memory_state WHERE theme='{theme}' ").df()
    st.write(exercise)


st.header("enter your code:")
query = st.text_area(label="votre code SQL ici", key="user_input")
#
if query:
    result = con.execute(query).df()
    st.dataframe(result)
#
#     try:
#         result = result[solution_df.columns]
#         st.dataframe(result.compare(solution_df))
#     except KeyError as e:
#         st.write("Some columns are missing")
#
#     n_lines_difference = result.shape[0] - solution_df.shape[0]
#     if n_lines_difference != 0:
#         st.write(
#             f"result has a {n_lines_difference} lines difference with the solution"
#         )
#
#
tab2, tab3 = st.tabs(["Tables", "Solution"])
#
with tab2:
    exercise_tables= ast.literal_eval(exercise.loc[0, "tables"])
    for table in exercise_tables:
        st.write(f"table : {table}")
        df_table =con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(df_table)

with tab3:
    exercise_name= exercise.loc[0, "exercise_name"]
    with open(f"answers/{exercise_name}.sql","r") as f:
        answer=f.read()
    st.write(answer)
