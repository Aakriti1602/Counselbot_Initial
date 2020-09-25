import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv (r"C:\Users\Aakriti Mishra\Hacksprint\Occupations.csv")

input_list = [1,1,1,1,4,0,6,1,2,4]


professions = {1:"Systems Security Administrator",
				2:"Business Systems Analyst",
				3:"Software Systems Engineer",
				4:"Database Developer",
				5:"Business Intelligence Analyst",
				6:"Business Systems Analyst",
				7:"CRM Technical Developer",
				8:"Mobile Applications Developer",
				9:"UX Designer",
				10:"CRM Technical Developer",
				11:"Quality Assurance Associate",
				12:"Web Developer"}

def output(listofanswers):
    class my_dictionary(dict):   
        def __init__(self): 
            self = dict()           
        def add(self, key, value): 
            self[key] = value 
    ques = my_dictionary()

    for i in range (0,10):
                ques.add(i,input_list[i])
    
    all_scores=[]

    score_Systems_Security_Administrator=(ques[0]+ques[1]+ques[2])/15
    all_scores.append(score_Systems_Security_Administrator)

    score_Business_Systems_Analyst=(ques[1]+ques[2]+ques[3])/15
    all_scores.append(score_Business_Systems_Analyst)

    score_Software_Systems_Engineer=(ques[3]+ques[1]+ques[5])/15
    all_scores.append(score_Software_Systems_Engineer)

    score_Database_Developer=(ques[0]+ques[1]+ques[5])/15
    all_scores.append(score_Database_Developer)

    score_Business_Intelligence_Analyst=(ques[0]+ques[6]+ques[9])/15
    all_scores.append(score_Business_Intelligence_Analyst)

    score_Business_Systems_Analyst=(ques[3]+ques[1]+ques[5])/15
    all_scores.append(score_Business_Systems_Analyst)

    score_CRM_Technical_Developer=(ques[0]+ques[9]+ques[5])/15
    all_scores.append(score_CRM_Technical_Developer)

    score_Mobile_Applications_Developer=(ques[3]+ques[1]+ques[8])/15
    all_scores.append(score_Mobile_Applications_Developer)

    score_UX_Designer=(ques[0]+ques[8]+ques[5])/15
    all_scores.append(score_UX_Designer)

    score_CRM_Technical_Developer=(ques[0]+ques[3]+ques[9])/15
    all_scores.append(score_CRM_Technical_Developer)

    score_Quality_Assurance_Associate=(ques[0]+ques[2]+ques[5])/15
    all_scores.append(score_Quality_Assurance_Associate)

    score_Web_Developer=(ques[0]+ques[2]+ques[4])/15
    all_scores.append(score_Web_Developer)
    
    li=[] 
 
    for i in range(len(all_scores)): 
          li.append([all_scores[i],i]) 
    li.sort() 
    sort_index = []  
    for x in li: 
          sort_index.append(x[1]+1) 
    all_scores.sort(reverse = True)
    
    a = sort_index[0:5]
    b = all_scores[0:5]
    s = sum(b)
    d = list(map(lambda x: x * (100/s) , b))
    
    return a,d        

l,data = output(input_list)

out = []
for i in range (0,5):
    n = l[i]
    c = professions[n]
    out.append(c)


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