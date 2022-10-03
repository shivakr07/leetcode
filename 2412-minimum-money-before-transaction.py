class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        
        
#         def compare(x, y):            
#             if min(-x[0],-x[0] + x[1] - y[0]) < min(-y[0],-y[0] + y[1] - x[0]):
#                 return -1
#             if min(-x[0],-x[0] + x[1] - y[0]) == min(-y[0],-y[0] + y[1] - x[0]):
#                 if x[0] < y[0]:
#                     return -1
#                 else:
#                     return 1
#             else:
#                 return 1

#         transactions.sort(key = cmp_to_key(compare))
        dip = 0
        ans = 0
        # print(transactions)
        transactions.sort(key = lambda x : [x[1]])
        print(transactions)
        curr_money = 0
        ans = 0
        for a, b in transactions:
            curr_money -= a
            ans = min(ans, curr_money)
            curr_money += b
        print(abs(ans))
        return abs(ans)
            
        # for a, b in transactions:
        #     ans = min(dip-a, ans)
        #     dip = dip + b
        # print(abs(dip) + transactions[-1][1])
        # x = abs(dip) + transactions[-1][1]
        return x