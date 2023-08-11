import streamlit as st
import glob
from nltk.sentiment import SentimentIntensityAnalyzer
from pathlib import Path
import plotly.express as px


analyzer = SentimentIntensityAnalyzer()
filepaths = glob.glob("diary/*.txt")
filenames = []
positve_scores = []
negative_scores = []

for filepath in filepaths:
    filenames.append(Path(filepath).stem)
    with open(filepath, 'r') as file:
        text = file.read()


    score = analyzer.polarity_scores(text)
    positve_scores.append(score['pos'])
    negative_scores.append(score['neg'])


st.header("Diary Tone")
st.subheader("Positivity")
fig = px.line(x=filenames, y=positve_scores, labels={"x": "Dates", "y": "Positivity"})
st.plotly_chart(fig)
st.subheader("Negativity")
fig = px.line(x=filenames, y=negative_scores, labels={"x": "Dates", "y": "Negativity"})
st.plotly_chart(fig)