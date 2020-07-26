def Scarp():
    def notifyme(title,message):
        plyer.notification.notify(
            title=title,
            message=message,
            app_icon='virus.ico',
            timeout=20
        )

    url = 'https://www.worldometers.info/coronavirus/'
    data = requests.get(url)
    ##Web Scaping
    s = BeautifulSoup(data.content, 'html.parser')
    tablebody = s.find('tbody')
    trow = tablebody.find_all('tr')
    notifyname= name.get()
    if(notifyname == ''):
        notifyname='india'
    countries, total_cases, new_cases, total_deaths, new_deaths, total_recovered, active_cases = [], [], [], [], [], [], []
    serious, totalcases_permillion, totaldeaths_permillion, totaltests, totaltests_permillion = [], [], [], [], []
    headers = ['countries', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_recovered', 'active_cases',
               'serious', 'totalcases_permillion', 'totaldeaths_permillion', 'totaltests', 'totaltests_permillion']

    for i in trow:
        id = i.find_all('td')
        if (id[1].text.strip().lower() == notifyname):
            totalcases1 = int(id[2].text.strip().replace(',', ''))
            totaldeaths1 = id[4].text.strip()
            newcases1 = id[3].text.strip()
            newdeaths1 = id[5].text.strip()
            notifyme('Corona Virus Details In {}'.format(notifyname),
                     'Total Cases : {}\nTotal Deaths : {}\nNew Cases : {}\nNew Deaths : {}'.format(totalcases1,
                                                                                                   totaldeaths1,
                                                                                                   newcases1,
                                                                                                   newdeaths1))

        countries.append(id[1].text.strip())
        total_cases.append(int(id[2].text.strip().replace(',', '')))
        new_cases.append(id[3].text.strip())
        total_deaths.append(id[4].text.strip())
        new_deaths.append(id[5].text.strip())
        total_recovered.append(id[6].text.strip())
        active_cases.append(id[7].text.strip())
        serious.append(id[8].text.strip())
        totalcases_permillion.append(id[9].text.strip())
        totaldeaths_permillion.append(id[10].text.strip())
        totaltests.append(id[11].text.strip())
        totaltests_permillion.append(id[12].text.strip())
    df = pd.DataFrame(list(zip( countries, total_cases, new_cases, total_deaths, new_deaths, total_recovered, active_cases,
                                serious, totalcases_permillion, totaldeaths_permillion, totaltests, totaltests_permillion)),columns=headers)
    sor = df.sort_values('total_cases',ascending=False)
    for k in formatlist:
        if(k == 'html'):
            path2 = '{}/alldata.html'.format(path)
            sor.to_html(r'{}'.format(path2))
        if (k == 'json'):
            path2 = '{}/alldata.json'.format(path)
            sor.to_json(r'{}'.format(path2))
        if (k == 'csv'):
            path2 = '{}/alldata.csv'.format(path)
            sor.to_csv(r'{}'.format(path2))
    if(len(formatlist) != 0):
        messagebox.showinfo('Notification','Virus Record is saved {}'.format(path2),parent=root)
def html():
    formatlist.append('html')
    inhtml.configure(state='disabled')
def json():
    formatlist.append('json')
    injson.configure(state='disabled')
def csv():
    formatlist.append('csv')
    incsv.configure(state='disabled')

def download():
    global path
    if(len(formatlist) != 0):
        path = filedialog.askdirectory()
    else :
        pass
    Scarp()
    formatlist.clear()
    inhtml.configure(state='normal')
    injson.configure(state='normal')
    incsv.configure(state='normal')



import plyer
import requests
import  pandas as pd
from tkinter import messagebox,filedialog
from bs4 import BeautifulSoup
from tkinter import *

root = Tk()
root.title('Virus Information')
root.geometry('530x300+200+80')
root.configure(bg='light blue')
root.wm_iconbitmap('virus.ico')
formatlist= []
path = ''
###Label
IntroLabel = Label(root, text='Virus Information', font=('new roman', 30, 'italic bold'),
                   bg='yellow', width=22)
IntroLabel.place(x=0, y=0)

EntryLabel = Label(root, text='Notify Country : ', font=('arial', 20, 'italic bold'),
                   bg='light blue')
EntryLabel.place(x=10, y=70)

formatlabel = Label(root, text='Download In :', font=('arial', 20, 'italic bold'),
                    bg='light blue')
formatlabel.place(x=10, y=150)

###Entry Box
name = StringVar()
entry = Entry(root, textvariable=name, font=('arial', 20, 'italic bold'), relief=RIDGE, bd=2, width=20)
entry.place(x=220, y=70)

##Button
inhtml = Button(root, text='HTML', bg='green', font=('arial', 15, 'italic bold'), relief=RIDGE, activebackground='red',
                activeforeground='white',
                bd=5, width=5,command=html)
inhtml.place(x=210, y=150)

injson = Button(root, text='Json', bg='green', font=('arial', 15, 'italic bold'), relief=RIDGE, activebackground='red',
                activeforeground='white',
                bd=5, width=5,command=json)
injson.place(x=320, y=150)

incsv = Button(root, text='Csv', bg='green', font=('arial', 15, 'italic bold'), relief=RIDGE, activebackground='red',
               activeforeground='white',
               bd=5, width=5,command=csv)
incsv.place(x=430, y=150)

submit = Button(root, text='Submit', bg='red', font=('arial', 15, 'italic bold'), relief=RIDGE, activebackground='red',
                activeforeground='white',
                bd=5, width=25,command=download)
submit.place(x=110, y=250)

root.mainloop()
