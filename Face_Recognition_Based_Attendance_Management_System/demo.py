import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import messagebox


class AttendanceManagerGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Attendance Manager")

        # create label for course selection
        course_label = tk.Label(self.window, text="Select Course:")
        course_label.grid(row=0, column=0)

        # create dropdown for course selection
        courses = ["DMBI", "WT", "AI&DS", "IP", "WEBX"]
        self.selected_course = tk.StringVar()
        self.course_dropdown = ttk.Combobox(
            self.window, values=courses, textvariable=self.selected_course)
        self.course_dropdown.grid(row=0, column=1)

        # create button to load attendance
        load_button = tk.Button(self.window, text="Load",
                                command=self.load_attendance)
        load_button.grid(row=0, column=2)

        # create treeview to display attendance
        self.attendance_treeview = ttk.Treeview(self.window)
        self.attendance_treeview["columns"] = (
            "Student", "Total Present", "Percentage")
        self.attendance_treeview.column("#0", width=0, stretch=tk.NO)
        self.attendance_treeview.column("Student", anchor=tk.CENTER, width=200)
        self.attendance_treeview.column(
            "Total Present", anchor=tk.CENTER, width=150)
        self.attendance_treeview.column(
            "Percentage", anchor=tk.CENTER, width=150)
        self.attendance_treeview.heading("#0", text="")
        self.attendance_treeview.heading(
            "Student", text="Student", anchor=tk.CENTER)
        self.attendance_treeview.heading(
            "Total Present", text="Total Present", anchor=tk.CENTER)
        self.attendance_treeview.heading(
            "Percentage", text="Percentage", anchor=tk.CENTER)
        self.attendance_treeview.grid(row=1, column=0, columnspan=3)

        # create label for total attendance
        total_label = tk.Label(self.window, text="Total Lectures:")
        total_label.grid(row=3, column=0)

        # create entry for total attendance
        self.total_entry = tk.Entry(self.window)
        self.total_entry.grid(row=3, column=1)

        # create button to show defaulters
        defaulters_button = tk.Button(
            self.window, text="Show Defaulters", command=self.show_defaulters)
        defaulters_button.grid(row=3, column=2)

        self.window.mainloop()

    def load_attendance(self):
        file_path = "./Mainattendance/" + self.selected_course.get() + ".csv"
        attendance_df = pd.read_csv(
            "./Mainattendance/" + self.selected_course.get() + ".csv")
        student_list = attendance_df["Name"].unique()
        total_attendance = int(self.total_entry.get())
        for student in student_list:
            present_count = attendance_df[attendance_df["Name"]
                                          == student]["Time"].count()
            percentage = present_count / total_attendance * 100
            self.attendance_treeview.insert("", tk.END, text="", values=(
                student, present_count, round(percentage, 2)))

    def show_defaulters(self):
        defaulter_list = []
        for student in self.attendance_treeview.get_children():
            percentage = self.attendance_treeview.item(student, "values")[2]
            if float(percentage) < 75:
                student_name = self.attendance_treeview.item(student, "values")[
                    0]
                defaulter_list.append(student_name)
        defaulter_string = ", ".join(defaulter_list)
        if defaulter_string:
            messagebox.showinfo(
                "Defaulters", "The following students have attendance less than 75%: {}".format(defaulter_string))
        else:
            messagebox.showinfo(
                "Defaulters", "No students have attendance less than 75%.")


if __name__ == "__main__":
    attendance_manager_gui = AttendanceManagerGUI()
