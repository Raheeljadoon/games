single_num = {1 :'one', 2 :'two', 3:'three', 4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fiften',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
double_num = {20:'twenty',30:'thirty',40:'fourty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninty'}
num = int(input("enter any number  "))
if 0 < num < 20:
    print(single_num[num])
elif 19 < num < 100:
    print(double_num[num])