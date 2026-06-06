def asset_multiplier(asset):
    multipliers = {
        "Bridge": 1.4,
        "Power Plant": 1.8,
        "Pipeline": 1.6,
        "Factory": 1.3,
        "Warehouse": 1.1
    }

    return multipliers.get(asset, 1.0)