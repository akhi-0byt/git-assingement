# steps for data visualization 
# 1. imports libraries
import seaborn as sns
import matplotlib.pyplot as plt

# 2.set a theme 
sns.set_theme(style="ticks",color_codes=True)

# 3.import data set(u can also import your own data)
kashti= sns.load_dataset("titanic")
print(kashti)
# 4.plot basic graph (with one variable)
p = sns.countplot(x="sex",data=kashti,hue="class")
p.set_title("graph of class in titanics")
plt.show()

# 4.plot basic graph (with two variable)