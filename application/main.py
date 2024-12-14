from tkinter import *
from app import *

root = Tk()
root.title("Water Quality (MIB)")
root.geometry("1070x600")
# root.resizable(width=False,height=False)

colour1 = '#020f12'
colour2 = '#05d7ff'
colour3 = '#65e7ff'
colour4 = 'BLACK'
colour5 = 'white'

left_frame = Frame(root, bg=colour5, pady=40)
left_frame.place(relx=0, rely=0.5, anchor='w', relheight=1, relwidth=1/3)
right_frame = Frame(root, bg=colour3, pady=40)
right_frame.place(relx=1/3, rely=0.5, anchor="w", relheight=1, relwidth=2/3)


modelLabel = Label(left_frame, text="Select Classification method",
              background=colour5,
              foreground=colour2,
              font="Arial 16 bold underline"
              )
modelLabel.place(relx=0.5,rely=0.08,anchor="center")
# modelLabel.config(font="Consolas")

model=StringVar()
model.set("none")
model1=Radiobutton(left_frame,text="Logistic Regression",variable=model,value="Logistic_Regression",bg=colour5,fg=colour4, font="Arial 12",activebackground=colour5,activeforeground=colour3)
model1.place(relx=0.2,rely=0.2,anchor="w")
model2=Radiobutton(left_frame,text="SVM",variable=model,value="SVM",bg=colour5,fg=colour4, font="Arial 12",activebackground=colour5,activeforeground=colour3)
model2.place(relx=0.2,rely=0.3,anchor="w")
model3=Radiobutton(left_frame,text="Decision Tree",variable=model,value="Decision_Tree",bg=colour5,fg=colour4, font="Arial 12",activebackground=colour5,activeforeground=colour3)
model3.place(relx=0.2,rely=0.4,anchor="w")
model4=Radiobutton(left_frame,text="Knn",variable=model,value="Knn",bg=colour5,fg=colour4, font="Arial 12",activebackground=colour5,activeforeground=colour3)
model4.place(relx=0.2,rely=0.5,anchor="w")
model5=Radiobutton(left_frame,text="Random Forest",variable=model,value="Random_Forest",bg=colour5,fg=colour4, font="Arial 12",activebackground=colour5,activeforeground=colour3)
model5.place(relx=0.2,rely=0.6,anchor="w")
model6=Radiobutton(left_frame,text="XGBoost",variable=model,value="xgb",bg=colour5,fg=colour4, font="Arial 12",activebackground=colour5,activeforeground=colour3)
model6.place(relx=0.2,rely=0.7,anchor="w")

def predict():
    if(phText.get()!="" and HardnessText.get()!="" and SolidsText.get()!="" and ChloraminesText.get()!="" and SulfateText.get() !="" and ConductivityText.get()!="" and Organic_carbonText.get()!="" and TrihalomethanesText.get() !="" and TurbidityText.get()!="" and model.get()!="none"):
        ph = float(phText.get())
        Hardness = float(HardnessText.get())
        Solids = float(SolidsText.get())
        Chloramines = float(ChloraminesText.get())
        Sulfate = float(SulfateText.get())
        Conductivity = float(ConductivityText.get())
        Organic_carbon = float(Organic_carbonText.get())
        Trihalomethanes = float(TrihalomethanesText.get())
        Turbidity = float(TurbidityText.get())
        predict_result = predictModels(ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon,
                                       Trihalomethanes, Turbidity, model.get())
        if(predict_result==[0]):
            resultLabel.config(text="This water is not suitable :(",foreground="Red")
        else:
            resultLabel.config(text="This water is good :)",foreground="Green")
        accuracy()
        report()
    else:
        resultLabel.config(text="the data is not complete",font="Arial 16 bold underline",foreground="black")


#label result
resultLabel=Label(right_frame,
              background=colour3,
              foreground=colour1,
              font="Arial 16 bold "
              )
resultLabel.place(relx=0.1,rely=0.42,anchor="w")

pridictButton =Button(left_frame,#padx=5,pady=3,#command=exit,
                 background=colour2,
                 foreground=colour4,
                 activebackground=colour3,
                 activeforeground=colour4,
                 highlightthickness=2,
                 highlightbackground=colour2,
                 highlightcolor='WHITE',
                 width=30,
                 height=2,
                 border=0,
                 cursor='hand2',
                 text="predict",
                 font="Arial 10 bold",
                 command=predict
                 )
pridictButton.place(relx=0.5,rely=0.9,anchor="center")

def accuracy():
    tex=accuracyModels(model.get())
    tex="The accuracy of the model is : "+str(round(tex, 4)*100)
    modelAccuracyLabel.config(text=tex)

modelAccuracyLabel=Label(right_frame,
              background=colour3,
              foreground=colour1,
              font="Arial 15 bold "
              )
modelAccuracyLabel.place(relx=0.1,rely=0.49,anchor="w")


modelLabel=Label(right_frame,text="Water Quality Prediction",
              background=colour3,
              foreground=colour1,
              font="Arial 25 bold "
              )
modelLabel.place(relx=0.5,rely=0,anchor="center")

def report():
    tex = str(reportModels(model.get()))
    modelReportLabel.config(text=tex)


modelReportLabel = Label(right_frame,
              background=colour3,
              foreground="#006400",
              font="Arial 16 bold "
              )
modelReportLabel.place(relx=0.15, rely=0.8, anchor="w")

#ph
phLabel=Label(right_frame,text="ph :",
              background=colour3,
              foreground=colour1,
              font="Arial 12 ")
phLabel.place(relx=0.09,rely=0.12,anchor="center")

phText=Entry(right_frame,width=15)
phText.place(relx=0.24,rely=0.12,anchor="center")

#Hardness
HardnessLabel=Label(right_frame,text="Hardness :",
              background=colour3,
              foreground=colour1,
              font="Arial 12 ")
HardnessLabel.place(relx=0.4,rely=0.12,anchor="center")

HardnessText=Entry(right_frame,width=15)
HardnessText.place(relx=0.56,rely=0.12,anchor="center")

#Solids
SolidsLabel=Label(right_frame,text="Solids :",
              background=colour3,
              foreground=colour1,
              font="Arial 12 ")
SolidsLabel.place(relx=0.73,rely=0.12,anchor="center")

SolidsText=Entry(right_frame,width=15)
SolidsText.place(relx=0.88,rely=0.12,anchor="center")


#Chloramines
ChloraminesLabel=Label(right_frame,text="Chloramines :",
              background=colour3,
              foreground=colour1,
              font="Arial 12 ")
ChloraminesLabel.place(relx=0.09,rely=0.22,anchor="center")

ChloraminesText=Entry(right_frame,width=15)
ChloraminesText.place(relx=0.24,rely=0.22,anchor="center")

#Sulfate
SulfateLabel=Label(right_frame,text="Sulfate :",
              background=colour3,
              foreground=colour1,
              font="Arial 12 ")
SulfateLabel.place(relx=0.4,rely=0.22,anchor="center")

SulfateText=Entry(right_frame,width=15)
SulfateText.place(relx=0.56,rely=0.22,anchor="center")

#Conductivity
ConductivityLabel=Label(right_frame,text="Conductivity :",
              background=colour3,
              foreground=colour1,
              font="Arial 12 ")
ConductivityLabel.place(relx=0.73,rely=0.22,anchor="center")

ConductivityText=Entry(right_frame,width=15)
ConductivityText.place(relx=0.88,rely=0.22,anchor="center")

#Organic_carbon
Organic_carbonLabel=Label(right_frame,text="Organic carbon :",
              background=colour3,
              foreground=colour1,
              font="Arial 12 ")
Organic_carbonLabel.place(relx=0.09,rely=0.32,anchor="center")

Organic_carbonText=Entry(right_frame,width=15)
Organic_carbonText.place(relx=0.24,rely=0.32,anchor="center")

#Trihalomethanes
TrihalomethanesLabel=Label(right_frame,text="Trihalomethanes :",
              background=colour3,
              foreground=colour1,
              font="Arial 12 ")
TrihalomethanesLabel.place(relx=0.4,rely=0.32,anchor="center")

TrihalomethanesText=Entry(right_frame,width=15)
TrihalomethanesText.place(relx=0.56,rely=0.32,anchor="center")

#Turbidity
TurbidityLabel=Label(right_frame,text="Turbidity :",
              background=colour3,
              foreground=colour1,
              font="Arial 12 ")
TurbidityLabel.place(relx=0.73,rely=0.32,anchor="center")

TurbidityText=Entry(right_frame,width=15)
TurbidityText.place(relx=0.88,rely=0.32,anchor="center")

#clear
def clearAll():
    phText.delete(0,"end")
    HardnessText.delete(0,"end")
    SolidsText.delete(0,"end")
    ChloraminesText.delete(0,"end")
    SulfateText.delete(0,"end")
    ConductivityText.delete(0,"end")
    Organic_carbonText.delete(0,"end")
    TrihalomethanesText.delete(0,"end")
    TurbidityText.delete(0,"end")
    model.set("none")
    modelAccuracyLabel.config(text="")
    resultLabel.config(text="")
    modelReportLabel.config(text="")
    phText.focus_set()


clearButton =Button(right_frame,#padx=5,pady=3,command=exit,
                 background=colour1,
                 foreground=colour2,
                 activebackground=colour3,
                 activeforeground=colour4,
                 highlightthickness=2,
                 highlightbackground=colour2,
                 highlightcolor='WHITE',
                 width=16,
                 height=2,
                 border=0,
                 cursor='hand2',
                 text="Clear",
                 font="Arial 10 bold",
                 command=clearAll
                 )
clearButton.place(relx=0.85,rely=0.45,anchor="center")

###test1
def modelTest1():
    if(phText.get()=="" and HardnessText.get()=="" and SolidsText.get()=="" and ChloraminesText.get()=="" and SulfateText.get() =="" and ConductivityText.get()=="" and Organic_carbonText.get()=="" and TrihalomethanesText.get() =="" and TurbidityText.get()=="" ):
        phText.insert(0, "4.66810168740591")
        HardnessText.insert(0, "193.681735475078")
        SolidsText.insert(0, "47580.9916033353")
        ChloraminesText.insert(0, "7.16663893548253")
        SulfateText.insert(0, "359.94857436696")
        ConductivityText.insert(0, "526.424170922359")
        Organic_carbonText.insert(0, "13.8944185181945")
        TrihalomethanesText.insert(0, "66.687694785397")
        TurbidityText.insert(0, "4.4358209095098")


test1Button =Button(left_frame,#padx=5,pady=3,command=exit,
                 background=colour1,
                 foreground=colour2,
                 activebackground=colour3,
                 activeforeground=colour4,
                 highlightthickness=2,
                 highlightbackground=colour2,
                 highlightcolor='WHITE',
                 width=16,
                 height=2,
                 border=0,
                 cursor='hand2',
                 text="Test 1",
                 font="Arial 6 ",
                 command=modelTest1
                 )
test1Button.place(relx=0.35,rely=0.8,anchor="center")

###test2
def modelTest2():
    if(phText.get()=="" and HardnessText.get()=="" and SolidsText.get()=="" and ChloraminesText.get()=="" and SulfateText.get() =="" and ConductivityText.get()=="" and Organic_carbonText.get()=="" and TrihalomethanesText.get() =="" and TurbidityText.get()=="" ):
        phText.insert(0, "5.23000318952593")
        HardnessText.insert(0, "176.714023440768")
        SolidsText.insert(0, "27971.891806145")
        ChloraminesText.insert(0, "7.59798058283956")
        SulfateText.insert(0, "413.914000522445")
        ConductivityText.insert(0, "440.355373773191")
        Organic_carbonText.insert(0, "14.4236141269885")
        TrihalomethanesText.insert(0, "72.8373702055684")
        TurbidityText.insert(0, "3.04561210593435")


test2Button =Button(left_frame,#padx=5,pady=3,command=exit,
                 background=colour1,
                 foreground=colour2,
                 activebackground=colour3,
                 activeforeground=colour4,
                 highlightthickness=2,
                 highlightbackground=colour2,
                 highlightcolor='WHITE',
                 width=16,
                 height=2,
                 border=0,
                 cursor='hand2',
                 text="Test 2",
                 font="Arial 6 ",
                 command=modelTest2
                 )
test2Button.place(relx=0.65,rely=0.8,anchor="center")


#IB label
IBLabel=Label(left_frame,text="IB",
              background=colour5,
              foreground=colour1,
              font=("Segoe Script", 15 ,"bold")
              )
IBLabel.place(relx=0.1,rely=1,anchor="center")


# mytext=Entry(root)
# mytext.pack()


root.mainloop()
