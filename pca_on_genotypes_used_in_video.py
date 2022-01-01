import pandas as pd
from sklearn import decomposition

df = pd.read_csv('matrix.csv')
df

df.rename(columns={'Unnamed: 0': 'Sample'}, inplace=True)
df

non_snp_columns = ['Population code', 'Sample']

df_snps = df.drop(non_snp_columns, axis=1)
matrix = df_snps.to_numpy()
print(matrix.shape)
matrix

pca = decomposition.PCA(n_components=2)
pca.fit(matrix)

print(pca.explained_variance_ratio_)
print(pca.singular_values_)

to_plot = pca.transform(matrix)
to_plot.shape

import matplotlib.pyplot as plt

plt.scatter(x=to_plot[:, 0], y=to_plot[:, 1])

import altair as alt

df_plot = df[non_snp_columns].copy()
df_plot

df_plot['PC1'] = to_plot[:, 0]
df_plot['PC2'] = to_plot[:, 1]
df_plot

alt.Chart(df_plot).mark_point().encode(
    x='PC1',
    y='PC2',
    color=alt.Color('Population code', scale=alt.Scale(scheme='category20'))
)

pop = pd.read_csv('igsr_populations.tsv', sep='\t')
pop

df_plot = df_plot.merge(pop, on='Population code', how='inner')
df_plot

alt.Chart(df_plot).mark_point().encode(
    x='PC1',
    y='PC2',
    color=alt.Color('Superpopulation name', scale=alt.Scale(scheme='category20')),
    fill='Population code'
)

"""# tSNE"""

from sklearn.manifold import TSNE

X = matrix
X_embedded = TSNE(n_components=2,
                  init='random').fit_transform(X)
X_embedded.shape

df_plot['tsne1'] = X_embedded[:,0]
df_plot['tsne2'] = X_embedded[:,1]

df_plot

"""### tSNE:"""

alt.Chart(df_plot).mark_point().encode(
    x='tsne1',
    y='tsne2',
    color=alt.Color('Superpopulation name', scale=alt.Scale(scheme='category20'))
)

alt.Chart(df_plot).mark_point().encode(
    x='tsne1',
    y='tsne2',
    color=alt.Color('Population code', scale=alt.Scale(scheme='category20'))
)

"""### PCA:"""

alt.Chart(df_plot).mark_point().encode(
    x='PC1',
    y='PC2',
    color=alt.Color('Superpopulation name', scale=alt.Scale(scheme='category20'))
)
