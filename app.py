from flask import Flask,render_template,request,jsonify

app= Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/get_data', methods=["POST","GET"])
def getAPI():
    data= request.data
    print(data)
    return {"success":"1"}


if __name__ == "__main__":
    app.run(debug=True)