from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
#student ka use hum esliye kr rhe hai ki jo student.py file hai use link kr ske tha's why now we make a funstion for that 
from student import Student


class Fase_reco_system:
    def __init__(self,root):
        self.root= root
        self.root.geometry("1800x1800+0+0")
        self.root.title("Fase recognagation system")
        #logo image in center 
        image= Image.open(r"D:\student_attandenc_system\logo.png")
        image=image.resize((150,141),Image.ANTIALIAS)
        self.photoimage= ImageTk.PhotoImage(image)
        fist_labal= Label(self.root, image=self.photoimage)
        fist_labal.place(x=680,y=20,width=150, height=141)
        
        #write a title
        #and we also put text informations like font name and size bg=background colour and fg font colour
        title_lable= Label(self.root, text="KCNIT Students Attendence System ", font=("times new romn", 40, "bold"), bg="gray", fg="black")
        #with the help of place we will put anything in whole window
        title_lable.place(x=20, y=170, width=1480, height=60 )

        #button for student detalis 
       
        image2= Image.open(r"D:\student_attandenc_system\studentsdetalis.jpg")
        image2=image2.resize((460, 200),Image.ANTIALIAS)
        self.photoimage2= ImageTk.PhotoImage(image2)
        button= Button(self.root,command=self.link_student_file,  image= self.photoimage2, cursor="hand2")
        button.place(x=60, y=250, width=460, height=200)
        button2= Button(self.root, text="Sudent Details", command=self.link_student_file,  font=("times new romn", 20, "bold"), bg="blue", fg="white",cursor="hand2")
        button2.place(x=65, y=452, width=450, height=40 )

        #buttton for attandence 
        image3= Image.open(r"D:\student_attandenc_system\attendance.jfif")
        image3=image3.resize((460, 200),Image.ANTIALIAS)
        self.photoimage3= ImageTk.PhotoImage(image3)
        button= Button(self.root, image= self.photoimage3, cursor="hand2")
        button.place(x=1000, y=250, width=460, height=200)
        button2= Button(self.root, text="Attandenc", font=("times new romn", 20, "bold"), bg="blue", fg="white",cursor="hand2")
        button2.place(x=1006, y=452, width=450, height=40 )
        
    def link_student_file(self):
        self.new= Toplevel(self.root)
    #now we want to call the class to we make a variable 
        self.variale= Student(self.new)
    
   




if __name__ == "__main__":          
        root= Tk()
        obj=Fase_reco_system(root)
        root.mainloop()
        
