def calculator(x, sign, y):
    try: 
        if sign == '+':
            return x + y
        elif sign == '-':
            return x - y
        elif sign == '*':
            return x * y
        elif sign == '/':
            if y == 0:
                raise ZeroDivisionError('Erreur ')
            return x / y
        else:
            raise ValueError('Invalid operator ')
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)

def calculdirect():
    try:
        operation = input('Operation : 👋👋👋 \n')
        operation = operation.replace(" ","")
        i = 0
        n1 = ""
        while i < len(operation) and operation[i].isdigit():
            n1 += operation[i]
            i += 1
        if i >= len(operation):
            raise ValueError('Invalid operation format')
        op = operation[i]
        n2 = operation[i + 1:]
        if not n1 or not n2:
            raise ValueError('Invalid numbers ')
        print(calculator(int(n1), op, int(n2)))
    except ValueError as e:
        print(e)

def main():
    while True:
        o = input('Tapez 1 : Calcul direct . Tapez 2 : Calcul guidé . Tapez 0 pour quitter \n')
        if o == '1':
            calculdirect()
        elif o == '2':
            try:
                x = float(input("x="))
                y = float(input("y="))
                sign = input("opération :")
                if sign not in ['+', '-', '*', '/']:
                    raise ValueError('Invalid operator ')
                print(calculator(x, sign, y))
            except ValueError as e:
                print(e)
            except Exception:
                print('Wrong Saisie ')
        elif o == '0':
            exit()
        else:
            print('Invalid choice ')

if __name__ == "__main__":
    main()
