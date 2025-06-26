"""
Configuration file for Smart Inventory Predictor
"""

# Business Configuration
BUSINESS_CONFIG = {
    'stockout_cost_multiplier': 2.5,  # Lost sale cost vs. normal profit
    'overstock_cost_multiplier': 0.3, # Holding cost as % of product value
    'reorder_lead_time_days': 3,      # Typical supplier lead time
    'safety_stock_days': 7,           # Minimum stock buffer
    'high_risk_threshold': 0.7,       # Risk score for immediate action
    'medium_risk_threshold': 0.4      # Risk score for attention needed
}

# Data Generation Configuration
DATA_CONFIG = {
    'num_stores': 5,
    'num_products': 50,
    'start_date': '2022-01-01',
    'end_date': '2024-01-01',
    'missing_data_rate': 0.15,        # 15% missing values
    'outlier_rate': 0.02,             # 2% outliers
    'seasonal_strength': 0.3          # Seasonality impact
}

# Model Configuration
MODEL_CONFIG = {
    'test_size': 0.2,
    'random_state': 42,
    'cv_folds': 5,
    'target_classes': ['LOW_RISK', 'STOCKOUT_RISK', 'OVERSTOCK_RISK', 'HIGH_RISK']
}

# Feature Engineering
FEATURE_CONFIG = {
    'moving_avg_windows': [7, 14, 30],
    'lag_features': [1, 7, 14],
    'seasonality_features': ['day_of_week', 'month', 'quarter', 'is_weekend', 'is_holiday']
}