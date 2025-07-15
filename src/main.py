from fetch_data import fetch_users_from_api

if __name__ == "__main__":
    users = fetch_users_from_api()
    print(f"Fetched {len(users)} users")
    for user in users:
        print(f"- {user['name']} ({user['email']})")