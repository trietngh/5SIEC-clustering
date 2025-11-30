# Pour le compte de rendu

Faire des analyse pourquoi ça ne marche pas
expliquer pour quoi on obtient ce type de contenu
...

1/ coefficient de silhouette

Il mesure à quel point les objets sont bien regroupés dans leur cluster, tout en étant bien séparés des autres clusters.

Pour chaque point il compare  la distance moyenne entre ce point et les autres points de son propre cluster et la distance moyenne entre ce point et les points du cluster le plus proche.

silhouette score = intracluster distance / intercluster distance

proche de 1: clustering bien séparé et cohérent
proche de 0: clusters qui se chevauchent

2/Indice de Davies-Bouldin

Il mesure la compacité des clusters et leur séparation les uns par rapport aux autres.

Pour chaque cluster il calcule comment les points sont serres entre eux et mesure la distance entre ce cluster et les autres.

L’indice est une moyenne du "ratio" compacité/séparation. Plus la valeur est proche de 0, meilleur est le clustering.

3/Indice de Calinski-Harabasz



davies_bouldin_score = metrics.davies_bouldin_score(datanp, labels)
print("Davies_bouldin score :", davies_bouldin_score)
plus le score est bas, plus les clusters sont compacts et eloignes

calinski_harabasz_score = metrics.calinski_harabasz_score(datanp, labels)
print("calinski_harabasz score :", calinski_harabasz_score)
plus le score est haut, mieu c'est


