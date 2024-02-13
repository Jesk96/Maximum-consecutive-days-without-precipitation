import pandas as pd
import matplotlib.pyplot as plt

# Read data from Excel file  (replace 'your_file.xlsx' with the actual path of your file)
file_path = 'your_file.xlsx'
df = pd.read_excel(file_path)

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Function to calculate the maximum consecutive days without precipitation
def max_consecutive_days_without_rain(series):
    consecutive_days = 0
    max_consecutive_days = 0

    for value in series:
        if value == 0:
            consecutive_days += 1
            if consecutive_days > max_consecutive_days:
                max_consecutive_days = consecutive_days
        else:
            consecutive_days = 0

    return max_consecutive_days

# Calculate the maximum consecutive days without precipitation per year
max_consecutive_days_per_year = df.groupby(df['Date'].dt.year)['Rain'].apply(max_consecutive_days_without_rain)

# Create a DataFrame with the results
results_df = pd.DataFrame({'Year': max_consecutive_days_per_year.index, 'MaxConsecutiveDaysWithoutRain': max_consecutive_days_per_year.values})

# Save the results to a new Excel file (replace 'results.xlsx' with whatever name you want)
results_file_path = 'resultados.xlsx'
results_df.to_excel(results_file_path, index=False)

# Plot the results
plt.bar(results_df['Year'], results_df['MaxConsecutiveDaysWithoutRain'])
plt.xlabel('Year')
plt.ylabel('Maximum Consecutive Days Without Rain')
plt.title('Maximum Consecutive Days Without Rain')
plt.show()