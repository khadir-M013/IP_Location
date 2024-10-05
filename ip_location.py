import time
import requests
import logo
logo.logo()

print(f"\033[1;33m_"*60)
def get_location(ip_address):
    try:
        # Send a request to the ipinfo.io API
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            location_info = {
                'IP': data.get("ip"),
                "City": data.get("city"),
                "Region": data.get("region"),
                "Country": data.get("country"),
                "Location": data.get("loc"),  # Latitude and Longitude
                "Postal": data.get("postal"),
                "Timezone": data.get("timezone"),
            }
            return location_info
        else:
            print("error")
    except Exception as e:
        return {"error": str(e)}

# Example usage
# Replace with the desired IP address
ip_address = input("please enter ip address: ")
print(ip_address)
location = get_location(ip_address)
print(location)