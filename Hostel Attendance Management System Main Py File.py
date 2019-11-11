###################################################
from tkinter import *
from tkinter import messagebox
##################################################
startscreen=Tk()
startscreen.title("Welcome!")

def admin_access_window():
    
    class Student():
        def __init__(self, ID, NAME, BRANCH, CONTACT_NO):
            self.ID = ID
            self.NAME = NAME
            self.BRANCH = BRANCH
            self.CONTACT_NO = CONTACT_NO
            StudentRecordCreation = open("Files\StudentRec\{}.txt".format(ID), "x")
            StudentRecordCreation.write("NAME{} \nNAME:{}\nBRANCH:{}\nCONTACT NUMBER:{}".format(ID,NAME,BRANCH,CONTACT_NO))
            StudentRecordCreation.close()
            
        def add_a_date(self,aDate=""):
            StudentRecordDateAddition = open("{}\AbsentDates.txt".format(self.ID),"a")
            StudentRecordDateAddtion.write(aDate)
            StudentRecordDateAddition.close()
            
    admin_access_screen = Toplevel()
    admin_access_screen.title("Admin Access Panel")
    canvasAdminAccess = Canvas(admin_access_screen, width= 700, height =700)
    canvasAdminAccess.pack()

    PhotoAdminAccessScreen = PhotoImage(file="Photos\entrance.png")
    PlacementAdminAccessScreen = Label(canvasAdminAccess, image = PhotoAdminAccessScreen)
    PlacementAdminAccessScreen.image = PhotoAdminAccessScreen
    PlacementAdminAccessScreen.pack()
    
                               
    adminEntryFrame = Frame(admin_access_screen,width= 700, height =700)

    Label(adminEntryFrame, text="Enter UserID:                   ").grid(row=10)
    UserIDEntry = Entry(adminEntryFrame)
    UserIDEntry.grid(row=10, column=10)

    Label(adminEntryFrame, text="_________________________________________  ").grid(row=11)
    

    Label(adminEntryFrame, text="Enter Name:                   ").grid(row=30)
    UserName = Entry(adminEntryFrame)
    UserName.grid(row=30, column=10)
    
    Label(adminEntryFrame, text="_________________________________________  ").grid(row=31)

    Label(adminEntryFrame, text="Enter Branch:                   ").grid(row=50)
    UserBranch = Entry(adminEntryFrame)
    UserBranch.grid(row=50, column=10)

    Label(adminEntryFrame, text="_________________________________________  ").grid(row=51)

    Label(adminEntryFrame, text="Contact Number:                   ").grid(row=70)
    UserContactNumber = Entry(adminEntryFrame)
    UserContactNumber.grid(row=70, column=10)

    Label(adminEntryFrame, text="_________________________________________  ").grid(row=71)

    AdminAccessFormCreation= canvasAdminAccess.create_window(500, 250, anchor='ne', window=adminEntryFrame)

    def StoreStudentData():
        if (UserIDEntry.get()!="" and UserName.get()!="" and UserBranch.get()!="" and UserContactNumber.get() !=""):
            S1 = Student(UserIDEntry.get(),UserName.get(),UserBranch.get(),UserContactNumber.get())
            messagebox.showinfo("Attention","Student Details Added")
        else:
            messagebox.showwarning("Attention","Make Sure The Entered Details Are Valid")


    SubmitButton = Button(adminEntryFrame, text="Submit", width=10, command=StoreStudentData)
    SubmitButton.grid(row=72, column=10)

    

def add_p_a():
    AddAttendance = Toplevel()
    AddAttendance.title("Manage Attendance")
    canvasAddAttendance = Canvas(AddAttendance, width=400, height=400)
    canvasAddAttendance.pack()

   

    AddAttFrame = Frame(AddAttendance)
    Label(AddAttFrame, text="Enter UserID:").grid(row=0)
    UserIDEntry = Entry(AddAttFrame)
    UserIDEntry.grid(row=0, column=10)

    PhotoHostelMess = PhotoImage(file="Photos\HostelMess.png")
    PhotoHostelMessPlacement = Label(canvasAddAttendance, image=PhotoHostelMess)
    PhotoHostelMessPlacement.image = PhotoHostelMess
    PhotoHostelMessPlacement.pack() 

    Label(AddAttFrame, text="Date in DD/MM/YY format").grid(row=5)
    DateEntry = Entry(AddAttFrame)
    DateEntry.grid(row=5, column=10)

    AddSubAtt = StringVar()
    
    Radiobutton(AddAttFrame, text="Mark Present", variable=AddSubAtt, value="Present").grid(row=3000, column=10)
    Radiobutton(AddAttFrame, text="Mark Absent", variable=AddSubAtt, value="Absent").grid(row=3000,column=20)
    UserIDEntryFormPlacement= canvasAddAttendance.create_window(20, 20, anchor='nw', window=AddAttFrame)

    def Mark_ATT():
        if AddSubAtt.get() == "Present":
            MarkPresent = open("Files\Attendance\Present{}.txt".format(UserIDEntry.get()),"a+")
            MarkPresent.write("{} \n".format(DateEntry.get()))
            MarkPresent.close()
            
        elif AddSubAtt.get() == "Absent":
            MarkAbsent = open("Files\Attendance\Absent{}.txt".format(UserIDEntry.get()),"a+")
            MarkAbsent.write("{} \n".format(DateEntry.get()))
            MarkAbsent.close()
            

    MarkButton = Button(AddAttFrame, text="Mark", width=10, command=Mark_ATT)
    MarkButton.grid(row=4000, column=10)
            
        
    

def admin_login_passcheck():
    PasscheckScreen = Toplevel()
    PasscheckScreen.title("Enter Password")
    canvasPassCheck = Canvas(PasscheckScreen, width=300, height=100)
    canvasPassCheck.pack()

    ##_______________________________PASSCHECK ADMIN LOGIN______________________________________________________________________________________________________________#
    EntryForm = Frame(PasscheckScreen)
    Label(EntryForm, text="Password:").grid(row=0)
    PasswordEntry= Entry(EntryForm)
    PasswordEntry.grid(row=0,column=10)

    OperationToBePerformed = StringVar()
    
    Radiobutton(EntryForm, text="Add Record", variable=OperationToBePerformed, value="AddRecord").grid(row=10, column=10)
    Radiobutton(EntryForm, text="Add Attendance", variable=OperationToBePerformed, value="AddAttendance").grid(row=10,column=20)
    EntryFormButton = canvasPassCheck.create_window(1, 20, anchor='nw', window=EntryForm)
    

    def PerformPassCheck():
        global Password
        Password = PasswordEntry.get()

        f = open("Files\password.txt","r")
        CorrPass = f.read()
        f.close()


        
        if Password == CorrPass and OperationToBePerformed.get() =="AddRecord":
            admin_access_window()

        elif Password == CorrPass and OperationToBePerformed.get() =="AddAttendance":
            add_p_a()

        else:
            messagebox.showwarning("Warning","Incorrect Password And/Or Selection")
        
            
            
        
            


    SubmitButton = Button(EntryForm, text="Submit", width=10, command=PerformPassCheck)
    SubmitButton.grid(row=30, column=10)


def disp_rec(r):
        disp_rec_window=Toplevel()
        disp_rec_window.title("Here are your details")

        dispRecCanvas = Canvas(disp_rec_window)
        dispRecCanvas.pack()

        dispRecImage = PhotoImage(file ="Photos\SITParking.png")
        dispRecImagePlacement = Label(dispRecCanvas, image = dispRecImage)
        dispRecImagePlacement.image = dispRecImage
        dispRecImagePlacement.pack(side=TOP, fill=BOTH)

        f = open("Files\StudentRec\{}.txt".format(r),"r")
        z=f.read()

        StudentRecordPresentDates = open("Files\Attendance\Present{}.txt".format(r),"r")
        TotalPresentDates=len(StudentRecordPresentDates.readlines())

        StudentRecordAbsentDates = open("Files\Attendance\Absent{}.txt".format(r),"r")
        TotalAbsentDates=len(StudentRecordAbsentDates.readlines())

        AttendancePercentage = (TotalPresentDates*100)/(TotalPresentDates+TotalAbsentDates)

        TextBoxForDetails = Text(disp_rec_window, height=20, width=80)
        TextBoxForDetails.pack(side=TOP)
        TextBoxForDetailsExtended = ("\n Your attendance percentage is {} \n You were present on {} days and absent on {} days".format(AttendancePercentage,TotalPresentDates,TotalAbsentDates))
        TextBoxForDetails.insert(END,z + TextBoxForDetailsExtended)
        TextBoxForDetailsCreation = dispRecCanvas.create_window(400, 100, anchor='nw', window=TextBoxForDetails)

        
            
        
def student_login_idcheck():
    IDcheckScreen = Toplevel()
    IDcheckScreen.title("Enter UserID")
    canvasIDCheck = Canvas(IDcheckScreen, width=300, height=100)
    canvasIDCheck.pack()
    
        
#___________________________________________________________________ID CHECK USER LOGIN___________________________________________________________________________________#

    IDEntryScreen = Frame(IDcheckScreen)
    Label(IDEntryScreen, text="UserID:").grid(row=0)
    IDEntry= Entry(IDEntryScreen)
    IDEntry.grid(row=0,column=10)
    IDPassCheckCreate = canvasIDCheck.create_window(1, 20, anchor='nw', window=IDEntryScreen)

    def Perform_id_check():
        try:
            IDCheck = open("Files\StudentRec\{}.txt".format(IDEntry.get()),"r+")
            Details = IDEntry.get()
            disp_rec(Details)
        except:
            messagebox.showwarning("Attention","Make Sure The Entered Details Are Valid")
        

    SubmitCheckID = Button(IDEntryScreen, text="Submit", width=10, command=Perform_id_check)
    SubmitCheckID.grid(row=30, column=10)

            
            
             

#__________________________________________________________________SYMBIOSIS PHOTO ON THE FRONT PAGE_______________________________________________________________________#
    
PhotoSymbiStartScreen = PhotoImage(file="Photos\SymbiStartScreen.png")

PlacementSymbiStartScreen = Label(startscreen, image = PhotoSymbiStartScreen)
PlacementSymbiStartScreen.pack(side="top", fill=X )

#_________________________________________________________________ADMIN AND STUDENT BUTTONS on the bottom of the first screen________________________________________________#
toolbar= Frame(startscreen,bg="red")
AdminLoginButton = Button(toolbar, text="Admin", relief = RAISED, command = admin_login_passcheck)
AdminLoginButton.pack(side="left", padx=20, pady=10)
StudentLoginButton = Button(toolbar, text="Student", relief = RAISED, command = student_login_idcheck)
StudentLoginButton.pack(side="right", padx=30, pady=10)

toolbar.pack(side="bottom")



