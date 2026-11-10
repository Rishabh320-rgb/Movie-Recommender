import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Load the movies
movies = pd.read_csv("movies.csv")

# 2. Make genres readable for the computer: "Comedy|Romance" -> "Comedy Romance"
movies["genres"] = movies["genres"].str.replace("|", " ", regex=False)

# 3. Turn genres into numbers (1 = movie has this genre, 0 = it doesn't)
cv = CountVectorizer()
matrix = cv.fit_transform(movies["genres"])


# 4. The function: give a movie name, get 5 similar movies
def recommend(title, n=5):
    matches = movies[movies["title"].str.contains(title, case=False, regex=False)]
    if matches.empty:
        return ["Movie not found"]
    idx = matches.index[0]
    scores = cosine_similarity(matrix[idx], matrix).flatten()
    top = scores.argsort()[::-1][1:n + 1]
    return movies["title"].iloc[top].tolist()


# 5. Test it
print("Because you liked Toy Story:")
for m in recommend("Toy Story"):
    print("-", m)