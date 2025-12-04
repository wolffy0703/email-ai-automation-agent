def categorize_email(email):
    subject = (email.get("subject") or "").lower()
    body = (email.get("body") or "").lower()
    if "invoice" in subject or "invoice" in body or "payment" in body:
        return "Finance / Invoice"
    if "password" in subject or "reset" in subject or "token" in body:
        return "Support"
    if "collaborat" in subject or "collaborat" in body or "proposal" in body:
        return "Partnership / Outreach"
    if "urgent" in subject or "asap" in body:
        return "Urgent"
    return "General"
