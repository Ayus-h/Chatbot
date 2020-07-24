from flask import Flask, render_template, request
import Convers

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = str(request.args.get('msg'))
    botText1= Convers.respond(userText)
    return botText1



"""
@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Talk') == 'Talk':
            print("Talked")
        else:
            return render_template("home.html")
    elif request.method == 'GET':
        return render_template("home.html")
        print("No Post Back Call")
    return render_template("home.html")
"""





if __name__ == "__main__":
    app.run()