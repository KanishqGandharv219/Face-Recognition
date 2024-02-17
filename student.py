from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x700+0+0")
        self.root.title("Attendance Management System")
        
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_section=StringVar()
        self.var_gender=StringVar()
        self.var_regno=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phno=StringVar()
        self.var_address=StringVar()
        self.var_classc=StringVar()

        #bg image
        img1=Image.open(r"C:\Users\kanis\OneDrive\Desktop\Face Recognition\Images\PIC.jpg")
        self.photoimg1=ImageTk.PhotoImage(img1)

        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=0,width=1530,height=710)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=0,y=150,width=1500,height=650)


        #Left Frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580)


        #Department
        dep_label=Label(Left_frame,text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=10)
      
        dep_combo=ttk.Combobox(Left_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","CSE","IT","CCE","DSE","AI & ML","IoT")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        #Course 
        course_label=Label(Left_frame,text="Course",font=("times new roman",13,"bold"))
        course_label.grid(row=0,column=2,padx=10)
      
        course_combo=ttk.Combobox(Left_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        course_combo["values"]=("Select Course","CSE","IT","CCE","DSE","AI & ML","IoT")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(Left_frame,text="Year",font=("times new roman",13,"bold"))
        year_label.grid(row=1,column=0,padx=10,sticky=W)
      
        year_combo=ttk.Combobox(Left_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #Semester
        semester_label=Label(Left_frame,text="Semester",font=("times new roman",13,"bold"))
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
      
        semester_combo=ttk.Combobox(Left_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","I","II","III","IV","V","VI","VII","VIII")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class Student
        class_student_frame=LabelFrame(Left_frame,bd=2,text="Enter Information",font=("times new roman",13,"bold"))
        class_student_frame.place(x=5,y=100,width=720,height=300)


        #Student ID
        studentid_label=Label(class_student_frame,text="Registration No.",font=("times new roman",13,"bold"))
        studentid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentid_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=20,font=("times new roman",13,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        

        #Student Name
        studentname_label=Label(class_student_frame,text="Student Name",font=("times new roman",13,"bold"))
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname__entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",13,"bold"))
        studentname__entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        
        #Section
        sec_label=Label(class_student_frame,text="Section",font=("times new roman",13,"bold"))
        sec_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        sec__entry=ttk.Entry(class_student_frame,textvariable=self.var_section,width=20,font=("times new roman",13,"bold"))
        sec__entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll No
        Rno_label=Label(class_student_frame,text="Student ID",font=("times new roman",13,"bold"))
        Rno_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Rno__entry=ttk.Entry(class_student_frame,textvariable=self.var_regno,width=20,font=("times new roman",13,"bold"))
        Rno__entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Email
        email_label=Label(class_student_frame,textvariable=self.var_email,text="E-mail",font=("times new roman",13,"bold"))
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email__entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        email__entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

         #Phone
        ph_label=Label(class_student_frame,text="Contact No",font=("times new roman",13,"bold"))
        ph_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        ph__entry=ttk.Entry(class_student_frame,textvariable=self.var_phno,width=20,font=("times new roman",13,"bold"))
        ph__entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Address
        add_label=Label(class_student_frame,text="Address",font=("times new roman",13,"bold"))
        add_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        add_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        add_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Class Coordinator
        cc_label=Label(class_student_frame,text="Class Coordinator",font=("times new roman",13,"bold"))
        cc_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        cc_entry=ttk.Entry(class_student_frame,textvariable=self.var_classc,width=20,font=("times new roman",13,"bold"))
        cc_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        email_label=Label(class_student_frame,text="E-Mail",font=("times new roman",13,"bold"))
        email_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        dob_label=Label(class_student_frame,text="D.O.B.",font=("times new roman",13,"bold"))
        dob_label.grid(row=5,column=0,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=5,column=1,padx=10,pady=5,sticky=W)

        gender_label=Label(class_student_frame,text="Gender",font=("times new roman",13,"bold"))
        gender_label.grid(row=5,column=2,padx=10,pady=5,sticky=W)

        gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",13,"bold"))
        gender_entry.grid(row=5,column=3,padx=10,pady=5,sticky=W)


        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text= "Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=1)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=2)

        #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=70)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=23,font=("times new roman",13,"bold"))
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=23,font=("times new roman",13,"bold"))
        update_btn.grid(row=0,column=1)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=22,font=("times new roman",13,"bold"))
        reset_btn.grid(row=0,column=2)


        takephoto_btn=Button(btn_frame,text="Take Photo",command=self.generate_dataset,width=23,font=("times new roman",13,"bold"))
        takephoto_btn.grid(row=1,column=0)

        updatephoto_btn=Button(btn_frame,text="Update Photo",width=23,font=("times new roman",13,"bold"))
        updatephoto_btn.grid(row=1,column=1)






         #rIGHT Frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        Right_frame.place(x=800,y=10,width=660,height=580)

        #Search System
        #Class Student
        Search_frame=LabelFrame(Right_frame,bd=2,text="Search System",font=("times new roman",13,"bold"))
        Search_frame.place(x=5,y=10,width=680,height=70)

        search_frame=LabelFrame(Search_frame,bd=2,text="Search By",font=("times new roman",13,"bold"))
        search_frame.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",13,"bold"),state="readonly")
        search_combo["values"]=("Select","Registration No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search__entry=ttk.Entry(Search_frame,width=16,font=("times new roman",13,"bold"))
        search__entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        src_btn=Button(Search_frame,text="Search",width=12,font=("times new roman",13,"bold"))
        src_btn.grid(row=0,column=3,padx=4)

        showall_btn=Button(Search_frame,text="Show All",width=12,font=("times new roman",13,"bold"))
        showall_btn.grid(row=0,column=4,padx=4)

        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=100,width=640,height=250)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","semester","id","name","section","gender","regno","dob","email","phno","address","classc","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("id",text="RegNo")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("section",text="Section")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("regno",text="ID")
        self.student_table.heading("dob",text="D.O.B.")
        self.student_table.heading("email",text="E-Mail")
        self.student_table.heading("phno",text="Phone No.")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("classc",text="Class Coordinator")
        self.student_table.heading("photo",text="Photo")

        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course", width=100) 
        self.student_table.column("year", width=100)
        self.student_table.column("semester", width=100)
        self.student_table.column("id",width=100) 
        self.student_table.column("name", width=100)
        self.student_table.column("section", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("regno", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phno", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("classc", width=100)
        self.student_table.column("photo", width=100)



        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #Fxn
    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Admin2003",database="attendance_system")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_id.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_section.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_regno.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phno.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_classc.get(),
                                                                                                                self.var_radio1.get()
                                                                                    
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details Added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Admin2003",database="attendance_system")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_section.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_regno.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phno.set(data[11]),
        self.var_address.set(data[12]),
        self.var_classc.set(data[13]),
        self.var_radio1.set(data[14])


    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do You Want to Update Table?",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Admin2003",database="attendance_system")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,id=%s,name=%s,section=%s,gender=%s,dob=%s,email=%s,phno=%s,address=%s,classc=%s,photo=%s where regno=%s",(

                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                            self.var_id.get(),
                                                                                                                                                                                            self.var_name.get(),
                                                                                                                                                                                            self.var_section.get(),
                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                            self.var_phno.get(),
                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                            self.var_classc.get(),
                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                            self.var_regno.get()

                                                                                                                                                                                         ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 



    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_section.set(""),
        self.var_gender.set(""),
        self.var_regno.set(""),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phno.set(""),
        self.var_address.set(""),
        self.var_classc.set(""),
        self.var_radio1.set("")
            
    #Generate data set take sample

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Admin2003",database="attendance_system")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                regno=0
                for x in myresult:
                    regno+=1
                my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,id=%s,name=%s,section=%s,gender=%s,dob=%s,email=%s,phno=%s,address=%s,classc=%s,photo=%s where regno=%s",(

                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                            self.var_id.get(),
                                                                                                                                                                                            self.var_name.get(),
                                                                                                                                                                                            self.var_section.get(),
                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                            self.var_phno.get(),
                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                            self.var_classc.get(),
                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                            self.var_regno.get()==regno+1

                                                                                                                                                                                         ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #Load Predefine Data

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(regno)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data Set Completed")

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
           











if __name__== "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()