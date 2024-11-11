import config
from typing import List
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

from data_loader import DataLoader
from model import Issue


class FourthAnalysis:
    def __init__(self):
        """
        Constructor
        """

        self.USER = config.get_parameter('user')

    def run(self):
        """
        Run the analysis for Frequency of Issues per Year.
        """
        issues: List[Issue]=DataLoader().get_issues()
        # Convert issues into a DataFrame for easier manipulation
        issues_data =[{
            'number':issue.number,
            'created_date':issue.created_date,
            'state':issue.state
        } for issue in issues]
        issues_df=pd.DataFrame(issues_data)
        issue_counts_per_year=Counter(pd.to_datetime(issues_df['created_date']).dt.year.dropna())
        years=sorted(issue_counts_per_year.keys())
        counts=[issue_counts_per_year[year] for year in years]
        # Create a figure for the plot
        plt.figure(figsize=(12,6))

        # Plot Frequency of Issues per Year
        plt.bar(years, counts, color='skyblue')
        plt.title('Frequency of Issues per Year')
        plt.xlabel('Year')
        plt.ylabel('Number of Issues')
        for i, count in enumerate(counts):
            plt.text(years[i],count,str(count),ha='center',va='bottom')
        plt.tight_layout()
        plt.show()