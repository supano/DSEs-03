# Installation  

pip install -r requirements.txt

## or

pip install flask   
pip install flask-cors    
pip install gunicorn    
pip install pandas    

# API
## Parameters

| Key | Value |
| :---: | :---: |
| gender | `Male` or `Female` (เพศ `ชาย` หรือ `หญิง`) |
| married | `Yes` or `No` (แต่งงานแล้วหรือยัง)|
| dependents | `0` or `1` or `2` or `3+` (มีผู้ที่อยู่ในอุปการะกี่คน)|
| education | `Graduate` or `Not Graduate` (ระดับการศึกษา)|
| self_employed | `Yes` or `No` (เป็นเจ้าของธุรกิจหรือไม่)|
| applicant_income | integer greater than or equal 0 (รายได้ของผู้ขอสินเชื่อ หน่วยเป็น USD / Month)|
| coapplicant_income | integer greater than or equal 0 (รายได้ผู้ค้ำประกัน หน่วยเป็น USD / Month)|
| loan_amount | integer between 0 - 599 (วงเงินสินเชื่อ 1 หน่วยเท่ากับ 1,000 USD)|
| loan_amount_term | integer greater than or equal 0 (ระยะเวลาของสินเชื่อหน่วยเป็นเดือน)|
| credit_history | `Yes` or `No` (มีประวัติการกู้ยืมหรือไม่)|
| property_area | `Rural` or `Urban` or `Semiurban` (ทรัพย์สินอยู่บริเวณไหน `ชนบท` หรือ `ในเมือง` หรือ `กึ่งชนบทกึ่งเมือง`)|

## Response

| Value | Meaning |
| :---: | :---: |
| Approve | อนุมัติการกู้ |
| Reject | ปฏิเสธการกู้ |

# Example
 - https://loan-predict.herokuapp.com/api
 - https://loan-predict.herokuapp.com/api?gender=Male&married=Yes&dependents=0&education=Graduate&self_employed=Yes&applicant_income=3000&coapplicant_income=0&loan_amount=66&loan_amount_term=360&credit_history=Yes&property_area=Urban