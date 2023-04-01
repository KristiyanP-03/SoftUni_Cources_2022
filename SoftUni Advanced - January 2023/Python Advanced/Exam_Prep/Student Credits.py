def students_credits(*courses):
    total_credits = 0
    course_credits = {}
    for course in courses:
        name, credits, max_points, diyan_points = course.split('-')
        credits = int(credits)
        max_points = int(max_points)
        diyan_points = int(diyan_points)
        diyan_credits = diyan_points / max_points * credits
        total_credits += diyan_credits
        course_credits[name] = diyan_credits

    sorted_course_credits = sorted(course_credits.items(), key=lambda x: x[1], reverse=True)

    output = ""

    if total_credits >= 240:
        output += f"Diyan gets a diploma with {total_credits:.1f} credits.\n"
    else:
        credits_needed = 240 - total_credits
        output += f"Diyan needs {credits_needed:.1f} credits more for a diploma.\n"

    for name, credits in sorted_course_credits:
        output += f"{name} - {credits:.1f}\n"

    return output




print(students_credits("Computer Science-12-300-250","Basic Algebra-15-400-200","Algorithms-25-500-490"))
