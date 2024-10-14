# PRODIGY_DS_02

This project explores the famous Titanic dataset, performing Exploratory Data Analysis (EDA) to uncover insights and patterns related to passenger survival rates and other key factors.

## Project Overview

The goal is to:
- Clean and preprocess the Titanic dataset.
- Analyze relationships between key variables such as survival rate, passenger class, gender, and age.
- Visualize the data using various charts (heatmaps, bar plots, pair plots) to reveal trends and correlations.

## Installation and Setup

### 1. Clone the Repository

First, clone the project repository to your local machine using the command:

git clone https://github.com/SiriNadig/PRODIGY_DS_02.git

### 2. Navigate to the Project Directory
Move into the cloned project folder: cd titanic-eda

### 3. Create and Activate a Virtual Environment
Create a virtual environment to isolate dependencies: python3 -m venv .venv

Activate the virtual environment:
For MacOS/Linux: source .venv/bin/activate
For Windows: .venv\Scripts\activate

### 4. Install Required Dependencies
Install the necessary Python packages listed in the requirements.txt file: pip install -r requirements.txt

### 5. Running the Project
Once the setup is complete, you can run the project by executing the following command: python titanic.py

## Visualizations

The project generates various visualizations, including:

Heatmap: Shows correlations between numerical variables like age, fare, and survival status.
Bar Plots: Compares survival rates based on passenger class and gender.
Pair Plots: Provides a pairwise relationship view of multiple variables.

## Dataset
The Titanic dataset used in this project is sourced from Seaborn's built-in datasets. It includes key information such as:
Passenger class (Pclass)
Gender (Sex)
Age
Fare
Survival status (Survived)


