from flask import Flask,render_template,request

app= Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/get_data', methods=["POST","GET"])
def getAPI():
    data= request.json
    print(data['array'])
    print(data['score'])
    return {"success":"1"}


if __name__ == "__main__":
    app.run(debug=True)