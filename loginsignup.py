from tkinter import *
from tkinter import messagebox
import ast
import subprocess

root = Tk()
root.title('Log In')
root.geometry('925x500+150+120')
root.configure(bg="#fff")
root.resizable(False, False)

def Signin():
    userid = user.get()
    password = code.get()

    '''
    file = open('datasheet.txt', 'r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    ##print(r.keys())
    ##print(r.values())
    '''
    # import pymysql for the connceting database
    import pymysql
    db = pymysql.connect(host='localhost', user='root', password='test', db='driverdb')
    sql = "select * from signup where userid=%s and password=%s"
    val = (userid,password)
    cur = db.cursor()  # use cursor to connect database with python:
    cur.execute(sql, val)
    if True:

        root.destroy()
        # code for opean another file ::
        import subprocess

        # Execute the other.py script as if it were written in the main.py file.
        subprocess.call(["python", "demo drowsiness.py"], shell=True)

        # Execute the other.py script as a separate process.
        subprocess.Popen(["python", "demo drowsiness.py"], shell=True)

    else:
        messagebox.showerror('Invalid', 'Invalid username and password')

##********************************************************************************************************************
def signup_command():
    window=Toplevel(root)
    window.title('Log Up')
    window.geometry('925x500+150+120')
    window.configure(bg="#fff")
    window.resizable(False, False)

    def Signup():
        userid = user.get()
        email = code.get()
        password = conform_code.get()


        try:
                import pymysql
                db = pymysql.connect(host='localhost', user='root', password='test', db='driverdb')
                sql = "insert into signup values(%s,%s,%s)"
                val = (userid,email,password)
                cur = db.cursor()
                cur.execute(sql, val)
                db.commit()
                print("information saved")

        except:
                file = open('datasheet.txt', 'w')
                pp = str({'username': 'password'})
                file.write(pp)
                file.close()

        else:
            messagebox.showinfo('Invalid', 'saved successfully')

    def sign():
        window.destroy()

    img = PhotoImage(file='signup.png')
    Label(window, image=img, bg='white').place(x=50, y=50)

    frame = Frame(window, width=350, height=390, bg='#fff')
    frame.place(x=480, y=50)

    heading = Label(frame, text='Sign Up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    # ------------------------------------------------------------------------------
    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name == '':
            user.insert(0, 'Username')

    user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0, 'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    # ---------------------------------------------------------------------------------------------------------------
    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        name = code.get()
        if name == '':
            code.insert(0, 'Email')

    code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    code.place(x=30, y=150)
    code.insert(0, 'Email')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    # --------------------------------------------------------------------------------
    def on_enter(e):
        conform_code.delete(0, 'end')

    def on_leave(e):
        if conform_code.get() == '':
            conform_code.insert(0, 'Password')

    conform_code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    conform_code.place(x=30, y=220)
    conform_code.insert(0, 'Password')
    conform_code.bind('<FocusIn>', on_enter)
    conform_code.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

    #####================================================================================
    Button(frame, width=39, pady=7, text='Sign Up', bg='#57a1f8', fg='white', border=0, command=Signup).place(x=35,
                                                                                                              y=280)
    label = Label(frame, text="I have an account", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
    label.place(x=90, y=340)

    sign_in = Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=sign)
    sign_in.place(x=200, y=340)

    window.mainloop()

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# SIGN IN  page code start from here ::
###****************************************************************************************************************

img = PhotoImage(file='signin.png')
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg='white')
frame.place(x=480, y=70)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

# ----------------------------------------------------------------------------------------
def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

# -------------------------------------------------------------------------------------------
def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'password')

code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

#####======================================================================================
Button(frame, width=39, pady=7, text='Sign In', bg='#57a1f8', fg='white', border=0, command=Signin).place(x=35, y=204)
label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text='Sign Up', border=0, bg='white', cursor='hand2', fg='#57a1f8',
                 command=signup_command)
sign_up.place(x=215, y=270)

root.mainloop()