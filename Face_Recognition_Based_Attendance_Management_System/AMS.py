from os import system
from tkinter import *
import tkinter.messagebox
import time
import os
import subprocess

student_login_frame = None
student_password_entry = None
student_username_entry = None


def student_login():
    cmd = "python ./attendance.py"
    subprocess.call(cmd, shell=True)


def home():
    global display_frame
    display_frame = Frame(student_login_frame, width=650,
                          height=500, bg='#EBF2F8')
    display_frame.place(x=250, y=0)
    display_frame.tkraise()
    ned_logo = Label(display_frame, image=img1, bg='#EBF2F8')
    ned_logo.place(x=-180, y=-200)
    sp_logo = Label(display_frame, image=img2, bg='#EBF2F8')
    sp_logo.place(x=150, y=175)


var2 = None
attendance_frame = None


display_frame = None
dashboard_button_1 = None


def admin_authorize(event):
    if admin_username_entry.get() == 'admin' and admin_password_entry.get() == 'password':
        cmd = "python ./main.py"
        subprocess.call(cmd, shell=True)


def student_exit():
    main_window()


def admin_exit():
    main_window()


admin_username_entry = None
admin_password_entry = None
admin_login_frame = None


def admin_login():
    global admin_login_frame
    admin_login_frame = Frame(
        student_admin_frame, width=900, height=500, bg='#EBF2F8')
    admin_login_frame.place(x=0, y=0)
    admin_login_frame.tkraise()
    admin_icon = Label(admin_login_frame, image=img7, bd=0, bg='#EBF2F8')
    admin_icon.place(x=370, y=10)
    username_label = Label(admin_login_frame, text='Username', font=(
        'Berlin Sans FB', 16), bg='#EBF2F8')
    username_label.place(x=405, y=200)
    global admin_username_entry
    admin_username_entry = Entry(admin_login_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',
                                 highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    admin_username_entry.place(x=350, y=240)
    password_label = Label(admin_login_frame, text='Password', font=(
        'Berlin Sans FB', 16), bg='#EBF2F8')
    password_label.place(x=405, y=280)
    global admin_password_entry
    admin_password_entry = Entry(admin_login_frame, bg='white', show='*', relief='sunken',
                                 highlightcolor='#D2E0F1', highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    admin_password_entry.place(x=350, y=320)
    admin_password_entry.bind('<Return>', admin_authorize)
    login_button = Button(admin_login_frame, image=img6, bd=0, bg='#EBF2F8')
    login_button.bind('<Button-1>', admin_authorize)
    login_button.place(x=357, y=380)
    cancel_button = Button(admin_login_frame, image=img8,
                           bd=0, bg='#EBF2F8', command=admin_exit)
    cancel_button.place(x=357, y=430)


student_admin_frame = None


def main_window():
    global student_admin_frame
    student_admin_frame = Frame(root, width=900, height=500, bg="#EBF2F8")
    student_admin_frame.place(x=0, y=0)
    main_logo_image = Label(student_admin_frame, image=img5, bg='#EBF2F8')
    main_logo_image.place(x=200, y=50)
    black_button_student = Button(
        student_admin_frame, image=img3, bd=0, command=student_login, bg="#EBF2F8")
    black_button_student.place(x=100, y=300)
    black_button_teacher = Button(
        student_admin_frame, image=img4, bd=0, command=admin_login, bg="#EBF2F8")
    black_button_teacher.place(x=500, y=300)


root = Tk()
root.geometry("900x500")
root.title("Attendance System")
img1 = PhotoImage(file='ned-student-portal-logo.png')
img2 = PhotoImage(file='student_portal-logo.png')
img3 = PhotoImage(file='student-login.png')
img4 = PhotoImage(file='admin-login.png')
img5 = PhotoImage(file='logo-eAttendance.png')
img6 = PhotoImage(file='login-button.png')
img7 = PhotoImage(file='admin-icon.png')
img8 = PhotoImage(file='cancel-button.png')

main_window()

root.mainloop()
