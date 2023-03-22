print("""
       |-------------------------------------------------------------------------------------|
       |This script can get the roots of equations like x²+x+5=0 or any rank up|
       |-------------------------------------------------------------------------------------|
       """)
equation=int(input("===Enter equation rank 1 to 3(for fast result) or up: "))+1
answer=float(input("===Equation =? : "))
#i=0
#a,b,c,d=0,0,0,0
#fs1,fs2,fs3,fs4="    "
def y():
    nrd=int(input("===Num Of Digits After ',' 2 for 0.00 3 for 0.000 or any: "))  #num_results_digits
    nrdx=str(float(nrd/(10**nrd)))
    x=float(input("===Enter x start point: "))
    l= float(input("===Enter x reach limit: "))
    r=0
    print("==="+"Enter numerical coefficients")
    xx=0
    numerical_coefficients=[]
    while(int(xx)< equation):   
        numerical_coefficients.append(float(input("===Enter numerical number "+str(xx+1)+": ")))
        xx=xx+1
    #a=float(input("enter the (a) value"))
    #b=float(input("enter the (b) value"))
    #c=float(input("enter the (c) value"))
    #d=float(input("enter the (d) value"))
    while (float(x)<=float(l)):
        serie1=0
        cashe1=0
        #for (int(i) < equation):
        for i in range(equation):
            cashe1=cashe1+(numerical_coefficients[i]*(x**(equation-i)))
                           
        serie1=cashe1
        serie2=0
        cashe2=0
        #for int(i) < equation:
        for i in range(equation):
            cashe2=cashe2+(numerical_coefficients[i]*(r**(equation-i)))
        serie2=cashe2
        #f=(a*(x**3))+(b*(x**2))+(c*(x**1))+d
        #f1=(a*(r**3))+(b*(r**2))+(c*(r**1))+d
        #variables=[x,r,f,f1]
        #var_str=[fs1,fs2,fs3,fs4]
        #i=0
        #while (i<4):
         #   var_str[i]=str(float(variables[i]))
          #  i=i+1
        fs1=str(float(x))
        fs2=str(float(r))
        fs3=str(float(serie1))
        fs4=str(float(serie2))
        r=x
        x=x+float(nrdx[0:nrd])
        #print("==="+serie1,serie2)
        if float(serie1)*float(serie2)<0 :
            print("==="+"x range: ["+fs2[0:4]+" to",fs1[0:4]+"] ,","f(x) range: ["+fs4[0:6]+" to",fs3[0:6]+"]")
def result(answer):
    func_list=[y(),1,2,3]#1,2 and 3 replace other functions will add later
    if answer==0:
        func_list[0]
    else:
        print("==="+"Can't give an answer right now come back later")
    #func_list[answer]

#func_list[equation]
result(answer)
