def generate_tips(score: float):
    tips = []

    if score < 40:
        tips.append("Increase sleep and reduce phone usage for better focus.")
        tips.append("Try using the Pomodoro technique for studying.")
        tips.append("Lower caffeine near evening to avoid sleep disturbance.")
    
    elif 40 <= score < 70:
        tips.append("Maintain consistent study and break cycles.")
        tips.append("Engage in light physical activity to boost energy.")
        tips.append("Reduce stress with short mindfulness sessions.")

    else:
        tips.append("You are performing well — optimize task batching.")
        tips.append("Keep caffeine intake moderate.")
        tips.append("Try deep-work sessions to increase productivity further.")

    return tips
