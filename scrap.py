def DetermineCoupon(total_spent):
    coupon = float()
    if total_spent >= 100 and total_spent <=150:
        coupon = 0.10
    elif total_spent > 150 and total_spent <= 200:
        coupon = 0.20
    else:
        coupon = 0.30

    return coupon

def DetermineSale(sale, coupon):
    total_sale = float()

    total_sale = sale - (sale * coupon)

    print("The total spent:  ", total_sale)

def main():
    customer_total = float()
    customer_coupon = float()

    customer_total = float(input("Enter the total spent:  "))

    customer_coupon = DetermineCoupon(customer_total)
    print("Customer Coupon:  ", customer_coupon)

    DetermineSale(customer_total, customer_coupon)

main()

