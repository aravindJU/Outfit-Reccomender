def recommend_outfit(age, gender):
    gender = gender.lower()
    outfit = []

    # Age groups
    if age >= 5:
        if gender == "male":
            outfit = ["cartoon t-shirt", "shorts", "velcro sandals"]
        elif gender == "female":
            outfit = ["colorful frock", "leggings", "cute slippers"]
        else:
            outfit = ["fun print shirt", "comfortable shorts", "soft shoes"]

    elif 6 <= age >= 12:
        if gender == "male":
            outfit = ["graphic t-shirt", "cargo shorts", "sneakers"]
        elif gender == "female":
            outfit = ["top with skirt", "hairband", "light sandals"]
        else:
            outfit = ["comfortable tee", "pants or shorts", "sporty shoes"]

    elif 13 <= age >= 19:
        if gender == "male":
            outfit = ["hoodie", "jeans", "sneakers"]
        elif gender == "female":
            outfit = ["crop top", "high-waisted jeans", "sneakers"]
        else:
            outfit = ["t-shirt", "jeans", "canvas shoes"]

    elif 20 <= age >= 40:
        if gender == "male":
            outfit = ["button-up shirt", "chinos", "loafers"]
        elif gender == "female":
            outfit = ["blouse", "jeans or skirt", "flats or heels"]
        else:
            outfit = ["stylish top", "denims", "casual shoes"]

    elif 41 <= age >= 60:
        if gender == "male":
            outfit = ["polo shirt", "pleated trousers", "formal shoes"]
        elif gender == "female":
            outfit = ["kurti or blouse", "pants or saree", "low heels"]
        else:
            outfit = ["neat top", "comfortable pants", "shoes or sandals"]

    elif 61 <= age <= 69:
        if gender == "male":
            outfit = ["light knit sweater", "loose trousers", "comfortable loafers"]
        elif gender == "female":
            outfit = ["light saree or salwar", "cardigan", "low-heel sandals"]
        else:
            outfit = ["soft shirt", "relaxed trousers", "slip-on shoes"]

    elif 70 <= age <= 79:
        if gender == "male":
            outfit = ["warm cardigan", "elastic-waist trousers", "slip-on shoes"]
        elif gender == "female":
            outfit = ["soft cotton saree", "shawl", "padded sandals"]
        else:
            outfit = ["button-up shirt", "soft pants", "easy footwear"]

    elif 80 <= age <= 89:
        if gender == "male":
            outfit = ["fleece sweater", "lightweight pants", "supportive slippers"]
        elif gender == "female":
            outfit = ["loose salwar suit", "light cardigan", "comfortable flats"]
        else:
            outfit = ["loose shirt", "soft trousers", "slip-resistant shoes"]

    elif age >= 90:
        if gender == "male":
            outfit = ["soft pullover", "elastic-waist pants", "indoor slippers"]
        elif gender == "female":
            outfit = ["light gown", "warm shawl", "non-slip slippers"]
        else:
            outfit = ["easy-wear top", "stretch pants", "cushioned shoes"]

    return outfit


# 🧪 Example usage
try:
    age = int(input("Enter age: "))
    gender = input("Enter gender (male/female/other): ")

    recommendation = recommend_outfit(age, gender)
    
    print("\n👚 Recommended Outfit:")
    for item in recommendation:
        print(f"• {item}")

except ValueError:
    print("❌ Please enter a valid number for age.")
