# sales = {   
#     'apple': 2, 
#     'orange': 3, 
#     'grapes': 4 
#     }

# print(sales.values())
# print(sales['apple'])

def profit(info):
    
	return round( ( info['sell_price'] - info['cost_price'] ) * info['inventory'])

test = {
    "cost_price": 32.67,
    "sell_price": 45.00,
    "inventory": 1200
}
print(profit(test))
