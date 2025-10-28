def my_function(**kid):
    print("The youngest kid is " + kid["fname"])

my_function(fname = "Bernardo", lname="Pontes")

def my_function(country = "Brazil"):
    print("I am from " + country)

my_function("paraguai")
my_function()

