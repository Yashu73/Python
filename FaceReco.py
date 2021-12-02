# face recoganization
from tkinter import*
from tkinter import ttk
from PIL import Image



class face_recoganization:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title("Face Recoganization System")
         #img
        img=Image.open(r"D:\MCA_II\AITLab\Media\banner.jpg")
        img=img.resize((500,130),Image.ANTIALIS)
        self.photoimg=imageTk.photoImage(img)

        flb=Label(self.root,image=self.photoimg)
        flb.place(x=0,y=0,width=500,height=130)

         #img1
        img1=Image.open(r"D:\MCA_II\AITLab\Media\banner.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=imageTk.photoImage(img1)

        flb=Label(self.root,image=self.photoimg1)
        flb.place(x=500,y=0,width=500,height=130)

         #img2
        img2=Image.open(r"D:\MCA_II\AITLab\Media\banner.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=imageTk.photoImage(img2)

        flb=Label(self.root,image=self.photoimg2)
        flb.place(x=1000,y=0,width=550,height=130)

         #back img3
        img3=Image.open(r"D:\MCA_II\AITLab\Media\banner.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=imageTk.photoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lb=Label(bg_img,text="Face Recoganization Attendance System",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lb.place(x=0,y=0,width=1530,height=45)

        #Student button img4
        img4=Image.open(r"D:\MCA_II\AITLab\Media\banner.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=imageTk.photoImage(img4)

        b1.Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1.Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=200,width=220,height=40)


        #detect face button img5
        img5=Image.open(r"D:\MCA_II\AITLab\Media\banner.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=imageTk.photoImage(img5)

        b1.Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)

        b1_1.Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=200,width=220,height=40)


        # Attendace button img6
        img6=Image.open(r"D:\MCA_II\AITLab\Media\banner.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=imageTk.photoImage(img6)

        b1.Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b1_1.Button(bg_img,text="Attendace",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=200,width=220,height=40)


        # Help button img7
        img7=Image.open(r"D:\MCA_II\AITLab\Media\banner.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=imageTk.photoImage(img7)

        b1.Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1.Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=200,width=220,height=40)


        # Train button img8
        img8=Image.open(r"D:\MCA_II\AITLab\Media\banner.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=imageTk.photoImage(img8)

        b1.Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)

        b1_1.Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)


        # photoes button img9
        img9=Image.open(r"D:\MCA_II\AITLab\Media\banner.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=imageTk.photoImage(img9)

        b1.Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=500,y=380,width=220,height=220)

        b1_1.Button(bg_img,text="Photoes",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)


        # Developer button img10
        img10=Image.open(r"D:\MCA_II\AITLab\Media\banner.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=imageTk.photoImage(img10)

        b1.Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        b1_1.Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)

        # Exit button img11
        img11=Image.open(r"D:\MCA_II\AITLab\Media\banner.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=imageTk.photoImage(img11)

        b1.Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1.Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)


if __name__ == "__main__":
    root=Tk()
    obj=face_recoganization(root)
    root.mainloop()
    
