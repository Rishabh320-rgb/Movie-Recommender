import html
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

# ---------- Styling ----------
st.markdown("""
<style>
.hero {
    background: linear-gradient(135deg, #141e30 0%, #243b55 50%, #e50914 140%);
    padding: 2.5rem 2rem; border-radius: 18px; margin-bottom: 1.5rem;
}
.hero h1 { color: #ffffff; font-size: 2.6rem; margin: 0; }
.hero p { color: #d6e0f0; font-size: 1.1rem; margin: 0.4rem 0 0 0; }
.card {
    background: linear-gradient(160deg, #1c1f2b, #2a2f45);
    border: 1px solid #3a4060; border-radius: 16px;
    padding: 1.2rem; margin-bottom: 1rem; min-height: 190px;
    transition: transform 0.2s, border-color 0.2s;
}
.card:hover { transform: translateY(-5px); border-color: #e50914; }
.rank { color: #e50914; font-weight: 700; font-size: 0.85rem; letter-spacing: 1px; }
.mtitle { color: #ffffff; font-size: 1.15rem; font-weight: 700; margin: 0.3rem 0; }
.year { color: #9aa4c0; font-size: 0.9rem; }
.chip {
    display: inline-block; background: #343b5a; color: #e8ecf8;
    padding: 2px 10px; border-radius: 999px; font-size: 0.75rem; margin: 3px 4px 0 0;
}
.bar { background: #343b5a; border-radius: 999px; height: 8px; margin-top: 12px; }
.fill { background: linear-gradient(90deg, #ff6b6b, #e50914); height: 8px; border-radius: 999px; }
.match { color: #9aa4c0; font-size: 0.8rem; margin-top: 4px; }
.footer { text-align: center; color: #8a93ad; font-size: 0.85rem; margin-top: 2rem; }
</style>
""", unsafe_allow_html=True)


# ---------- Data ----------
@st.cache_data
def load_data():
    movies = pd.read_csv("movies.csv")
    movies["year"] = movies["title"].str.extract(r"\((\d{4})\)\s*$")[0]
    movies["name"] = movies["title"].str.replace(r"\s*\(\d{4}\)\s*$", "", regex=True)
    movies["genre_list"] = movies["genres"].str.split("|")
    text = movies["genres"].str.replace("|", " ", regex=False)
    matrix = CountVectorizer().fit_transform(text)
    return movies, matrix


movies, matrix = load_data()
all_genres = sorted({g for lst in movies["genre_list"] for g in lst
                     if g != "(no genres listed)"})


def recommend(idx, n, genre):
    scores = cosine_similarity(matrix[idx], matrix).flatten()
    results = []
    for i in scores.argsort()[::-1]:
        if i == idx:
            continue
        if genre != "Any" and genre not in movies["genre_list"].iloc[i]:
            continue
        results.append((i, scores[i]))
        if len(results) == n:
            break
    return results


def card(rank, i, score):
    row = movies.iloc[i]
    chips = "".join(f'<span class="chip">{html.escape(g)}</span>'
                    for g in row["genre_list"])
    year = row["year"] if pd.notna(row["year"]) else ""
    pct = int(score * 100)
    return (
        '<div class="card">'
        f'<div class="rank">#{rank}</div>'
        f'<div class="mtitle">{html.escape(row["name"])}</div>'
        f'<div class="year">{year}</div>'
        f'<div>{chips}</div>'
        f'<div class="bar"><div class="fill" style="width:{pct}%"></div></div>'
        f'<div class="match">{pct}% match</div>'
        '</div>'
    )


# ---------- Sidebar ----------
st.sidebar.header("⚙️ Settings")
n = st.sidebar.slider("How many recommendations?", 3, 12, 6)
genre = st.sidebar.selectbox("Only show this genre", ["Any"] + all_genres)
st.sidebar.caption("Tip: pick a genre to narrow the results.")

# ---------- Main page ----------
st.markdown("""
<div class="hero">
<h1>🎬 Movie Recommender</h1>
<p>Pick a movie you love and discover similar ones.</p>
</div>
""", unsafe_allow_html=True)

choice = st.selectbox("🔍 Search or choose a movie", movies["title"].tolist())

if st.button("✨ Recommend", type="primary"):
    idx = movies.index[movies["title"] == choice][0]
    results = recommend(idx, n, genre)
    st.subheader(f"Because you liked {choice}")
    if not results:
        st.warning("No movies found. Try a different genre.")
    cols = st.columns(3)
    for k, (i, score) in enumerate(results):
        with cols[k % 3]:
            st.markdown(card(k + 1, i, score), unsafe_allow_html=True)

st.markdown('<div class="footer">Built with Python and Streamlit · '
            'Data: MovieLens</div>', unsafe_allow_html=True)