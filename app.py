import streamlit as st
from utils.api_utils import search_recipes

SPOONACULAR_API_KEY = "67ad3dd831b447a096e38d3220ea710c"

st.title('Recipe Finder')
st.write('Enter an ingredient and find some tasty recipes!')

# Input for the ingredient
ingredient = st.text_input('Enter an ingredient:')

# When the search button is pressed
if st.button('Search'):
    if ingredient:
        recipes = search_recipes(SPOONACULAR_API_KEY, ingredient)
        if recipes:
            st.write(f"Recipes found with {ingredient}:")
            for recipe in recipes:
                st.write(f"**{recipe['title']}**")
                st.image(recipe['image'], width=200)
        else:
            st.write('No recipes found. Try another ingredient.')
