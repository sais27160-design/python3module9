"""Problem 03: GET request for HTML content.

Task:
1. Send GET to https://example.com
2. Print:
   - status code
   - Content-Type header
   - HTML body (response.text)
3. Verify content type contains text/html
4. Add raise_for_status()
"""

import requests

URL = "https://example.com"

def main():
    
    response = requests.get(URL, verify=False)
    response.raise_for_status()  

    print("Status Code:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))

    
    if "text/html" in response.headers.get("Content-Type", "").lower():
        print("This is an HTML page.")

    
    print("\nHTML Body Preview:\n", response.text[:500], "...")

if __name__ == "__main__":
    main()
