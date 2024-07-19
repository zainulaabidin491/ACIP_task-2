# Define constants for prices and discounts
PRICES = {
  'Sunday': {'day': 2.00, 'night': 2.00},
  'Monday': {'day': 10.00, 'night': 2.00},
  'Tuesday': {'day': 10.00, 'night': 2.00},
  'Wednesday': {'day': 10.00, 'night': 2.00},
  'Thursday': {'day': 10.00, 'night': 2.00},
  'Friday': {'day': 10.00, 'night': 2.00},
  'Saturday': {'day': 3.00, 'night': 2.00}
}
DISCOUNT_10 = 0.10
DISCOUNT_50 = 0.50

# Define a function to calculate the check digit for a frequent parking number
def calculate_check_digit(frequent_parking_number):
  digits = [int(d) for d in str(frequent_parking_number)]
  check_digit = sum(digits[:-1]) % 11
  return check_digit == digits[-1]

# Define a function to calculate the price to park
def calculate_price(day, hour, num_hours, frequent_parking_number=None):
  price_per_hour = PRICES[day]['day' if hour < 16 else 'night']
  discount = DISCOUNT_10
  if hour >= 16 and hour < 24:
    discount = DISCOUNT_50
  if frequent_parking_number and calculate_check_digit(frequent_parking_number):
    discount *= 2
  price = num_hours * price_per_hour * (1 - discount)
  return price

# Define a function to keep a daily total of payments
def keep_daily_total():
  daily_total = 0
  while True:
    amount_paid = float(input("Enter amount paid: "))
    daily_total += amount_paid
    print(f"Daily total: {daily_total:.2f}")
    response = input("Another customer? (y/n): ")
    if response.lower() != 'y':
      break
  print(f"Daily total: {daily_total:.2f}")

# Define a function to calculate the price to park with the new pricing scheme
def calculate_price_new(day, hour, num_hours, frequent_parking_number=None):
  if hour < 16:
    price = calculate_price(day, hour, num_hours, frequent_parking_number)
  else:
    morning_hours = min(16 - hour, num_hours)
    evening_hours = num_hours - morning_hours
    morning_price = calculate_price(day, hour, morning_hours, frequent_parking_number)
    evening_price = calculate_price(day, 16, evening_hours, frequent_parking_number)
    price = morning_price + evening_price
  return price

# Test the program
day = input("Enter day: ")
hour = int(input("Enter hour of arrival: "))
num_hours = int(input("Enter number of hours to park: "))
frequent_parking_number = input("Enter frequent parking number (optional): ")
if frequent_parking_number:
  frequent_parking_number = int(frequent_parking_number)

price = calculate_price(day, hour, num_hours, frequent_parking_number)
print(f"Price to park: {price:.2f}")

keep_daily_total()

price_new = calculate_price_new(day, hour, num_hours, frequent_parking_number)
print(f"New price to park: {price_new:.2f}")