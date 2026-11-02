import streamlit as st
import pandas as pd
import joblib
import os

# Premium EstateAI Design css code
st.markdown("""
<style>

/* Main background */
.stApp {
    background: linear-gradient(135deg,#eef2f7,#dce6f1)!important;
}

/* Main heading */
h1 {
    color: #17365D;
    font-weight: 800;
}

/* Section headings */
h2, h3 {
    color: #24476B;
    font-weight: 700;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #142d4e, #3973a8) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 14px 25px !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    box-shadow: 0 5px 15px rgba(20, 45, 78, 0.2);
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(20, 45, 78, 0.3);
}

/* Button hover */
.stButton > button:hover {
    background: #102B4C;
    color: white;
    border: none;
}

/* Input fields */
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {
    border-radius: 8px;
}

/* Metric cards */
[data-testid="stMetric"] {
    background: white;
    padding: 18px;
    border-radius: 12px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.07);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #eaf0f8;
}

</style>
""", unsafe_allow_html=True)

# EstateAI Hero Section

st.markdown("""
<div style="
    background: linear-gradient(120deg, #142d4e, #3973a8);
    padding: 40px;
    border-radius: 18px;
    color: white;
    margin-bottom: 25px;
">
<div style="display:flex; align-items:center; gap:25px;">
    <div>
    <h1 style="color:white; font-size:38px;">
        Welcome to EstateAI 🏡
    </h1>
    <h3 style="color:#dcecff;">
        Smart House Price Prediction with Machine Learning
    </h3>
    <p style="font-size:17px;">
        Find. Predict. Invest. Make smarter property decisions
        with the power of AI.
    </p>
    </div>
""", unsafe_allow_html=True)

# Load trained model and feature columns
model = joblib.load("model.pkl")
feature_columns = joblib.load("feature_columns.pkl")

# Page configuration
st.set_page_config(
    page_title="EstateAI | House Price Predictor",
    page_icon="🏡",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.stApp {
    background-color: #f4f7fb;
}
.main-title {
    font-size: 38px;
    font-weight: 800;
    color: #17365D;
}
.subtitle {
    color: #64748b;
    font-size: 17px;
}
div.stButton > button {
    background-color: #17365D;
    color: white;
    border-radius: 10px;
    height: 48px;
    width: 100%;
    font-weight: bold;
}
div.stButton > button:hover {
    background-color: #2563eb;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Header

st.divider()

# Sidebar
st.sidebar.title("🏠 EstateAI")
st.sidebar.write("AI-powered real estate price estimation.")
st.sidebar.info("Enter property details to get an estimated price.")

# Main heading
st.header("Property Details")
st.write("Fill in the information about your dream property.")

# Input form
with st.form("house_form"):

    st.subheader("📐 Basic Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        area = st.number_input(
            "Area (sq. ft.)",
            min_value=100,
            max_value=100000,
            value=3000
        )

    with col2:
        bedrooms = st.number_input(
            "Bedrooms",
            min_value=1,
            max_value=10,
            value=3
        )

    with col3:
        bathrooms = st.number_input(
            "Bathrooms",
            min_value=1,
            max_value=10,
            value=2
        )

    col4, col5 = st.columns(2)

    with col4:
        stories = st.selectbox(
            "Number of Stories",
            [1, 2, 3, 4]
        )

    with col5:
        parking = st.selectbox(
            "Parking Spaces",
            [0, 1, 2, 3]
        )

    st.divider()
    st.subheader("✨ Property Features")

    col6, col7 = st.columns(2)

    with col6:
        mainroad = st.selectbox(
            "Main Road Access",
            ["yes", "no"]
        )

        guestroom = st.selectbox(
            "Guest Room",
            ["yes", "no"]
        )

        basement = st.selectbox(
            "Basement",
            ["yes", "no"]
        )

    with col7:
        hotwaterheating = st.selectbox(
            "Hot Water Heating",
            ["yes", "no"]
        )

        airconditioning = st.selectbox(
            "Air Conditioning",
            ["yes", "no"]
        )

        prefarea = st.selectbox(
            "Preferred Area",
            ["yes", "no"]
        )

    furnishingstatus = st.selectbox(
        "Furnishing Status",
        ["furnished", "semi-furnished", "unfurnished"]
    )

    submitted = st.form_submit_button(
        "✨ Predict House Price"
    )

# Prediction
if submitted:

    input_data = pd.DataFrame([{
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "stories": stories,
        "parking": parking,
        "mainroad": mainroad,
        "guestroom": guestroom,
        "basement": basement,
        "hotwaterheating": hotwaterheating,
        "airconditioning": airconditioning,
        "prefarea": prefarea,
        "furnishingstatus": furnishingstatus
    }])

    # Convert categorical values into numerical columns
    input_data = pd.get_dummies(input_data)

    # Match training columns
    input_data = input_data.reindex(
        columns=feature_columns,
        fill_value=0
    )

    # Predict
    prediction = model.predict(input_data)[0]

    # Save prediction in history
    history_entry = pd.DataFrame([{
        "Date & Time": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Area": area,
        "Bedrooms": bedrooms,
        "Bathrooms": bathrooms,
        "Predicted Price": round(float(prediction), 2)
    }])

    try:
        old_history = pd.read_csv("prediction_history.csv")
        updated_history = pd.concat(
            [old_history, history_entry],
            ignore_index=True
        )
    except FileNotFoundError:
        updated_history = history_entry

    updated_history.to_csv("prediction_history.csv", index=False)

    st.divider()
    st.success("Prediction generated successfully!")

    st.subheader("🏡 Estimated House Price")

    st.markdown(
        f"""
        <div style="
            background-color: #17365D;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
        ">
            <h3 style="color:white;">Estimated Property Value</h3>
            <h1 style="color:#7CFCB2;">
                {prediction:,.0f}
            </h1>
            <p style="color:white;">
                Price is an estimate generated by the ML model.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("📋 Your Property Summary")
    st.dataframe(input_data, use_container_width=True)

st.divider()

st.caption("EstateAI | BCA Machine Learning Project | Educational Use")

# Price Comparison Graph

st.divider()

st.header("📊 House Price Comparison")
st.write("Compare estimated prices for different house sizes.")

areas = [1000, 2000, 3000, 4000, 5000]
prices = []

for house_area in areas:

    sample_data = pd.DataFrame([{
        "area": house_area,
        "bedrooms": 3,
        "bathrooms": 2,
        "stories": 2,
        "parking": 1,
        "mainroad": "yes",
        "guestroom": "no",
        "basement": "yes",
        "hotwaterheating": "no",
        "airconditioning": "yes",
        "prefarea": "yes",
        "furnishingstatus": "semi-furnished"
    }])

    sample_data = pd.get_dummies(sample_data)

    sample_data = sample_data.reindex(
        columns=feature_columns,
        fill_value=0
    )

    price = model.predict(sample_data)[0]
    prices.append(price)

chart_data = pd.DataFrame({
    "House Area (sq. ft.)": areas,
    "Estimated Price": prices
})

st.line_chart(
    chart_data.set_index("House Area (sq. ft.)")
)

st.caption("Other property features are kept constant for comparison.")

# House Pictures Gallery

st.divider()

st.header("🏡 Explore Beautiful Properties")
st.write("Discover modern homes and beautiful interiors.")

col1, col2 = st.columns(2)

with col1:
    st.image(
        "https://images.unsplash.com/photo-1600585154340-be6161a56a0c",
        caption="Modern Luxury House",
        use_container_width=True
    )

with col2:
    st.image(
        "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0",
        caption="Luxury Living Room",
        use_container_width=True
    )

col3, col4 = st.columns(2)

with col3:
    st.image(
        "https://images.unsplash.com/photo-1616486338812-3dadae4b4ace",
        caption="Modern Bedroom",
        use_container_width=True
    )

with col4:
    st.image(
        "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c",
        caption="Beautiful Interior",
        use_container_width=True
    )

# EstateAI Dashboard

st.divider()

st.header("📊 EstateAI Dashboard")
st.write("Overview of your house price predictions.")

try:
    history = pd.read_csv("prediction_history.csv")

    # Calculate dashboard statistics
    total_predictions = len(history)
    average_price = history["Predicted Price"].mean()
    highest_price = history["Predicted Price"].max()

    # Dashboard metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Predictions",
            total_predictions
        )

    with col2:
        st.metric(
            "Average House Price",
            f"{average_price:,.0f}"
        )

    with col3:
        st.metric(
            "Highest House Price",
            f"{highest_price:,.0f}"
        )

    # Recent predictions
    st.subheader("🕒 Recent Predictions")

    st.dataframe(
        history.tail(5).iloc[::-1],
        use_container_width=True
    )

except FileNotFoundError:
    st.info("Make your first prediction to see dashboard statistics.")

# Model Performance
st.divider()
st.header("📈 Model Performance")

st.write("Evaluation results of the Linear Regression model.")

col1, col2 = st.columns(2)

with col1:
    st.metric("R² Score", "65.3%")

with col2:
    st.metric("Mean Absolute Error", "979,043")

st.caption(
    "The R² score indicates how much variation in house prices "
    "is explained by the model. MAE represents the average "
    "prediction error in the dataset's price units."
)

# About EstateAI
st.divider()

st.header("ℹ️ About EstateAI")

st.write("""
EstateAI is a Machine Learning based House Price Prediction System
designed to estimate house prices using important property features.

The system analyzes property details such as area, bedrooms,
bathrooms, stories, parking and furnishing status to predict
an estimated house price.
""")

st.subheader("🛠️ Technologies Used")

tech1, tech2, tech3, tech4 = st.columns(4)

tech1.info("Python")
tech2.info("Pandas")
tech3.info("Scikit-learn")
tech4.info("Streamlit")

st.subheader("🤖 Machine Learning Algorithm")
st.write("Linear regression is a foundational supervised machine learning algorithm used to predict continuous numeric outcomes by modeling a linear relationship between an input feature and a target variable")

st.subheader("🎯 Project Objective")
st.write("""
To develop an interactive and user-friendly application
that predicts estimated house prices using Machine Learning.
""")
st.subheader("👩‍💻 Project Developer")

st.markdown("""
<div style="
    background: linear-gradient(135deg, #17365D, #2874A6);
    padding: 20px;
    border-radius: 12px;
    color: white;
    margin-bottom: 15px;
">
    <h2 style="color: white; margin-bottom: 10px;">
        Gungun Goyal
    </h2>
    <h4 style="color: #BFE3FF; margin: 0;">
        Bachelor of Computer Applications (BCA)
    </h4>
    <p style="color: white; margin-top: 8px;">
        3rd Year Student
    </p>
</div>
""", unsafe_allow_html=True)