# Affirm partners with a lot of merchants today and many users will make purchases at more than one merchant.
# We'd like to analyze that cross purchasing behavior to make recommendations to new user about where else they might like to shop.
# Imagine we have a list where each entry is an individual user's history of purchases,
# i.e., the list of merchants that the user has made a purchase at.
# We want to take that list and find, for any merchant with at least one purchase, what other merchant(s) are most frequently seen in users' shopping behavior.

# e.g. [['Casper', 'Purple', 'Wayfair'],['Purple', 'Wayfair', 'Tradesy'],['Wayfair', 'Tradesy', 'Peloton']]

# [['Casper', 'Purple', 'Wayfair'],['Purple', 'Wayfair', 'Tradesy'],['Wayfair', 'Tradesy', 'Peloton']] =>
# {
#    'Casper': ['Purple', 'Wayfair'],
#    'Purple': ['Wayfair'],
#    'Wayfair': ['Purple', 'Tradesy'],
#    'Tradesy': ['Wayfair'],
#    'Peloton': ['Wayfa‍‍ir', 'Tradesy']
# }

from collections import defaultdict, Counter

purchases = [['Casper', 'Purple', 'Wayfair'],['Purple', 'Wayfair', 'Tradesy'],['Wayfair', 'Tradesy', 'Peloton']]

def get_most_frequent_merchants(purchases):
    related_merchant_map = defaultdict(Counter)
    for purchase in purchases:
        merchant_counter = Counter(purchase)
        for merchant in purchase:
            tmp_merchant_counter = merchant_counter.copy()
            tmp_merchant_counter.pop(merchant)
            related_merchant_map[merchant].update(tmp_merchant_counter)
    # print(related_merchant_map)

    res = {}
    for k, v in related_merchant_map.items():
        sorted_merchant_count = sorted(v.items(), reverse=True)
        max_count = sorted_merchant_count[0][1]
        res[k] = [sorted_merchant_count[0][0]]
        for i in range(1, len(sorted_merchant_count)):
            if sorted_merchant_count[i][1] == max_count:
                res[k].append(sorted_merchant_count[i][0])
    print(res)

get_most_frequent_merchants(purchases)


