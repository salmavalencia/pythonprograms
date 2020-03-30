print("CONVERTIDOR DE SISTEMAS NUMERICOS\n\n")
print("\t1. Binary\n\t2. Octal\n\t3. Decimal\n\t4. Hexadecimal\n\n")
basein = input("Elige el formato del numero introducido: ")
baseout = input("\nElige el formato del cual lo quiere convertir: ")
input1 = input("\nDigite el valor al convertir ")

Arr = [ ]



def convertdec(valor, input2):

    while True:
        resultado = int(input2) % int(valor)
        division = int(input2) / int(valor)
        if resultado == 10:
            Arr.append('A')
        elif resultado == 11:
            Arr.append('B')
        elif resultado == 12:
            Arr.append('C')
        elif resultado == 13:
            Arr.append('D')
        elif resultado == 14:
            Arr.append('E')
        elif resultado == 15:
            Arr.append('F')
        else:
            Arr.append(str(resultado))
        input2 = division
        if int(resultado) == division:
            break

    def convert(list):
        s = [str(i) for i in list]
        res = "".join(s)
        return(res)

    output = str(convert(Arr))[::-1]

    return output


def converttodec(valor, input2):
    length = len(input2)
    index = length - 1
    int(length)
    suma = 0
    i = 0

    while True:
        if input2[index] == 'A':
            suma = suma + (10 * pow(int(valor),i))
        elif input2[index] == 'B':
            suma = suma + (11 * pow(int(valor),i))
        elif input2[index] == 'C':
            suma = suma + (12 * pow(int(valor),i))
        elif input2[index] == 'D':
            suma = suma + (13 * pow(int(valor),i))
        elif input2[index] == 'E':
            suma = suma + (14 * pow(int(valor),i))
        elif input2[index] == 'F':
            suma = suma + (15 * pow(int(valor),i))
        else:
            suma = suma + (int(input2[index]) * pow(int(valor),i))

        index = index - 1
        i = i + 1
        if int(index) == -1:
            break

    return suma

#binario a octal

if basein == '1':
    if baseout == '1':
        #binario a binario
        print(input1)
    if baseout == '2':
        decvalue = converttodec(2,input1)
        final = convertdec(8,str(decvalue))
        print(final)
    if baseout == '3':
        #binario a decimal

        decvalue = converttodec(2,input1)
        print(decvalue)
    if baseout == '4':
        #binario a hex
        decvalue = converttodec(2,input1)
        final = convertdec(16,str(decvalue))
        print(final)
        #convertdec(16,converttodec(2,input1))

if basein == '2':
    if baseout == '1':
        #octal a binario
        decvalue = converttodec(8,input1)
        final = convertdec(2,str(decvalue))
        print(final)

    if baseout == '2':
        print(input1)
    if baseout == '3':
        decvalue = converttodec(8,input1)
        print(decvalue)
    if baseout == '4':
        decvalue = converttodec(8,input1)
        final = convertdec(16,str(decvalue))
        print(final)

if basein == '3':
    if baseout == '1':
        decvalue = convertdec(2,input1)
        print(decvalue)
    if baseout == '2':
        decvalue = convertdec(8,input1)
        print(decvalue)
    if baseout == '3':
        print(input1)
    if baseout == '4':
        decvalue = convertdec(16,input1)
        print(decvalue)
if basein == '4':
    if baseout == '1':
        decvalue = converttodec(16,input1)
        final = convertdec(2,str(decvalue))
        print(final)
    if baseout == '2':
        decvalue = converttodec(16,input1)
        final = convertdec(8,str(decvalue))
        print(final)
    if baseout == '3':
        decvalue = converttodec(16,input1)
        print(decvalue)
    if baseout == '4':
        print(input1)
