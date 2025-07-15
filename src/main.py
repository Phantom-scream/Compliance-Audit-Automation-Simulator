from fetch_data import fetch_users_from_api
from audit_checker import check_compliance
from report_generator import save_report

if __name__ == "__main__":
    users = fetch_users_from_api()

    print(f"\nFetched {len(users)} users")

    violations, duplicate_companies = check_compliance(users)

    print("\n Compliance Violations:")
    for v in violations:
        print(f"- {v['name']} ({v['email']}): {', '.join(v['issues'])}")

    print("\n Duplicate Companies:")
    for company in duplicate_companies:
        print(f"- {company}")
    save_report(violations, duplicate_companies)