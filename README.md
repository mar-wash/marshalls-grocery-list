

# Grocery List Generator

This **Grocery List Generator** allows users to input recipes, specify what ingredients they already have, and generate a grocery list with the missing ingredients. The app saves recipes to a local file to ensure that your data persists between sessions.

## Features

- **Add Recipes**: Input the name of a recipe along with its ingredients.
- **Track Pantry Items**: Specify what ingredients you already have.
- **Generate Grocery List**: Select recipes to cook, and the app will generate a list of missing ingredients based on what you have in your pantry.
- **Persistent Storage**: All recipes are saved to a local `recipes.json` file so they are available across sessions.

## Requirements

- Python 3.7 or higher
- Streamlit

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/grocery-list-generator.git
cd grocery-list-generator
```

### 2. Install the required dependencies
Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # For Windows, use venv\Scripts\activate
```

Then install the required packages:
```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, you can install Streamlit directly:
```bash
pip install streamlit
```

### 3. Run the app locally
```bash
streamlit run grocery_list_app.py
```
Your app will open in your default browser at [http://localhost:8501](http://localhost:8501).

### 4. (Optional) Create a `requirements.txt` file
You can create a `requirements.txt` file to list all the Python dependencies:
```bash
pip freeze > requirements.txt
```

