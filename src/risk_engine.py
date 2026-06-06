def calculate_risk(strength, corrosion):
    risk = (100 - strength) + corrosion
    return risk