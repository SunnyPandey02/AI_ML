import pandas as pd
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    price = ''    
    if request.args.get('income') and \
        request.args.get('age') and \
            request.args.get('rooms') and \
                request.args.get('population'):
        model = pd.read_pickle('housePricePredictor.pkl')
        income = eval(request.args.get('income'))
        age = eval(request.args.get('age'))
        rooms = eval(request.args.get('rooms'))
        population = eval(request.args.get('population'))
        query = pd.DataFrame([[income,age,rooms,population]],model.feature_names_in_)
        result = model.predict(query)[0]
        price = f'${round(result,2)}'

    return render_template('index.html', result = price)

app.run(debug=True)