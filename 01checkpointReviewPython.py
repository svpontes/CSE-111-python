"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum.
"""

age = int(input("What is your age ?"))
heart_rate = 220 - age
min_rate_round =round(0.65*heart_rate)
max_rate_round = round(0.85*heart_rate)
print("When you exercise to strengthen your heart, you should keep your heart rate between", min_rate_round, "and" , max_rate_round, "beats per minutes.")
