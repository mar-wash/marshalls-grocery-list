import streamlit as st

import streamlit as st
import json
import os

RECIPE_FILE = "recipes.json"

# --- Helper Functions ---
def load_recipes():
    if os.path.exists(RECIPE_FILE):
        with open(RECIPE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_recipes(recipes):
    with open(RECIPE_FILE, "w") as f:
        json.dump(recipes, f, indent=2)

# --- Initialize Recipes ---
if "recipes" not in st.session_state:
    st.session_state.recipes = load_recipes()

# --- Title ---
st.title("Marshall's Grocery List Generator")

# --- Add Recipes ---
st.header("Add a Recipe")
recipe_name = st.text_input("Recipe Name")
ingredients_input = st.text_area("Ingredients (comma-separated)", placeholder="e.g., eggs, flour, sugar")

if st.button("Add Recipe"):
    if recipe_name and ingredients_input:
        ingredients = [i.strip().lower() for i in ingredients_input.split(",")]
        st.session_state.recipes[recipe_name] = ingredients
        save_recipes(st.session_state.recipes)  # Persist to file
        st.success(f"Added recipe: {recipe_name}")
    else:
        st.warning("Please provide both a name and ingredients.")

# --- Pantry Items ---
st.header("What Do You Already Have?")
pantry_input = st.text_area("Pantry Items (comma-separated)", placeholder="e.g., eggs, milk")
pantry = [i.strip().lower() for i in pantry_input.split(",") if i.strip()]

# --- Select Recipes to Cook ---
st.header("What Do You Want to Make?")
selected_recipes = st.multiselect("Select Recipes", list(st.session_state.recipes.keys()))

# --- Grocery List Output ---
if st.button("Generate Grocery List"):
    needed = set()
    for recipe in selected_recipes:
        needed.update(st.session_state.recipes[recipe])

    grocery_list = needed - set(pantry)

    st.subheader("🛒 Your Grocery List")
    if grocery_list:
        for item in sorted(grocery_list):
            st.markdown(f"- {item}")
    else:
        st.success("You already have everything you need!")

# Debug: View all recipes
with st.expander("📂 View All Recipes"):
    st.json(st.session_state.recipes)

