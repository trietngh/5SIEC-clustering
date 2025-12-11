import pandas as pd

df = pd.read_csv("./dataset/nba_players.csv")

# trier par saison
df = df.sort_values("season")

# garder la dernière ligne (donc la dernière saison) pour chaque joueur
df = df.groupby("player_name").tail(1).reset_index(drop=True)

print(df.shape)
print(df.head(10))

#print PCA
# Noms des colonnes d'origine
feature_names = data.columns

# Matrice des loadings (composantes)
loadings = pd.DataFrame(
    pca.components_.T,
    columns=[f"PC{i+1}" for i in range(pca.n_components_)],
    index=feature_names
)

print(loadings)


#kmeans
WCSS = []

for i in range(1,30):
  kmeans_pca = KMeans(n_clusters = i, init = "k-means++", random_state = 42)
  kmeans_pca.fit(scores_pca)
  WCSS.append(kmeans_pca.inertia_)