import time
def cal_prod():
    product = 1
    for i in range(1, 1000):
        product *= i
    return product

start_time = time.time()
prod = cal_prod()
end_time = time.time()
print(f"Product: {prod}")
