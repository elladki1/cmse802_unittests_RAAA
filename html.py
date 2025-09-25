#def load_html(source: str) -> str
def load_html(url):
       """
       Accepts a url (string) and returns the source html of a webpage.
       """
       import requests

       try:
         response = requests.get(url)
         return response.text # Return the HTML content of the page for valid URLs
       
       except requests.exceptions.RequestException as e:
         print(f"Error fetching URL {url}: {e}")
         return None # Return None for invalid URLs or request errors, print the error (above)