from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(_name_)

model=pickle.load(open('smartindiamodel.pickle','rb'))


@app.route('/')
def hello_world():
    return render_template("predictionmodel.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output>=str(0.5):
        return render_template('predictionmodel.html',pred='You are a Slow Learner.\nProbability that he/she is Slow learner {}'.format(output),bhai="Slow Learner")
    else:
        return render_template('predictionmodel.html',pred='You are a Fast Learner.\n with Probablity of {}'.format(output),bhai="Fast Learner")


if _name== 'main_':
    app.run(debug=True)
