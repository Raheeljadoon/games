
num_words1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four',
 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
               10: 'Ten', 11: 'Eleven', 12: 'Twelve', 
               13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
                16: 'Sixteen',
               17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
               20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty',
                60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
               90: 'Ninety', 100: 'Hundred'}
num_words2 = {1: 'ten', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
                 6: 'sixty', 7: 'Seventy',8: 'Eighty', 9: 'Ninety'}
num_words3 = {1:'one hundred',2:'two hundred',3:'three hundred',
                4:'four hundred',5:'five hundred',6:'six hundred',
                7:'seven hundred',8:'eight hundred',9:'nine hundred'}
num_words4 = {1:'one thousand',2:'two thousand',3:'three thousand',
                4:'four thousand',5:'five thousand',6:'six thousand',
                7:'seven thousand',8:'eight thousand',9:'nine thousand'}

num = int(input(" enter any number "))
if num < 100:
    if num % 10 == 0:
        print(num_words1[num])

    elif num < 20 :
        print(num_words1[num])
    
    else :
        num_1 = int(num / 10)
        num_2 = num % 10
        print(num_words2[num_1],num_words1[num_2])

elif 100 <= num < 1000:
    if num % 100 == 0 :
    
        num_3 =  int(num / 100 )
        print(num_words3[num_3])

    else :
        num_4 = int(num / 100)
        num_5 = num % 100

        if (num > 110) and (num < 120):
            print( num_words3[num_4], num_words1[num_5])

        elif num_5 % 10 == 0:
            num_4_1 = int(num_5 / 10)
            
            print(num_words3[num_4],"and",num_words2[num_4_1])
        
        else:
            num_4_3 = int(num_5 / 10)
            num_4_4 = num_5 % 10
            print( num_words3[num_4], num_words2[num_4_3], num_words1[num_4_4])


elif num >= 1000:
    if num % 1000 == 0:
        num_6 = int( num / 1000 )
        print(num_words4[num_6])
    else :
        num_7 = int(num / 1000)
        num_8 = num % 1000
        num_8_1 = int(num_8 / 10)
        num_8_2 = num_8 % 10
        print(num_words4[num_7],"and",num_words2[num_8_1],num_words1[num_8_2])
