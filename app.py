##########Сейчас############
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    answer = None

    if request.method == "POST":
        name = request.form.get("user_name")
        age = int(request.form.get("user_age"))

        birth_year = 2026 - age
        answer = f"Привет, {name}! Сервер посчитал: ты родился примерно в {birth_year} году!"
        
    return render_template("index.html", reply=answer)

if __name__ == "__main__":
    app.run(debug=True)

