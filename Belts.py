# Mat Lockhart
# %%
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime

seatbelt_law_date = datetime.strptime("08/01/2013", "%m/%d/%Y")

# Only read in one set of data at a time
# data = pd.read_csv("Traffic_Violations_2.csv")
data = pd.read_csv("C:/Users/mathi/Documents/Traffic_Violations.csv")

data = data.dropna()
data['Belts'] = data['Belts'].map({'Yes': 1, 'No': 0})
data

# %%
# Belt usage over time

belt_percentages = []
year = []

for i in range(2012, 2017):
    i_str = f"{i}"
    for j in range(1, 13):
        j_str = f"{j}"
        year.append(datetime.strptime(f"{j}/{i}", "%m/%Y"))
        temp_df = data.loc[data['Date Of Stop'].str.contains(rf"{j}/../{i}")]
        temp_val = temp_df['Belts'].sum() / temp_df['Belts'].count()
        temp_val = temp_val * 100
        belt_percentages.append(temp_val)

print(belt_percentages)
  
plt.plot(year, belt_percentages)
plt.title('Belt Usage over 2012-2016')
plt.xlabel('Year')
plt.ylabel('Percent Belt Use')
# plt.locator_params(axis='x', nbins=5)

plt.axvline(x=seatbelt_law_date, label='Seatbelt Law', color='g', dashes=[3,2])

plt.legend()
plt.show()

# %%
# Belt usage by race
races = data.Race.unique()
races_belts = []

for race in races:
    temp_df = data.loc[data['Race'].str.contains(rf"{race}")]
    temp_val = temp_df['Belts'].sum() / temp_df['Belts'].count() * 100
    races_belts.append(temp_val)
    print(f"{race}: {temp_val}")

races[5] = "NATIVE"

plt.bar(races, races_belts, color=['purple', 'blue', 'green', 'yellow', 'orange', 'red'])

plt.show()


# %%
# Get first and last date from data

first_date = datetime.today()
last_date = datetime.min

print(f"Today: {first_date}")

# Find first date in data
for i, row in data.iterrows():
    temp_date = datetime.strptime(row['Date Of Stop'], "%m/%d/%Y")
    if temp_date < first_date:
        first_date = temp_date
    if temp_date > last_date:
        last_date = temp_date

print(f"First date in data: {first_date}\nLast date in data: {last_date}")

# %%
