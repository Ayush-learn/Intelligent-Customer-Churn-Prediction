def get_risk_level(probability):

    if probability < 0.30:
        return "LOW RISK"

    elif probability < 0.70:
        return "MEDIUM RISK"

    else:
        return "HIGH RISK"
    