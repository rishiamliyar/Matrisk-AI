def shock_event(event, risk):
    impacts = {
        "Steel Price Spike": 15,
        "Corrosion Failure": 25,
        "Supply Chain Disruption": 20,
        "Natural Disaster": 30,
        "No Event": 0
    }

    return risk + impacts.get(event, 0)