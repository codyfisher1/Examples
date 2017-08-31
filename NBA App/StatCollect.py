

def average(Array):
    return round(sum(Array)/max(len(Array),1),2)
   
def element_difference(Array,Number):
    element_difference.difference_array = []
    for p in Array:
        diff = round(p  - Number,2)
        element_difference.difference_array.append(diff)

def element_square(Array):
    element_square.squared_array = []
    for p in Array:
        square = round(p*p,2)
        element_square.squared_array.append(square)

def element_multiply(Array1,Array2):
    element_multiply.multiply_array = []
    for p in range(0, len(Array1)):
        mult = round(Array1[p]*Array2[p],2)
        element_multiply.multiply_array.append(mult)

def Standard_Deviation(Array):
    Standard_Deviation.Dev_Array = []
    Avg = average(Array)
    element_difference(Array,Avg)
    Sub_Avg = element_difference.difference_array
    element_square(Sub_Avg)
    Sub_Avg_Sqr = element_square.squared_array
    Summation_Sub_Avg_Sqr = sum(Sub_Avg_Sqr)
    Length = len(Sub_Avg_Sqr)
    Standard_Dev = round(((Summation_Sub_Avg_Sqr)/(Length - 1))**(1/2),2)
    Standard_Deviation.Dev_Array.append(Standard_Dev)

def Correlation_Coef(Array1,Array2):
    Correlation_Coef.r_array = []
    Avg1 = average(Array1)
    element_difference(Array1,Avg1)
    Sub_Avg1 = element_difference.difference_array
    element_square(Sub_Avg1)
    Sub_Avg_Sqr1 = element_square.squared_array
    Summation_Sub_Avg_Sqr1 = sum(Sub_Avg_Sqr1)
    
    Avg2 = average(Array1)
    element_difference(Array2,Avg2)
    Sub_Avg2 = element_difference.difference_array
    element_square(Sub_Avg2)
    Sub_Avg_Sqr2 = element_square.squared_array
    Summation_Sub_Avg_Sqr2 = sum(Sub_Avg_Sqr2)

    
    element_multiply(Sub_Avg1,Sub_Avg2)
    Sub_Avg1_times_Sub_Avg2 = element_multiply.multiply_array
    Summation_Sub_Avg1_times_Sub_Avg2 = sum(Sub_Avg1_times_Sub_Avg2)

    r = round((Summation_Sub_Avg1_times_Sub_Avg2)/((Summation_Sub_Avg_Sqr1*Summation_Sub_Avg_Sqr2)**(1/2)),2)
    r2 = r*r
    Correlation_Coef.r_array.append(r)