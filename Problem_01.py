#E-Commerce Order Revenue Analyzer

class Solution:

    def city_revenue(self, orders):
        revenue_dict = {}
        ## Write your code here and don't forget to return value.
        for element in orders:
            if element['city'] in revenue_dict.keys():
                revenue_dict[element['city']]+=element['amount']
            else:
                revenue_dict[element['city']]=element['amount']
        
        max=float('-inf')
        max_city=''
        for key,val in revenue_dict.items():
            if val>max:
                max=val
                max_city=key
        final_list=[]
        final_list.append(revenue_dict)
        final_list.append(max_city)

        return final_list