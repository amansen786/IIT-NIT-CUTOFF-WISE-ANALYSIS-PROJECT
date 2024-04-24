import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('iit- nit.csv')
print()

var=df.head(10000)
print(var)
#__________________________________________________________________________________________________________________________________

df1 = var.drop(['is_preparatory','round_no', 'quota', 'id'], axis = 1, inplace= True )    # I REMOVED UNNECESSARY COLUMNS HERE
print(df1)

df2=var.info()  # INFO() about columns with thier names,their datatypes,and missing values
print(df2)

df3=var.rename(columns= {'Pool':'Gender'}, inplace=True)     # I Changed Name of the column of the data frame here.
print(df3)

df4=var.describe()  #the Describe() Methods used for calcultating some statistical data like percentile,mean,min,max and numerical values of the series or data frame.
print(df4)

#**************************************************************************************************************************************

gender_male = var.where(var['pool'] == "Gender-Neutral") # here we saw how many (GENDER-Neutral) have been selected in different IITS.
out_male = gender_male.groupby('institute_short')
print(out_male.describe()) 

#************************************************************************************************************************************
gender_female = var.where(var['pool'] == "Female-Only")  # here we saw how many female-only have been selected in different IITS.
out_female = gender_female.groupby('institute_short')
print(out_female.describe()) 
#________________________________________________________________________________________________________________________


df5 = var["pool"].value_counts()    # TOTAL  NUMBER'S OF MALE'S AND FEMALE'S  WHO HAVE BEEN SELETED IIT & NIT
print(df5)
#____________________________________________________________________________________________________________________________

df6=var["degree_short"].value_counts() #  IN THIS METHODS WE SAW WHICH COURSES OF IIT & NIT WERE TAKEN THE MOST 
print(df6)
#_______________________________________________________________________________________________________________________________
df7=var["year"].value_counts() # in this methods's we saw maximum number of student"s were seleted in IIT & NIT in which year 
print(df7)

#________________________________________________________________________________________________________________________________



#_________________________________________________________________________________________________________________________________

grouby_iit= var.where(var['institute_short'] == "IIT-Bombay")

out_male12 = grouby_iit.groupby('year')  #  We Analyzed it IIT - bombay data by using (groupby) function

print(out_male12.describe()) 

#______________----------_________----------_____________-----------______________----------------____________-----------_____________
#/////////////////////////////////////////// DATA VISUALISATION //////////////////////////////////////////////////////
#______________----------_________----------_____________-----------______________----------------____________-----------_____________

x= var['year']
y= var['category'] 
plt.figure(figsize=(12,6))         # in this Graph we saw  which Caste's have been selected in which year's
plt.xlabel('year')
plt.ylabel('category')
plt.title("year's by category",fontsize=15)
plt.bar(x,y)
plt.show()
#****************************************************************************************************************************************************

x= var['year']
y= var['institute_short'] 
plt.figure(figsize=(12,6))
plt.xlabel('year')
plt.ylabel('institute_short')
plt.title("year's by iit & nit",fontsize=15)
plt.bar(x,y)
plt.show()

#******************************************************************************************************************************************************

x= var['year']
y= var['opening_rank'] 
plt.figure(figsize=(12,6))
plt.xlabel('year')
plt.ylabel('opening_rank')
plt.title("",fontsize=15)
plt.bar(x,y)
plt.show()

#****************************************************************************************************************************************************

x= var['year']
y= var['pool'] 
plt.figure(figsize=(12,6))
plt.xlabel('year')
plt.ylabel('pool')
plt.title("IN WHICH YEAR THE MAXIMUM NUMBER OF BOY'S AND GIRL'S HAVE BEEN SELETED IN IIT & NIT",fontsize=15)
plt.bar(x,y)
plt.show()


df["pool"].value_counts().plot.bar()    
plt.show()

#***************************************************************************************************************************************************

