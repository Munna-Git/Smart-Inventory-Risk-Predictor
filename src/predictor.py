def predict_inventory_risk(product_name, current_stock, avg_daily_sales, days_until_reorder, is_weekend=False, is_holiday=False):
    """Simple prediction function for demo"""
    
    # Adjust sales for weekend/holiday
    predicted_daily_sales = avg_daily_sales
    if is_weekend:
        predicted_daily_sales *= 1.3
    if is_holiday:
        predicted_daily_sales *= 1.8
    
    # Calculate expected demand until reorder
    expected_demand = predicted_daily_sales * days_until_reorder
    
    # Risk calculation
    if current_stock < expected_demand * 0.5:
        risk = "HIGH_RISK"
        recommendation = f"URGENT: Order {int(expected_demand * 2)} units immediately"
    elif current_stock < expected_demand:
        risk = "STOCKOUT_RISK"
        recommendation = f"Order {int(expected_demand * 1.5)} units within 2 days"
    elif current_stock > expected_demand * 5:
        risk = "OVERSTOCK_RISK"
        recommendation = "Reduce next order by 30% or run promotion"
    else:
        risk = "LOW_RISK"
        recommendation = f"Maintain current levels, next order: {int(expected_demand)} units"
    
    # Explanation
    explanation = f"Based on {avg_daily_sales:.1f} daily sales, expecting {expected_demand:.0f} units needed in {days_until_reorder} days"
    
    return {
        'product': product_name,
        'risk_level': risk,
        'recommendation': recommendation,
        'explanation': explanation,
        'current_stock': current_stock,
        'expected_demand': expected_demand
    }
