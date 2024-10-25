# scatter plot
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.set_theme(style="ticks", color_codes=True)
# titanic = sns.load_dataset("titanic")
# g=sns. FacetGrid(titanic, row="sex", hue="alone")
# g=(g.map(plt.scatter, "age", "fare").add_legend())
# plt.show()
# print(5+6)


import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", marginal_y="violin",
marginal_x="box", trendline="ols", template="simple_white")
fig.show()