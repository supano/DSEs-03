## Installation  

pip install -r requirements.txt

## or

pip install flask
pip install flask-cors
pip install gunicorn
pip install pandas


## /api arguments

| Key | Value |
| :---: | :---: |
| gender | `Male` or `Female` |
| married | `Yes` or `No` |
| dependents | `0` or `1` or `2` or `3+` |
| education | `Graduate` or `Not Graduate` |
| self_employed | `Yes` or `No` |
| applicantIncome | integer greater than or equal 0 |
| coapplicantIncome | integer greater than or equal 0 |
| loanAmount | integer greater than or equal 0 |
| loan_amount_term | integer greater than or equal 0 |
| credit_history | `Yes` or `No` |
| property_area | `Rural` or `Urban` or `Semiurban`|

## /api response

| Value | Meaning |
| :---: | :---: |
| yes | อนุมัติการกู้ |
| No | ปฏิเสธการกู้ |

## example call
https://loan-predict.herokuapp.com/api?gender=Male&married=Yes&dependents=0&education=Graduate&self_employed=Yes&applicantIncome=3000&coapplicantIncome=0&loanAmount=66&loan_amount_term=360&credit_history=Yes&property_area=Urban
