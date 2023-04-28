import pandas as pd
import matplotlib.pyplot as plt

# Read the data into a DataFrame
df = pd.read_csv("covid.csv")

# Filter the data to only include the United States
us_data = df[df['Country'] == 'Romania']

# Group the data by date and sum the new deaths
daily_new_deaths = us_data.groupby("Date_reported").agg({"New_deaths": "sum"})

# Create a plot of new deaths per day
fig, ax = plt.subplots()
daily_new_deaths.plot(ax=ax)

ax.set_title("New Deaths per Day in the Romania")
ax.set_xlabel("Date")
ax.set_ylabel("Number of New Deaths")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

plt.show()
