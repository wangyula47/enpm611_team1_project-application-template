
from typing import List
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter


from data_loader import DataLoader
from model import Issue,Event
import config

class FirstAnalysis:

    def __init__(self):
        """
        Constructor
        """
        # Parameter is passed in via command line (--user)
        self.USER:str = config.get_parameter('user')

    def run(self):
    
        """
        Starting point for this analysis.
        
        Note: this is just an example analysis. You should replace the code here
        with your own implementation and then implement two more such analyses.
        """


        issues:List[Issue] = DataLoader().get_issues()    

        event_label_counter = {}    
        

        # view label frequnecies, exclude events with no label (none)
        for issue in issues:
            # print(issue.url)
            for event in issue.events:
                if event.label is not None:
                    if event.label in event_label_counter.keys():
                        event_label_counter[event.label] += 1  
                    else:
                        event_label_counter[event.label] = 1 


        # print(event_label_counter)
            # Convert the dictionary to a pandas DataFrame
        df = pd.DataFrame.from_dict(event_label_counter, orient='index', columns=['frequency'])

        # Plot the DataFrame as a bar chart
        df.plot(kind='bar')

        # Add a title and labels
        plt.title('Frequency Distribution')
        plt.xlabel('Item')
        plt.ylabel('Frequency')

        # Show the plot
        plt.show()

        event_type_counter = {} 

        # search across eventypes that are unlabeled 
        for issue in issues:
            # print(issue.url)
            for event in issue.events:
                
                if event.label is None:
                    if event.event_type in event_type_counter.keys():
                        event_type_counter[event.event_type] += 1  
                    else:
                        event_type_counter[event.event_type] = 1 


        #print(event_type_counter)

        df = pd.DataFrame.from_dict(event_type_counter, orient='index', columns=['frequency'])

        # Plot the DataFrame as a bar chart
        df.plot(kind='bar')

        # Add a title and labels
        plt.title('Frequency Distribution')
        plt.xlabel('Item')
        plt.ylabel('Frequency')

        # Show the plot
        plt.show()
        


if __name__ == '__main__':
    # Invoke run method when running this module directly
    FirstAnalysis().run()