import pandas as pd
import random

# Read the data
data = pd.read_csv('imdb_top_1000.csv')

# Emotion and genres
fear = data[data['Genre'].str.contains('Horror')]
happy = data[data['Genre'].str.contains('Comedy')]
angry = data[data['Genre'].str.contains('Action')]
sad = data[data['Genre'].str.contains('Romance')]
surprise = data[data['Genre'].str.contains('Thriller')]
disgust = data[data['Genre'].str.contains('Crime')]
neutral = data[data['Genre'].str.contains('Adventure')]

# Return film with its info
def random_film(emotion):
    if emotion == 'fear':
        return fear.sample().values[0]
    elif emotion == 'happy':
        return happy.sample().values[0]
    elif emotion == 'angry':
        return angry.sample().values[0]
    elif emotion == 'sad':
        return sad.sample().values[0]
    elif emotion == 'surprise':
        return surprise.sample().values[0]
    elif emotion == 'disgust':
        return disgust.sample().values[0]
    elif emotion == 'neutral':
        return neutral.sample().values[0]
    else:
        return 'No emotion'  
