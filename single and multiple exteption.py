# single

try:
    result=10/0
    print(result)

except:
    print("dibision by zero")    


try:
    with open("arafat islam.text","r")as file:
        content = file.read()
        print(content)
        result=10/0
        print(result)

except Exception as e:
    print("e") 

finally:
    print("Exception complete")           

             