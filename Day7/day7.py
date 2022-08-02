import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")
value = [65,30,50,20,15]
labels = ["Tamil","English","Maths","science","social"]
plt.pie(value,labels=labels,wedgeprops={'edgecolor':'black'})
plt.tight_layout()
plt.title("Marks")
plt.savefig("marks pie chart")
plt.show()