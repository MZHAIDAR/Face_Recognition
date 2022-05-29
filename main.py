from cProfile import label
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student



class Face_recognition_system:
    def __init__(self,root) :
       self.root=root
       self.root.geometry("1530x790+0+0")
       self.root.title("face Recogniton System")

       img=Image.open(r"D:\face recognition\photos\pic1.jpg")
       img=img.resize((500,130),Image.ANTIALIAS)  
       self.photoimage=ImageTk.PhotoImage(img)

       f_lbl=Label(self.root,image=self.photoimage)
       f_lbl.place(x=0,y=0,width=500,height=130)

       img1=Image.open(r"D:\face recognition\photos\pic3.png")
       img1=img1.resize((500,130),Image.ANTIALIAS)  
       self.photoimage1=ImageTk.PhotoImage(img1)

       f_lbl=Label(self.root,image=self.photoimage1)
       f_lbl.place(x=505,y=0,width=500,height=130)

       img2=Image.open(r"D:\face recognition\photos\pic4.jpg")
       img2=img2.resize((500,130),Image.ANTIALIAS)  
       self.photoimage2=ImageTk.PhotoImage(img2)

       f_lbl=Label(self.root,image=self.photoimage2)
       f_lbl.place(x=1010,y=0,width=500,height=130)

       #bg image

       bg=Image.open(r"D:\face recognition\photos\pic14.jpg")
       bg=bg.resize((1530,710),Image.ANTIALIAS)  
       self.photoimage3=ImageTk.PhotoImage(bg)

       bg_img=Label(self.root,image=self.photoimage3)
       bg_img.place(x=0,y=130,width=1530,height=710)

       title_lbl=Label(bg_img,text="Attendance System Application Using Face Recognition",font=("poppins",30,"bold"),bg="dark blue",fg="yellow")
       title_lbl.place(x=150,y=10,width=1250,height=50)

       #student button

       img4=Image.open(r"D:\face recognition\photos\pic5.jpg")
       img4=img4.resize((240,180),Image.ANTIALIAS)
       self.photoimg4=ImageTk.PhotoImage(img4)

       b1=Button(bg_img,image=self.photoimg4,command=self.std_detailsbtn,cursor="hand2")
       b1.place(x=100,y=100,width=240,height=180)

       b1_1=Button(bg_img,text="Student Details",command=self.std_detailsbtn,cursor="hand2",font=("poppins",12,"bold"),bg="dark blue",fg="yellow")
       b1_1.place(x=100,y=280,width=240,height=40)



#button 2
       img7=Image.open(r"D:\face recognition\photos\pic1.jpg")
       img7=img7.resize((240,180),Image.ANTIALIAS)
       self.photoimg5=ImageTk.PhotoImage(img7)

       b2=Button(bg_img,image=self.photoimg5,cursor="hand2")
       b2.place(x=500,y=100,width=240,height=180)

       b2_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("poppins",12,"bold"),bg="dark blue",fg="yellow")
       b2_1.place(x=500,y=280,width=240,height=40)



#button 3

       img8=Image.open(r"D:\face recognition\photos\pic2.jpg")
       img8=img8.resize((240,180),Image.ANTIALIAS)
       self.photoimg6=ImageTk.PhotoImage(img8)

       b3=Button(bg_img,image=self.photoimg6,cursor="hand2")
       b3.place(x=900,y=100,width=240,height=180)

       b3_1=Button(bg_img,text="Attendance",cursor="hand2",font=("poppins",12,"bold"),bg="dark blue",fg="yellow")
       b3_1.place(x=900,y=280,width=240,height=40)


#button 4
       img9=Image.open(r"D:\face recognition\photos\pic1.jpg")
       img9=img9.resize((240,180),Image.ANTIALIAS)
       self.photoimg7=ImageTk.PhotoImage(img9)

       b5=Button(bg_img,image=self.photoimg7,cursor="hand2")
       b5.place(x=100,y=400,width=240,height=180)

       b5_1=Button(bg_img,text="Photos",cursor="hand2",font=("poppins",12,"bold"),bg="dark blue",fg="yellow")
       b5_1.place(x=100,y=580,width=240,height=40)

#button 5
       img10=Image.open(r"D:\face recognition\photos\pic1.jpg")
       img10=img10.resize((240,180),Image.ANTIALIAS)
       self.photoimg8=ImageTk.PhotoImage(img10)

       b5=Button(bg_img,image=self.photoimg8,cursor="hand2")
       b5.place(x=500,y=400,width=240,height=180)

       b5_1=Button(bg_img,text="Train Data",cursor="hand2",font=("poppins",12,"bold"),bg="dark blue",fg="yellow")
       b5_1.place(x=500,y=580,width=240,height=40)



#button 6

       img11=Image.open(r"D:\face recognition\photos\pic1.jpg")
       img11=img11.resize((240,180),Image.ANTIALIAS)
       self.photoimg9=ImageTk.PhotoImage(img11)

       b6=Button(bg_img,image=self.photoimg9,cursor="hand2")
       b6.place(x=900,y=400,width=240,height=180)

       b6_1=Button(bg_img,text="Exit",cursor="hand2",font=("poppins",12,"bold"),bg="dark blue",fg="yellow")
       b6_1.place(x=900,y=580,width=240,height=40)

    def std_detailsbtn(self):
       self.new_window=Toplevel(self.root)
       self.appopen=Student(self.new_window)



if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition_system(root)
    root.mainloop()
  
