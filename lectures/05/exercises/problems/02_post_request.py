"""Problem 02: POST request to JSONPlaceholder.

Task:
1. Send POST to https://jsonplaceholder.typicode.com/posts
2. Send JSON payload with fields: title, body, userId
3. Print:
   - status code
   - raw body
   - parsed JSON
4. Confirm response includes your data + id

Note: JSONPlaceholder simulates writes; data is not truly persisted.
"""

import requests

URL = "https://jsonplaceholder.typicode.com/posts"

def main():
    payload = {
        "title": "My First Post",
        "body": "Hello, this is a test post!",
        "userId": 123
    }
    response = requests.post(URL, json=payload)

    print("Status Code:", response.status_code)
    print("Raw Response Body:", response.text)

    json_data = response.json()
    print("Parsed JSON:", json_data)

if __name__ == "__main__":
    main()