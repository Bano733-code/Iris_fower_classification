import streamlit as st
import numpy as np
import joblib


st.set_page_config(
    page_title="Iris Flower Classification",
    page_icon="🌸"
)


st.title("🌸 Iris Flower Classification")

st.write(
    "Enter flower measurements to predict the species."
)


@st.cache_resource
def load_model():

    model = joblib.load(
        "iris_model.pkl"
    )

    scaler = joblib.load(
        "scaler.pkl"
    )

    return model, scaler


model, scaler = load_model()



sepal_length = st.number_input(
    "Sepal Length (cm)",
    value=5.1
)

sepal_width = st.number_input(
    "Sepal Width (cm)",
    value=3.5
)

petal_length = st.number_input(
    "Petal Length (cm)",
    value=1.4
)

petal_width = st.number_input(
    "Petal Width (cm)",
    value=0.2
)



if st.button("Predict Species"):


    input_data = np.array(
        [[
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]]
    )


    input_scaled = scaler.transform(
        input_data
    )


    prediction = model.predict(
        input_scaled
    )


    probability = model.predict_proba(
        input_scaled
    )


    st.success(
        f"Predicted Species: {prediction[0]}"
    )


    st.write(
        "Confidence:"
    )

    st.write(
        f"{np.max(probability)*100:.2f}%"
    )
