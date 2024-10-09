from tkinter import Tk, Label, Button
import subprocess

def show():
    root = Tk()  # Use the main Tk window
    root.title("APP")
    root.geometry('925x500+150+120')
    root.configure(bg="powderblue")  # Set the background color

    label_text = 'WELCOME TO \n \n DRIVER DROWSINESS DETECTION!'
    # Set text, text color, and center the text
    label = Label(root, text=label_text, bg='powderblue', font=('calibri(Body)', 38, 'bold'), fg='black', justify='center')
    label.pack(expand=True)

    # Define the function to open loginsignup.py and close the main window
    def open_loginsignup():
        root.destroy()  # Close the main window
        subprocess.run(["python", "loginsignup.py"])

    start_button = Button(root, text="Start Project", command=open_loginsignup, bg='darkgreen', fg='white', font=('calibri(Body)', 10, 'bold'), height=2, width=15)
    # Set button color, text color, font size, height, and width
    start_button.pack(pady=20)

    root.mainloop()

# Call the show function
show()
