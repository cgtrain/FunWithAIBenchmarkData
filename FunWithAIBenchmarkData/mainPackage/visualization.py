# File Name : visualization.py
# Student Name: Drew Wolfe
# email:  wolfeaw@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:  3/27/25
# Course #/Section:  4010-002
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Display an image and data visualization
# Brief Description of what this module does: Displays data visualization for a dataset
# Citations: https://chatgpt.com/ , https://mavenanalytics.io/data-playground

import pandas as pd
import matplotlib.pyplot as plt

def visualize_candy_popularity():
    try:
        # Load the dataset
        df = pd.read_csv("mainPackage/team_data/candy-data.csv")

        # Sort by winpercent and get top 10
        top_candies = df.sort_values(by="winpercent", ascending=False).head(10)

        # Plot
        plt.figure(figsize=(10, 6))
        plt.barh(top_candies['competitorname'], top_candies['winpercent'], color='orange')
        plt.xlabel("Win Percentage")
        plt.title("Top 10 Most Popular Candies")
        plt.gca().invert_yaxis()  # So highest is on top
        plt.grid(axis='x', linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print("Could not find 'candy-data.csv'. Check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
