import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Survival by Passenger Class
class_survival = pd.DataFrame({
    'Class': ['Class 1', 'Class 2', 'Class 3'],
    'Survival Rate (%)': [52.4, 21.4, 36.1]
})

# 2. Gender Impact on Survival
gender_survival = pd.DataFrame({
    'Gender': ['Female', 'Male'],
    'Survival Rate (%)': [56.8, 23.2]
})

# 3. Age Distribution
age_distribution = pd.DataFrame({
    'Age Group': ['0-20', '21-40', '41-60', '61+'],
    'Passenger Count': [29, 26, 29, 16]
})

# 4. Port of Embarkation
embarkation = pd.DataFrame({
    'Port': ['Cherbourg (C)', 'Queenstown (Q)', 'Southampton (S)'],
    'Passenger Count': [29, 37, 34]
})

# Set seaborn style
sns.set(style='whitegrid')

# Plot 1: Survival by Passenger Class
plt.figure(figsize=(6, 4))
sns.barplot(x='Class', y='Survival Rate (%)', data=class_survival, palette='Blues_d')
plt.title('Survival Rate by Passenger Class')
plt.ylim(0, 100)
plt.show()

# Plot 2: Survival by Gender
plt.figure(figsize=(6, 4))
sns.barplot(x='Gender', y='Survival Rate (%)', data=gender_survival, palette='Purples_d')
plt.title('Survival Rate by Gender')
plt.ylim(0, 100)
plt.show()

# Plot 3: Age Distribution
plt.figure(figsize=(6, 4))
sns.barplot(x='Age Group', y='Passenger Count', data=age_distribution, palette='Greens_d')
plt.title('Age Distribution of Passengers')
plt.show()

# Plot 4: Port of Embarkation
plt.figure(figsize=(6, 4))
sns.barplot(x='Port', y='Passenger Count', data=embarkation, palette='Oranges_d')
plt.title('Passenger Count by Port of Embarkation')
plt.show()
