
<h1 align="center">Fake News Detection using LSTM in Flask</h1>
<p align=center>
<a href="https://udhay86kumar.github.io/Fake-News-Detection/">click here to visit website</a>
</p>
## Fake News Detection using LSTM in Flask
This project implements a web application for fake news detection using LSTM (Long Short-Term Memory) neural networks. The application is built using the Flask framework, allowing users to input news articles and get predictions on whether they are fake or real.

## Dataset

The project utilizes a dataset of labeled news articles as either fake or real. The dataset can be obtained from [source link :https://www.kaggle.com/c/fake-news/data#]. 
## Preprocessing

Before training the LSTM model, the dataset undergoes several preprocessing steps:

1. Text cleaning: Remove unnecessary characters, symbols, and URLs from the text.
2. Tokenization: Split the text into individual words or tokens.
3. Padding: Ensure all input sequences have the same length by adding padding tokens.
4. Word embedding: Convert the words into dense vectors to capture semantic meaning.

## LSTM Model

The LSTM model architecture consists of the following layers:

1. Embedding layer: Maps the input tokens to dense vectors.
2. LSTM layer: Processes the sequential input and captures long-term dependencies.
3. Dense layer: Performs the final classification based on the learned representations.
4. Output layer: Produces the probability of the input being fake or real news.

## Flask Application

The Flask application allows users to input news articles through a web form. The input articles are preprocessed using the same steps mentioned above. The preprocessed text is then passed through the trained LSTM model to obtain the predicted label. The result is displayed to the user on the web page.

## Usage

To use the fake news detection web application:

1. Install the required dependencies mentioned in `requirements.txt`.
2. Load the trained LSTM model from the saved model weights.
3. Run the Flask application using the command `python app.py`.
4. Access the application through a web browser at the provided URL.
5. Enter a news article in the input form and submit it.
6. The application will display the predicted label (fake or real) for the input article.

## Deployment

The application can be deployed to a hosting platform or cloud service provider to make it accessible to users over the internet. Common options for deployment include Heroku, AWS, or Azure. Refer to the respective documentation for instructions on deploying Flask applications.

## Conclusion

Fake news detection using LSTM in Flask provides a user-friendly and accessible way to identify and combat the spread of misinformation. The LSTM model's ability to capture sequential dependencies makes it effective in analyzing text data and making accurate predictions.


