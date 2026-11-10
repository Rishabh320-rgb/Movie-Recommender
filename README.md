# 🎬 Movie Recommender

A web app that recommends similar movies based on genres. Built with Python, scikit-learn and Streamlit.

## 📌 Overview
🔗 **Live demo:** https://movie-recommender-3spmnjubpq6qxsl6m9skha.streamlit.app/

*(If the app is asleep, click "Yes, get this app back up!" and wait about 30 seconds.)*
Pick a movie you like and the app suggests similar ones, ranked by a match percentage. It uses content-based filtering: movies are compared by their genres.

## 📊 Project at a Glance
| Metric | Value |
|---|---|
| Movies in dataset | 9,742 |
| Unique genres | 19 |
| Release years covered | 1902 to 2018 |
| Average genres per movie | 2.3 |
| Recommendations per search | 3 to 12 (adjustable) |
| Technique | Content-based filtering (cosine similarity) |

## ✨ Features
- Search or choose from 9,742 movies
- Adjustable number of recommendations (3 to 12)
- Genre filter for the results
- Result cards with title, year and genre tags
- Match percentage bar for each recommendation

## ⚙️ How It Works
1. **Load:** read `movies.csv` with pandas.
2. **Convert:** turn each movie's genres into numbers (1 = has the genre, 0 = does not) using CountVectorizer.
3. **Compare:** calculate cosine similarity between the chosen movie and all other movies.
4. **Rank:** show the highest-scoring movies as cards.

## 🛠️ Tech Stack
| Tool | Use |
|---|---|
| Python | Main language |
| pandas | Data loading and cleaning |
| scikit-learn | CountVectorizer, cosine similarity |
| Streamlit | Web interface |

## 📁 Project Structure
```
Movie-Recommender/
├── app.py              # Streamlit web app
├── recommender.py      # Command-line version
├── movies.csv          # Movie data (MovieLens)
├── requirements.txt    # Dependencies
└── README.md
```

## 🚀 Run Locally
```
pip install -r requirements.txt
streamlit run app.py
```
Then open http://localhost:8501 in your browser.

## 🔮 Future Improvements
- Movie posters using the TMDB API
- Collaborative filtering using user ratings
- Hybrid model combining both methods

## 📊 Dataset
[MovieLens](https://grouplens.org/datasets/movielens/) (ml-latest-small), provided by GroupLens Research, University of Minnesota.

##Note
Live demo: <your-app-link>
(If the app is asleep, click "Yes, get this app back up!" and wait about 30 seconds.)

## 👤 Author
**Rishabh Shukla**
[GitHub](https://github.com/Rishabh320-rgb) · [LinkedIn](https://www.linkedin.com/in/rishabh-shukla-4673323a2)
