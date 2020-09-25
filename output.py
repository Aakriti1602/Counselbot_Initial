import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv (r"C:\Users\Aakriti Mishra\Hacksprint\Occupations.csv")

st.title("YOUR REPORT!!!")

professions = {'1':"Systems Security Administrator",
				'2':"Business Systems Analyst",
				'3':"Software Systems Engineer",
				'4':"Database Developer",
				'5':"Business Intelligence Analyst",
				'6':"Business Systems Analyst",
				'7':"CRM Technical Developer",
				'8':"Mobile Applications Developer",
				'9':"UX Designer",
				'10':"CRM Technical Developer",
				'11':"Quality Assurance Associate",
				'12':"Web Developer"}

#l = ['1','6','9','12','4']
l = ['1','8','10','12','5']
#l = ['1','2','10','4','9']
#l = ['11','9','3','2','4']


out = []
for i in range (0,5):
    n = l[i]
    c = professions[n]
    out.append(c)

data = [55,25,10,6,4] 
  
  

explode = (0.0, 0.05, 0.1, 0.15, 0.3)

colors = ( "orange", "cyan", "brown", "indigo", "beige") 
   
wp = { 'linewidth' : 0.5, 'edgecolor' : "green" } 

def func(pct, allvalues): 
    absolute = int(pct / 100.*np.sum(allvalues)) 
    return "{:.1f}%\n({:d} g)".format(pct, absolute) 
  

fig, ax = plt.subplots(figsize =(10, 7)) 
wedges, texts, autotexts = ax.pie(data,  
                                  autopct = lambda pct: func(pct, data), 
                                  explode = explode,  
                                  labels = out, 
                                  shadow = True, 
                                  colors = colors,  
                                  wedgeprops = wp, 
                                  textprops = dict(color ="magenta")) 
ax.legend(wedges, out, 
          title ="Careers", 
          loc ="center left", 
          bbox_to_anchor =(1, 0, 0.5, 1)) 
  
ax.set_title("Recommended Occupation") 
   
st.pyplot(fig)

st.header('More info on Occupation')
#We'll be using a csv file for that
for i in range (0,5):
    st.write(df['Info On that'][int(l[i]) - 1])

st.header('Expected Incomes')
#We'll be using a csv file for that
for i in range (0,5):
    st.write(df['Income'][int(l[i]) - 1])

st.header('Trends over years')
#We'll be using a csv file for that
fig, ax = plt.subplots()

def Convert(string): 
    li = list(string.split(","))
    li=list(map(float,li))
    return li 

x = ['2000','2005','2010','2015','2020']  
y = []
for i in range (0,5):
    t = Convert(df['Trends Over Years'][int(l[i]) - 1])
    y.append(t)
plt.plot(x, (y[0]),'pink')
plt.plot(x, y[1],'g')
plt.plot(x, y[2],'blue')
plt.plot(x, y[3],'y')
plt.plot(x, y[4],'r')
plt.xlabel('Years')  
plt.ylabel('People')   
plt.title('Trends over the years!!')   
st.pyplot(fig)