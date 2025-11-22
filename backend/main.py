from flask import Flask, request
import pickle
# from markupsafe import escape

app=Flask(__name__)

with open("crop_rec_model.pkl","rb") as f:
    model=pickle.load(f)



@app.route('/predict',methods=['POST','GET'])
def index():
    try:
        N=float(request.args.get("N"))
        P=float(request.args.get("P"))
        K=float(request.args.get("K"))
        temp=float(request.args.get("T"))
        Humidity=float(request.args.get("H"))
        pH=float(request.args.get("pH"))
        RainFall=float(request.args.get("R"))
    except:
        return {
            "error":"Enter all the inputs properly ",
                "inputs":"N->Nitrogen, P->Phosphorus, K->Potassium ,T->Temperature, H->Humidity, pH, R->Rainfall "
        }

    data=[N,P,K,temp,Humidity,pH,RainFall]
    check=isproper(data)
    if check!="OK":
        return{"error":check}
    crop=model.predict([data])
    return {'crop':crop[0]}
    
    
def isproper(d):
    N, P, K, T, H, pH, R = d

    if not (5 <= N <= 200):
        return "Nitrogen must be between 5 and 200."
    if not (5 <= P <= 200):
        return "Phosphorus must be between 5 and 200."
    if not (5 <= K <= 210):
        return "Potassium must be between 5 and 210."
    if not (5 <= T <= 45):
        return "Temperature must be between 5 and 45°C."
    if not (14 <= H <= 100):
        return "Humidity must be between 14% and 100%."
    if not (3.5 <= pH <= 10):
        return "pH must be between 3.5 and 10."
    if not (20 <= R <= 350):
        return "Rainfall must be between 20 and 350 mm."

    return "OK"

if __name__ == "__main__":
    app.run(debug=True)
    # host="0.0.0.0", port=8000