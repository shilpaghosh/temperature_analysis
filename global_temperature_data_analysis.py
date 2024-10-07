import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st



# Add a title with text and emoji
st.title("Global Temperature Data Analysis 💃")

# Use a dancing GIF to make it fun!
st.write("Let's dance through the data! 🕺💃")

# Display a dancing GIF (use a URL or local file path)
gif_url = "https://media.giphy.com/media/3o7TKMt1VVNkHV2PaE/giphy.gif"
st.image(gif_url, caption='Dancing while analyzing the data!', use_column_width=True)


data=pd.read_csv('/Users/shilpaghosh/Downloads/archive (13)/GlobalLandTemperaturesByCountry.csv')
print(data.head())


# Convert 'dt' column to datetime
data["date"] = pd.to_datetime(data['dt'], errors='coerce')

# Remove rows with missing temperatures
data = data.dropna(subset=["AverageTemperature"])

# Extract Year and Month
data["year"] = data["date"].dt.year
data["month"] = data["date"].dt.month

# Yearly average temperature
yearly_avg = data.groupby("year")["AverageTemperature"].mean().reset_index()

# Monthly average temperature
monthly_avg = data.groupby(["year", "month"])["AverageTemperature"].mean().reset_index()

st.write("## Yearly Average Temperature")
st.write(yearly_avg)

# Plotting Yearly Trends
st.write("### Yearly Average Global Temperature Plot")
plt.figure(figsize=(10, 6))
sns.lineplot(data=yearly_avg, x='year', y='AverageTemperature')
plt.title('Yearly Average Global Temperature')
plt.xlabel("Year")
plt.ylabel("Average Temperature (°C)")
st.pyplot(plt.gcf())  # Display the plot in Streamlit

# Plotting Monthly Trends
st.write("### Monthly Average Global Temperature Plot")
plt.figure(figsize=(10, 6))
sns.lineplot(data=monthly_avg, x='month', y="AverageTemperature")
plt.title("Monthly Average Global Temperature")
plt.xlabel('Month')
plt.ylabel('Average Temperature (°C)')
st.pyplot(plt.gcf())  # Display the plot in Streamlit

# Correlation Analysis Between Regions
st.write("### Correlation Analysis Between Countries")

# Filter data for a few countries
Country = ["Canada", "India", "China", "United States"]
df_countries = data[data['Country'].isin(Country)]

# Pivot the data to have countries as columns
data_pivot = df_countries.pivot_table(index='year', columns='Country', values='AverageTemperature')
st.write("## Pivoted Data for Selected Countries")
st.write(data_pivot)

# Correlation matrix
correlation_matrix = data_pivot.corr()

# Plot the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation between Temperatures in Different Countries')
st.pyplot(plt.gcf())  # Display the plot in Streamlit
