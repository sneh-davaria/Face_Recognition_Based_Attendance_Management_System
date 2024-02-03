import pandas as pd

df = pd.read_csv("./Attendance/Attendance_05-04-2023.csv")
total_lec = 6  # int(input("Enter Total number of lectures:"))
counts = df["Name"].value_counts()
percentage = (counts/total_lec)*100
print(percentage[percentage < 75])
