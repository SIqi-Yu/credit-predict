from email.policy import default
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


st.set_page_config(
    page_title="LUCY and 00",
    page_icon="🎈",
)

plt.style.use('seaborn')

st.title('📊Credit Score Analysis')

from PIL import Image
image = Image.open('1.jpg')

st.image(image)

with st.expander("ℹ️ - About this app", expanded=True):

    st.write(
        """     
-    Over the years, the company has collected basic bank details and gathered a lot of credit-related information. The management wants to build an intelligent system to segregate the people into credit score brackets to reduce the manual efforts.
-   🤗It took 00 and me more than two weeks to finish analysis and prediction, it's a complicated dataset that worth digging!!!
-   You can find the source code in the [Credit Score Classification Clean Data](https://www.kaggle.com/datasets/clkmuhammed/creditscoreclassification)
	    """
    )

    st.markdown("")

st.markdown("")

df = pd.read_csv('train.csv')
st.title('Data Preview')
# show data
st.write(df.sample(10))

################
### ANALYSIS ###
################

### DATA EXPLORER ###

st.title('EDA')
######################
# the outsanding debt#
######################
st.header('Outstanding Debt')
fig, ax = plt.subplots(figsize=(10,5),facecolor=(.18, .31, .31))
df.sort_values(by='Outstanding_Debt',ignore_index=True).Outstanding_Debt.plot(ax=ax,linestyle='dashed',color='black')
ax.set_facecolor('#eafff5')
ax.set_ylabel('Number of People',color='peachpuff',)
ax.set_xlabel('Outstanding Debt',color='peachpuff')
ax.tick_params(labelcolor='tab:orange')
st.pyplot(fig)



st.header('Annual Income')
fig3, ax3 = plt.subplots(figsize=(10,5))
df.Annual_Income.hist(ax=ax3,bins=500)
st.pyplot(fig3)


###########################
# age distribution#########
###########################
st.header('Age Distribution')
age = {}
x = 0
ages = df.Age.value_counts()
for i in range(14, 57):
    x += ages[i]
    if i == 20:
        age['14-20'] = x
        x = 0
    elif i == 30:
        age['21-30'] = x
        x = 0
    elif i == 40:
        age['31-40'] = x
        x = 0
    elif i == 50:
        age['41-50'] = x
        x = 0
    elif i == 56:
        age['51-56'] = x
age_groups = pd.DataFrame({'Age_range': age.keys(), 'Total_persons': age.values()})


fig1 = plt.figure(figsize=(10,4), dpi=100)
plt.title('Transaction according to age groups')
sns.barplot(data=age_groups, x='Age_range', y='Total_persons', palette='twilight_r')
sns.pointplot(data=age_groups, x='Age_range', y='Total_persons', color=(.18, .31, .31))
st.pyplot(fig1)

#####################################
#installment amount and credit score#
#####################################
st.header('installment amount and credit score')
df1 = df.drop(df[df['Payment_of_Min_Amount'].str.contains('NM',na=False)].index)
df2 = df1.groupby('Credit_Score').Payment_of_Min_Amount.value_counts(normalize=True)
fig2, ax2 = plt.subplots(figsize=(10,5))
df2.plot.bar(ax=ax2,color=(.18, .31, .31))
plt.xticks(rotation=45)
plt.ylabel('proportion')
ax2.tick_params(labelcolor='Grey')
st.pyplot(fig2)

# scatter
#Outstanding_Debt: Represents the remaining debt to be paid (in USD)
st.header('Distribution between age and Outstanding Debt')
fig4, ax4 = plt.subplots(figsize=(10,5))
df.plot.scatter(ax=ax4,x = 'Age',y = 'Outstanding_Debt') # make explaination about sudden drop
st.pyplot(fig4)


# filter
st.sidebar.markdown("**First select the data range you want to analyze:** 👇")
st.header('Histogram of the Annual Income')
income_filter = st.sidebar.slider('choose income:', 7005.93, 179987.28, 10000.00)  # min, max, default 滑块



####occupation select
df_o = np.append(df.Occupation.unique(),"ALL")
default_occupation = st.sidebar.selectbox(
    "Select the occupation you want to explore or just explore all",
    (df_o)
)
if default_occupation!="ALL":
    df = df[df.Occupation == default_occupation]


# filter by income
df = df[df.Annual_Income >= income_filter]

# filter by the paymant behavior
Payment_Behaviour_filter = st.sidebar.multiselect(
    'choose the Payment_Behaviour',
    df.Payment_Behaviour.unique(), 
    df.Payment_Behaviour.unique()
)
df = df[df.Payment_Behaviour.isin(Payment_Behaviour_filter)]


fig, ax = plt.subplots(figsize=(15,10))
df.Credit_Score.hist(xlabelsize=25,ylabelsize=25)
#ax = sns.barplot(x=['Good','Bad','Poor'], y=df.Credit_Score, data=df.reset_index(), color = "#b80606")
st.pyplot(fig)

