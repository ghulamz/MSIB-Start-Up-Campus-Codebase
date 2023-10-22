from math_function import add
from math_function import multiply, divide

def main():

    data_1 = int(input("masukkan input 1 :"))
    data_2 = int(input("masukkan input 2 :"))
    operator = input("masukkan operator :")

    if operator == "+":
        result = add(data_1, data_2)

    print("{} {} {} = {} ".format(data_1, operator, data_2, result))


if __name__ == "__main__":
    print("Hello Main !")
    main()



result_multiply = multiply(2, 3)
result_divide = divide(6, 2)

print("Multiply result:", result_multiply)
print("Divide result:", result_divide)