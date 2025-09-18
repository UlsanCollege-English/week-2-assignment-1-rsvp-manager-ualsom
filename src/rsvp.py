from typing import List, Tuple


def dedupe_emails_case_preserve_order(emails: List[str]) -> List[str]:
    seen = set()
    result = []
    for email in emails:
        if '@' not in email:
            continue
        lower_email = email.lower()
        if lower_email not in seen:
            seen.add(lower_email)
            result.append(email)
    return result


def first_with_domain(emails: List[str], domain: str) -> int | None:
    domain = domain.lower()
    for i, email in enumerate(emails):
        if '@' not in email:
            continue
        _, email_domain = email.rsplit('@', 1)
        if email_domain.lower() == domain:
            return i
    return None


def domain_counts(emails: List[str]) -> List[Tuple[str, int]]:
    counts = {}
    for email in emails:
        if '@' not in email:
            continue
        _, domain = email.rsplit('@', 1)
        domain_lower = domain.lower()
        counts[domain_lower] = counts.get(domain_lower, 0) + 1
    return sorted(counts.items())
