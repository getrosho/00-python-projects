import requests
import random
# This script fetches a random joke from the FreeAPI and prints it.

def fetch_random_jokes():
    url = "https://api.freeapi.app/api/v1/public/randomjokes"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Check if the structure is valid and successful
        if data.get("success") and "data" in data and "data" in data["data"]:
            jokes_list = data["data"]["data"]  # The inner "data" is a list of jokes

            if jokes_list:
                # You can loop through all jokes, or pick one
                joke = random.choice(jokes_list)["content"]
                # joke = jokes_list[0]["content"]  # Get the first joke
                return joke
            else:
                raise Exception("No jokes found in the response.")
        else:
            raise Exception("Unexpected response structure or unsuccessful request.")
    else:
        raise Exception(f"API request failed with status code {response.status_code}")

def main():
    try:
        joke = fetch_random_jokes()
        print(f"Here's a random joke for you: {joke}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
