import requests
import create_oauth_token

# https://developer.ups.com/api/reference?loc=en_US#tag/Rating

access_token = create_oauth_token.get_oauth_token()
version = "v2403"
requestoption = "Rate"

url = "https://wwwcie.ups.com/api/rating/" + version + "/" + requestoption

payload = {
    "RateRequest": {
        "Request": {
            "TransactionReference": {
                "CustomerContext": "CustomerContext"
            }
        },
        "Shipment": {
            "Shipper": {
                "Name": "Ted Kaczynski",
                "Address": {
                    "AddressLine": [
                        "515 S Wisconsin Ave",
                        "Suite F"
                    ],
                    "City": "Gaylord",
                    "StateProvinceCode": "MI",
                    "PostalCode": "49735",
                    "CountryCode": "US"
                }
            },
            "ShipTo": {
                "Name": "Quentin Tarantino",
                "Address": {
                    "AddressLine": [
                        "1211 Beaumont Ave",
                        "Unit G"
                    ],
                    "City": "Knoxville",
                    "StateProvinceCode": "TN",
                    "PostalCode": "37921",
                    "CountryCode": "US"
                }
            },
            "Service": {
                "Code": "03",  # 03 means ground shipping. i am assuming this one will be used most of the times. however, it does have an option to provide
                "Description": "Ground"
            },

            # Package information:
            "Package": [
                {
                "PackagingType": {
                    "Code": "02",  # 02 means package
                    "Description": "Packaging"
                },
                "Dimensions": {
                    "UnitOfMeasurement": {
                        "Code": "IN",
                        "Description": "Inches"
                    },
                    "Length": "5",
                    "Width": "5",
                    "Height": "5"
                },
                "PackageWeight": {
                    "UnitOfMeasurement": {
                        "Code": "LBS",
                        "Description": "Pounds"
                    },
                    "Weight": "5"
                }
            },
                {
                "PackagingType": {
                    "Code": "02",  # 02 means a package
                    "Description": "Packaging"
                },
                "Dimensions": {
                    "UnitOfMeasurement": {
                        "Code": "IN",
                        "Description": "Inches"
                    },
                    "Length": "30",
                    "Width": "10",
                    "Height": "6"
                },
                "PackageWeight": {
                    "UnitOfMeasurement": {
                        "Code": "LBS",
                        "Description": "Pounds"
                    },
                    "Weight": "24"
                }
            },
            ]
        }
    }
}



headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}"
}

response = requests.post(url, json=payload, headers=headers)

data = response.json()
print(data) # the entire response
print(data['RateResponse']['RatedShipment']['TotalCharges'])  # gets the total cost of all the packages described in the Package field of the payload
