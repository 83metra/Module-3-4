def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) == 1:
        return number
    else:
        #print('Длина под else', len(str_number)) #
        return first * get_multiplied_digits(int(str_number[1:])) #каким-то неведомым образом пропускаются срезы,
                                                                  # в которых стоит ноль

result = get_multiplied_digits(40203)
print(result)