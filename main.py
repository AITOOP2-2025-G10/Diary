from diaries.DiarySample import DiarySample
from diaries.UnoDiary import UnoDiary
from diaries.TsubouchiDiary import TsubouchiDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
  DiarySample(),
  UnoDiary(), 
  TsubouchiDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()