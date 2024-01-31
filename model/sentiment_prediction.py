from transformers import pipeline

# Initialize the sentiment analysis model from the transformers library
CLASSIFIER_SENTIMENT = pipeline("sentiment-analysis")

def sentiment_analysis(text):
    """Sentiment prediction

    Args:
        The text to be classified

    Returns:
        Prediction: Prediction with the label and score
    """
    # Use the sentiment analysis model to predict sentiment for the input text
    sentiment_prediction = CLASSIFIER_SENTIMENT(text)

    # Return the label and score from the prediction result

    return sentiment_prediction[0]