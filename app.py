import streamlit as st
from model import train_model, predict_match

# ------------------ PAGE CONFIG ------------------

st.set_page_config(
    page_title="Premier League Match Predictor",
    page_icon="⚽",
    layout="centered"
)

# ------------------ STYLING ------------------

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    max-width:900px;
}

h1{
    text-align:center;
}

.stButton>button{
    width:100%;
    height:50px;
    font-size:18px;
    font-weight:bold;
    border-radius:10px;
}

div[data-baseweb="select"]{
    font-size:16px;
}

.score-box{
    border:2px solid #3b82f6;
    border-radius:15px;
    padding:30px;
    text-align:center;
    font-size:34px;
    font-weight:bold;
    margin-top:20px;
    margin-bottom:20px;
}

.small-text{
    text-align:center;
    color:gray;
}

</style>
""", unsafe_allow_html=True)

# ------------------ LOAD MODEL ------------------

@st.cache_resource
def load_model():
    train_model()

load_model()

# ------------------ TEAM LIST ------------------

teams = sorted([
    "Arsenal",
    "Aston Villa",
    "Bournemouth",
    "Brentford",
    "Brighton",
    "Burnley",
    "Cardiff",
    "Chelsea",
    "Crystal Palace",
    "Everton",
    "Fulham",
    "Huddersfield",
    "Hull",
    "Ipswich",
    "Leeds",
    "Leicester",
    "Liverpool",
    "Luton",
    "Man City",
    "Man United",
    "Middlesbrough",
    "Newcastle",
    "Norwich",
    "Nott'm Forest",
    "Sheffield United",
    "Southampton",
    "Stoke",
    "Sunderland",
    "Swansea",
    "Tottenham",
    "Watford",
    "West Brom",
    "West Ham",
    "Wolves"
])


st.title("Premier League Match Predictor")

st.markdown(
    "<p class='small-text'>Predict the final score of a Premier League match using a machine learning model trained on historical match data.</p>",
    unsafe_allow_html=True
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    home = st.selectbox("Home Team", teams)

with col2:
    away = st.selectbox("Away Team", teams)

st.write("")

if st.button("Predict Match"):

    if home == away:
        st.error("Please choose two different teams.")

    else:

        home_score, away_score = predict_match(home, away)

        st.divider()

        st.subheader("Prediction")

        st.markdown(
            f"""
            <div class="score-box">
                {home}<br><br>
                {home_score} - {away_score}<br><br>
                {away}
            </div>
            """,
            unsafe_allow_html=True
        )

        if home_score > away_score:
            st.success(f"Predicted Winner: {home}")

        elif away_score > home_score:
            st.success(f"Predicted Winner: {away}")

        else:
            st.info("Predicted Result: Draw")
