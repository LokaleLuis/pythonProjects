while True:
    try:
        print("How many numbers do you want to calculate? (1, 2, 3, 4, 5, ...)")
        number_of_numbers = int(input())
        numbers = []
        for i in range(number_of_numbers):
            print("Give me a your number: ")
            numbers.append(int(input()))
        print("What do you want to do with the numbers? (add, subtract, multiply, divide)")
        operation = input()
        if operation == "add":
            result = sum(numbers)
            print("The sum of the numbers is: " + str(result))
        elif operation == "subtract":
            result = numbers[0]
            for num in numbers[1:]:
                result -= num
            print("The difference of the numbers is: " + str(result))
        elif operation == "multiply":
            result = 1
            for num in numbers:
                result *= num
            print("The product of the numbers is: " + str(result))
        elif operation == "divide":
            result = numbers[0]
            for num in numbers[1:]:
                if num == 0:
                    print("Error: Cannot divide by zero!")
                    break
                result /= num
            else:
                print("The quotient of the numbers is: " + str(result))
        else:
            print("Invalid operation! Please choose add, subtract, multiply, or divide.")
            continue
        
        again = input("Do you want to calculate again? (Y/N)")
        if again == "Y":
            continue
        elif again == "N":
            break
        else:
            print("Invalid input! Please enter Y or N.")
            continue
    except ValueError:
        print("Please enter valid numbers only!")
        continue
