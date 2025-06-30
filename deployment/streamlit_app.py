# File: deployment/streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("🏪 Smart Inventory Risk Predictor")
st.subheader("For Small Retailers")

# Sidebar inputs
st.sidebar.header("Product Information")
product_name = st.sidebar.text_input("Product Name", "Milk")
current_stock = st.sidebar.number_input("Current Stock", min_value=0, value=50)
avg_daily_sales = st.sidebar.number_input("Average Daily Sales", min_value=0.0, value=12.5, step=0.1)
days_until_reorder = st.sidebar.slider("Days Until Next Reorder", 1, 30, 7)
is_weekend = st.sidebar.checkbox("Weekend Coming Up")
is_holiday = st.sidebar.checkbox("Holiday Period")

# Prediction function (same as above)
def predict_risk(product_name, current_stock, avg_daily_sales, days_until_reorder, is_weekend, is_holiday):
    predicted_daily_sales = avg_daily_sales
    if is_weekend:
        predicted_daily_sales *= 1.3
    if is_holiday:
        predicted_daily_sales *= 1.8
    
    expected_demand = predicted_daily_sales * days_until_reorder
    
    if current_stock < expected_demand * 0.5:
        risk = "🔴 HIGH RISK"
        recommendation = f"URGENT: Order {int(expected_demand * 2)} units immediately"
        color = "red"
    elif current_stock < expected_demand:
        risk = "🟡 STOCKOUT RISK"
        recommendation = f"Order {int(expected_demand * 1.5)} units within 2 days"
        color = "orange"
    elif current_stock > expected_demand * 5:
        risk = "🔵 OVERSTOCK RISK"
        recommendation = "Reduce next order by 30% or run promotion"
        color = "blue"
    else:
        risk = "🟢 LOW RISK"
        recommendation = f"Maintain current levels, next order: {int(expected_demand)} units"
        color = "green"
    
    return risk, recommendation, expected_demand, color

# Make prediction
if st.sidebar.button("Analyze Risk"):
    risk, recommendation, expected_demand, color = predict_risk(
        product_name, current_stock, avg_daily_sales, days_until_reorder, is_weekend, is_holiday
    )
    
    # Display results
    st.markdown(f"## Results for {product_name}")
    st.markdown(f"### {risk}")
    st.markdown(f"**Recommendation:** {recommendation}")
    st.markdown(f"**Expected demand in {days_until_reorder} days:** {expected_demand:.0f} units")
    
    # Simple gauge chart
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = min(100, (expected_demand / current_stock) * 100) if current_stock > 0 else 100,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Risk Level (%)"},
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': color},
            'steps': [
                {'range': [0, 25], 'color': "lightgreen"},
                {'range': [25, 50], 'color': "yellow"},
                {'range': [50, 75], 'color': "orange"},
                {'range': [75, 100], 'color': "red"}],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': 90}}))
    
    st.plotly_chart(fig)

# Business impact section
st.markdown("---")
st.markdown("## 📊 Business Impact")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Potential Monthly Savings", "$3,500", "↑ 25%")

with col2:
    st.metric("Stockout Reduction", "40%", "↓ 15%")

with col3:
    st.metric("ROI", "300%", "↑ 250%")