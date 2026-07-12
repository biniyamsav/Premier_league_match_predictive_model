# Premier League Match Predictor ⚽

A machine learning model that predicts Premier League match scorelines using 10 seasons of historical match data. Built with Python, scikit-learn, and Streamlit.

---

## What It Does

The user selects a home team and an away team from a dropdown. The model predicts the final scoreline and announces the predicted winner. For example: Liverpool vs Burnley → **2 - 1, Liverpool win**.

---

## How It Works

1. **Data** — 10 seasons of Premier League match data (E0.csv through E0(9).csv) sourced from football-data.co.uk. Each file contains match stats including shots, fouls, corners, cards, and betting odds from three bookmakers (Bet365, Betway, Pinnacle).

2. **Feature Engineering** — Team names are one-hot encoded using `pd.get_dummies`. For a new prediction, each team's historical average stats are calculated from their past matches — home stats for the home team, away stats for the away team. Betting odds are averaged across both teams' historical records.

3. **Model** — Multi-output Linear Regression predicting both FTHG (home goals) and FTAG (away goals) simultaneously.

4. **UI** — Streamlit app with dropdown team selectors and a styled score display.

---

## Model Performance

| Metric | Score |
|--------|-------|
| R² | 0.42 |
| MAE | 0.74 goals |
| MSE | 0.90 |

R² of 0.42 means the model explains 42% of the variation in goals scored — solid for football prediction where randomness is high.

---

## Key Findings

**Home advantage is real.** The model consistently predicts higher scores for home teams, which reflects the actual data — home teams win roughly 45% of Premier League matches historically.

**Scorelines cluster around the average.** Linear regression optimizes for the mean, so predictions tend to fall in the 1-2 goal range per team. It does not capture rare high-scoring outliers like 5-0 or 6-1. This is a known limitation of linear regression for count data.

**Shots on target are the strongest predictor.** When in-match stats are included, R² improves significantly — shots on target (HST, AST) carry the most signal. This is consistent with football analytics research showing expected goals (xG) are heavily shot-based.

---

## Limitations

- Linear regression predicts the statistical average. It cannot model rare high-scoring games.
- Historical averages are used for new match prediction — the model does not account for current form, injuries, or suspensions.
- A Poisson regression model would be more appropriate for goal prediction and is a planned improvement.

---

## Tech Stack

- Python 3.12
- pandas
- scikit-learn
- NumPy
- Streamlit

---

## Setup

```bash
git clone https://github.com/biniyamsav/Premier_league_match_predictive_model
cd Premier_league_match_predictive_model

python3 -m venv venv
source venv/bin/activate
pip install pandas scikit-learn numpy streamlit

streamlit run app.py
```

Make sure all 10 CSV files (E0.csv through E0(9).csv) are in the project root directory.

---

## Data Source

Match data sourced from [football-data.co.uk](https://www.football-data.co.uk) — a trusted source for historical football statistics.

---

## Future Improvements

- Switch to Poisson regression for more realistic goal distribution
- Add current season form (last 5 matches) as a feature
- Include head-to-head historical record between the two teams
- Add player availability / injury data
- Deploy to Streamlit Cloud for public access

---

## Author

**Biniyam** — 2nd year Computer Science student at Addis Ababa University  
GitHub: [@biniyamsav](https://github.com/biniyamsav)
