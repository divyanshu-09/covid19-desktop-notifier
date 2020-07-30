import requests
import plyer
from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup


def notification(title,message):
    plyer.notification.notify(
        title = title,
        message = message,
        app_name = "India Coronavirus Stats",
        ticker = "India Coronavirus Stats",
        app_icon = r'C:\Users\HP\Documents\python\Corona Project\p.ico',
        timeout = 40
    )
    exit()


def webscrap(targetstate):

    url = 'https://www.mygov.in/covid-19/'
    data = requests.get(url)
    file = BeautifulSoup(data.content,'html.parser')
    table = file.find('tbody')
    tab = table.find_all('tr')

    for st in tab:
        dat = st.find_all('td')
        if(dat[0].text.strip().lower()==targetstate.lower()):
            confirmed = dat[1].text.strip()
            active = dat[2].text.strip()
            recovered = dat[3].text.strip()
            deceased = dat[4].text.strip()
            notification('Coronavirus Details In {}'.format(targetstate),
            'Confirmed : {}\nActive : {}\nRecovered : {}\nDeceased : {}'
            .format(confirmed,active,recovered,deceased))


def clicked():
    if(state.get()==''):
        notification('Oops no State name found!','You must enter a State\'s name!!')
    else:
        webscrap(state.get())


#webscrap()
gui = Tk()
gui.title("Corona Virus Information")
gui.geometry("500x290+400+200")
gui.configure(bg="black")
gui.iconbitmap(r'C:\Users\HP\Documents\python\Corona Project\vv.ico')

IntroLabel = Label(gui,text="India Coronavirus Stats",font=('new roman',28,'italic bold'),fg='indian red',bg = 'black',width=22)
IntroLabel.place(x=0,y=10)

stateLabel = Label(gui,text="State/UT :",font=('arial',20,'bold'),bg='black',fg='dark slate gray',width=12)
stateLabel.place(x=0,y=106)

state = StringVar()

cb = ttk.Combobox(gui,textvariable=state,width=20,height=10,font=('new roman',15,'bold'))
cb.grid(column=0, row=1)
cb.place(x=200,y=110)
cb['values'] = ('Andaman and Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh',
                   'Dadra and Nagar Haveli and Daman', 'Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh',
                    'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Maharashtra', 'Manipur',
                    'Meghalaya', 'Mizoram', 'Madhya Pradesh', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim',
                    'Tamil Nadu', 'Telengana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal')
cb.current(4)
cb.focus()

Notify = Button(gui,text='Notify',bg='thistle4',font=('arial',16,'bold'),relief=RIDGE,activebackground='black',activeforeground='yellow',width=18,command = clicked)
Notify.place(x=130,y=200)

gui.mainloop()
