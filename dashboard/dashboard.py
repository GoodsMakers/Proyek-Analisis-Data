import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
@st.cache_data
def load_data():
        # Load your data here, replace 'your_data.csv' with the actual data file
        data = pd.read_csv('dashboard/day_cleaned.csv')
        return data

data = load_data()

# Set the title of the app
st.title("Bike Sharing Analysis Dashboard")

# Question 1: How does temperature affect bike sharing?
st.header("1. How does temperature affect bike sharing?")

# Create a scatter plot to show the relationship between temperature and total users
fig_temp, ax_temp = plt.subplots()
sns.scatterplot(x='temperature', y='total_user', data=data, ax=ax_temp)
ax_temp.set_xlabel('Temperature')
ax_temp.set_ylabel('Total Users')
ax_temp.set_title('Temperature vs. Total Users')
st.pyplot(fig_temp)

# Question 2: In which season does bike sharing get the highest users?
st.header("2. In which season does bike sharing get the highest users?")

# Aggregate data by season
seasonal_data = data.groupby('season')['total_user'].sum().reset_index()

# Create a bar plot to show total users per season
fig_season, ax_season = plt.subplots()
sns.barplot(x='season', y='total_user', data=seasonal_data, ax=ax_season, palette="viridis")
ax_season.set_xlabel('Season')
ax_season.set_ylabel('Total Users')
ax_season.set_title('Total Users by Season')
st.pyplot(fig_season)

# Calculate the season with the highest users
max_season = seasonal_data.loc[seasonal_data['total_user'].idxmax()]
st.write(f"The season with the highest number of users is **{max_season['season']}** with **{max_season['total_user']}** total users.")

# Add a footer
st.write("This dashboard provides insights into how temperature affects bike sharing and identifies the season with the highest usage.")
