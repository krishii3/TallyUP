from flask import Flask,render_template,request
import json
app= Flask(__name__)



def algo(data):
    pass
    










@app.route('/')

def index():
    return render_template('index.html')

@app.route('/get_data', methods=["POST","GET"])
def getAPI():
    data= json.loads(request.data)
    algo(data)
    return {"success":"1"}


if __name__ == "__main__":
    app.run(debug=True)



