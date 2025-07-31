from sjf_algo import sjf_scheduler
from results import print_results

orders = [          # Input orders
    ("ORD1", 0, 5),
    ("ORD2", 1, 6),
    ("ORD3", 2, 4)
]

result = sjf_scheduler(orders)

print_results(orders, result)
