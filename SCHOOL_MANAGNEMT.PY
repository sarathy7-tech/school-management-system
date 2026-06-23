from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
from config import DB_CONFIG




class employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("SCHOOL STUDENT MANAGMENT SYSTEM")

        #variables
        self.var_name = StringVar()
        self.var_DOB = StringVar()
        self.var_gender = StringVar()
        self.var_phoneno = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_adno = StringVar()
        self.var_father = StringVar()
        self.var_mother = StringVar()
        self.var_class = StringVar()
        self.var_Section = StringVar()
        self.var_roll = StringVar()
        self.var_first = StringVar()
        self.var_sesub = StringVar()
        self.var_trsub = StringVar()
        self.var_core1 = StringVar()
        self.var_core2 = StringVar()
        self.var_core3 = StringVar()
        self.var_med = StringVar()
        self.var_bg = StringVar()
        self.var_pd = StringVar()
        self.var_id_type = StringVar()
        self.var_id_proof = StringVar()
        self.var_fee = StringVar()
        self.var_mop = StringVar()
        self.var_spo = StringVar()
        self.var_ce = StringVar()
        self.var_cm = StringVar()
        self.var_single = StringVar()


        
        


        Ibl_title=Label(self.root,text="SCHOOL STUDENT MANAGMENT SYSTEM",font=("times new roman",32,"bold"),fg="darkblue",bg= ('#ffffff'))
        Ibl_title.place(x=0,y=0,width=1550,height=50)

        #logo
        img_logo=Image.open("school img/AMS.jpg")
        img_logo =img_logo.resize((60,60),Image.Resampling.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=150,y=0,width=50,height=50)
        
        #image frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1550,height=160)

        #list 
        img1=Image.open('school img/2.jpg')
        img1=img1.resize((300,160),Image.Resampling.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.image_1=Label(img_frame,image=self.photo1)
        self.image_1.place(x=0,y=0,width=300,height=160)

        #2nd
        img_2=Image.open('school img/1.jpg')
        img_2=img_2.resize((300,160),Image.Resampling.LANCZOS)
        self.photo2=ImageTk.PhotoImage(img_2)

        self.image_2=Label(img_frame,image=self.photo2)
        self.image_2.place(x=310,y=0,width=300,height=160)

        #5nd(SCHOOL IMG)
        img_5=Image.open('school img/schoolimg.jpg')
        img_5=img_5.resize((280,160),Image.Resampling.LANCZOS)
        self.photo5=ImageTk.PhotoImage(img_5)

        self.image_5=Label(img_frame,image=self.photo5)
        self.image_5.place(x=620,y=0,width=280,height=160)

        #3nd
        img_3=Image.open('school img/3.jpg')
        img_3=img_3.resize((300,160),Image.Resampling.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img_3)

        self.image_3=Label(img_frame,image=self.photo3)
        self.image_3.place(x=910,y=0,width=300,height=160)

        #4nd
        img_4=Image.open('school img/4.jpg')
        img_4=img_4.resize((300,160),Image.Resampling.LANCZOS)
        self.photo4=ImageTk.PhotoImage(img_4)

        self.image_4=Label(img_frame,image=self.photo4)
        self.image_4.place(x=1220,y=0,width=300,height=160)



        #main frame
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg="#ffffff")
        Main_frame.place(x=5,y=220,width=1510,height=550)

        #upper frame
        Main_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='#ffffff',text='student information',font=("times new roman",11,'bold'),fg='darkblue')
        Main_frame.place(x=10,y=10,width=1480,height=270)
        

        #name
        Ibl_name=Label(Main_frame,font=("arial",8,'bold'),text='NAME:-',bg="#ffffff")
        Ibl_name.grid(row=0,column=0,sticky=W,padx=2,pady=7)

        txt_name=ttk.Entry(Main_frame,textvariable=self.var_name,width=25,font=("arial",8,'bold'))
        txt_name.grid(row=0,column=1,sticky=W,padx=2,pady=7)

        #DOB
        Ibl_dob=Label(Main_frame,font=("arial",8,'bold'),text="DOB:-",bg="#ffffff")
        Ibl_dob.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_name=ttk.Entry(Main_frame,textvariable=self.var_DOB,width=25,font=("arial",8,'bold'))
        txt_name.grid(row=1,column=1,sticky=W,padx=2,pady=7)

       #GEnder
        Ibl_gender=Label(Main_frame,font=("arial",8,'bold'),text='GENDER:-',bg="#ffffff")
        Ibl_gender.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        com_txt_gender=ttk.Combobox(Main_frame,textvariable=self.var_gender,state='readonly',font=("arial",8,'bold'),width=22)
        com_txt_gender['value']=("GENDER",'MALE',"FEMALE",'OTHER')
        com_txt_gender.current(0)
        com_txt_gender.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        #phone
        Ibl_phone=Label(Main_frame,font=("arial",8,'bold'),text="PHONE NO:-",bg='#ffffff')
        Ibl_phone.grid(row=3,column=0,sticky=W,padx=2,pady=7)


        txt_doj=ttk.Entry(Main_frame,textvariable=self.var_phoneno,width=25,font=("arial",8,"bold"))
        txt_doj.grid(row=3,column=1,sticky=W,padx=2,pady=7)

        #eamil
        Ibl_Email=Label(Main_frame,font=("arial",8,'bold'),text="EMAIL:-",bg="#ffffff")
        Ibl_Email.grid(row=4,column=0,sticky=W,padx=3,pady=7)

        txt_Email=ttk.Entry(Main_frame,textvariable=self.var_email,width=25,font=("arial",8,'bold'))
        txt_Email.grid(row=4,column=1,sticky=W,padx=2,pady=7)

        

        #address
        Ibl_address=Label(Main_frame,font=("arial",8,"bold"),text="ADDRESS:-",bg="#ffffff")
        Ibl_address.grid(row=5,column=0,sticky=W,padx=2,pady=7)

        txt_address=ttk.Entry(Main_frame,textvariable=self.var_address,width=25,font=("arial",8,"bold"))
        txt_address.grid(row=5,column=1,sticky=W,padx=2,pady=7)

        #Admission Number
        Ibl_Admission_Number=Label(Main_frame,font=("arial",8,'bold'),text='Admission Number:-',bg="#ffffff")
        Ibl_Admission_Number.grid(row=6,column=0,sticky=W,padx=2,pady=7)

        txt_Admission_Number=ttk.Entry(Main_frame,textvariable=self.var_adno,width=25,font=("arial",8,'bold'))
        txt_Admission_Number.grid(row=6,column=1,sticky=W,padx=2,pady=7)


        #father's name
        Ibl_fname=Label(Main_frame,font=("arial",8,'bold'),text='FATHER\'S NAME:-',bg="#ffffff")
        Ibl_fname.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_fname=ttk.Entry(Main_frame,textvariable=self.var_father,width=25,font=("arial",8,'bold'))
        txt_fname.grid(row=0,column=3,sticky=W,padx=2,pady=7)


        #mother's name
        Ibl_mname=Label(Main_frame,font=("arial",8,'bold'),text='MOTHER\'S NAME:-',bg="#ffffff")
        Ibl_mname.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_mname=ttk.Entry(Main_frame,textvariable=self.var_mother,width=25,font=("arial",8,'bold'))
        txt_mname.grid(row=1,column=3,sticky=W,padx=2,pady=7)

        #class
        Ibl_class=Label(Main_frame,font=("arial",8,'bold'),text='CLASS:-',bg="#ffffff")
        Ibl_class.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        com_txt_c=ttk.Combobox(Main_frame,textvariable=self.var_class,state="readonly",font=("arial",8,"bold"),width=22)
        com_txt_c['value']=('class',1,2,3,4,5,6,7,8,9,10)
        com_txt_c.current(0)
        com_txt_c.grid(row=2,column=3,sticky=W,padx=2,pady=7)


        #Section
        Ibl_Section=Label(Main_frame,font=("arial",8,'bold'),text="Section:-",bg="#ffffff")
        Ibl_Section.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        com_txt_s=ttk.Combobox(Main_frame,textvariable=self.var_Section,state="readonly",font=("arial",8,"bold"),width=22)
        com_txt_s['value']=('Section','A','B','C')
        com_txt_s.current(0)
        com_txt_s.grid(row=3,column=3,sticky=W,padx=2,pady=7)

        #Roll Number  
        Ibl_rollno=Label(Main_frame,font=("arial",8,'bold'),text='Roll Number:-',bg="#ffffff")
        Ibl_rollno.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        txt_rollno=ttk.Entry(Main_frame,textvariable=self.var_roll,width=25,font=("arial",8,'bold'))
        txt_rollno.grid(row=4,column=3,sticky=W,padx=2,pady=7)

        #Subjects taken
        Ibl_sub1=Label(Main_frame,font=("arial",8,'bold'),text="First Language:-",bg="#ffffff")
        Ibl_sub1.grid(row=5,column=2,sticky=W,padx=2,pady=7)

        com_txt_sub1=ttk.Combobox(Main_frame,textvariable=self.var_first,state="readonly",font=("arial",8,"bold"),width=22)
        com_txt_sub1['value']=('Choose','Tamil','Kannada','Hindi','English')
        com_txt_sub1.current(0)
        com_txt_sub1.grid(row=5,column=3,sticky=W,padx=2,pady=7)


        Ibl_sub2=Label(Main_frame,font=("arial",8,'bold'),text="Second Language:-",bg="#ffffff")
        Ibl_sub2.grid(row=6,column=2,sticky=W,padx=2,pady=7)

        com_txt_sub2=ttk.Combobox(Main_frame,textvariable=self.var_sesub,state="readonly",font=("arial",8,"bold"),width=22)
        com_txt_sub2['value']=('Choose','Tamil','Kannada','Hindi','English')
        com_txt_sub2.current(0)
        com_txt_sub2.grid(row=6,column=3,sticky=W,padx=2,pady=7)


        Ibl_sub3=Label(Main_frame,font=("arial",8,'bold'),text="Third Language:-",bg="#ffffff")
        Ibl_sub3.grid(row=0,column=4,padx=3,pady=7)

        com_txt_sub3=ttk.Combobox(Main_frame,textvariable=self.var_trsub,state="readonly",font=("arial",8,"bold"),width=22)
        com_txt_sub3['value']=('Choose','Tamil','Kannada','Hindi','English')
        com_txt_sub3.current(0)
        com_txt_sub3.grid(row=0,column=5,sticky=W,padx=3,pady=7)


        Ibl_sub4=Label(Main_frame,font=("arial",8,'bold'),text="core subject1:-",bg="#ffffff")
        Ibl_sub4.grid(row=1,column=4,padx=3,pady=7)

        com_txt_sub4=ttk.Combobox(Main_frame,textvariable=self.var_core1,state="readonly",font=("arial",8,"bold"),width=22)
        com_txt_sub4['value']=('Maths')
        com_txt_sub4.current(0)
        com_txt_sub4.grid(row=1,column=5,sticky=W,padx=3,pady=7)


        Ibl_sub5=Label(Main_frame,font=("arial",8,'bold'),text="core subject2:-",bg="#ffffff")
        Ibl_sub5.grid(row=2,column=4,padx=3,pady=7)

        com_txt_sub5=ttk.Combobox(Main_frame,textvariable=self.var_core2,state="readonly",font=("arial",8,"bold"),width=22)
        com_txt_sub5['value']=('science')
        com_txt_sub5.current(0)
        com_txt_sub5.grid(row=2,column=5,sticky=W,padx=3,pady=7)


        Ibl_sub6=Label(Main_frame,font=("arial",8,'bold'),text="core subject3:-",bg="#ffffff")
        Ibl_sub6.grid(row=3,column=4,padx=3,pady=7)

        com_txt_sub6=ttk.Combobox(Main_frame,textvariable=self.var_core3,state="readonly",font=("arial",8,"bold"),width=22)
        com_txt_sub6['value']=('socialscience')
        com_txt_sub6.current(0)
        com_txt_sub6.grid(row=3,column=5,sticky=W,padx=3,pady=7)

        #Medium
        Ibl_Medium=Label(Main_frame,font=("arial",8,'bold'),text="Medium:-",bg="#ffffff")
        Ibl_Medium.grid(row=4,column=4,padx=3,pady=7)

        com_txt_Medium=ttk.Combobox(Main_frame,textvariable=self.var_med,state="readonly",font=("arial",8,"bold"),width=22)
        com_txt_Medium['value']=('Medium','Tamil','Kannada','Hindi','English')
        com_txt_Medium.current(0)
        com_txt_Medium.grid(row=4,column=5,sticky=W,padx=3,pady=7)

        #Blood Group
        Ibl_bg=Label(Main_frame,font=("arial",8,'bold'),text="Blood Group:-",bg="#ffffff")
        Ibl_bg.grid(row=5,column=4,padx=3,pady=7)

        com_txt_bg=ttk.Combobox(Main_frame,textvariable=self.var_bg,state="readonly",font=("arial",8,"bold"),width=22)
        com_txt_bg['value']=('Choose',"A+","A−", 'B+', 'B−', 'AB+','AB−', 'O+', 'O−')
        com_txt_bg.current(0)
        com_txt_bg.grid(row=5,column=5,sticky=W,padx=3,pady=7)

        #Physical Disabilities
        Ibl_pd=Label(Main_frame,font=("arial",8,'bold'),text="Physical Disabilities:-",bg="#ffffff")
        Ibl_pd.grid(row=6,column=4,padx=3,pady=7)

        com_txt_pd=ttk.Combobox(Main_frame,textvariable=self.var_pd,state="readonly",font=("arial",8,"bold"),width=22)
        com_txt_pd['value']=('if Physical Disabilities','Paralysis','Amputation','Cerebral Palsy','Spinal Cord Injury','Muscular Dystrophy','Multiple Sclerosis',
                            'Parkinson’s Disease','Epilepsy','Post-Stroke Disability'
                            'Arthritis','Osteogenesis Imperfecta','Scoliosis','Kyphosi',
                            'Congenital Limb Deficiency','Polio-Affected Limb','Clubfoot',
                            'Chronic Fatigue Syndrome','Dwarfism','Blindness','Hearing Loss'
                            )
        com_txt_pd.current(0)
        com_txt_pd.grid(row=6,column=5,sticky=W,padx=3,pady=7)


        #ID proof
        com_txt_poof=ttk.Combobox(Main_frame,textvariable=self.var_id_type,state="readonly",font=('arial',8,'bold'),width=18)
        com_txt_poof['value']=("select ID PROOF",'Birth Certificate','ADHAR CARD','Passport')
        com_txt_poof.current(0)
        com_txt_poof.grid(row=0,column=8,sticky=W,padx=2,pady=7)

        txt_poof=ttk.Entry(Main_frame,textvariable=self.var_id_proof,width=22,font=("arial",8,'bold'))
        txt_poof.grid(row=0,column=9,padx=2,pady=7)
        

        #fee
        Ibl_fee=Label(Main_frame,font=("arial",8,'bold'),text='FEE:-',bg="#ffffff")
        Ibl_fee.grid(row=1,column=8,sticky=W,padx=2,pady=7)

        txt_fee=ttk.Entry(Main_frame,textvariable=self.var_fee,width=22,font=("arial",8,'bold'))
        txt_fee.grid(row=1,column=9,padx=2,pady=7)

        #Mode of Payment
        Ibl_mop=Label(Main_frame,font=("arial",8,'bold'),text="Mode of Payment:-",bg="#ffffff")
        Ibl_mop.grid(row=2,column=8,sticky=W,padx=3,pady=7)

        com_txt_mop=ttk.Combobox(Main_frame,textvariable=self.var_mop,state="readonly",font=("arial",8,"bold"),width=20)
        com_txt_mop['value']=('Mode of Payment','Cash','UPI','Cheque','credit card','debit card')
        com_txt_mop.current(0)
        com_txt_mop.grid(row=2,column=9,sticky=W,padx=3,pady=7)
        

        #Sports
        Ibl_Sports=Label(Main_frame,font=("arial",8,'bold'),text='Sports:-',bg="#ffffff")
        Ibl_Sports.grid(row=3,column=8,sticky=W,padx=2,pady=7)

        txt_Sports=ttk.Entry(Main_frame,textvariable=self.var_spo,width=23,font=("arial",8,'bold'))
        txt_Sports.grid(row=3,column=9,sticky=W,padx=2,pady=7)

        #Cultural events
        Ibl_ce=Label(Main_frame,font=("arial",8,'bold'),text="Cultural events:-",bg="#ffffff")
        Ibl_ce.grid(row=4,column=8,sticky=W,padx=3,pady=7)

        com_txt_ce=ttk.Combobox(Main_frame,textvariable=self.var_ce,state="readonly",font=("arial",8,"bold"),width=20)
        com_txt_ce['value']=('Cultural events','Dance','Singing','Drama & Skit','Fancy Dress','Elocution',
                             'Storytelling','Poetry Recitation','Quiz','Drawing & Painting', 
                             'Craft & Model Making','Festival Celebrations','Speech & Debate', 
                             'Traditional Events','Music Instrumental','Yoga/Martial Arts Display'
                            )
        com_txt_ce.current(0)
        com_txt_ce.grid(row=4,column=9,sticky=W,padx=3,pady=7)

        #Club Memberships 
        Ibl_cm=Label(Main_frame,font=("arial",8,'bold'),text="Club Memberships:-",bg="#ffffff")
        Ibl_cm.grid(row=5,column=8,sticky=W,padx=3,pady=7)

        com_txt_cm=ttk.Combobox(Main_frame,textvariable=self.var_cm,state="readonly",font=("arial",8,"bold"),width=20)
        com_txt_cm['value']=('Club Memberships',"Science Club",'Math Club','Literary Club','Art & Craft Club',
                             'Music & Dance Club','Eco Club','Drama & Theatre Club','Sports Club', 
                             'Computer Club','Heritage Club','Quiz Club','Photography Club','Health & Wellness Club',
                              'Social Service Club',"Robotics Club")
        com_txt_cm.current(0)
        com_txt_cm.grid(row=5,column=9,sticky=W,padx=3,pady=7)


        #single parent or no parent
        Ibl_sanop=Label(Main_frame,font=("arial",8,'bold'),text="single parent \nor no parent:-",bg="#ffffff")
        Ibl_sanop.grid(row=6,column=8,sticky=W,padx=3,pady=7)

        com_txt_sanop=ttk.Combobox(Main_frame,textvariable=self.var_single,state="readonly",font=("arial",8,"bold"),width=20)
        com_txt_sanop['value']=('not applicable','only father','only mother','Guardian')
        com_txt_sanop.current(0)
        com_txt_sanop.grid(row=6,column=9,sticky=W,padx=3,pady=7)




        #Student image
        img_emg=Image.open("school img/5.jpg")
        img_emg=img_emg.resize((160,230),Image.Resampling.LANCZOS)
        self.photoemg=ImageTk.PhotoImage(img_emg)

        self.img_emg=Label(Main_frame,image=self.photoemg)
        self.img_emg.place(x=1140,y=4,width=160,height=230)

        #button frame
        Button_frame=Frame(Main_frame,bd=2,relief=RIDGE,bg="#ffffff")
        Button_frame.place(x=1310,y=11,width=155,height=210)

        btn_save=Button(Button_frame,text='SAVE',command=self.add_data,font=("arial",10,'bold'),width=16,bg='blue',fg='#ffffff')
        btn_save.grid(row=0,column=0,padx=11,pady=11)

        btn_updata=Button(Button_frame,text='UPDATE',command=self.updata_data,font=("arial",10,'bold'),width=16,bg='blue',fg='#ffffff')
        btn_updata.grid(row=1,column=0,padx=11,pady=11)


        btn_delete=Button(Button_frame,text='DELETE',command=self.delete_data,font=("arial",10,'bold'),width=16,bg='blue',fg='#ffffff')
        btn_delete.grid(row=2,column=0,padx=11,pady=11)


        btn_clean=Button(Button_frame,text='CLEAN',command=self.reset_data,font=("arial",10,'bold'),width=16,bg='blue',fg='#ffffff')
        btn_clean.grid(row=3,column=0,padx=11,pady=11)



        #down frame
        down_frame=LabelFrame(root,bd=2,relief=RIDGE,bg="#ffffff",text='Student information table',font=('times mew roman',11,'bold'),fg='darkblue')
        down_frame.place(x=20,y=502,width=1480,height=260)


        #search frame
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg="#ffffff",text="SEARCH STUDENT INFORMATION",font=("time new roman",11,"bold"),fg="red")
        search_frame.place(x=0,y=0,width=1470,height=50)

        search_by=Label(search_frame,font=("arail",8,'bold'),text="search by",fg="#ffffff",bg="red")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        #search
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,state="readonly",font=("arial",8,"bold"),width=15)
        com_txt_search['value']=("selection option","phone","id proof")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=2)


        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=("arial",8,'bold'))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(search_frame,text="search",command=self.serach_data,font=("arial",8,'bold'),width=13,bg="blue",fg="#ffffff")
        btn_search.grid(row=0,column=3,padx=5)

        btn_showall=Button(search_frame,text="show all",command=self.fetch_data,font=("arial",8,'bold'),width=13,bg="blue",fg="#ffffff")
        btn_showall.grid(row=0,column=4,padx=5)


        empiddeatails=Label(search_frame,text="Student detalils",font=("arial",8,'bold'),fg='red')
        empiddeatails.place(x=800,y=0,width=120,height=20)



        img_logo=Image.open('school img/6.jpg')
        img_logo=img_logo.resize((60,60),Image.Resampling.LANCZOS)
        self.photoloemp=ImageTk.PhotoImage(img_logo)

        self.image_lemp=Label(search_frame,image=self.photoloemp)
        self.image_lemp.place(x=700,y=3,width=60,height=60)


        #===============================Student table===============================
        #table from
        table_frame=Frame(down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=50,width=1470,height=118)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=('name','DOB','gender','phoneno','email','address','adno','father','mother','class','Section','roll','first','sesub','trsub','core1','core2','core3','med','bg','pd','id_type','id_proof','fee','mop','spo','ce','cm','single'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading("name",text="NAME")
        self.employee_table.heading("DOB",text="DOB")
        self.employee_table.heading("gender",text="GENDER")
        self.employee_table.heading("phoneno",text="PHONE")
        self.employee_table.heading("email",text="EMAIL")
        self.employee_table.heading("address",text="ADDRESS")
        self.employee_table.heading("adno",text="Admission Number")
        self.employee_table.heading("father",text="FATHER NAME")
        self.employee_table.heading("mother",text="MOTHER NAME")
        self.employee_table.heading("class",text="CLASS")
        self.employee_table.heading("Section",text="Section")
        self.employee_table.heading("roll",text="ROLL NUMBER")
        self.employee_table.heading("first",text="First Language")
        self.employee_table.heading("sesub",text="Second Language")
        self.employee_table.heading("trsub",text="Third Language")
        self.employee_table.heading("core1",text="core subject1")
        self.employee_table.heading("core2",text="core subject2")
        self.employee_table.heading("core3",text="core subject3")
        self.employee_table.heading("med",text="Medium")
        self.employee_table.heading("bg",text="Blood Group")
        self.employee_table.heading("pd",text="Physical Disabilities")
        self.employee_table.heading("id_type",text="ID TYPE")
        self.employee_table.heading("id_proof",text="ID POOF")
        self.employee_table.heading("fee",text="FEE")
        self.employee_table.heading("mop",text="Mode of Payment")
        self.employee_table.heading("spo",text="Sports")
        self.employee_table.heading("ce",text="Cultural events")
        self.employee_table.heading("cm",text="Club Memberships")
        self.employee_table.heading("single",text="single parent or no parent")



        self.employee_table['show']='headings'


        self.employee_table.column("name",width=100)
        self.employee_table.column("DOB",width=100)
        self.employee_table.column("gender",width=100)
        self.employee_table.column("phoneno",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("address",width=100)
        self.employee_table.column("adno",width=150)
        self.employee_table.column("father",width=100)
        self.employee_table.column("mother",width=100)
        self.employee_table.column("class",width=100)
        self.employee_table.column("Section",width=100)
        self.employee_table.column("roll",width=100)
        self.employee_table.column("first",width=100)
        self.employee_table.column("sesub",width=100)
        self.employee_table.column("trsub",width=100)
        self.employee_table.column("core1",width=100)
        self.employee_table.column("core2",width=100)
        self.employee_table.column("core3",width=100)
        self.employee_table.column("med",width=100)
        self.employee_table.column("bg",width=100)
        self.employee_table.column("pd",width=100)
        self.employee_table.column("id_type",width=100)
        self.employee_table.column("id_proof",width=100)
        self.employee_table.column("fee",width=100)
        self.employee_table.column("mop",width=100)
        self.employee_table.column("spo",width=100)
        self.employee_table.column("ce",width=100)
        self.employee_table.column("cm",width=150)
        self.employee_table.column("single",width=200)
        
        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()
    #==============================function declation==================
    def add_data(self):
        if self.var_name.get()=="" or self.var_phoneno.get()=="":
           messagebox.showerror("error",'all fields are required')
        else:
            try:
                conn = mysql.connector.connect(**DB_CONFIG)
                my_cursor=conn.cursor()
                my_cursor.execute("insert into school_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",   (
                                                                                                                                                     self.var_name.get(),
                                                                                                                                                     self.var_DOB.get(),
                                                                                                                                                     self.var_gender.get(),
                                                                                                                                                     self.var_phoneno.get(),
                                                                                                                                                     self.var_email.get(),
                                                                                                                                                     self.var_address.get(),
                                                                                                                                                     self.var_adno.get(),
                                                                                                                                                     self.var_father.get(),
                                                                                                                                                     self.var_mother.get(),
                                                                                                                                                     self.var_class.get(),
                                                                                                                                                     self.var_Section.get(),
                                                                                                                                                     self.var_roll.get(),
                                                                                                                                                     self.var_first.get(),
                                                                                                                                                     self.var_sesub.get(),
                                                                                                                                                     self.var_trsub.get(),
                                                                                                                                                     self.var_core1.get(),
                                                                                                                                                     self.var_core2.get(),
                                                                                                                                                     self.var_core3.get(),
                                                                                                                                                     self.var_med.get(),
                                                                                                                                                     self.var_bg.get(),
                                                                                                                                                     self.var_pd.get(),
                                                                                                                                                     self.var_id_type.get(),
                                                                                                                                                     self.var_id_proof.get(),
                                                                                                                                                     self.var_fee.get(),
                                                                                                                                                     self.var_mop.get(),
                                                                                                                                                     self.var_spo.get(),
                                                                                                                                                     self.var_ce.get(),
                                                                                                                                                     self.var_cm.get(),
                                                                                                                                                     self.var_single.get()

                                                                                                                                                       ))   
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("sucsess","STUDENT as been added",parent=self.root)
            except Exception as es:
                messagebox.showerror("error",f'due to : {str(es)}',parent=self.root)
    


    #fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(**DB_CONFIG)
        my_cursor=conn.cursor()
        my_cursor.execute("select * from school_details")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,value=i)
            conn.commit()
        conn.close()


    #get cusosor
    def get_cursor(self,event=""):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values']

        self.var_name.set(data[0])
        self.var_DOB.set(data[1])
        self.var_gender.set(data[2])
        self.var_phoneno.set(data[3])
        self.var_email.set(data[4])
        self.var_address.set(data[5])
        self.var_adno.set(data[6])
        self.var_father.set(data[7])
        self.var_mother.set(data[8])
        self.var_class.set(data[9])
        self.var_Section.set(data[10])
        self.var_roll.set(data[11])
        self.var_first.set(data[12])
        self.var_sesub.set(data[13])
        self.var_trsub.set(data[14])
        self.var_core1.set(data[15])
        self.var_core2.set(data[16])
        self.var_core3.set(data[17])
        self.var_med.set(data[18])
        self.var_bg.set(data[19])
        self.var_pd.set(data[20])
        self.var_id_type.set(data[21])
        self.var_id_proof.set(data[22])
        self.var_fee.set(data[23])
        self.var_mop.set(data[24])
        self.var_spo.set(data[25])
        self.var_ce.set(data[26])
        self.var_cm.set(data[27])
        self.var_single.set(data[28])
    


    def updata_data(self):
        if self.var_name.get()=="" or self.var_phoneno.get()=="":
            messagebox.showerror("error","all fields are required")
        else:
            try:
                updata=messagebox.askyesno("UPDATE","are you shure update this STUDENT data")
                if updata>0:
                    conn = mysql.connector.connect(**DB_CONFIG)
                    my_cursor=conn.cursor()
                    my_cursor.execute("UPDATE school_details SET NAME=%s,DOB=%s,GENDER=%s,PHONE=%s,EMAIL=%s,ADDRESS=%s,`Admission Number`=%s,`FATHER NAME`=%s,`MOTHER NAME`=%s,CLASS=%s,Section=%s,`ROLL NUMBER`=%s,`First Language`=%s,`Second Language`=%s,`Third Language`=%s,`core subject1`=%s,`core subject2`=%s,`core subject3`=%s,Medium=%s,`Blood Group`=%s,`Physical Disabilities`=%s,`ID TYPE`=%s,FEE=%s,`Mode of Payment`=%s,Sports=%s,`Cultural events`=%s,`Club Memberships`=%s,`single parent or no parent`=%s WHERE `ID PROOF`=%s",    (
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_name.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_DOB.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_gender.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_phoneno.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_email.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_address.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_adno.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_father.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_mother.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_class.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_Section.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_roll.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_first.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_sesub.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_trsub.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_core1.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_core2.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_core3.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_med.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_bg.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_pd.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_id_type.get(),

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_fee.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_mop.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_spo.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_ce.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_cm.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_single.get(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             self.var_id_proof.get()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ))


                    if not updata:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("sucees",'STUDENT successfully updated',parent=self.root)
            except Exception as es:
                messagebox.showerror("error",f"due to : {str(es)}",parent=self.root)
    

    #delete
    def delete_data(self):
        if self.var_id_proof.get()=="":
            messagebox.showerror("error","all fields are required")
        else:
            try:
                Delete=messagebox.askyesno("delete","are you want to delete this STUDENT",parent=self.root)
                if Delete>0:
                    conn = mysql.connector.connect(**DB_CONFIG)
                    my_cursor=conn.cursor()
                    sql="delete from school_details where `ID PROOF`=%s"
                    value=(self.var_id_proof.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","STUDENT successfully deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("error",f"due to:{str(es)}",parent=self.root)


    #reset
    def reset_data(self):
        self.var_name.set("")
        self.var_DOB.set("")
        self.var_gender.set("GENDER")
        self.var_phoneno.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_adno.set("")
        self.var_father.set("")
        self.var_mother.set("")
        self.var_class.set("class")
        self.var_Section.set("")
        self.var_roll.set("")
        self.var_first.set("choose")
        self.var_sesub.set("choose")
        self.var_trsub.set("choose")
        self.var_core1.set("")
        self.var_core2.set("")
        self.var_core3.set("")
        self.var_med.set("medium")
        self.var_bg.set("choose")
        self.var_pd.set("if Physical Disabilities")
        self.var_id_type.set("select ID PROOF")
        self.var_id_proof.set("")
        self.var_fee.set("")
        self.var_mop.set("Mode of Payment")
        self.var_spo.set("")
        self.var_ce.set("Cultural events")
        self.var_cm.set("Club Memberships")
        self.var_single.set("not applicable")

    #search
    def serach_data(self):
        if self.var_com_search.get()=='' or self.var_search.get()=="":
            messagebox.showerror("error","please select option")
        else:
            try:
                conn = mysql.connector.connect(**DB_CONFIG)
                my_cursor=conn.cursor()
                my_cursor.execute("select * from school_details where " +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("",END,value=i)
                conn.commit
                conn.close()
            except Exception as es:
                messagebox.showerror("error",f"due to:{str(es)}",parnet=self.root)
        
if __name__ == "__main__":
   root= Tk()
   obj= employee(root)
   root.mainloop()