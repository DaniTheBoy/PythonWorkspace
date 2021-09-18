def convert_gender(gender: str):
    gender = gender.upper()
    if gender == "F":
        return "FEMALE"
    elif gender == "M":
        return "MALE"
    else:
        return "MALDITO OPRESOR"
