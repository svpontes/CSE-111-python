import requests
from requests import status_codes

def main():
    
    url = input("Enter the url you want to test: ")
    url_to_test = get_status(url)
    
    if url_to_test == 200:
        print(f" The status code for {url} is :  {url_to_test}")
    else:
        print(f" The status code for {url} is: {url_to_test} - TEST FAILLURE")
    
def get_status(url):
  
    r = requests.get(url)
    return r.status_code
    
if __name__ == "__main__":
    main()