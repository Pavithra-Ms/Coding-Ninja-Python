#
#Fahrenheit to Celsius Table
#Send Feedback
#Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.
#Input Format :
#3 integers - S, E and W respectively 
#Output Format :
#Fahrenheit to Celsius conversion table. One line for every Fahrenheit and corresponding Celsius value. On Fahrenheit value and its corresponding Celsius value should be separate by tab ("\t")
#Sample Input :
#0 
#100 
#20
#Sample Output :
#0   -17
#20  -6
#40  4
#60  15
#80  26
#100 37

s=int(input())
e=int(input())
w=int(input())
while True:
    c=0
    if s<=e:
        c=(s-32)*5/9
        print(s,int(c))
        s = s + w

    else:break
