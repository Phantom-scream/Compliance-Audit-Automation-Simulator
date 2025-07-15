import csv
import json
import os
from datetime import datetime

def save_report(violations, duplicate_companies):
    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_file = f"reports/compliance_report_{timestamp}.csv"
    json_file = f"reports/compliance_report_{timestamp}.json"

    # CSV
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["User ID", "Name", "Email", "Violations"])
        for v in violations:
            writer.writerow([v["user_id"], v["name"], v["email"], "; ".join(v["issues"])])

    # JSON
    report = {
        "violations": violations,
        "duplicate_companies": duplicate_companies,
        "generated_at": timestamp
    }

    with open(json_file, 'w') as f:
        json.dump(report, f, indent=4)

    print(f"\n Reports saved to:\n- {csv_file}\n- {json_file}")