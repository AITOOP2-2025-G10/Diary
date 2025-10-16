from diaries.AbstractDiary import AbstractDiary

class UnoDiary(AbstractDiary):

    def get_date(self):
        return "2025-10-16"
    
    def get_summary(self):
        return "授業で疲れた"
    
    def get_author(self):
        return "Sample"