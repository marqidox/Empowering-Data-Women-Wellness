# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame

# If you wish change which data set you are working with, do that here: 
lwd=pd.read_csv("livwell175.csv")
#print(lwd['country_name'].unique())

nigeriaBooleanList = lwd["country_name"]=="Nigeria"
nigeriaData = lwd.loc[nigeriaBooleanList]

ocBooleanList = lwd["country_name"]=="Turkey"
otherCountryData = lwd.loc[ocBooleanList]

print("Education in Nigeria and Turkey:")
print("In both Nigeria and Turkey, secondary education is a crucial need for all citizens. In Nigeria, secondary education is the bridge to higher education such as college and entering the workforce. In Turkey, secondary education is compulsory to move onto higher education.")
input("Press return to continue quote")
print()
print("Despite the importance of education in these countries, women face many barriers when it comes to obtaining it.")
print("In Nigeria, women's education has many challenges such as gender discrimination, cultural and religious limitations, poverty, illiteracy, among others. In Turkey, opportunities for secondary education are rare, discouraging female interest at primary level.")
print("Futhermore, girls in both Nigeria and Turkey are commonly raised in patriarchal families and are taught to take care of the household rather than going to school. This leaves them vulnerable and unable to have control of their lives, causing girls to fall prey to abuse, child marriage, and early pregnancy.")
input("Press return to continue quote")
print()
print("This brings us to the question: How can we increase access to education for women in Nigeria and Turkey to reduce early-age pregnancy?")
print("Education is vital, as it is able to empower girls within their family and community. Providing more education for girls will increase the involvement of women in the political process and further the spread of information on several health threats including female circumcision, early pregnancy and sexually transmitted diseases.")
print("According to the graph, as the percentage of secondary and higher education increases, the median age for a woman's first birth increases. This can likely be attributed to the knowledge gained on reproductive health, and shows why we must break down barriers to education.")
# ED_attainment_secondary_higher_p vs FP_desired_daugh_mean

plt.scatter(x="ED_attainment_secondary_higher_p",y="RH_age_first_birth_mean",data=nigeriaData,color='green')
plt.scatter(x="ED_attainment_secondary_higher_p",y="RH_age_first_birth_mean",data=otherCountryData,color='red')
#plt.ylim(0,4)
#plt.xlim(0,70)
plt.title("Women with secondary education or higher education(%) vs Median age at first birth for women aged 25-49 who ever had a child")
plt.xlabel("ED_attainment_secondary_higher_p")
plt.ylabel("RH_age_first_birth_mean")
plt.legend(['Nigeria','Turkey'])
plt.show()
