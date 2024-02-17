from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_recognition



class Attendance_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x700+0+0")
        self.root.title("Attendace Management System")

        img=Image.open(r"C:\Users\kanis\OneDrive\Desktop\Face Recognition\Images\PIC.jpg")
        self.photoimg=ImageTk.PhotoImage(img)

        first=Label(self.root,image=self.photoimg)
        first.place(x=0,y=0,width=1660,height=1080)

        #bg image
        img1=Image.open(r"C:\Users\kanis\OneDrive\Desktop\Face Recognition\Images\PIC.jpg")
        self.photoimg1=ImageTk.PhotoImage(img1)

        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=130,width=1530,height=710)

        # label-1
        img2=Image.open(r"C:\Users\kanis\OneDrive\Desktop\Face Recognition\Images\Student.jpeg")
        self.photoimg2=ImageTk.PhotoImage(img2)

        b1=Button(bg_img, image=self.photoimg2,command=self.new_student,cursor="hand2")
        b1.place(x=150,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="NEW STUDENT",command=self.new_student,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=150,y=325,width=220,height=40)

        # label-2
        
        img3=Image.open(r"C:\Users\kanis\OneDrive\Desktop\Face Recognition\Images\Att.jpeg")
        self.photoimg3=ImageTk.PhotoImage(img3)

        b1=Button(bg_img, image=self.photoimg3,cursor="hand2")
        b1.place(x=650,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="ATTENDANCE",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=650,y=325,width=220,height=40)

        # label-3
        img4=Image.open(r"C:\Users\kanis\OneDrive\Desktop\Face Recognition\Images\face.jpeg")
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img, image=self.photoimg4,command=self.face_data,cursor="hand2")
        b1.place(x=1150,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="FACE RECOGNITION",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=1150,y=325,width=220,height=40)

        # label-4
        img5=Image.open(r"C:\Users\kanis\OneDrive\Desktop\Face Recognition\Images\data.jpeg")
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img, image=self.photoimg5,command=self.train_data,cursor="hand2")
        b1.place(x=400,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="TRAIN DATA",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=400,y=605,width=220,height=40)

        # label-5
        img6=Image.open(r"C:\Users\kanis\OneDrive\Desktop\Face Recognition\Images\dev.jpeg")
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img, image=self.photoimg6,cursor="hand2")
        b1.place(x=900,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="DEVELOPER",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=900,y=605,width=220,height=40)

        #Function Buttons

    def new_student(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)
    




if __name__== "__main__":
    root=Tk()
    obj=Attendance_System(root)
    root.mainloop()


    