

class Converter:

    def num_lists(self,num, suffix):
        Empty = ""

        list_1 = [Empty, "One ", "Two ", "Three ", "Four ", "Five ", "Six ",
        "Seven ", "Eight ", "Nine ", "Ten ", "Eleven ", "Twelve ",
        "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ",
        "Seventeen ", "Eighteen ", "nineteen"]

        list_2 = [Empty, Empty, "Twenty ", "Thirty ", "Forty ", "Fifty ",
        "Sixty ", "Seventy ", "Eighty ", "Ninety "]
        if num == 0:
            return Empty

        if num > 19:

            return list_2[num // 10] + list_1[num % 10]+ suffix 

        else:
            return list_1[num]  + suffix

    def convert_To_Words(self):

        num = int(input("enter number to convert :")) 
        
        
        result = self.num_lists((num // 100000)% 100, "Lakh ")

        result += self.num_lists((num //1000 )% 100 , " Thousand ")

        result += self.num_lists((num // 100 ) % 10 , "Hundred " )

        if num > 100 and num % 100:
            result += " and "
            

        result += self.num_lists((num % 100), "")

        return result


    
s = Converter()

print(s.convert_To_Words())



