import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./dataset/nba_players.csv")

unused_features = ['index', 'age','team_abbreviation', 'college', 'country', 'draft_round', 'season']

for feature in unused_features:
    if feature in df.columns:
        df = df.drop(columns=[feature])

# Nombre d'échantillons et de features
print("Number of samples:", df.shape[0])
print("Number of features:", df.shape[1])

df.head(10)
#preprocessing à faire :
#1)collones à retirer -> #,team_abbreviation,college,country,draft_year,draft_number,draft_number,season
#2)pour chaque valeur possible de player_name, il faut moyenner les valeur de toutes les des diff années


