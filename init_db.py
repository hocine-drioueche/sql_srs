# Import des modules nécessaires
import io
import pandas as pd
import duckdb

# Connexion à la base de données DuckDB et création du fichier si nécessaire
con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

# ------------------------------------------------------------
# Liste des exercices
# ------------------------------------------------------------
data = {
    "theme": ["cross_joins", "cross_joins"],  # Thèmes des exercices
    "exercise_name": [
        "beverages_and_food",
        "sizes_and_trademarks",
    ],  # Noms des exercices
    "tables": [
        ["beverages", "food_items"],
        ["sizes", "trademarks"],
    ],  # Tables nécessaires pour chaque exercice
    "last_reviewed": [
        "1980-01-01",
        "1970-01-01",
    ],  # Dates de dernière révision initiales
}
memory_state_df = pd.DataFrame(data)
con.execute("CREATE TABLE IF NOT EXISTS memory_state AS SELECT * FROM memory_state_df")

# ------------------------------------------------------------
# Exercices de CROSS JOIN
# ------------------------------------------------------------

# Données de la table "beverages"
csv = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""
beverages = pd.read_csv(io.StringIO(csv))
con.execute("CREATE TABLE IF NOT EXISTS beverages AS SELECT * FROM beverages")

# Données de la table "food_items"
csv2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""
food_items = pd.read_csv(io.StringIO(csv2))
con.execute("CREATE TABLE IF NOT EXISTS food_items AS SELECT * FROM food_items")

# Données de la table "sizes"
sizes = """
size
XS
M
L
XL
"""
sizes = pd.read_csv(io.StringIO(sizes))
con.execute("CREATE TABLE IF NOT EXISTS sizes AS SELECT * FROM sizes")

# Données de la table "trademarks"
trademarks = """
trademark
Nike
Asphalte
Abercrombie
Lewis
"""
trademarks = pd.read_csv(io.StringIO(trademarks))
con.execute("CREATE TABLE IF NOT EXISTS trademarks AS SELECT * FROM trademarks")

# Ferme la connexion à la base de données
con.close()
