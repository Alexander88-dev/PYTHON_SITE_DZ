from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])

def index():
    answer = None

    if request.method == "POST":
        name = request.form.get("user_name")
        age = int(request.form.get("user_age"))
        ageExperience = int(request.form.get("user_ageExperience"))
        speciality = request.form.get("speciality")


        if (age-10) < ageExperience:
            answer = f"Вы вели не правдивый опыт работы"    
        elif age <= 17:
            answer = f"Ваш возраст слишком мал"
        elif age > 90:
            answer = f"Введите верный возраст"
        else:
            salary = 200000

            if ageExperience <= 1:
                salary = (salary * 30) / 100 
                stars = "🌟Джун🌟"
            elif ageExperience <= 5:
                salary = (salary * 50) / 100
                stars = "🌟🌟Мидал🌟🌟"
            else:
                stars = "🌟🌟🌟Сеньор🌟🌟🌟"

            answer = f"Имя: {name}\nСпециальность: {speciality}\nРанг: {stars}\nЗарплата: {salary} руб."
        
    return render_template("index.html", reply=answer)

if __name__ == "__main__":
    app.run(debug=True)
