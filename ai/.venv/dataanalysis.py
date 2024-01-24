import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from textblob import TextBlob
import spacy
from collections import defaultdict
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# nlp = spacy.load('en_core_web_sm')

data = pd.read_csv("articles.csv", encoding='latin-1')
# data = pd.read_csv("data.txt", encoding='latin-1')
print(data.head())



# Combine all titles into a single string
titles_text = ' '.join(data['Title'])

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles_text)

# Plot the Word Cloud
fig = px.imshow(wordcloud, title='Word Cloud of Titles')
fig.update_layout(showlegend=False)
fig.show()



# Sentiment Analysis
data['Sentiment'] = data['Article'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Sentiment Distribution
fig = px.histogram(data, x='Sentiment', title='Sentiment Distribution')
fig.show()