
#"" (double quatation mark)
#''(single quatation mark)
#"''"(triple quatation mark )
# kisi bhi quatation mark
#  me likhe answer same ata hai koi 
#reason nhi hai ki kisi bhi quatation me likh sakte hain

# print('Test for double quate test ')
# print ('''test for double quatq test''')
# print(  "what's up   ?")
# print(17+90)
# print("Suraj+gutame")
# a = "suraj "
# b = "gautam"
# c = a+b
# print(c)


import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", marginal_y="violin",
marginal_x="box", trendline="ols", template="simple_white")
fig.show()

