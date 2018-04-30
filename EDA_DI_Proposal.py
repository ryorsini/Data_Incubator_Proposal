
# coding: utf-8

# In[4]:


#Ryan Orsini
#Data Incubator 
#Deadline - Monday April 30th, 2018


#Import requisite libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
get_ipython().run_line_magic('matplotlib', 'inline')
from ggplot import *


#Get working directory
os.getcwd()

#Change working directory
os.chdir('/Users/rhinomonkey/Desktop/data_incubator/Data/')

#Assigned Variables to correct data sets after initial cleaning in Excel. 
#Assign m_spend to data for Total Military Spending per Country
m_spend = pd.read_excel("country_spending.xlsx", na_values=['. .','xxx'])
m_spend = m_spend.set_index(['Country'])


#Assign percent_gdp to Military Spending as Percent of GDP per Country 
percent_gdp = pd.read_excel('perc_of_gdp.xlsx', na_values=['. .','xxx'])
percent_gdp = percent_gdp.set_index(['Country'])
percent_gdp.head()

#Assign per_cap to Military Spending per Capita
#Determine which data sets you will be using - World Bank or SIPRI
per_cap = pd.read_excel('per_capita_spending.xlsx',  na_values=['. .','xxx'])
per_cap = per_cap.set_index(["Country"])
per_cap.head()

#Want to have 10 years of data to work with

#Determine top ten military spenders by amt. of money
#Create a data frame with 'Countries' as the column headers and all of their values per year below
#This enables the .mean function to work so that I can glean the top ten from the list

#Goals:

#Sort each data set by country / military spending / GDP / per person military spending

#Find Fastest growing countries in military spending over the course of the 10 years 

#Compare the data to that country’s GDP
#After sorting by military spending show each country's GPD (good comparisons will be ratios)

#Take all countries in the top ten and compare them to each other's spending 

#Find or calculate (total military spending per person to per person GPD)

#Over a period of time determine the rate of increase of each country’s spending


# In[3]:


#Military Spending for Years 2005 - 2015
m_spend10 = m_spend.drop(m_spend.columns[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,-1]], axis=1)
m_spend10['mean']=m_spend10.mean(axis=1)
#Sort by mean of the last ten years
m_spend10 = m_spend10.sort_values("mean", ascending=False)
m_spend10


# In[5]:


#Miltary Spending for 2015 (in 2014 dollars)
m_spend2015 = m_spend.drop(m_spend.columns[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28]], axis=1)
#Sort by 2015 spending
m_spend2015 = m_spend2015.sort_values(2015, ascending=False)
m_spend2015


# In[6]:


#Military spending - top tens sorted by mean
m_spend_top_ten_mean = m_spend10[0:10]
m_spend_top_ten_mean
#Military spending - top tens for 2015 spending
m_spend_top_ten_2015 = m_spend2015[0:10]
m_spend_top_ten_2015


# In[7]:


#Percent of GDP used for military spending - 2005 - 2015
percent_gdp10 = percent_gdp.drop(percent_gdp.columns[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]], axis=1)
percent_gdp10['mean']=percent_gdp10.mean(axis=1)
#Sort by mean percentage of spending
percent_gdp10 = percent_gdp10.sort_values('mean', ascending=False) 
percent_gdp10


# In[8]:


#Percent of GDP - only year 2015
percent_gdp2015 = percent_gdp.drop(percent_gdp.columns[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]],axis=1)
percent_gdp2015 = percent_gdp2015.sort_values(2015, ascending=False)


# In[9]:


#Top ten after sorted by mean & also year 2015
percent_gdp_top_ten_mean = percent_gdp10[0:10]
percent_gdp_top_ten_mean
percent_gdp_top_ten_2015 = percent_gdp2015[0:10]
percent_gdp_top_ten_2015


# In[10]:


#For Per Capita - must compare to per person gdp. Since Per capita military spending is merely a share of GDP
#I can get per capita GDP from percent military spending of GDP 
#per capita gdp = per capita military spending / percent miilitary spending of gdp 

#Get Top Ten Millitary Spending Per Capita

#Create a data frame that creates per capita GDP from per capita military spending and % military spending


# In[11]:


#Military Spending Per Capita - 2005 - 2015 
per_cap10 = per_cap.drop(per_cap.columns[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]], axis=1)
#Per Capita sorted by mean
per_cap10 ['mean'] = per_cap10.mean(axis=1)
per_cap10 = per_cap10.sort_values('mean', ascending=False)
per_cap10


# In[12]:


#Military Spending per Capita only 2015 - sorted by 2015 spending
per_cap2015 = per_cap.drop(per_cap.columns[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]], axis=1)
per_cap2015 = per_cap2015.sort_values(2015, ascending=False)
per_cap2015


# In[13]:


#Top ten of both sorted by mean and year 2015
per_cap_top_ten_mean = per_cap10[0:10]
per_cap_top_ten_mean
per_cap_top_ten_2015 = per_cap2015[0:10]
per_cap_top_ten_2015


# In[14]:


#Make Data Frame with per capita GDP
per_cap_gdp = per_cap10/percent_gdp10
per_cap_gdp_mean = per_cap_gdp.sort_values('mean', ascending=False)
per_cap_gdp_2015 = per_cap_gdp.drop(per_cap_gdp.columns[[0,1,2,3,4,5,6,7,8,9,11]],axis=1)
per_cap_gdp_2015 = per_cap_gdp_2015.sort_values(2015, ascending=False)
per_cap_gdp_2015

#Per Capita GDP Top Ten Sorted by year 2015
pcgdp_tt_mean = per_cap_gdp_mean[0:10]
pcgdp_tt_mean 

#Per Capita GDP Top Ten Sorted by year 2015
pcg_tt_2015 = per_cap_gdp_2015[0:10]
pcg_tt_2015


# In[16]:


#Drop Mean from data set m_spend10 & assign to new data frame
m_spend10_nomean = m_spend10.drop(m_spend10.columns[[10]], axis=1)
m_spend10_nomean_topten =m_spend10_nomean[0:10]
#Graph
B1=m_spend10_nomean_topten.plot(kind='bar',legend=False, title='Military Spending of Top Ten Countries (Mean Spending from Ten Years)')
B1.set(ylabel="US Dollars (Adjusted to 2014)", xlabel="Spending from 2005-2015 by Country")


# In[184]:


#Make a data frame with solely Country and Mean
m_spend10_onlymean = m_spend10.drop(m_spend.columns[[17,18,19,20,21,22,23,24,25,26,27]], axis=1)
m_spend10_onlymean_topten = m_spend10_onlymean[0:10]
#Graph in a bar chart
B2=m_spend10_onlymean_topten.plot(kind="bar", title='Military Spending of Top Ten Countries (Based on Mean Spending from Ten Years)',
                                   grid = True, color="maroon",legend=False)
B2.set(ylabel="US Dollars (Adjusted to 2014)", xlabel="Country")


# In[185]:


#Bar Graph of Top Ten Countries Based on 2015 Spending
B3=m_spend_top_ten_2015.plot(kind='bar',title="Military Spending of Top Ten Countries (Based on 2015 Spending)", color="maroon", grid=True)
B3.set(ylabel="US Dollars (Adjusted to 2014)", xlabel="Country")
#Note that the ordering is different and Italy is no longer on the graph (replaced by South Korea)


# In[186]:


#Percent Military Spending Takes up of GDP
percent_gdp10_nomean = percent_gdp10.drop(percent_gdp10.columns[11],axis=1)
percent_gdp10_nomean = percent_gdp10_nomean[0:10]
percent_gdp10_nomean = percent_gdp10_nomean*100
B4=percent_gdp10_nomean.plot(kind='bar', legend=False, title="Countries with Highest Percentage of GDP Spent on Military (Based on Mean Spending from Ten Years)")
B4.set(ylabel="Percentage of GDP Spent on Military", xlabel="Spending from 2005-2015 by Country")


# In[187]:


#Bar Graph of Highest Percentage of GDP Spent on Military (Only Mean Values)
percent_gdp10_onlymean=percent_gdp_top_ten_mean.drop(percent_gdp_top_ten_mean.columns[[0,1,2,3,4,5,6,7,8,9,10]],axis=1)
percent_gdp10_onlymean=percent_gdp10_onlymean*100
B5=percent_gdp10_onlymean.plot(kind='bar', title='Countries with Highest Percentage of GDP Spent on Military (Based on Mean Spending from Ten Years)', color="maroon")
B5.set(xlabel='Country', ylabel="Percentage of GDP Spent on Military")


# In[188]:


#Bar Graph of Highest Percentage of GDP Spent on Military (Based on 2015 Spending)
percent_gdp_tt_2015=percent_gdp_top_ten_2015*100
B6=percent_gdp_tt_2015.plot(kind='bar',title="Countries with Highest Percent of GDP Spent on Military (Based on 2015 Spending)", color="maroon")
B6.set(xlabel="Country",ylabel="Percentage of GDP Spent on Military")


# In[189]:


#Bar Graph of Countries with Top Ten Per Capita Military Spending 2005-2015
per_cap10_nomean = per_cap10.drop(per_cap10.columns[[11]], axis=1)
per_cap10_nomean = per_cap10_nomean[0:10]
B7=per_cap10_nomean.plot(kind="bar",legend=False, title="Per Capita Military Spending: 2005-2015")
B7.set(xlabel="Spending from 2005-2015 by Country", ylabel="USD Per Person")


# In[190]:


per_cap_meanonly=per_cap_top_ten_mean.drop(per_cap_top_ten_mean.columns[[0,1,2,3,4,5,6,7,8,9,10]], axis=1)
B8=per_cap_meanonly.plot(kind='bar', title='Per Capita Spending on Military (Based on Mean Spending From Ten Years)',color="maroon")
B8.set(xlabel="Country",ylabel="USD Per Person")



# In[191]:


B9=per_cap_top_ten_2015.plot(kind="bar",title="Per Capita Spending on Military (Based on 2015 Spending)", color="maroon")
B9.set(xlabel="Country", ylabel="USD Per Person")


# In[192]:


#Line Graph of Military Spending Over 2005-2015
ms=pd.read_excel("csb.xlsx")
P1=ms.plot(kind="line", x='Year',figsize=(10,5.5),title="Total Military Spending from 2005-2015 in 2014 USD")
P1.set(ylabel='USD (Adjusted to 2014)')

#Without USA
ms_nousa=ms.drop(ms.columns[[1]], axis=1)
P2=ms_nousa.plot(kind='line', x="Year",figsize=(10,5.5),title="Total Military Spending from 2005-2015 in 2014 USD (Not Including USA)")
P2.set(ylabel="USD (Adjusted to 2014)")



# In[193]:


capitas_combined=per_cap2015
capitas_combined["Per Capita GDP"]=per_cap_gdp_2015
capitas_combined=capitas_combined.rename(columns={2015:"Per Capita Military Spending"})
capitas_combined20=capitas_combined[0:20]
P3=capitas_combined20.plot.bar(title="Per Capita GDP vs. Per Capita Military Spending")
P3.set(ylabel='USD (Adjusted to 2014)')


# In[194]:


#Growth Rates of Top Ten Countries
m_spend_growth=m_spend10
m_spend_growth["Growth Rate"]=abs(m_spend_growth[2015]-m_spend[2005])/m_spend_growth[2005]*100
m_spend_growth=m_spend_growth.sort_values("Growth Rate", ascending=False)
m_spend_growth_tt=m_spend_growth[0:10]
m_spend_growth_tt=m_spend_growth_tt.drop(m_spend_growth_tt.columns[[0,1,2,3,4,5,6,7,8,9,10,11]],axis=1)
m_spend_growth_tt

#Graph of Fastest Growing Countries
P4=m_spend_growth_tt.plot(kind='bar',title="Countries with Highest Growth in Military Spending from 2005-2015", color='maroon')
P4.set(ylabel="Growth Rate")


# In[195]:


#Graph of Fastest Growth Rate in Top Ten Military Spending Countries By Mean

m_spend_growth_meanoftt=m_spend_growth.sort_values("mean", ascending=False)
m_spend_growth_meanoftt=m_spend_growth_meanoftt[0:10]
m_spend_growth_meanoftt=m_spend_growth_meanoftt.sort_values("Growth Rate", ascending=False)
m_spend_growth_meanoftt=m_spend_growth_meanoftt.drop(m_spend_growth_meanoftt.columns[[0,1,2,3,4,5,6,7,8,9,10,11]],axis=1)
P5=m_spend_growth_meanoftt.plot(kind='bar', color="maroon",title="Top Ten Countries and Growth Rate")
P5.set(ylabel="Percentage Growth")


# In[196]:


#GDP vs. Military Spending in Numbers (2015)
m_spend_gdp_2015=m_spend2015/percent_gdp2015
m_spend_gdp_2015["Military Spending 2015"]=m_spend2015
m_spend_gdp_2015=m_spend_gdp_2015.sort_values('Military Spending 2015',ascending=False)
m_spend_gdp_2015=m_spend_gdp_2015[0:20]
P6=m_spend_gdp_2015.plot(kind="bar",title="2015 GDP vs. 2015 Military Spending")
P6.set(ylabel="USD in Trillions (Adjusted to 2014 USD)")

#Without USA
m_spend_gdp_2015nousa=m_spend_gdp_2015.drop(m_spend_gdp_2015.index[0])
P7=m_spend_gdp_2015nousa.plot(kind='bar', title="2015 GDP vs. 2015 Military Spending(Without USA)")
P7.set(ylabel="USD in Trillions (Adjusted to 2014 USD)")
#Without USA & China 
m_spend_gdp_2015nousorchina=m_spend_gdp_2015nousa.drop(m_spend_gdp_2015nousa.index[0])
P9=m_spend_gdp_2015nousorchina.plot(kind='bar', title="2015 GDP vs. 2015 Military Spending(Without USA & China)")
P9.set(ylabel="USD in Trillions (Adjusted to 2014 USD)")


# In[197]:


m_spend10_nomean = m_spend10.drop(m_spend10.columns[[10]], axis=1)
m_spend10_nomean_topten =m_spend10_nomean[1:10]
#Graph
B1=m_spend10_nomean_topten.plot(kind='bar',legend=False, title='Military Spending of Top Ten Countries (Not Including USA)')
B1.set(ylabel="US Dollars (Adjusted to 2014)", xlabel="Spending from 2005-2015 by Country")


# In[198]:


#USA Percent GDP
percent_gdp10[13:14]*100


# In[199]:


#Create a data frame for Power Point
ms_00=m_spend10.drop(m_spend10.columns[[0,1,2,3,4,5,6,7,12]],axis=1)
ms_00.head()

