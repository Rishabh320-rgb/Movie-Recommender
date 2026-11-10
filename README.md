# Movie Recommender

A web app that suggests similar movies based on genres.

## How it works
- Each movie's genres are converted into numbers
- Cosine similarity finds the closest movies to your pick
- Streamlit shows the results as a web page

## Run it
pip install -r requirements.txt
streamlit run app.py

## Tech used
Python, pandas, scikit-learn, Streamlit

## Dataset
MovieLens (GroupLens Research, University of Minnesota)
