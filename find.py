def classify(number):
    toplam = 0
    if number <1:
        raise ValueError("Classification is only possible for positive integers.")
    for i in range(1,number):
        if number % i == 0:
            toplam +=i
    if toplam == number:
        return "perfect"
    elif toplam< number:
        return "deficient"
    elif toplam > number:
        return "abundant"
