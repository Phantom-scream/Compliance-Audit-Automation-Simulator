def check_compliance(users):
    violations = []

    company_count = {}

    for user in users:
        user_issues = []
        user_id = user.get('id')
        name = user.get('name', '')
        email = user.get('email', '')
        username = user.get('username', '')
        company = user.get('company', {}).get('name', '')

        if not email:
            user_issues.append("Missing email")

        if len(username) < 5:
            user_issues.append("Username too short")

        if any(char.isdigit() for char in username):
            user_issues.append("Username contains numbers")

        company_count[company] = company_count.get(company, 0) + 1

        if user_issues:
            violations.append({
                "user_id": user_id,
                "name": name,
                "email": email,
                "issues": user_issues
            })

    duplicate_companies = [name for name, count in company_count.items() if count > 1]

    return violations, duplicate_companies