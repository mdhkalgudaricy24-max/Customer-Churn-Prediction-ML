from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained ML pipeline
pipeline = joblib.load("model/pipeline.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = {
            "gender": request.form["gender"],
            "SeniorCitizen": int(request.form["SeniorCitizen"]),
            "Partner": request.form["Partner"],
            "Dependents": request.form["Dependents"],
            "tenure": float(request.form["tenure"]),
            "PhoneService": request.form["PhoneService"],
            "MultipleLines": request.form["MultipleLines"],
            "InternetService": request.form["InternetService"],
            "OnlineSecurity": request.form["OnlineSecurity"],
            "OnlineBackup": request.form["OnlineBackup"],
            "DeviceProtection": request.form["DeviceProtection"],
            "TechSupport": request.form["TechSupport"],
            "StreamingTV": request.form["StreamingTV"],
            "StreamingMovies": request.form["StreamingMovies"],
            "Contract": request.form["Contract"],
            "PaperlessBilling": request.form["PaperlessBilling"],
            "PaymentMethod": request.form["PaymentMethod"],
            "MonthlyCharges": float(request.form["MonthlyCharges"]),
            "TotalCharges": float(request.form["TotalCharges"])
        }

        input_df = pd.DataFrame([data])

        prediction = pipeline.predict(input_df)[0]

        probability = pipeline.predict_proba(input_df)[0]

        stay_probability = probability[0] * 100
        churn_probability = probability[1] * 100

        # Risk Level
        if churn_probability >= 70:
            risk = "🔴 High Risk of Churn"
        elif churn_probability >= 40:
            risk = "🟠 Medium Risk of Churn"
        else:
            risk = "🟢 Low Risk of Churn"

        # Prediction Result
        if prediction == 1:
            result = "⚠️ Customer is likely to Churn"
            confidence = churn_probability
        else:
            result = "✅ Customer is likely to Stay"
            confidence = stay_probability

        return render_template(
            "index.html",
            prediction=result,
            confidence=f"{confidence:.2f}%",
            stay_probability=f"{stay_probability:.2f}%",
            churn_probability=f"{churn_probability:.2f}%",
            risk=risk
        )

    except Exception as e:

        return render_template(
            "index.html",
            prediction="Prediction Failed",
            confidence="0%",
            stay_probability="0%",
            churn_probability="0%",
            risk="N/A",
            error=str(e)
        )


if __name__ == "__main__":
    app.run(debug=True)