import joblib

model = joblib.load("model.pkl")

questions = [
    ("real", "Onko hahmo oikeassa elämässä olemassa?"),
    ("movie", "Onko hahmo elokuvasta?"),
    ("superpowers", "Onko hahmolla supervoimia?"),
    ("human", "Onko hahmo ihminen?"),
    ("anime", "Onko hahmo animesta?")
]

def predict(answers):
    X = [answers.get(q[0], False) for q in questions]
    return model.predict([X])[0]
