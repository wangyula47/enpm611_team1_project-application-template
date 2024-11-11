
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
 
        author_event_count = {} 
        
        for issue in issues:
            # print(issue.url)
            for event in issue.events:
                if event.author is not None:
                    if event.author not in author_event_count:
                        author_event_count[event.author] = 1 
                    else:
                        author_event_count[event.author] += 1 


        key_width = max(len(key) for key in author_event_count.keys())

        # Function to categorize keys based on alphabetical range
        def categorize_key(key):
            if 'A' <= key[0] <= 'G':
                return 'A-G'
            elif 'H' <= key[0] <= 'N':
                return 'H-N'
            elif 'O' <= key[0] <= 'T':
                return 'O-T'
            elif 'U' <= key[0] <= 'Z':
                return 'U-Z'
            else:
                return 'Other'

        # Group keys into alphabetical ranges
        grouped_keys = {
            'A-G': [],
            'H-N': [],
            'O-T': [],
            'U-Z': []
        }

        # Assign each key to its respective group
        for key in sorted(author_event_count.keys()):
            category = categorize_key(key)
            if category in grouped_keys:
                grouped_keys[category].append((key, author_event_count[key]))

        # Map numerical choices to alphabetical ranges
        choices = {
            1: 'A-G',
            2: 'H-N',
            3: 'O-T',
            4: 'U-Z'
        }

        # Display choices for the user
        print("Please select an alphabetical range of author usernames to view:")
        for num, label in choices.items():
            print(f"{num}. {label}")


        while True: 
            user_choice = int(input("Enter your choice (1, 2, 3, or 4): "))
            selected_category = choices.get(user_choice)
                
            if selected_category in grouped_keys:
                print(f"\nCategory: {selected_category}")
                print(f"{'No.':<3} | {'Author username':{key_width}} | Events")
                print("-" * (key_width + 15))  # separator line for readability

                for idx, (key, value) in enumerate(grouped_keys[selected_category], start=1):
                    print(f"{idx:<3} | {key:{key_width}} | {value:>5}")
                
                break
            else:
                print("Invalid choice. Please select a number between 1 and 4.")
            
        
        while True:
            user_selection = (input("Enter authors name or No. in list: "))
            try:
                # Check if input is an index
                selection_index = int(user_selection) - 1
                if 0 <= selection_index < len(grouped_keys[selected_category]):
                    selected_author = grouped_keys[selected_category][selection_index][0]
                    print("Event Author found: ", selected_author)
                    break
                else:
                    print("Invalid index. Please try again.")
            except ValueError:
                # Check if input matches an author name
                if any(user_selection == author[0] for author in grouped_keys[selected_category]):
                    print("Event Author found: ", user_selection)
                    selected_author = user_selection
                    break
                else:
                    print("Author not found in the selected category.")

        event_type_count = {}
        for issue in issues:
            for event in issue.events:
                if event.author == selected_author:

                    if event.event_type not in event_type_count:
                        event_type_count[event.event_type] = 1 
                    else:
                        event_type_count[event.event_type] += 1 

        #print(event_type_count)

        key_width = max(len(str(key)) for key in event_type_count.keys())
        value_width = max(len(str(value)) for value in event_type_count.values())
        
        # Header with column names
        print(f"{'No.':<3} | {'Event Type':{key_width}} | {'Count':{value_width}}")
        print("-" * (key_width + value_width + 10))  # separator line for readability

        # Print each key-value pair with an index
        for idx, (key, value) in enumerate(sorted(event_type_count.items()), start=1):
            print(f"{idx:<3} | {key:{key_width}} | {value:>{value_width}}")


if __name__ == '__main__':
    # Invoke run method when running this module directly
    FirstAnalysis().run()