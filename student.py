from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root= root
        self.root.geometry("1800x1800+0+0")
        self.root.title("Student Detalis ")
        #===============variable======
        self.var_department= StringVar()
        self.var_semester= StringVar()
        self.var_subjet= StringVar()
        self.var_rollnumer=IntVar()
        self.var_name= StringVar()
        self.var_email= StringVar()
        self.var_phonenumber= IntVar()
        self.var_address= StringVar()
        self.var_teachersname= StringVar()
        
        #logo and title 
        image= Image.open(r"D:\student_attandenc_system\logo.png")
        image=image.resize((150,141),Image.ANTIALIAS)
        self.photoimage= ImageTk.PhotoImage(image)
        fist_labal= Label(self.root, image=self.photoimage)
        fist_labal.place(x=680,y=20,width=150, height=141)
        title_lable= Label(self.root, text="Student Detalis", font=("times new romn", 40, "bold"), bg="gray", fg="black")
        title_lable.place(x=20, y=170, width=1480, height=60)
        
        #Now we make fram so start 
        main_frame= Frame(self.root, bd=10)
        main_frame.place(x=0, y=230, width= 1600, height=1800)

        #left labale fram 
        left_frame= LabelFrame(main_frame,bd=1, text="B.Tech 4 Year", font=("times new romn", 16, "bold", ), bg="white", fg="red", relief="solid")
        left_frame.place(x=10,y=0, width=800, height=530)

        logo= Image.open(r"D:\student_attandenc_system\iconstudent.png")
        logo=logo.resize((120, 100),Image.ANTIALIAS)
        self.photologo= ImageTk.PhotoImage(logo)
        fist_labal= Label(left_frame, image=self.photologo)
        fist_labal.place(x=300,y=10,width=120, height=100)

        #student Information 
        Info= LabelFrame(left_frame,bd=2, text="Department Information", font=("times new romn", 16, "bold", ),  bg="white", fg="red", relief=RIDGE)
        Info.place(x=10,y=115, width=775, height=130)
        
        #department 
        name=Label(Info, text="Department",font=("times new romn", 16, "bold", ), bg="white", fg="red")
        name.grid(row=0, column=0, padx=5, pady=10)
        name_info=ttk.Combobox(Info,textvariable=self.var_department, font=("times new romn", 16, "bold", ), width=17, state="read only" )
        name_info["values"]= ("Select Department","CSE", "EC/En", "Civil")
        #tuple and jab bhi tuple me hum index dete hai to 0 se hi start hota hai 
        name_info.current(0)
        name_info.grid(row=0, column=1, padx=20, pady=12,)

        #semester
        course=Label(Info, text="Semester",font=("times new romn", 16, "bold", ), bg="white", fg="red")
        course.grid(row=0, column=2, padx=5, pady=10)
        course_info=ttk.Combobox(Info,textvariable=self.var_semester, font=("times new romn", 16, "bold", ), width=15, state="read only" )
        course_info["values"]= ("Select Semester","7th", "8th")
        #tuple and jab bhi tuple me hum index dete hai to 0 se hi start hota hai 
        course_info.current(0)
        course_info.grid(row=0, column=3, padx=20, pady=12)   

        #subject
        semester=Label(Info, text="Subject",font=("times new romn", 16, "bold", ), bg="white", fg="red")
        semester.grid(row=1, column=0, padx=5, pady=10)
        semester_info=ttk.Combobox(Info,textvariable=self.var_subjet, font=("times new romn", 16, "bold", ), width=17, state="read only" )
        semester_info["values"]= ("Select Subject","AI", "Cloud Computing", "RER", "RDAP")
        #tuple and jab bhi tuple me hum index dete hai to 0 se hi start hota hai 
        semester_info.current(0)
        semester_info.grid(row=1, column=1, padx=20, pady=12)

        #class student informations like what is his name 
        class_s_Info= LabelFrame(left_frame,bd=2, text="Student Detalis ", font=("times new romn", 16, "bold"), bg="white", fg="red",relief=RIDGE )
        class_s_Info.place(x=10,y=250, width=775, height=250)
       
        #roll number
        rollnumber=Label(class_s_Info, text="Roll Number",font=("times new romn", 12, "bold" ), bg="white", fg="black")
        rollnumber.grid(row=0, column=0, padx=5, pady=10)
        
        #entry 
        rollnumber_entry=ttk.Entry(class_s_Info,textvariable=self.var_rollnumer, width=25,  font=("times new romn", 11))
        rollnumber_entry.grid(row=0, column=1)


        #name
        Name=Label(class_s_Info, text="Name",font=("times new romn", 12, "bold" ), bg="white", fg="black",)
        Name.grid(row=0, column=2, padx=15, pady=10) 
        Name_entry=ttk.Entry(class_s_Info, textvariable=self.var_name, width=25,  font=("times new romn", 11),)
        Name_entry.grid(row=0, column=3, )

        
        #e-mail
        Email=Label(class_s_Info, text="E-mail",font=("times new romn", 12, "bold" ), bg="white", fg="black")
        Email.grid(row=1, column=0, padx=5, pady=10)
        Email_entry=ttk.Entry(class_s_Info, width=25,textvariable=self.var_email,  font=("times new romn", 11))
        Email_entry.grid(row=1, column=1)

        #phone number
        
        phone_number=Label(class_s_Info, text="Phone Number",font=("times new romn", 12, "bold" ), bg="white", fg="black")
        phone_number.grid(row=1, column=2, padx=10, pady=10)
        phone_number_entry=ttk.Entry(class_s_Info, width=25,textvariable=self.var_phonenumber,  font=("times new romn", 11))
        phone_number_entry.grid(row=1, column=3)
        
        #address
        address=Label(class_s_Info, text="Address",font=("times new romn", 12, "bold" ), bg="white", fg="black")
        address.grid(row=2, column=0, padx=10, pady=10)
        address_entry=ttk.Entry(class_s_Info,textvariable=self.var_address, width=25, font=("times new romn", 11))
        address_entry.grid(row=2, column=1)
        
        #teacher's name
        teachersname=Label(class_s_Info, text="Teacher's Name",font=("times new romn", 12, "bold", ), bg="white", fg="black")
        teachersname.grid(row=2, column=2, padx=5, pady=10)
        teachersname_info=ttk.Combobox(class_s_Info,textvariable=self.var_teachersname, font=("times new romn", 11, "bold", ), width=23, state="read only" )
        teachersname_info["values"]= ("Select Teacher's Name","AI", "Cloud Computing", "RER", "RDAP")
        teachersname_info.current(0)
        teachersname_info.grid(row=2, column=3, padx=20, pady=12)
        
        #to make radio button
        self.var_takephoto=StringVar()
        radio_button1= Radiobutton(class_s_Info, text="Take Photo",variable=self.var_takephoto, command=self.generate_dataset, value="Yes", font=("times new romn", 12, "bold"), bg="blue", fg= "white")
        radio_button1.grid(row=3, column=0, padx=15)

        #self.var_selectphoto=StringVar()
        radio_button2= Radiobutton(class_s_Info, text="Select Photo",variable=self.var_takephoto, value="No", font=("times new romn", 12, "bold"), bg="blue", fg= "white")
        radio_button2.grid(row=3, column=3, padx=55)

        #button frame 
        
        button_frame= LabelFrame(class_s_Info,bd=2, relief="solid")
        button_frame.place(x=10,y=176, width=750, height=45)
        #for save button
       # self.var_save= StringVar()
        save_button= Button(button_frame,width=22,command=self.add_data, text="SAVE",font=("times new romn", 12, "bold"), bg="blue", fg= "white")
        save_button.grid(row=0, column=0,padx=10,  pady=5,)
        
        #Update button
        #self.var_update= StringVar()
        Update_button= Button(button_frame,width=22, text="UPDATE",command=self.update_data, font=("times new romn", 12, "bold"), bg="blue", fg= "white")
        Update_button.grid(row=0, column=1, padx=0, pady=5)
       
       #delete button
        delete_button= Button(button_frame,width=22, text="DELETE",command=self.delete_data, font=("times new romn", 12, "bold"), bg="blue", fg= "white")
        delete_button.grid(row=0, column=2, padx=10, pady=5)
       

        #right labale fram 
        right_frame= LabelFrame(main_frame,bd=1, text="B.Tech 4 Year", font=("times new romn", 16, "bold", ), bg="white", fg="red", relief="solid")
        right_frame.place(x=815,y=0, width=675, height=530)

        #set the logo image
        logo1= Image.open(r"D:\student_attandenc_system\iconstudent.png")
        logo1=logo1.resize((120, 100),Image.ANTIALIAS)
        self.photologo1= ImageTk.PhotoImage(logo1)
        right_labal= Label(right_frame, image=self.photologo1)
        right_labal.place(x=300,y=10,width=120, height=100)

        #                       searching system 

        search_frame= LabelFrame(right_frame,bd=2, text="Search System", font=("times new romn", 16, "bold", ), bg="white", fg="red", relief=RIDGE)
        search_frame.place(x=10,y=120, width=653, height=80)
       
       #search bar and combo
       
        searchbar=Label(search_frame, text="Search By: ",font=("times new romn", 12, "bold", ), bg="black", fg="white")
        searchbar.grid(row=0, column=0, padx=5, pady=10)
        searchbar_info=ttk.Combobox(search_frame, font=("times new romn", 11, "bold", ), width=8, state="read only" )
        searchbar_info["values"]= ("Select", "Roll No.", "Name", "E-mail")
        searchbar_info.current(0)
        searchbar_info.grid(row=0, column=1, padx=8, pady=10)

        #entry fidles for searching 
        search_entry=ttk.Entry(search_frame, width=23, font=("times new romn", 14))
        search_entry.grid(row=0, column=2, padx=0, pady=10)
        
        #we want to button
        search_button= Button(search_frame, text="Search",font=("times new romn", 12, "bold"), bg="blue", fg= "white")
        search_button.grid(row=0, column=3,padx=8,  pady=10,)
        
        #showall button
        showall_button= Button(search_frame, text="Show All ",font=("times new romn", 12, "bold"), bg="blue", fg= "white")
        showall_button.grid(row=0, column=4, padx=8, pady=10)

        #we want to make table for see all data 
        table_frame= Frame(right_frame,bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10,y=210, width=653, height=285)
       
       
        #now we want to make sclor bar
        #x me horizontal hota hai and y me vertical
        scroll_x= ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(table_frame,orient=VERTICAL)
        #now we want to make table, colums ke ander hum ek tubles paass krne hote hai 
        self.student_table= ttk.Treeview(table_frame, columns=('department', 'semseter', 'subject','rollNumebr', 'name', 'e-mail', 'phone number', 'address',  "teacher's name", "photosample"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        #scroll bar ko working me lane ke liye hum scroll bar ko config krna hoga 
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        #Now we want to show heading in the table so ttk ke file me hota hai heading ka options then we can use there .heading 
        self.student_table.heading("department",text="Department")
        self.student_table.heading("semseter",text="Semseter")
        self.student_table.heading("subject",text="Subject")
        self.student_table.heading("rollNumebr",text="Roll Number")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("e-mail",text="E-mail")
        self.student_table.heading("phone number",text="Phone Number")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher's name",text="Teacher's Name")
        self.student_table.heading("photosample", text="Photo Sample")
       #heading ko show krane ke liye hum use krte 
        self.student_table["show"]= "headings"
        #heading ki widh set krne ke liye hum 
        self.student_table.column("department", width=100)
        self.student_table.column("semseter", width=100)
        self.student_table.column("subject", width=100)
        self.student_table.column("rollNumebr", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("e-mail", width=100)
        self.student_table.column("phone number", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher's name", width=100)
        self.student_table.column("photosample", width=100)
        self.student_table.pack(fill=BOTH, expand=1)
        #ynha hume just get cursor ki likhna hai call nhi krna.
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()
       
# ======================== funstion delecation for sending the data in thek
    def add_data(self):
        if self.var_department.get()=="Select Department" or self.var_semester.get()=="Select semester" or  self.var_subjet.get()=="Select Subject" or self.var_rollnumer.get()=="" or self.var_name.get()=="" or self.var_email.get()=="" or self.var_phonenumber.get()=="" or self.var_address.get()=="" or self.var_teachersname.get()=="" or self.var_takephoto.get()=="" :


            messagebox.showerror("Something is wrong", "All Fields are required", parent=self.root)
        else:
            
            
            try:
                connection=mysql.connector.connect(host="localhost", username="root", password="Sudh@2004", database="attandance" )
                #when you want to creat a currser bnayenge and cursor ki help se msq qure ko run krte hai 
                my_cursor= connection.cursor()
                my_cursor.execute("insert into studentinformation values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                                                                                                            self.var_department.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_subjet.get(),
                                                                                                            self.var_rollnumer.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phonenumber.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teachersname.get(),
                                                                                                            self.var_takephoto.get() 
                                                                                                            ))
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo("Congratulations", "You form is sbmited",parent=self.root)
            except Exception as es:
                messagebox.showerror("Something is wrong", f"Due TO :{str(es)}", parent=self.root)
    
    
    
    #=================== now we want to fech the data to databae and put into our table 
    def fetch_data(self):
        connection=mysql.connector.connect(host="localhost", username="root", password="Sudh@2004", database="attandance" )
        my_cursor= connection.cursor()
        my_cursor.execute("select * from studentinformation")
        #So we can do that we hum data ftch krke stor kr lete hai variable me 
        fatchdata=my_cursor.fetchall()
        if len(fatchdata)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in fatchdata:
                self.student_table.insert("", END, values=i)
            connection.commit()
        connection.close()

#============get cursor to fouse in table and with the help of that we update the table
                        #Ynha event yha hum yese hi dete hai event ki jgh hum kuch bhi likh skte hai.
    def get_cursor(self, event=""):
        cursor_focus=self.student_table.focus()
        content= self.student_table.item(cursor_focus)
        info=content["values"]
        #Ye values ko humko entry fild me dalana hoga 
        self.var_department.set(info[0]),
        self.var_semester.set(info[1]),
        self.var_subjet.set(info[2]),
        self.var_rollnumer.set(info[3]),
        self.var_name.set(info[4]),
        self.var_email.set(info[5]),
        self.var_phonenumber.set(info[6]),
        self.var_address.set(info[7]),
        self.var_teachersname.set(info[8]),
        self.var_takephoto.set(info[9])

# Now we are working on update button or update fuction so 
    def update_data(self):
        #info=messagebox.askyesno("Update", "Do You Want Update the Student Information",parent=self.root )
        if self.var_department.get()=="Select Department" or self.var_semester.get()=="Select semester" or  self.var_subjet.get()=="Select Subject" or self.var_rollnumer.get()=="" or self.var_name.get()=="" or self.var_email.get()=="" or self.var_phonenumber.get()=="" or self.var_address.get()=="" or self.var_teachersname.get()=="" or self.var_takephoto.get()=="" :
             messagebox.showerror("Something is wrong", "All Fields are required", parent=self.root)
        else:
            try:
                info=messagebox.askyesno("Update", "Do You Want Update the Student Information",parent=self.root )
                if info>0:
                    connection=mysql.connector.connect(host="localhost", username="root", password="Sudh@2004", database="attandance" )
                    my_cursor= connection.cursor()
                    my_cursor.execute("update studentinformation set Department=%s, Semester=%s, Subject=%s, Name=%s, E_mail=%s, PhoneNumber=%s, Address=%s,  TeachersName=%s, photosample=%s where RollNumber=%s", (
                                                                                                                                                                                                
                                                                                                                                                                                                self.var_department.get(),
                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                self.var_subjet.get(),
                                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                self.var_phonenumber.get(),
                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                self.var_teachersname.get(),
                                                                                                                                                                                                self.var_takephoto.get(), 
                                                                                                                                                                                                self.var_rollnumer.get()
                                                                                                                                                                                                ))
                else:
                    if not info:
                        return
                messagebox.showinfo("Congratulations", "Student Information is Updated",parent=self.root)
                connection.commit()
                self.fetch_data()
                connection.close()
            except Exception as es:
                messagebox.showerror("Something is wrong", f"Due TO :{str(es)}", parent=self.root)

#===================================== Delete Function==========================================================
    def delete_data(self):
        if self.var_rollnumer.get()=="":
            messagebox.showerror("Something is wrong", "Kindly select the Roll Number", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete Page", "Do You want to Delet this Information",parent=self.root )
                if delete>0:
                    connection=mysql.connector.connect(host="localhost", username="root", password="Sudh@2004", database="attandance" )
                    my_cursor= connection.cursor()
                    sql= "delete from studentinformation where RollNumber=%s"
                    value=(self.var_rollnumer.get(),)
                    my_cursor.execute(sql, value)
                else:
                    if not delete:
                        return
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo("Delete Page", "Successfully Deleted Student Information",parent=self.root )
            except Exception as es:
                messagebox.showerror("Something is wrong", f"Due TO :{str(es)}", parent=self.root)


#==================================use open cv for takeing image in our project======================================================== 
    def generate_dataset(self):
        if self.var_department.get()=="Select Department" or self.var_semester.get()=="Select semester" or  self.var_subjet.get()=="Select Subject" or self.var_rollnumer.get()=="" or self.var_name.get()=="" or self.var_email.get()=="" or self.var_phonenumber.get()=="" or self.var_address.get()=="" or self.var_teachersname.get()=="" or self.var_takephoto.get()=="" :
            messagebox.showerror("Something is wrong", "All Fields are required", parent=self.root)
        else:
            try:
                connection=mysql.connector.connect(host="localhost", username="root", password="Sudh@2004", database="attandance" )
                my_cursor= connection.cursor()
                my_cursor.execute("select * from studentinformation")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id=id+1
                my_cursor.execute("update studentinformation set Department=%s, Semester=%s, Subject=%s, Name=%s, E_mail=%s, PhoneNumber=%s, Address=%s,  TeachersName=%s, photosample=%s where RollNumber=%s", (
                                                                                                                                                                                                
                                                                                                                                                                                                self.var_department.get(),
                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                self.var_subjet.get(),
                                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                self.var_phonenumber.get(),
                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                self.var_teachersname.get(),
                                                                                                                                                                                                self.var_takephoto.get(), 
                                                                                                                                                                                                self.var_rollnumer.get()==id+1
                                                                                                                                                                                                ))

                connection.commit()
                self.fetch_data()
                connection.close()
#====================load predefine data on face ===============================
                face_classifier= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(image):
                    #bgy to gray scal me convert krna hai than 
                    gray=cv2.cvtColor(image,cv2.COLOR_BGRA2GRAY)
                    faces=face_classifier.detectMultiScale(gray, 1.3,5)
                    #for making a raktangele 
                    for (x,y,w,h) in faces:
                        face_cropped= image[y:y+h, x:x+w]
                        return face_cropped
                #capchetr krne ke liye 
                cap= cv2.VideoCapture(0)
                image_id= 0
                while True:
                    ret, myframe= cap.read()
                    if face_cropped(myframe) is not None:
                        image_id=image_id+1
                        face=cv2.resize(face_cropped(myframe), (800,800))
                        face=cv2.cvtColor(face,cv2.COLOR_BGRA2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(image_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(image_id),(50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 2)
                        cv2.imshow("Crooped Face", face)
                    if cv2.waitKey(1)==13 or int(image_id)==100:
                        break
                
                cap.release()
                #cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!",parent=self.root )
            except Exception as es:
                messagebox.showerror("Something is wrong", f"Due TO :{str(es)}", parent=self.root)





                
                


                        
                




                     

                                                                                               


        



                                                                        



if __name__ == "__main__":          
        root= Tk()
        obj=Student(root)
        root.mainloop()
