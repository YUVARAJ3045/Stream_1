import streamlit
import pandas as pd

streamlit.title('Hi Sushmitha')

streamlit.header('Breakfast Menu')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text( '🥑🍞 Avacoda Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit') #seting index as fruit


# Let's put a pick list here so they can pick the fruit they want to include 
fruit_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruit_selected]

if len(fruits_to_show)>0:
  streamlit.dataframe(fruits_to_show)#display all fruit list
streamlit.dataframe(my_fruit_list)#display selected fruit list
