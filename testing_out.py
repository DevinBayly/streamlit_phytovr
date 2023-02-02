import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
import random
import os
import pandas as  pd 
import seaborn
print(os.getcwd())
# st.write("ID of plant")
plant_name= st.text_input("")
print("given name",plant_name)
df = pd.read_csv("s10_flir_rgb_clustering_v4.csv")
print("filtering")
print(df["plant_name"].str.contains(plant_name))
df["fahrenheit"] = (df["roi_temp"] - 273.15) * 9/5 + 32
df.sort_values(by=["date"],inplace=True)
filtered = df[df["plant_name"].str.contains(plant_name).fillna(False)]
# filtered = df[df["plant_name"].str.contains(plant_name)]
# print()
# print(filtered)
# print()
# st.write(df)
# st.write("result")
# st.write(filtered)

def generate_ridge_plot(df,filtered):
    sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})

    # Create the data
    rs = np.random.RandomState(1979)
    x = df["fahrenheit"]
    g = df["date"]
    df = pd.DataFrame(dict(fahrenheit=x, g=g))
    # df["x"] += m

    # Initialize the FacetGrid object
    pal = sns.cubehelix_palette(10, rot=-.25, light=.7)
    g = sns.FacetGrid(df, row="g", hue="g", aspect=15, height=.5, palette=pal)

    # Draw the densities in a few steps
    g.map(sns.kdeplot, "fahrenheit",
        bw_adjust=.5, clip_on=False,
        fill=True, alpha=1, linewidth=1.5)
    g.map(sns.kdeplot, "fahrenheit", clip_on=False, color="w", lw=2, bw_adjust=.5)

    # passing color=None to refline() uses the hue mapping

    g.refline(y=0, linewidth=2, linestyle="-", color=None, clip_on=False)
    # Sarah's idea is to go over axes and provide a refline

    subplot_height = g.figure.get_figheight()
    # # Define and use a simple function to label the plot in axes coordinates
    def label(x, color, label):
        print("label is",label,"date is",filtered["date"].to_numpy())
        ax = plt.gca()
        ax.text(0, .2, label, fontweight="bold", color=color,
                ha="left", va="center", transform=ax.transAxes)
        # add a vertical line for the plant data here
        ind = filtered["date"].to_numpy() == label
        ind = np.where(ind ==True)
        if (len(ind[0])> 0):
            print(ind)
            val = filtered.iloc[ind[0][0]]["fahrenheit"]

            plt.axvline(x=val,ymin =0 ,ymax =.75  ,color = "red")



    g.map(label, "fahrenheit")

    # Set the subplots to overlap
    g.figure.subplots_adjust(hspace=-.25)

    # Remove axes details that don't play well with overlap
    g.set_titles("")
    g.set(yticks=[], ylabel="")
    g.despine(bottom=True, left=True)
    st.pyplot(g)

def make_temp_line(df,filtered):
    ## just try to make a lineplot after with the filtered data in a new way
    f, ax = plt.subplots()
    # this causes tons and tons of slow downs because the page draws a giant legend
    # sns.scatterplot(df,x="date",y="fahrenheit",hue="genotype")
    # plt.hist2d(df["date"], df["fahrenheit"], bins=(300, 30), cmap=plt.cm.jet)
    sns.lineplot(filtered,x="date",y="fahrenheit")
    st.pyplot(f)

# make_temp_line(df,filtered)


st.write("## Selected Plant Canopy Temp over time")
generate_ridge_plot(df,filtered)
st.write("done")