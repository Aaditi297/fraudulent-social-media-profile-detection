from flask import Flask, request, render_template
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Project developed by Aaditi Sachdeva

app = Flask(__name__, template_folder='templates')

# Sample dataset (manually created)
data = {
    'followers_count': [150, 5200, 80, 14000, 95, 3800, 60, 7200, 850, 1100],
    'following_count': [1800, 450, 1400, 320, 1100, 300, 1700, 480, 120, 140],
    'post_count': [3, 300, 2, 450, 1, 180, 4, 160, 40, 55],
    'is_fake': [1, 0, 1, 0, 1, 0, 1, 0, 0, 0]
}

df = pd.DataFrame(data)

X = df[['followers_count', 'following_count', 'post_count']]
y = df['is_fake']

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    followers = int(request.form['followers'])
    following = int(request.form['following'])
    posts = int(request.form['posts'])

    input_data = pd.DataFrame(
        [[followers, following, posts]],
        columns=['followers_count', 'following_count', 'post_count']
    )

    prediction = model.predict(input_data)
    prob = model.predict_proba(input_data)

    fake_prob = round(prob[0][1] * 100, 2)
    real_prob = round(prob[0][0] * 100, 2)

    # Human logic
    if followers < 100 and posts < 5:
        result = "Low activity detected, profile may not be genuine."
    elif prediction[0] == 1:
        result = "This profile seems suspicious based on given data."
    else:
        result = "This profile appears to be normal."

    return render_template(
        'result.html',
        result=result,
        fake_prob=fake_prob,
        real_prob=real_prob
    )

if __name__ == '__main__':
    app.run(debug=False, port=5009)