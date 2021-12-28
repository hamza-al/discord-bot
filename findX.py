def findX(equation: str):
    try:
        alphabet = 'abcdefghijklmnopqrstuvwyz'
        alphabet += alphabet.upper()
        alphabet += "X"
        if "=" not in equation:
            for i in equation:
                if i in alphabet:
                    return "Invalid Statement; statement must be an equation or not have variables"

        elif equation.count("=") > 1:
            return "Invalid equation; equation can only have two sides (one equal sign)"
        else:
            for i in range(len(equation)):
                if equation[i] in alphabet:
                    return "Invalid equation; equation can only have one variable (lower case x) "
                if equation[i] in "()":
                    return "Sorry I'm too dumb to use brackets"
                if equation[i] in "*/+-":
                    if i == 0 or i == len(equation) - 1 or equation[i-1] in "*/+-" or equation[i+1] in "*/+-":
                        return "Misplaced equation symbol"

            left = equation.split("=")[0].split(' ')
            left = [word for word in left if word != '']
            right = equation.split("=")[1].split(' ')
            right = [word for word in right if word != '']

            leftVal = 0
            leftX = 0
            rightVal = 0
            rightX = 0
            if right[0] in "*/+-":
                return "Misplaced equation symbol"
            if len(left) == 1:
                if left[0] == 'x':
                    leftX += 1
                else:
                    leftVal += float(left[0])
            if len(right) == 1:
                if right[0] == 'x':
                    rightX += 1
                else:
                    rightVal += float(right[0])
            if len(left) > 1:
                for i in range(len(left) - 1):
                    if left[i] == "*" or left[i] == '/':
                        if left[i-1] == 'x' and left[i+1] == 'x':
                            return "Multiplication/division of x with/by x is not yet supported"
                        if left[i-1] == 'x':
                            if left[i] == "*":
                                leftX += float(left[i+1])
                            if left[i] == "/":
                                leftX += float(1/left[i+1])
                        if left[i+1] == 'x':
                            if left[i] == "*":
                                leftX += float(left[i-1])
                            if left[i] == "/":
                                return "Division by variables in not suported"
                        else:
                            if left[i] == "*" and left[i-1] != 'x' and left[i+1] != 'x':
                                leftVal += (float(left[i+1])
                                            * float(left[i-1]))
                            if left[i] == "/" and left[i-1] != 'x' and left[i+1] != 'x':
                                leftVal += (float(left[i+1]) /
                                            float(left[i-1]))
                    if left[i] == '+':
                        if left[i+1] == 'x':
                            leftX += 1
                        else:
                            if i+1 == len(left) - 1 or left[i+2] not in '/*':
                                leftVal += float(left[i+1])
                    if left[i] == '-':
                        if left[i+1] == 'x':
                            leftX += 1
                        else:
                            leftVal -= float(left[i+1])
                if left[0] == 'x' and left[1] in "-+":
                    leftX += 1
                if left[0] != 'x' and left[1] in '-+':
                    leftVal += float(left[0])
            if len(right) > 1:
                for i in range(len(right) - 1):
                    if right[i] == "*" or right[i] == '/':
                        if right[i-1] == 'x' and right[i+1] == 'x':
                            return "Multiplication/division of x with/by x is not yet supported"
                        if right[i-1] == 'x':
                            if right[i] == "*":
                                rightX += float(right[i+1])
                            if left[i] == "/":
                                rightX += float(1/right[i+1])
                        if right[i+1] == 'x':
                            if right[i] == "*":
                                rightX += float(right[i-1])
                            if left[i] == "/":
                                rightX += float(1/right[i-1])
                        else:
                            if right[i] == "*" and right[i-1] != 'x' and right[i+1] != 'x':
                                rightVal += (float(right[i+1])
                                             * float(right[i-1]))
                            if right[i] == "/" and right[i-1] != 'x' and right[i+1] != 'x':
                                rightVal += (float(right[i+1]) /
                                             float(right[i-1]))
                    if right[i] == '+':
                        if right[i+1] == 'x':
                            rightX += 1
                        else:
                            if i+1 == len(right) - 1 or right[i+2] not in "*/":
                                rightVal += float(right[i+1])

                    if right[i] == '-':
                        if right[i + 1] == 'x':
                            rightX -= 1
                        else:
                            rightVal -= float(right[i+1])

                if right[0] == 'x' and right[1] in '-+':
                    rightX += 1
                if right[0] != 'x' and right[1] in '-+':
                    rightVal += float(right[0])

            finalX = leftX - rightX
            finalVal = rightVal - leftVal
            final = finalVal / finalX
            return final
    except ZeroDivisionError:
        if 'x' not in equation:
            return "What exactly do you want me to do with this information 🤨"
        else:
            return "x can be anything here broski"
