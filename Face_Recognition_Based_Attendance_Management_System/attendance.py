import tkinter as tk
import pandas as pd


class AttendanceGUI:
    def __init__(self, master):
        # Initialize the GUI
        self.master = master
        self.master.geometry("600x400")

        # Create a label and entry box for the student ID
        id_label = tk.Label(self.master, text="Enter your student ID:")
        id_label.pack()
        self.id_entry = tk.Entry(self.master)
        self.id_entry.pack()

        # Create a button to search for the student's attendance
        search_button = tk.Button(
            self.master, text="Search Attendance", command=self.search_attendance)
        search_button.pack()

        # Create a text box to display the student's attendance
        self.text_box = tk.Text(self.master)
        self.text_box.pack()

        # Load the attendance files into a dictionary of data frames
        self.attendance_dfs = {}
        subjects = ["DMBI", "WT", "AI&DS", "IP", "WEBX"]
        for subject in subjects:
            filename = f"./Mainattendance/{subject}.csv"
            self.attendance_dfs[subject] = pd.read_csv(filename)

    def search_attendance(self):
        # Get the student ID from the entry box
        student_id = self.id_entry.get()

        # Search for the student's attendance in each subject's data frame
        results = []
        for subject, attendance_df in self.attendance_dfs.items():
            student_attendance = attendance_df[attendance_df["Id"] == int(
                student_id)]
            if len(student_attendance) == 0:
                results.append(
                    f"No attendance found for student ID {student_id} in {subject}")
            else:
                results.append(
                    f"Attendance for {subject}:\n{student_attendance.to_string(index=False)}")

        # Display the results in the text box
        self.text_box.delete("1.0", tk.END)
        self.text_box.insert(tk.END, "\n\n".join(results))


if __name__ == '__main__':
    root = tk.Tk()
    app = AttendanceGUI(root)
    root.mainloop()
