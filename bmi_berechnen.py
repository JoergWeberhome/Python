def berechne_bmi(weight, height):  # berechne den BMI
    print(weight)

    print(height)

    if height >= 2.5:
        height = height / 100

    bmi = round(weight / (height * height), 2)


    return bmi
