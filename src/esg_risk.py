def esg_score(material):
    scores = {
        "Steel": 60,
        "Aluminum": 75,
        "Copper": 70,
        "Titanium": 65,
        "Concrete": 55
    }

    return scores.get(material, 50)