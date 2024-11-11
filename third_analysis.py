from typing import List
import matplotlib.pyplot as plt
import pandas as pd
import config
from data_loader import DataLoader
from model import Issue, Event
from collections import Counter
import numpy as np

class ThirdFeatureAnalysis:
    """
    Implements an analysis of GitHub issues that outputs the result of that analysis.
    """
    
    def __init__(self):
        """
        Constructor
        """
        # Initialize configuration and data loader
        config._init_config()
        self.issues: List[Issue] = DataLoader().get_issues()
        # self.output_path = "/Users/wangyu/Desktop/ENPM611_group_project/enpm611_team1_project-application-template" 

    def run(self):
        """
        Starting point for this analysis.
        """
        self.analyze_event_impact_on_resolution_time()

    def analyze_event_impact_on_resolution_time(self):
        """
        Analyzes how specific events impact the time taken to resolve issues, providing insights into what actions are most effective.
        """
        event_impact_data = []

        for issue in self.issues:
            if issue.state in ['closed', 'open']:  # Considering both closed and open issues
                # Extract the event types and their timestamps
                event_types = [event.event_type for event in issue.events if event.event_type]
                event_dates = [event.event_date for event in issue.events if event.event_date]
                
                # Ensure event_types and event_dates have the same length
                if len(event_types) != len(event_dates):
                    continue
                
                if issue.created_date:
                    resolution_time = (issue.updated_date - issue.created_date).days if issue.updated_date else None
                    
                    # Check if certain key events like 'labeled' or 'assigned' occurred early or late in the process
                    labeled_time = None
                    assigned_time = None
                    for i, event in enumerate(event_types):
                        if event == 'labeled' and labeled_time is None:
                            labeled_time = (event_dates[i] - issue.created_date).days
                        elif event == 'assigned' and assigned_time is None:
                            assigned_time = (event_dates[i] - issue.created_date).days
                    
                    event_impact_data.append({
                        'resolution_time': resolution_time if resolution_time is not None else float('nan'),
                        'labeled_time': labeled_time if labeled_time is not None else float('nan'),
                        'assigned_time': assigned_time if assigned_time is not None else float('nan')
                    })
        
        # Convert to DataFrame for analysis
        event_impact_df = pd.DataFrame(event_impact_data)
        
        # Ensure columns exist before attempting to drop NaNs
        if 'labeled_time' in event_impact_df.columns:
            labeled_df = event_impact_df.dropna(subset=['labeled_time'])
            if not labeled_df.empty:
                # Plot the impact of 'labeled' time on resolution time
                plt.figure(figsize=(12, 6))
                plt.scatter(labeled_df['labeled_time'], labeled_df['resolution_time'], color='orange', alpha=0.6)
                plt.title('Impact of Labeling Time on Issue Resolution Time')
                plt.xlabel('Days Since Creation to Labeling')
                plt.ylabel('Resolution Time (Days)')
                plt.tight_layout()
                plt.savefig(f"{self.output_path}/impact_of_labeling_time.png")
                plt.show()
            else:
                print("No labeled events available for plotting.")
        else:
            print("No labeled events found in the data.")
        
        if 'assigned_time' in event_impact_df.columns:
            assigned_df = event_impact_df.dropna(subset=['assigned_time'])
            if not assigned_df.empty:
                # Plot the impact of 'assigned' time on resolution time
                plt.figure(figsize=(12, 6))
                plt.scatter(assigned_df['assigned_time'], assigned_df['resolution_time'], color='green', alpha=0.6)
                plt.title('Impact of Assignment Time on Issue Resolution Time')
                plt.xlabel('Days Since Creation to Assignment')
                plt.ylabel('Resolution Time (Days)')
                plt.tight_layout()
                plt.savefig(f"{self.output_path}/impact_of_assignment_time.png")
                plt.show()
            else:
                print("No assigned events available for plotting.")
        else:
            print("No assigned events found in the data.")

if __name__ == "__main__":
    # Invoke run method when running this module directly
    ThirdFeatureAnalysis().run()
