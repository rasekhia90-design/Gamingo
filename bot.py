participants = set()

ADMIN_ID = 123456789  # اینو بعداً با آیدی خودت عوض می‌کنی

def join_lottery(user):
    if user["id"] not in participants:
        participants.add(user["id"])
        return "✅ در قرعه‌کشی ثبت شدی"
    else:
        return "قبلاً ثبت شدی ✔️"
