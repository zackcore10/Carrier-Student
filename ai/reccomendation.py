def recommend_career(programming, math, communication, interest, experience):

    if interest == "Artificial Intelligence":
        return "AI/ML Engineer"

    elif interest == "Web Development":
        return "Full Stack Developer"

    elif interest == "Data Science":
        return "Data Scientist"

    elif interest == "Cyber Security":
        return "Cyber Security Analyst"

    elif interest == "Cloud Computing":
        return "Cloud Engineer"

    else:
        return "Career not found"


# Test the recommendation system
if __name__ == "__main__":

    career = recommend_career(
        "Excellent",
        "Good",
        "Good",
        "Artificial Intelligence",
        "Beginner"
    )

    print("Recommended Career:", career)