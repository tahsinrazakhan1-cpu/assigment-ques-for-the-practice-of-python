# Q2: The FitPulse Check-in Audit

MANAGER_BIT = 0b100     # permission: manager (bit 2)
TRAINER_BIT = 0b010     # permission: trainer (bit 1)
FRONT_DESK_BIT = 0b001  # permission: front desk (bit 0)
MAX_MINUTES = 120
 
 
def audit_checkins(checkins, staff_flags):
    """
    checkins   : list of dicts - each has 'member_id' (str), 'minutes' (int),
                 'fee' (float), 'guest' (bool)
    staff_flags: int, bit-encoded permissions of the staff member
    Returns    : set of member IDs flagged for manual review
    """
    if not checkins:
        print("No check-ins to audit")
        return set()
 
    # 1. Full report is only for staff who are BOTH manager and trainer
    needed = MANAGER_BIT | TRAINER_BIT
    if (staff_flags & needed) == needed:
        print("Full report access granted")
    else:
        print("Limited access - summary only")
 
    flagged = set()
 
    # 2. Flag sessions of 120 minutes or more
    for c in checkins:
        if c["minutes"] >= MAX_MINUTES:
            flagged.add(c["member_id"])
 
    # 3. Flag invalid records: negative minutes OR negative fee
    for c in checkins:
        if c["minutes"] < 0 or c["fee"] < 0:
            flagged.add(c["member_id"])
 
    # 4. Flag free check-ins made by members (not guests)
    for c in checkins:
        if c["fee"] == 0 and not c["guest"]:
            flagged.add(c["member_id"])
 
    # 5. Percentage of guest check-ins
    guest_count = sum(1 for c in checkins if c["guest"])
    guest_pct = guest_count / len(checkins) * 100
    print(f"Guest check-ins: {guest_pct:.1f}%")
 
    # 6. Show the most recent check-in (last record in the list)
    last = checkins[-1]
    print("Last check-in:", last["member_id"])
 
    print("Flagged members:", sorted(flagged))
    return flagged
 
 
# ---------------- Input / output (do not change) ----------------
import json
 
data = json.loads(input())
result = audit_checkins(data["checkins"], data["staff_flags"])
print("Returned:", sorted(result))
