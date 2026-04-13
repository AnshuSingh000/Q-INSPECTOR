def optimization_verdict(percentage):
    if percentage >= 70:
        return "High redundancy detected"
    elif percentage >= 30:
        return "Moderate optimization opportunity"
    elif percentage > 0:
        return "Low optimization opportunity"
    return "Circuit already efficient"