from flask import Flask,render_template,request
import json
app= Flask(__name__)



Traits=["Maths","time","apti","CT","PS","Eng","imagination","QT"]

def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

def results(trait,trait_name):
    if(trait>=0.60 and trait<0.90):
        return("Fairly good in " + trait_name)
    if(trait>=0.90):
        return("Very good in " + trait_name)
    if(trait<0.60 and trait>=0.30):
        return("Below average in " + trait_name)
    if(trait<0.30):
        return("Poor, Need some work in " + trait_name)

def algo(data):
    correct=data['score']
    total_rounds=len(data['array'])
    wrong=total_rounds - correct    
    failed_perc=(wrong/correct)
    correct_perc= 1-failed_perc
    timings=data['array']
    skip=0
    
    maths = correct_perc - failed_perc
    time = 1- (sum(data['array'])/(total_rounds*500))
    ps= correct_perc -skip
    #score_percentile = #data related 

    total_traits={"maths":maths,"time":time,"Problem Solving":ps}
    print(total_traits)

    Final_analysis=[]
    for i,j in (total_traits.items()):
        Final_analysis.append(results(j, i))
    
    for a in Final_analysis:
        print(a)

    return

    





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



