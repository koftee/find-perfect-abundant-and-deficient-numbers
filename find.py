def classify(number):
    toplam = 0
    if number <1:
        #checks the value of the number
        raise ValueError("Classification is only possible for positive integers.")
    for i in range(1,number):
        #find the divisors of the number
        if number % i == 0:
            #find the sum of the divisors
            toplam +=i
    if toplam == number:
        return "perfect"
    elif toplam< number:
        return "deficient"
    elif toplam > number:
        return "abundant"
