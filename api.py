
# pregnancy weight suggestion
# https://www.mayoclinic.org/healthy-lifestyle/pregnancy-week-by-week/in-depth/pregnancy-weight-gain/art-20044360

# Pre-pregnancy weight             |Recommended weight gain
# Underweight (BMI under 18.5)     |28 to 40 lbs. (about 13 to 18 kg)
# Normal weight (BMI 18.5 to 24.9) |25 to 35 lbs. (about 11 to 16 kg)
# Overweight (BMI 25 to 29.9)      |15 to 25 lbs. (about 7 to 11 kg)
# Obesity (BMI 30 or more)         |11 to 20 lbs. (about 5 to 9 kg)

# Source: Institute of Medicine and National Research Council

# Carrying 2+ babies
# Pre-pregnancy weight              |Recommended weight gain
# Normal weight (BMI 18.5 to 24.9)  |37 to 54 lbs. (about 17 to 25 kg)
# Overweight (BMI 25 to 29.9)       |31 to 50 lbs. (about 14 to 23 kg)
# Obesity (BMI 30 or more)          |25 to 42 lbs. (about 11 to 19 kg)

# Source: Institute of Medicine and National Research Council


# pregnancy blood pressure suggestion
# https://www.mayoclinic.org/healthy-lifestyle/pregnancy-week-by-week/in-depth/pregnancy/art-20046098
# https://www.healthline.com/health/pregnancy/chronic-hypertension-blood-pressure#causes

# High blood pressure     | systolic pressure | diastolic pressure
# Elevated blood pressure | 120 - 129 mm Hg   | < 80 mm Hg
# Stage 1 hypertension    | 130 - 139 mm Hg   | 80 to 89 mm Hg
# Stage 2 hypertension    | >= 140 mm Hg      | >= 90 mm Hg 
# hypertensive crisis     | >= 180            | >= 120

# After 20 weeks of pregnancy, blood pressure that exceeds 140/90 mm HG — documented on two or more occasions, at least four hours apart, without any other organ damage — is considered to be gestational hypertension.


from flask import Flask, render_template, request, jsonify, send_file

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
def advice_page():
    syspre = request.form['syspre']
    diapre = request.form['diapre']
    b4weight = request.form['b4weight']
    curweight = request.form['curweight']
    height = request.form['height']
    cntbb = request.form['cntbb']

    syspre = int(syspre)
    diapre = int(diapre)
    b4weight = int(b4weight)
    curweight = int(curweight)
    height = int(height)
    cntbb = int(cntbb)
    return advice(syspre,diapre,b4weight,curweight,height,cntbb)


def advice(syspre,diapre,b4weight,curweight,height,cntbb):
    advice = None 
    advice_weight = None
    advice_bldpre = None
    if syspre <= 0 or diapre <= 0 or b4weight <= 0 or curweight <= 0 or height <= 0 or cntbb <= 0:
        advice = "Please input positive number!"
    else:
        b4BMI = b4weight / ((height/100)*(height/100))
        diff_weight = round(curweight - b4weight)

        if cntbb == 1:
            if b4BMI > 0 and b4BMI < 18.5 :
                advice_weight = '13-18 kg'
            elif b4BMI >= 18.5 and b4BMI < 25 :
                advice_weight = '11-16 kg'
            elif b4BMI >= 25 and b4BMI < 30 :
                advice_weight = '7-11 kg'
            elif b4BMI >= 30 :
                advice_weight = '5-9 kg'
            else:
                advice_weight = None
        elif cntbb >= 2:
            if b4BMI > 0 and b4BMI < 18.5 :
                advice_weight = '17-25 kg'
            elif b4BMI >= 18.5 and b4BMI < 25 :
                advice_weight = '17-25 kg'
            elif b4BMI >= 25 and b4BMI < 30 :
                advice_weight = '14-23 kg'
            elif b4BMI >= 30 :
                advice_weight = '11-19 kg'
            else:
                advice_weight = None
        else: 
                advice_weight = None

        if (syspre >= 180) or (diapre >= 120):
            advice_bldpre = 'Hypertensive crisis'
        elif (syspre >= 140 and syspre < 180) or (diapre >= 90 and diapre < 120):
            advice_bldpre = 'Stage 2 hypertension'
        elif (syspre >= 130 and syspre < 140) or (diapre >= 80 and diapre < 90):
            advice_bldpre = 'Stage 1 hypertension'
        elif (syspre >= 120 and syspre < 130) or (diapre >= 70 and diapre < 80):
            advice_bldpre = 'Elevated blood pressure'
        else:
            advice_bldpre = 'Not high blood pressure'

        advice = advice_bldpre + ' | ' + 'Your weight change is ' + str(diff_weight) + ' kg. Your suggested weight gain after pregnancy is ' + advice_weight + '.'


    return advice 





# syspre
# diapre
# b4weight
# curweight
# height
# cntbb


if __name__ == '__main__':
    app.run(debug=True)





# from flask import Flask, request, render_template

# app = Flask(__name__)

# @app.route('/')
# def my_form():
#     return render_template('my-form.html')

# @app.route('/', methods=['POST'])
# def my_form_post():
#     text = request.form['text']
#     processed_text = text.upper()
#     return processed_text


# if __name__ == '__main__':
#     app.run(debug=True)