# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

extra_payment_start_month = int(input('Which month should extra payment start in?').strip() or "61")
extra_payment_end_month = int(input('Which month should extra payment end in?').strip() or "109")
extra_payment = int(input('How much extra payment per month can you afford?').strip() or "1000")

while principal > 0:
    months = months + 1
    this_months_payment = payment

    if months > extra_payment_start_month and months <= extra_payment_end_month:
        this_months_payment = payment + extra_payment
    
    if this_months_payment > principal * (1+rate/12):
      this_months_payment = principal * (1+rate/12)

    principal = principal * (1+rate/12) - this_months_payment
      
    total_paid = total_paid + this_months_payment
    print(months, round(total_paid, 2), round(principal, 2))

print('Total paid', round(total_paid, 2))
print('Months', months)
