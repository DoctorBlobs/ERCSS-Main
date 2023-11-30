import json

def save_credentials(data):
    # Save the data to the JSON file
    with open('credentials.json', 'w') as file:
        json.dump(data, file, indent=2)

def add_camera_credentials():
    # Get user input for credentials
    username = input("Enter username: ")
    password = input("Enter password: ")
    ip_address = input("Enter IP address: ")

    return {
        'username': username,
        'password': password,
        'ip_address': ip_address
    }
    
def get_all_cameras(data):
    # Return a list of all cameras from the credentials
    return list(data.keys())

def extraction(credentials_data):
    # Read credentials from the JSON file
    credentials_data = read_credentials()
    
    extracted_credentials = []

    for _, credentials_list in credentials_data.items():
        if isinstance(credentials_list, list):
            for credentials in credentials_list:
                if isinstance(credentials, dict):
                    username = credentials.get('username')
                    password = credentials.get('password')
                    ip_address = credentials.get('ip_address')

                    if username and password and ip_address:
                        extracted_credentials.append((username, password, ip_address))
    if not credentials_data:
        print("No credentials found.")
    
    return extracted_credentials

def password_save_process():
    # Load existing data from the file
    try:
        with open('credentials.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist or is not a valid JSON, start with an empty dictionary
        data = {}

    show_or_add = input("Add or Show")
    if show_or_add == "add":
        # Allow the user to add multiple sets of credentials
        while True:
            camera_label = f"camera_{len(data) + 1}"
            credentials = add_camera_credentials()

            # Add new credentials to the data
            if camera_label not in data:
                data[camera_label] = []
            data[camera_label].append(credentials)

            # Ask the user if they want to add more credentials
            more_credentials = input("Do you want to add more credentials? (yes/no): ").lower()
            if more_credentials != 'yes':
                break
    else:
        all_cameras = get_all_cameras(data)
        print("List of all cameras:", all_cameras)

    # Save the updated data to the file
    save_credentials(data)

def read_credentials():
    try:
        with open('credentials.json', 'r') as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error reading credentials file.")
        return {}

#password_save_process()
