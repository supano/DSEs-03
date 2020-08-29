#!/usr/bin/python
#-*-coding: utf-8 -*-
######
import flask
from flask import request as fl_requests, jsonify
from flask_cors import CORS, cross_origin
import predict as pd 

app = flask.Flask(__name__, static_url_path='/static')
cors = CORS(app)

@app.route('/', methods=['GET'])
def home():
    return "ok"

@app.route('/api', methods=['GET'])
@cross_origin()
def api():
    # gender,	married, dependents,	education,	self_employed,	applicantIncome,	coapplicantIncome,	loanAmount,	loan_amount_term,	credit_history,	property_area
    if 'gender' in fl_requests.args:
        gender = fl_requests.args['gender']
        if gender != 'Male' and gender != 'Female':
            return "Error: gender must be Male or Female but got "+  gender
    else:
        return "Error: No gender field provided. Please specify gender."

    if 'married' in fl_requests.args:
        married = fl_requests.args['married']
        if married != 'Yes' and married != 'No':
            return "Error: gender must be Yes or No but got "+  married
    else:
        return "Error: No married field provided. Please specify married."

    if 'dependents' in fl_requests.args:
        dependents = fl_requests.args['dependents']
        if dependents != '0' and dependents != '1' and dependents != '2' and dependents != '3+':
            return "Error: dependents must be 0 or 1 or 2 or 3+ but got "+  dependents
    else:
        return "Error: No dependents field provided. Please specify dependents."

    if 'education' in fl_requests.args:
        education = fl_requests.args['education']
        if education != 'Graduate' and education != 'Not Graduate':
            return "Error: education must be Graduate or Not Graduate but got "+  education
    else:
        return "Error: No education field provided. Please specify education."

    if 'self_employed' in fl_requests.args:
        self_employed = fl_requests.args['self_employed']
        if self_employed != 'Yes' and self_employed != 'No':
            return "Error: self_employed must be Yes or No but got "+  self_employed
    else:
        return "Error: No self_employed field provided. Please specify self_employed."

    if 'applicantIncome' in fl_requests.args:
        applicantIncome = int(fl_requests.args['applicantIncome'])
        if applicantIncome < 0:
            return "Error: applicantIncome must be greater than or equal 0 but got "+  applicantIncome
    else:
        return "Error: No applicantIncome field provided. Please specify applicantIncome."

    if 'coapplicantIncome' in fl_requests.args:
        coapplicantIncome = int(fl_requests.args['coapplicantIncome'])
        if coapplicantIncome < 0:
            return "Error: coapplicantIncome must be greater than or equal 0 but got "+  coapplicantIncome
    else:
        return "Error: No coapplicantIncome field provided. Please specify coapplicantIncome."

    if 'loanAmount' in fl_requests.args:
        loanAmount = int(fl_requests.args['loanAmount'])
        if loanAmount < 0:
            return "Error: loanAmount must be greater than or equal 0 but got "+  loanAmount
    else:
        return "Error: No loanAmount field provided. Please specify loanAmount."

    if 'loan_amount_term' in fl_requests.args:
        loan_amount_term = int(fl_requests.args['loan_amount_term'])
        if loan_amount_term < 0:
            return "Error: loan_amount_term must be greater than or equal 0 but got "+  loan_amount_term
    else:
        return "Error: No loan_amount_term field provided. Please specify loan_amount_term."

    if 'credit_history' in fl_requests.args:
        credit_history = fl_requests.args['credit_history']
        if credit_history != 'Yes' and credit_history != 'No':
            return "Error: credit_history must be Yes or No but got "+  credit_history

        if credit_history == 'Yes':
            credit_history = 1
        else:
            credit_history = 0
    else:
        return "Error: No credit_history field provided. Please specify credit_history."

    if 'property_area' in fl_requests.args:
        property_area = fl_requests.args['property_area']
        if property_area != 'Rural' and property_area != 'Urban' and property_area != 'Semiurban':
            return "Error: property_area must Rural Yes or Urban or Semiurban but got "+  property_area

    else:
        return "Error: No property_area field provided. Please specify property_area."


    return pd.predict(gender,	married, dependents,	education,	self_employed,	applicantIncome,	coapplicantIncome,	loanAmount,	loan_amount_term,	credit_history,	property_area)

if __name__ == "__main__":
    app.run()