"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

print("\n------------Heart Rate Program-------------\n")
user_age = int(input("How old are you? : "))

maximun_heart_rate_per_minute = 220 - user_age
beats_at_65_percent = maximun_heart_rate_per_minute * 0.65
beats_at_85_percent = maximun_heart_rate_per_minute * 0.85

print(f"\nWhen exercising to strengthen your heart, you should \nkeep your heart rate between {beats_at_65_percent:.0f} and {beats_at_85_percent:.0f} per minute\n")

x = "sun"
y = "moon"
z = "stars"
print (x, y, z, sep="|", flush=True )