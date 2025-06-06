
CLASS_LABELS = {
    0: "Leave Request",
    1: "Workplace Harassment",
    2: "Payroll Discrepancy",
    3: "Promotion Query",
    4: "Workplace Safety",
    5: "Salary Delay",
    6: "Unfair Treatment",
    7: "Workload Issue",
    8: "Transfer Request",
    9: "Resignation Concern",
    10: "Work From Home Request",
    11: "Remote Work Issue",
    12: "Manager Misconduct",
    13: "Training Need",
    14: "Resource Request",
    15: "Mental Health Concern",
    16: "Appraisal Issue",
    17: "Team Conflict",
    18: "IT Support Request",
    19: "Onboarding Issue",
    20: "Policy Clarification",
    21: "Workplace Discrimination",
    22: "Facilities Issue",
    23: "Reimbursement Delay",
    24: "Holiday Confusion",
    25: "Contract Clarification",
    26: "Overtime Payment",
    27: "Leave Balance Error",
    28: "Health Insurance Query",
    29: "Feedback Submission",
    30: "Travel Expense Issue",
    31: "Access Rights Problem",
    32: "Login Issue",
    33: "Career Development",
    34: "Probation Concern",
    35: "Laptop Request",
    36: "Promotion Denial",
    37: "Flexible Timing Request",
    38: "Workplace Cleanliness",
    39: "Transport Request",
    40: "Shift Change Request",
    41: "Relocation Query",
    42: "Medical Emergency Leave",
    43: "Retirement Process Query",
    44: "Exit Interview Feedback",
    45: "Workstation Issue",
    46: "Security Concern",
    47: "Bonus Clarification",
    48: "Attendance Discrepancy",
    49: "Project Allocation Issue",
    50: "Team Collaboration Issue",
    51: "Salary Issue"
}

TEMPLATES = {}

for class_id, label in CLASS_LABELS.items():
    TEMPLATES[class_id] = {
        "empathetic": f"We truly understand your concern regarding {label.lower()}. Please know that we are here to support you. Issue reported: {{text}}",
        "formal": f"Your grievance related to {label.lower()} has been received and will be addressed as per company policy. Details: {{text}}",
        "assertive": f"The matter of {label.lower()} is noted and will be acted upon urgently. Submitted issue: {{text}}"
    }
