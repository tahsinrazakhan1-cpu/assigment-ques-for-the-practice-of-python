# Q1: The QuizNest Exam Review

# Write your reference solution here
ADMIN_BIT = 0b100   # permission: admin (bit 2)
GRADER_BIT = 0b010  # permission: grader (bit 1)
VIEWER_BIT = 0b001  # permission: viewer (bit 0)
PASS_MARK = 40
 
 
def review_submissions(submissions, staff_flags):
    """
    submissions: list of dicts - each has 'student_id' (str), 'score' (int),
                 'minutes' (int)
    staff_flags: int, bit-encoded permissions of the staff member
    Returns    : set of student IDs flagged for manual review
    """
    if not submissions:
        print("No submissions to review")
        return set()
 
    needed = ADMIN_BIT | GRADER_BIT
    if (staff_flags & needed) == needed:
        print("Full report access granted")
    else:
        print("Limited access - summary only")
 
    flagged = set()
    unique_students = set()
    total_minutes = 0
    scores = []
 
    for s in submissions:
        sid = s["student_id"].strip().upper()
        unique_students.add(sid)
        scores.append(s["score"])
        total_minutes += s["minutes"]
 
        if s["score"] < PASS_MARK:
            flagged.add(sid)
 
        if s["score"] == 100 and s["minutes"] < 5:
            flagged.add(sid)
 
    print("Unique students:", len(unique_students))
 
    hours, mins = total_minutes // 60, total_minutes % 60
    print(f"Total exam time: {hours} h {mins} min")
 
    ranked = sorted(scores, reverse=True)
    top3 = ranked[:3]
    print("Top 3 scores:", top3)
 
    print("Flagged students:", sorted(flagged))
    return flagged

# ---------------- Input / output (do not change) ----------------
import json
data = json.loads(input())
result = review_submissions(data["submissions"], data["staff_flags"])
print("Returned:", sorted(result))
