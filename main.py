import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

st.title("Sentiment Analysis Web App")

# User Input
user_text = st.text_area("Enter a review:")

if user_text:
    # Get sentiment score
    sentiment_scores = analyzer.polarity_scores(user_text)
    compound_score = sentiment_scores['compound']

    # Convert score to sentiment label
    def score_to_text(score):
        if score >= 0.05:
            return "Positive 😊"
        elif score <= -0.05:
            return "Negative 😞"
        else:
            return "Neutral 😐"

    sentiment = score_to_text(compound_score)

    # Display results
    
    st.write(f"**Sentiment:** {sentiment}")
    
