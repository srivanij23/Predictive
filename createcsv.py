# import csv

# # Define the data
# data = [
#     ["MachineID", "Model", "ManufacturingDate", "OperatingHours", "Status"],
#     ["001", "Model A", "2020-01-15", 1500, "Active"],
#     ["002", "Model B", "2021-03-20", 800, "Maintenance"],
#     ["003", "Model C", "2019-11-05", 2500, "Active"],
#     ["004", "Model D", "2022-07-13", 600, "Idle"],
#     ["005", "Model E", "2020-05-25", 1200, "Active"]
# ]

# # Write to CSV
# with open('machine_data.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

# print("CSV file 'machine_data.csv' has been generated.")
import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(42)

# Number of rows in the dataset
num_samples = 1000

# Random data for the features
machine_ids = np.arange(1, num_samples + 1)
temperature = np.random.uniform(70, 100, size=num_samples)  # Temperature in Celsius
vibration = np.random.uniform(2, 5, size=num_samples)  # Vibration in mm/s
pressure = np.random.uniform(90, 110, size=num_samples)  # Pressure in psi
speed = np.random.uniform(1200, 1600, size=num_samples)  # Speed in rpm
humidity = np.random.uniform(40, 70, size=num_samples)  # Humidity in percentage
power_consumption = np.random.uniform(150, 250, size=num_samples)  # Power consumption in watts
machine_age = np.random.randint(1, 6, size=num_samples)  # Machine age in years

# Simulate Maintenance (1 = maintenance required, 0 = no maintenance)
# Let's assume maintenance is required when temperature > 95 or vibration > 4.5
maintenance = np.where((temperature > 95) | (vibration > 4.5), 1, 0)

# Create a DataFrame
data = {
    'Machine_ID': machine_ids,
    'Temperature': temperature,
    'Vibration': vibration,
    'Pressure': pressure,
    'Speed': speed,
    'Humidity': humidity,
    'Power_Consumption': power_consumption,
    'Machine_Age': machine_age,
    'Maintenance': maintenance
}

df = pd.DataFrame(data)

# Save the DataFrame to CSV
df.to_csv('machine_data_updated.csv', index=False)

# Display the first few rows of the DataFrame
print(df.head())
