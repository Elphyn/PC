import pandas as pd
import matplotlib.pyplot as plt

# save in dataframe pandas
df = pd.read_csv("my_file.csv")

# Group the data by country and sum the deaths and cases
country_data = df.groupby("Country").agg({"New_deaths": "sum", "New_cases": "sum"})
top_countries = country_data.sort_values("New_deaths", ascending=False)[:5]

fig, ax = plt.subplots()
top_countries.plot(kind="bar", ax=ax)

ax.set_title("Total Deaths and Cases by Country (Top 5)")
ax.set_xlabel("Country")
ax.set_ylabel("Number")


plt.show()



# для одной страны по датам значения заражений и смертей