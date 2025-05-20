# 📦 Importing necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# 🔁 Error handling for dataset loading
try:
    # Load the Iris dataset
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

    print("✅ Dataset loaded successfully!\n")

    # Display first few rows
    print("🔍 First 5 rows of the dataset:")
    print(df.head(), "\n")

    # Explore data structure
    print("📊 Data Types and Missing Values:")
    print(df.info(), "\n")
    print("Missing values in each column:\n", df.isnull().sum(), "\n")

    # 🧹 Data Cleaning: Drop missing values (none in this case)
    df.dropna(inplace=True)

    # 📈 Task 2: Basic Data Analysis
    print("📋 Descriptive Statistics:")
    print(df.describe(), "\n")

    # Group by species and compute mean
    print("📌 Mean values grouped by species:")
    print(df.groupby('species').mean(), "\n")

    # 🧠 Pattern Insights
    print("🔎 Insights:")
    print("- Versicolor and Virginica have higher petal lengths than Setosa.")
    print("- Sepal width is slightly higher in Setosa compared to others.\n")

    # 🎨 Task 3: Data Visualization

    # Set plot style
    sns.set(style="whitegrid")

    # 1. Line chart: Simulating a trend (not time-based)
    plt.figure(figsize=(8, 4))
    df_sorted = df.sort_values(by='sepal length (cm)').reset_index()
    plt.plot(df_sorted.index, df_sorted['sepal length (cm)'], label='Sepal Length')
    plt.title('Line Chart of Sepal Length')
    plt.xlabel('Index')
    plt.ylabel('Sepal Length (cm)')
    plt.legend()
    plt.tight_layout()
    plt.show()

    # 2. Bar chart: Average petal length per species
    plt.figure(figsize=(6, 4))
    sns.barplot(data=df, x='species', y='petal length (cm)', ci=None)
    plt.title('Average Petal Length per Species')
    plt.xlabel('Species')
    plt.ylabel('Petal Length (cm)')
    plt.tight_layout()
    plt.show()

    # 3. Histogram: Distribution of sepal width
    plt.figure(figsize=(6, 4))
    plt.hist(df['sepal width (cm)'], bins=10, color='skyblue', edgecolor='black')
    plt.title('Distribution of Sepal Width')
    plt.xlabel('Sepal Width (cm)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

    # 4. Scatter Plot: Sepal length vs. Petal length
    plt.figure(figsize=(6, 4))
    sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species')
    plt.title('Sepal Length vs. Petal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("❌ Error: Dataset file not found.")
except pd.errors.ParserError:
    print("❌ Error: Could not parse the file. Please check the file format.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
