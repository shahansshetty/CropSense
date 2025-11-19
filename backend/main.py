from flask import Flask, request
import pickle
# from markupsafe import escape

app=Flask(__name__)

with open("crop_rec_model.pkl","rb") as f:
    model=pickle.load(f)



@app.route('/predict',methods=['GET'])
def index():
    if request.method  =='GET':
        N=request.args.get("N")
        P=request.args.get("P")
        K=request.args.get("K")
        temp=request.args.get("T")
        Humidity=request.args.get("H")
        pH=request.args.get("pH")
        RainFall=request.args.get("R")

        data=[[N,P,K,temp,Humidity,pH,RainFall]]
        prediction=model.predict(data)
        return {"crop":prediction[0]}
    else:
        return "Improper http request"

if __name__ == "__main__":
    app.run(debug=True)