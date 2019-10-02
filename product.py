def product():

    """calculate 10 rs"""

    print("Denomination of notes(10)")
    user_input_10 = input("how many notes do you have?")
    value_of_10 = 10
    product_of_10 = int(value_of_10) * int(user_input_10)
    print(product_of_10)

    """calculate 20 rs"""

    print("Denomination of notes(20)")
    user_input_20 = input("how many notes do you have?")
    value_of_20 = 20
    product_of_20 = int(value_of_20) * int(user_input_20)
    print(product_of_20)

    """calculate 50 rs"""

    print("Denomination of notes(50)")
    user_input_50 = input("how many notes do you have?")
    value_of_50 = 50
    product_of_50 = int(value_of_50) * int(user_input_50)
    print(product_of_50)

    """calculate 100 rs"""

    print("Denomination of notes(100)")
    user_input_100 = input("how many notes do you have?")
    value_of_100 = 100
    product_of_100 = int(value_of_100) * int(user_input_100)
    print(product_of_100)

    """calculate 200 rs"""
    
    print("Denomination of notes(200)")
    user_input_200 = input("how many notes do you have?")
    value_of_200 = 200
    product_of_200 = int(value_of_200) * int(user_input_200)
    print(product_of_200)

    """calculate 500 rs"""

    print("Denomination of notes(500)")
    user_input_500 = input("how many notes do you have?")
    value_of_500 = 500
    product_of_500 = int(value_of_500) * int(user_input_500)
    print(product_of_500)

    """calculate 2000 rs"""

    print("Denomination of notes(2000)")
    user_input_2000 = input("how many notes do you have?")
    value_of_2000 = 2000
    product_of_2000 = int(value_of_2000) * int(user_input_2000)
    print(product_of_2000)

    Result = [product_of_10 , product_of_20 , product_of_50 , product_of_100 , product_of_200 , product_of_500 , product_of_2000]
    Result = sum(Result)
    print("Result :",Result)

    if Result < 10000:
        print("You need to work hard or save more.")
    elif Result > 10000:
        print("Nice you should donate some money")
    else:
         print("Error, no money!")

product()