"""Problem 07 (part B): messenger sender client.

Task:
1. Split into pairs
2. Write an infinite loop reading message text from terminal
3. Send each message to partner API endpoint /messages
4. Show send status in terminal


Partner setup:
- Partner gives you ngrok public URL
- You set TARGET_BASE_URL to that URL
"""

import requests

TARGET_BASE_URL = "https://ellipsoidal-cisternal-thi.ngrok-free.dev"
SENDER_NAME = "Sai"


def main() -> None:
    print("Messenger started. Type messages (Ctrl+C to stop)\n")

    while True:
        try:
            text = input("You: ").strip()

            if not text:
                continue  

            
            payload = {
                "sender": SENDER_NAME,
                "text": text
            }

            
            response = requests.post(
                f"{TARGET_BASE_URL}/messages",
                json=payload
            )

            response.raise_for_status()

            print(f"Sent! Status: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"Failed to send: {e}")

        except KeyboardInterrupt:
            print("\nExiting messenger...")
            break
    


if __name__ == "__main__":
    main()
