import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


MODEL = None
DF = None
X_COLUMNS = None


def train_model():
    global MODEL, DF, X_COLUMNS

    cols = [
        'HomeTeam','AwayTeam','FTHG','FTAG','FTR',
        'HTHG','HTAG','HTR','HS','AS','HST','AST',
        'HF','AF','HC','AC','HY','AY','HR','AR',
        'B365H','B365D','B365A',
        'BWH','BWD','BWA',
        'PSH','PSD','PSA'
    ]

    files = []

    for i in range(10):
        if i == 0:
            name = "E0.csv"
        else:
            name = f"E0({i}).csv"

        df = pd.read_csv(name)
        files.append(df[cols])

    DF = pd.concat(files, ignore_index=True).dropna()

    X = DF[
        [
            'HomeTeam','AwayTeam',
            'HS','AS','HST','AST',
            'HF','AF','HC','AC',
            'HY','AY','HR','AR',
            'B365H','B365D','B365A',
            'BWH','BWD','BWA',
            'PSH','PSD','PSA'
        ]
    ]

    y = DF[['FTHG','FTAG']]

    X = pd.get_dummies(X, columns=["HomeTeam","AwayTeam"])

    X_COLUMNS = X.columns

    x_train, x_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    MODEL = LinearRegression()
    MODEL.fit(x_train, y_train)
   
def predict_match(home_team, away_team):

    new_match = pd.DataFrame([{}], columns=X_COLUMNS).fillna(0)
   

    home_stats = DF[DF["HomeTeam"] == home_team].mean(numeric_only=True)
    away_stats = DF[DF["AwayTeam"] == away_team].mean(numeric_only=True)

    stat_cols = [
        'HS','AS','HST','AST',
        'HF','AF','HC','AC',
        'HY','AY','HR','AR',
        'B365H','B365D','B365A',
        'BWH','BWD','BWA',
        'PSH','PSD','PSA'
    ]

    home_stats = home_stats[stat_cols]
    away_stats = away_stats[stat_cols]

    new_match[f"HomeTeam_{home_team}"] = 1
    new_match[f"AwayTeam_{away_team}"] = 1

    new_match["HS"] = home_stats["HS"]
    new_match["AS"] = away_stats["AS"]

    new_match["HST"] = home_stats["HST"]
    new_match["AST"] = away_stats["AST"]

    new_match["HF"] = home_stats["HF"]
    new_match["HC"] = home_stats["HC"]
    new_match["HY"] = home_stats["HY"]
    new_match["HR"] = home_stats["HR"]

    new_match["AF"] = away_stats["AF"]
    new_match["AC"] = away_stats["AC"]
    new_match["AY"] = away_stats["AY"]
    new_match["AR"] = away_stats["AR"]

    for col in [
        "B365H","B365D","B365A",
        "BWH","BWD","BWA",
        "PSH","PSD","PSA"
    ]:
        new_match[col] = (home_stats[col] + away_stats[col]) / 2

    prediction = MODEL.predict(new_match)

    return (
        round(prediction[0][0]),
        round(prediction[0][1])
    )

train_model()
    






