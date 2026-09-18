def recommend_career(programming, math, communication, interest, experience):

    skill_score = {
        "Beginner": 1,
        "Average": 2,
        "Good": 3,
        "Excellent": 4
    }

    experience_score = {
        "Beginner": 1,
        "Intermediate": 2,
        "Advanced": 3,
        "Excellent": 4
    }

    programming_score = skill_score.get(programming, 1)
    math_score = skill_score.get(math, 1)
    communication_score = skill_score.get(communication, 1)
    exp_score = experience_score.get(experience, 1)

    careers = {
        "AI/ML Engineer": 0,
        "Full Stack Developer": 0,
        "Data Scientist": 0,
        "Cyber Security Analyst": 0,
        "Cloud Engineer": 0
    }

    if interest == "Artificial Intelligence":
        careers["AI/ML Engineer"] += 5
    elif interest == "Web Development":
        careers["Full Stack Developer"] += 5
    elif interest == "Data Science":
        careers["Data Scientist"] += 5
    elif interest == "Cyber Security":
        careers["Cyber Security Analyst"] += 5
    elif interest == "Cloud Computing":
        careers["Cloud Engineer"] += 5

    careers["Full Stack Developer"] += programming_score * 2
    careers["AI/ML Engineer"] += programming_score
    careers["Data Scientist"] += programming_score
    careers["Cyber Security Analyst"] += programming_score
    careers["Cloud Engineer"] += programming_score

    careers["AI/ML Engineer"] += math_score * 2
    careers["Data Scientist"] += math_score * 2
    careers["Cyber Security Analyst"] += math_score
    careers["Cloud Engineer"] += math_score

    careers["Full Stack Developer"] += communication_score
    careers["Cyber Security Analyst"] += communication_score
    careers["Cloud Engineer"] += communication_score

    careers["AI/ML Engineer"] += exp_score
    careers["Full Stack Developer"] += exp_score
    careers["Data Scientist"] += exp_score
    careers["Cyber Security Analyst"] += exp_score
    careers["Cloud Engineer"] += exp_score

    recommended_career = max(careers, key=careers.get)

    return recommended_career


if __name__ == "__main__":

    career = recommend_career(
        "Excellent",
        "Excellent",
        "Excellent",
        "Artificial Intelligence",
        "Advanced"
    )

    print("Recommended Career:", career)