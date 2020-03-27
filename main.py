import re
import matplotlib.pyplot as plt
import numpy as np
import collections

mainFile = open('textFile.txt','r')

data = {'S.R.J':[0,0,0],'Rohan Singh':[0,0,0],'Sapta':[0,0,0],'Choti IITJ':[0,0,0],'Kwanit IITJ':[0,0,0],'Shriyog':[0,0,0],'Maruf IITJ':[0,0,0],'Niel IITJ':[0,0,0],'Ridhima IITJ':[0,0,0],'Roopesh':[0,0,0],'Tarun Tomar':[0,0,0],'Soumya':[0,0,0],'Samarth':[0,0,0],'Shivam':[0,0,0]}

totalLines = mainFile.readlines()

# main code for calculating totals messages, total no of characters and total media messages per person
for line in totalLines:
    name = ''
    try:
        if line[15]=='-':
            i = 17 
            while line[i]!= ':':
                name+=line[i]
                i+=1
            data[name][0]+=1 
            if line[i+2]=='<':
                data[name][2]+= 1
            else:    
                data[name][1]+=len(line[i:])
    except:
        pass

#Let's make Pie Graph/charts

labels = []
sizes = []
colors = ['red', 'orange', 'blue', 'green', 'gold','black','violet','purple','pink','black','beige','lightblue','teal','grey']
explode = [0.1,0,0,0,0,0.1,0,0,0,0.1,0,0,0,0]

for key in data.keys():
    labels.append(key)
    sizes.append(data[key][0])

plt.pie(sizes,explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', startangle=90)
plt.title('Percentage of Total Messages In The Group!')
plt.axis('equal')

#Kwanit ki maka

# labels = ['Kwanit']
# sizes = [10]
# colors = ['green']
# explode = [0.1]


# plt.pie(sizes,explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', startangle=90, shadow=True)
# plt.title('No Of Messages Ignored!')
# plt.axis('equal')

#RIP KWANIT


#Let's make Histograms

#No of characters per person

histData = {}

for key in data.keys():
    histData[key] = data[key][1]

histData = sorted(histData.items(), key=lambda kv: kv[1])

histData = collections.OrderedDict(histData)

histLabels = []
histValues = []

for key in histData.keys():
    histLabels.append(key)
    histValues.append(histData[key])
 
fig, ax = plt.subplots()    
width = 0.75 # the width of the bars 
ind = np.arange(len(histValues))  # the x locations for the groups
ax.barh(ind, histValues, width, color="blue")
ax.set_yticks(ind+width/2)
ax.set_yticklabels(histLabels, minor=False)
plt.title('No of Characters Per Person')
plt.xlabel('x')
plt.ylabel('y')        

for i, v in enumerate(histValues):
    ax.text(v, i, str(v), color='black', fontweight='bold')

#No of Media Messages(Including stickers) per Person

histData = {}

for key in data.keys():
    histData[key] = data[key][2]

histData = sorted(histData.items(), key=lambda kv: kv[1])

histData = collections.OrderedDict(histData)

histLabels = []
histValues = []

for key in histData.keys():
    histLabels.append(key)
    histValues.append(histData[key])
 
fig, ax = plt.subplots()    
width = 0.75 # the width of the bars 
ind = np.arange(len(histValues))  # the x locations for the groups
ax.barh(ind, histValues, width, color="blue")
ax.set_yticks(ind+width/2)
ax.set_yticklabels(histLabels, minor=False)
plt.title('No of Media Messages(including stickers) Per Person')
plt.xlabel('x')
plt.ylabel('y')        

for i, v in enumerate(histValues):
    ax.text(v, i, str(v), color='black', fontweight='bold')

#No of Characters Per Message per Person

histData = {}

for key in data.keys():
    histData[key] = round(data[key][1]/data[key][0],2)

histData = sorted(histData.items(), key=lambda kv: kv[1])

histData = collections.OrderedDict(histData)

histLabels = []
histValues = []

for key in histData.keys():
    histLabels.append(key)
    histValues.append(histData[key])
 
fig, ax = plt.subplots()    
width = 0.75 # the width of the bars 
ind = np.arange(len(histValues))  # the x locations for the groups
ax.barh(ind, histValues, width, color="blue")
ax.set_yticks(ind+width/2)
ax.set_yticklabels(histLabels, minor=False)
plt.title('No of Characters Per Message per Person')
plt.xlabel('x')
plt.ylabel('y')        

for i, v in enumerate(histValues):
    ax.text(v, i, str(v), color='black', fontweight='bold')

# for key in data.keys():
#     print(key,' Has ',data[key][0],"Messages and ",data[key][1],'characters  and ',data[key][2],'media messages') 
#     print("Characters per message",data[key][1]/data[key][0]) 
#     print()         
         
plt.show()
