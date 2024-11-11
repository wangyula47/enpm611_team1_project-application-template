from collections import Counter
from typing import List
import config
import matplotlib.pyplot as plt
from data_loader import DataLoader
from model import Issue


class Second_analysis:
    def __init__(self):
        """
        Constructor
        """
        # Parameter is passed in via command line (--user)
        self.USER:str = config.get_parameter('user')

    def run(self):
        issues:List[Issue] = DataLoader().get_issues()
        bug_creators = []
        for issue in issues:
            for event in issue.events:
                if event.event_type == 'commented': 
                    bug_creators.append(event.author)
           
        # Get the top 50 bug creators
        bug_creator_counts = Counter(bug_creators)
        top_50_creators = bug_creator_counts.most_common(50)

        # Prepare data for plotting
        creators, counts = zip(*top_50_creators) if top_50_creators else ([], [])

        # Create the bar plot
        plt.figure(figsize=(15, 10))
        bars = plt.bar(creators, counts)
        plt.title('Top 50 Commenters')
        plt.xlabel('Creator')
        plt.ylabel('Number of Comments')
        plt.xticks(rotation=90)

        # Add frequency count on top of each bar
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height}',
                    ha='center', va='bottom')

        plt.tight_layout()

        # Show the plot
        plt.show()