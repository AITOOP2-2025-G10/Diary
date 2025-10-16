from diaries.AbstractDiary import AbstractDiary
class TsubouchiDiary(AbstractDiary):
    def get_date(self):
        return "2005-12-27"

    def get_summary(self):
        return "今日私が生まれた"

    def get_author(self):
        return "Tsubouchi"