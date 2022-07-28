import numpy as np
import matplotlib.pyplot as plt

subjects = ["Tamil", "English", "Maths", "Science", "Social Science"]
x_indexes = np.arange(len(subjects))
width = 0.30
student1_mark = [44, 66, 77, 89, 94]
plt.bar(x_indexes-width, student1_mark,width=width, label="student1_marks")

student2_mark = [39, 45, 60, 88, 97]
plt.bar(x_indexes, student2_mark,width=width,label="student2_marks")

student3_mark = [40, 56, 66, 88, 99]
plt.bar(x_indexes+width, student3_mark,width=width,  label="student3_marks")
plt.xticks(ticks=x_indexes,labels=subjects)
plt.title("marks graph")
plt.xlabel("Subjects")
plt.ylabel("marks")
plt.legend()
plt.tight_layout()
plt.savefig("marks barchart.png")
plt.show()
