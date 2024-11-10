# GitHub Issue Analysis Project

This project aims to analyze GitHub issues using data loaded from a JSON file (`poetry_issues.json`). The analysis explores various metrics of GitHub issues, such as the impact of specific events on issue resolution, the most common labels, and frequent word occurrences in issue descriptions.

The repository includes several Python scripts, each performing a unique analysis, and utility functions that help load, configure, and model the data for use in these analyses.

## File Descriptions

- `config.json`: Contains configuration details, such as the path to the dataset file (`poetry_issues.json`). The data path is referenced in other modules to load the issue data.
- `config.py`: Manages the loading of configuration settings, allowing easy access to parameters specified in `config.json`. You can extend this to add more configuration options as needed.
- `data_loader.py`: Defines a `DataLoader` class responsible for loading GitHub issues from the specified JSON file. It loads the issues into memory and provides access to the data in the form of Python objects.
- `model.py`: Defines data models (`Issue` and `Event`) used to represent GitHub issues and their associated events. The data models make it easy to access and manipulate issue data.
- `example_analysis.py`: Provides an example analysis that examines the top creators of issues. This serves as a starting point for implementing additional analyses.
- `third_analysis.py`: Implements an analysis to explore the impact of certain events on issue resolution time. It generates scatter plots showing the relationship between event occurrences and resolution time.
- `run.py`: This script serves as the main entry point to execute the analyses. It allows users to select which analysis to run using command line arguments.
- `requirements.txt`: Lists the dependencies needed to run the project. Install these dependencies before running the scripts.

## Setup

To get started, clone this repository to your local computer and set up your environment as described below.

### Install Dependencies

In the root directory of the project, create a virtual environment, activate it, and install the required dependencies by running the following command:

```sh
pip install -r requirements.txt
```

### Download and Configure the Data File

Download the data file (`poetry_issues.json`) and update the `config.json` with the correct path to the file. Alternatively, you can specify an environment variable (`ENPM611_PROJECT_DATA_PATH`) with the same value to avoid hardcoding the path.

### Run an Analysis

With everything set up, you can run the analyses provided in the project. For example, to run the third analysis:

```sh
python run.py --feature 3
```

This command runs the analysis described in `third_analysis.py` and produces relevant output and visualizations.

## VS Code Run Configuration

To make development easier, runtime configurations are provided to run each of the analyses. When you click the run button in the left-hand side toolbar of VS Code, you can select any of the analyses to run or simply run the currently opened file. This setup makes debugging more convenient.

The run configuration is specified in `.vscode/launch.json`, which you can modify as needed. The `.vscode/settings.json` file also customizes the VS Code interface slightly to make navigation and debugging easier, but you can remove or modify those settings according to your preference.

## Example Analysis

- **Third Analysis (`third_analysis.py`)**: Analyzes how specific events (e.g., labeling or assigning) impact the resolution time of GitHub issues. It generates scatter plots showing the relationship between event occurrence and resolution time.
- **Example Analysis (`example_analysis.py`)**: Examines the top creators of GitHub issues and displays a bar chart showing their contributions.

## Notes

- Ensure that the dataset file (`poetry_issues.json`) is located in the correct path as specified in `config.json`.
- You can modify `config.json` if your dataset is located elsewhere.

## Editing in VS Code

To edit and run the files in VS Code:

1. **Open Project Folder**: Open the project folder in VS Code by selecting `File > Open Folder...`.
2. **Locate and Edit Files**: Click on any file in the Explorer pane on the left to open it for editing.
3. **Run the Analysis**: Use the integrated terminal or the run configurations to execute the analysis scripts.

Feel free to expand upon the example analyses and create more insightful visualizations of the GitHub issues data!