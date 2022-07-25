from matplotlib import pyplot as plt
plt.style.use("bmh")
subjects = ["Tamil", "English", "Maths", "Science", "Social Science"]

student1_mark = [44, 66, 77, 89, 94]
plt.plot(subjects, student1_mark, 'k--o', label="student1_marks")

student2_mark = [39, 45, 60, 88, 97]
plt.plot(subjects, student2_mark, 'b:o', label="student2_marks")

student3_mark = [40, 56, 66, 88, 99]
plt.plot(subjects, student3_mark,'c-o', label="student3_marks")
plt.title("marks graph")
plt.xlabel("Subjects")
plt.ylabel("marks")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("marks plot.png")
plt.show()
