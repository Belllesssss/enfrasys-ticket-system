import json
import os
from datetime import datetime

# Path to your data
DATA_PATH = '../data/tickets.json'
REPORT_PATH = '../reports/'

def generate_monthly_report():
    # 1. Load Data
    if not os.path.exists(DATA_PATH):
        print("Error: No tickets.json found. Key in some tickets first!")
        return

    with open(DATA_PATH, 'r') as f:
        tickets = json.load(f)

    if not tickets:
        print("No tickets found to report.")
        return

    # 2. Analyze Data
    total_tickets = len(tickets)
    resolved = sum(1 for t in tickets if t['status'] == 'Resolved')
    pending = sum(1 for t in tickets if 'Pending' in t['status'])
    
    # 3. Create Report Content
    report_date = datetime.now().strftime("%B %Y")
    filename = f"Monthly_Maintenance_Report_{datetime.now().strftime('%Y_%m')}.txt"
    
    report_content = f"""
==================================================
M365 MAINTENANCE REPORT - {report_date.upper()}
Prepared by: Protege Solutions Engineer (Enfrasys)
==================================================

SUMMARY OVERVIEW:
-----------------
Total Issues Handled: {total_tickets}
Resolved Issues:      {resolved}
Pending/Escalated:    {total_tickets - resolved}
Efficiency Rate:      {(resolved/total_tickets)*100:.1f}%

DETAILED TROUBLESHOOTING LOG:
-----------------------------
"""
    for t in tickets:
        report_content += f"[{t['date']}] User: {t['user']}\n"
        report_content += f"Status: {t['status']}\n"
        report_content += f"Issue:  {t['issue']}\n"
        report_content += f"Fix:    {t['solution']}\n"
        report_content += "-" * 30 + "\n"

    # 4. Save to /reports/ folder
    full_path = os.path.join(REPORT_PATH, filename)
    with open(full_path, 'w') as f:
        f.write(report_content)

    print(f"Success! Report generated at: {full_path}")

if __name__ == "__main__":
    generate_monthly_report()
