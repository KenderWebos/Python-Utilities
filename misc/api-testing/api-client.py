import requests

def main():
    url = "http://45.7.231.76/api/ping"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        result = response.json()

        for key, value in result.items():
            print(f"{key}: {value}")

        # print(result)
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
    
    input()

if __name__ == "__main__":
    main()