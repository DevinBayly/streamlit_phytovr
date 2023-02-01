import streamlit as st
from PIL import Image
import random
import pandas as  pd 

st.set_page_config(
    layout="wide",
    page_title="""
Demo data vis card
"""
)
st.header("""
Demo data vis card
""")

import numpy as np
def make_line_chart(col):
    with col:
        randdata = np.random.random((20,2))

        df = pd.DataFrame(data = randdata,columns=["x","y"])

        st.line_chart(df)
def make_map(col):
    with col:
        map_data = pd.DataFrame(
            np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
            columns=['lat', 'lon'])

        st.map(map_data)
    
def area_chart(col):
    with col:
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c'])

        st.area_chart(chart_data)

def bar_chart(col):
    with col:
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=["a", "b", "c"])

        st.bar_chart(chart_data)


def make_image(col):
    with col:
        image = Image.open('./test.png')

        st.image(image, caption='density plot')
# create three columns
kpi1, kpi2, kpi3 = st.columns(3)
firstrand= np.random.random(20)
plantsDisplayed= np.random.random()*2000
other= np.random.random()*200
# fill in those three columns with respective metrics or KPIs
kpi1.metric(
    label="Carbon Dioxide (ppm)",
    value=np.mean(firstrand),
    delta=np.mean(firstrand) - 10,
)

kpi2.metric(
    label="plants Displayed",
    value=int(plantsDisplayed),
)


kpi3.metric(
    label="Other research metrics",
    value=f"{round(other,2)} ",
)
# left_column, right_column = st.columns(2)
# # You can use a column just like st.sidebar:
# left_column.button('Press me!')

# # Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     chosen = st.radio(
#         'Sorting hat',
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     st.write(f"You are in {chosen} house!")

funcs =[
    make_line_chart,
    make_map,
    area_chart,
    bar_chart,
    make_image
]
col1,col2 = st.columns(2)
cols = [col1,col2]
for i in range(10):
    func = random.choice(funcs)
    col = cols[i%2]
    func(col)

