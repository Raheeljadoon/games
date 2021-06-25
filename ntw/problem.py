
num_words1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
               10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
               17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
               20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
               90: 'Ninety', 100: 'Hundred'}
num_words2 = {1: 'ten', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'Seventy',
               8: 'Eighty', 9: 'Ninety'}

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