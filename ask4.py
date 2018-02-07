# -*- coding: utf-8 -*-
#Aσκηση 4

i = 2
while i > 1:
    #Δηλωση αριθμου απο τον χρηστη
    user_input = input("Give an integer number from 0 to 1000000:")
    #έλεγχος του input
    if (user_input > 0 and user_input < 1000000):
        def romannumber(number):
            #Αντιστοίχιση λατινικών με αριθμούς
            numerals={1:"I", 4:"IV", 5:"V", 9: "IX", 10:"X", 40:"XL", 50:"L",
                      90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
            result=""
        #Μετατροπή σε ακεραιο
            for value, numeral in sorted(numerals.items(), reverse=True):
                while number >= value:
                    result += numeral
                    number -= value
            return result
        print romannumber(user_input)
    else:
        print "NOT FOUND"
