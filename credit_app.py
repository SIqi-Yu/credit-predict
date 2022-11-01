import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')

st.title('Credit Score Analysis')
df = pd.read_csv('train.csv')

# the outsanding debt
st.header('Outstanding Debt')
fig, ax = plt.subplots(figsize=(10,5),facecolor=(.18, .31, .31))
df.sort_values(by='Outstanding_Debt',ignore_index=True).Outstanding_Debt.plot(ax=ax,linestyle='dashed',color='black')
ax.set_facecolor('#eafff5')
ax.set_ylabel('Number of People',color='peachpuff',)
ax.set_xlabel('Outstanding Debt',color='peachpuff')
ax.tick_params(labelcolor='tab:orange')
st.pyplot(fig)



# age distribution
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


#installment amount and credit score
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


# fiilter
st.header('Histogram of the Annual Income')
income_filter = st.slider('choose income:', 7005.93, 179987.28, 10000.00)  # min, max, default 滑块


# filter by income
df = df[df.Annual_Income >= income_filter]

# filter by the occupation
Payment_Behaviour_filter = st.sidebar.multiselect(
    'choose the Payment_Behaviour',
    df.Payment_Behaviour.unique(), 
    df.Payment_Behaviour.unique()
)
df = df[df.Payment_Behaviour.isin(Payment_Behaviour_filter)]


# filter by payment behavior


# a radio button



fig, ax = plt.subplots(figsize=(20,15))
df.Credit_Score.hist(xlabelsize=30,ylabelsize=30)
st.pyplot(fig)

