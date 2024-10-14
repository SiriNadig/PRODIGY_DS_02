import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
titanic = sns.load_dataset('titanic')

# Basic dataset info
print(titanic.info())

# Handling missing values
# Fill missing age with median
titanic['age'].fillna(titanic['age'].median(), inplace=True)

# Fill missing embarked with mode
titanic['embarked'].fillna(titanic['embarked'].mode()[0], inplace=True)

# Drop any remaining rows with missing values
titanic.dropna(inplace=True)

# Categorical variable encoding
# Encode 'sex' column: male -> 0, female -> 1
titanic['sex'] = titanic['sex'].map({'male': 0, 'female': 1})

# Encode 'embarked' column: S -> 0, C -> 1, Q -> 2
titanic['embarked'] = titanic['embarked'].map({'S': 0, 'C': 1, 'Q': 2})

# Encode 'who' column: man -> 0, woman -> 1, child -> 2
titanic['who'] = titanic['who'].map({'man': 0, 'woman': 1, 'child': 2})

# Encode 'class' column: First -> 1, Second -> 2, Third -> 3
titanic['class'] = titanic['class'].map({'First': 1, 'Second': 2, 'Third': 3})

# Encode 'deck' column: A -> 0, B -> 1, C -> 2, ..., G -> 6
titanic['deck'] = titanic['deck'].map({'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6})

# Drop 'alive' and 'adult_male' columns as they are not useful for correlation analysis
titanic = titanic.drop(columns=['alive', 'adult_male'])

# Pairplot visualization
sns.pairplot(titanic, diag_kind='kde')
plt.show()

# Correlation heatmap
# Select only numerical columns
numerical_columns = titanic.select_dtypes(include=['float64', 'int64'])

# Plotting the heatmap with the numerical columns
plt.figure(figsize=(10, 8))
sns.heatmap(numerical_columns.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap of Titanic Dataset')
plt.show()
