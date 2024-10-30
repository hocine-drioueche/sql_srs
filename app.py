import io
import duckdb
import pandas as pd
import streamlit as st
import ast

# Connexion à la base de données
con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

# Menu latéral pour sélectionner le thème
with st.sidebar:
    theme = st.selectbox(
        "What would you like to review?",
        ("cross_joins", "GroupBy", "Windows functions"),
        index=0,  # index=0 par défaut, ajustable selon votre besoin
        placeholder="Select a theme..."
    )
    st.write("You selected:", theme)

    # Récupération de l'exercice pour le thème sélectionné
    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme='{theme}'").df()
    st.write(exercise)

    exercise_name = exercise.loc[0, "exercise_name"]
    with open(f"answers/{exercise_name}.sql", "r") as f:
            answer = f.read()

    solution_df =con.execute(answer).df()


st.header("Enter your code:")
query = st.text_area(label="Votre code SQL ici", key="user_input")

if query:
    # Exécution de la requête SQL de l'utilisateur
    result = con.execute(query).df()
    st.dataframe(result)


    try:
        result= result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write ("some columns are missing")


    n_lines_difference =result.shape[0]-solution_df.shape[0]
    if n_lines_difference != 0:
        st.write(
            f"result has a {n_lines_difference} lines difference with the solution_df"
        )


# Onglets pour afficher les tables et la solution
tab2, tab3 = st.tabs(["Tables", "Solution"])

# Onglet Tables
with tab2:
    exercise_tables = ast.literal_eval(exercise.loc[0, "tables"])  # Conversion en liste
    for table in exercise_tables:
        st.write(f"Table : {table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(df_table)

# Onglet Solution
with tab3:
        st.write(answer)

