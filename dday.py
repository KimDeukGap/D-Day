from datetime import datetime
import json, os

FILE = "dday.json"
dday_data = json.load(open(FILE, "r", encoding="utf-8")) if os.path.exists(FILE) else {}

while True:
    print("\n--- [1] D-Day 목록 [2] D-Day 추가 [3] 삭제 [4] 종료 ---")
    cmd = input("선택: ")
    
    if cmd == "1":
        if not dday_data:
            print("등록된 D-Day가 없습니다.")
        else:
            today = datetime.now().date()
            for title, date_str in dday_data.items():
                target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                delta = (target_date - today).days
                if delta > 0:
                    print(- D-{delta} : {title} ({date_str}))
                elif delta == 0:
                    print(- D-DAY : {title} ({date_str}))
                else:
                    print(- D+{abs(delta)} : {title} ({date_str}))
    elif cmd == "2":
        title = input("이벤트 이름: ")
        date_str = input("날짜 (YYYY-MM-DD): ")
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            dday_data[title] = date_str
            json.dump(dday_data, open(FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
            print("저장되었습니다.")
        except ValueError:
            print("날짜 형식이 잘못되었습니다. (예: 2026-12-31)")
    elif cmd == "3":
        title = input("삭제할 이벤트 이름: ")
        if dday_data.pop(title, None):
            json.dump(dday_data, open(FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
            print("삭제되었습니다.")
        else:
            print("해당 이벤트가 존재하지 않습니다.")
    elif cmd == "4":
        break
