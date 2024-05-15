
from tkinter import * # for creating grapic
from tkinter import ttk#for creating combo box
#creating api for weather data search weather api in goggle
import requests
# city_name="delhi"
# data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=c20286959aab3974aaf2e501a063ca9a").json()#AVInash23@#
# print(  data)
#creating a function for fetch usefull data by api
def data_get():#we want city name so we use combo box
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=c20286959aab3974aaf2e501a063ca9a").json()#AVInash23@#
    W_label1.config(text=data["weather"][0]["main"])
    Wd_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=int(data["main"]["temp"]-273.15))
    per_label1.config(text=data["main"]["pressure"])
    
    
    
#creating window tk is class
win=Tk()
win.title("Weather app")
win.config(bg="sky blue")
win.geometry('500x700')
name_label=Label(win,text="Weather app",font=("Time New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name= StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com=ttk.Combobox(win,text="Weather app",values=list_name,font=("Time New Roman",30,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

#
W_label=Label(win,text="Weather Climate",font=("Time New Roman",18))
W_label.place(x=25,y=260,height=50,width=200)
W_label1=Label(win,text="",font=("Time New Roman",18))
W_label1.place(x=250,y=260,height=50,width=200)

#
Wd_label=Label(win,text="Weather description",font=("Time New Roman",18))
Wd_label.place(x=25,y=330,height=50,width=200)
Wd_label1=Label(win,text="",font=("Time New Roman",18))
Wd_label1.place(x=250,y=330,height=50,width=200)

#
temp_label=Label(win,text="Weather Temperature",font=("Time New Roman",20))
temp_label.place(x=25,y=400,height=50,width=200)
temp_label1=Label(win,text="",font=("Time New Roman",20))
temp_label1.place(x=250,y=400,height=50,width=200)

#
per_label=Label(win,text="Weather Pressure",font=("Time New Roman",20))
per_label.place(x=25,y=470,height=50,width=200)
per_label1=Label(win,text="",font=("Time New Roman",20))
per_label1.place(x=250,y=470,height=50,width=200)

#button 
done_button=Button(win,text="Send",font=("Time New Roman",20,"bold"),command=data_get)
done_button.place(x=200,y=190,height=50,width=100)


#we want to run countieu
win.mainloop()