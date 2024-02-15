from flask import Flask, render_template, redirect, url_for
from morse import Morse
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, validators
import os
from dotenv import load_dotenv

load_dotenv()
ms = Morse()

# flask app config
app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
print(os.environ.get('SECRET_KEY'))

class MorseForm(FlaskForm):
    to_crypt = StringField(label='Morse or Word')
    type = RadioField(label='a', choices=('list', 'string'))
    submit = SubmitField('Decrypt', render_kw={'class': "btn btn-primary"})


@app.route('/', methods=['GET', 'POST'])
def main():
    result = None
    form = MorseForm()
    if form.validate_on_submit():
        if form.to_crypt.data is not None:
            if form.type.data == 'list':
                result = ms.morse_crypt(form.to_crypt.data, return_list=True)
            else:
                result = ms.morse_crypt(form.to_crypt.data)
    return render_template("index.html",
                           form=form, result=result)


if __name__ == "__main__":
    app.run(debug=False)
