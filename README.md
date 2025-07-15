# Compliance Audit Automation Simulator

This project automates compliance checks for user data, generates violation reports, and identifies duplicate companies. It fetches user data from an API, checks for compliance issues, and saves reports in CSV and JSON formats.

## Features

- Fetches user data from a public API
- Checks for compliance violations:
  - Missing email
  - Username too short
  - Username contains numbers
- Identifies companies with duplicate users
- Generates and saves reports in CSV and JSON formats

## Project Structure

```
src/
├── audit_checker.py        # Compliance checking logic
├── fetch_data.py           # Fetches user data from API
├── main.py                 # Main entry point
├── report_generator.py     # Report generation and saving
reports/
└── ...                     # Generated reports
requirements.txt            # Python dependencies
```

## Getting Started

### Prerequisites

- Python 3.8+
- `requests` library

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/compliance-audit-automation-simulator.git
    cd compliance-audit-automation-simulator
    ```
2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Usage

Run the main script:
```sh
python src/main.py
```

Reports will be saved in the `reports/` directory.

## Example Output

- Lists compliance violations per user
- Lists companies with duplicate users
- Saves detailed reports in CSV and JSON formats

## License

MIT License

##
