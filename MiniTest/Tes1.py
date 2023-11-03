first_number = 1
last_number = 100
array_data_number = []

for i in range(first_number, last_number+1):
    array_data_number.append(i)

array_data_number.reverse()

for num in array_data_number:
    if(num > 1):
        for i in range(2, num):
            #check not prime
            if(num%i == 0):
                #change print
                if(num%3 == 0 and num%5 == 0):
                    print("FooBar", end=", ")
                elif(num%3 == 0):
                    print("Foo", end=", ")
                elif(num%5 == 0):
                    print("Bar", end=", ")
                else:
                    print(num, end=", ")
                break
    else:
        print(num)
