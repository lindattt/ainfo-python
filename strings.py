#slides 17-25 python2.pdf,  lezione 5

# quotes
a = """I am a string spanning in 3 rows, ... containing 'sigle quotes',
... containing "double quotes",
... containing '''triple quotes''' """

print(a)


# slicing
str1 = "Parola"
str2 = "ABCDEFGHIJKL"

print("slicing:", str1[0], str2[0:2])


# string operations
p1 = "Provo"
p2 = "a"+"comporre"+"una"
p3 = "frase"
p = p1+p2+p3

print(p1+p2+p3, p)
print(p1+" "+p2+" "+p3)
print(str2[1]+str2[4]+str2[11]*2) #BELL

planet = "Earth"
adj = "amazing"
str3 = "We live on planet %s" %planet
str4 = "We live on planet %s and it is %s" %(planet,adj)

print(str3, "\n", str4)


# escape characters
print("Trying\tto\nfit\tall escape characters (\\,\",\') in one sentence")


# raw string
rstr = r'is this \n raw string'
print(rstr)
 
