from tkinter import *
from tkinter import ttk
from ListRequest import ListTickets
from tkinter import messagebox
from DbConnect import DBConnect


dbConnect=DBConnect()

root=Tk()
root.title('Hotel Del Luna Reservation')
root.configure(background="#eeb4b4")
#Style
style=ttk.Style()
style.theme_use('classic')
style.configure('Tlabel',background="#eeb4b4")
style.configure('TButton',background="#eeb4b4")
style.configure('TRadiobutton',background="#eeb4b4")

#FullName
ttk.Label(root, text="Full Name: ").grid(row=0,column=0,padx=10,pady=10)
EntryFullName=ttk.Entry(root, width=30, font=('Arial',16))
EntryFullName.grid(row=0,column=1,columnspan=2,pady=10)
#Gender
ttk.Label(root, text="Gender: ").grid(row=1,column=0)
SpanGender=StringVar()
ttk.Radiobutton(root,text="Male",variable=SpanGender ,value="Male").grid(row=1,column=1)
ttk.Radiobutton(root,text="Female",variable=SpanGender ,value="Female").grid(row=1,column=2)
#Comments
ttk.Label(root, text="Comments : ").grid(row=2,column=0)
txtComments=Text(root, width=30, height=15,font=('Arial',16))
txtComments.grid(row=2, column=1, columnspan=2)
#buttons
buSubmit=ttk.Button(root,text="Submit")
buSubmit.grid(row=3,column=3)
buList=ttk.Button(root,text="List Res")
buList.grid(row=3,column=2)

def BuSaveData():
    #print("Full Name:{}".format(EntryFullName.get()))
    #print("Gender:{}".format(SpanGender.get()))
    #print("Comments:{}".format(txtComments.get(1.0,'end')))
    msg=dbConnect.Add(EntryFullName.get(),SpanGender.get(),txtComments.get(1.0,'end'))
    messagebox.showinfo(title="Add info",message=msg)
    EntryFullName.delete(0,'end')
    txtComments.delete(1.0,'end')
def BuListData():
    #Todo: show orders
    #print('not implemented yet ')
    listrequest=ListTicket()

buSubmit.config(command=BuSaveData)
buList.config(command=BuListData)
root.mainloop()