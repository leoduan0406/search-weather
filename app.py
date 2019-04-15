# -*- coding:utf-8 -*-
"""
Author:duan
Date:2019/4/15 14:35
"""
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from query import read_code, query_code, query_weather

FILENAME = 'city_code.txt'
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a secret string'


class WeatherForm(FlaskForm):
    city = StringField(
        label='城市',
        validators=[
            DataRequired("请输入城市!")
        ],
        description='城市',
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号!",
            "required": "required",
        }
    )
    submit = SubmitField(
        "查询",
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"
        }
    )


@app.route('/', methods=['GET', 'POST'])
def index():
    city_codes = read_code()
    form = WeatherForm()
    city_weather = ''
    if form.validate_on_submit():
        data = form.data
        city_code = query_code(city_codes, data['city'])
        city_weather = query_weather(city_code)
        print(len(city_weather))
        print(city_weather)
    return render_template('index.html', form=form, city_weather=city_weather)


if __name__ == '__main__':
    app.run(debug=True)
