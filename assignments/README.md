# Web Services and Applications

by Oksana Abrosimova

This repository contains a set of Jupyter Notebooks created as part of the *Web Services and Applications* module. The notebooks include practical assignments designed to demonstrate skills in retrieving data from external sources, working with various data formats and retrieving and processing data through API.

## Contents

| Notebook | Description |
|---------|-------------|
| assignment01-deals.ipynb | Write a program that deals 5 cards, prints out their value and suit using API |
| assignment03-cso.ipynb | Retrieve a dataset from CSO and store it into a JSON file |
| assignment04-github.ipynb | Read a file from a repository, replace instances of text with another keyword, commit and push the file back to the repository |

## Requirements

### Software
- **Python 3.10+** — required to run the scripts and notebooks  
  Install from: https://www.python.org  
- **Jupyter Notebook** (or VS Code + Jupyter extension)  
  Installation instructions: https://jupyter.org/install

### Python Packages
All required packages are imported within each respective notebook: 
- `requests`: retrieving data from API's
- `json`: handling JSON data
- `base64`: encoding/decoding content for API requests

### Authentication

Some notebooks require API authentication. API keys are stored in a separate file (`config.py`) which is not included in this repository.

You will need to create your own file with the required keys, for example:

```python
API_KEY = "your_api_key_here"
```