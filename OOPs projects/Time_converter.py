class Time:
    def __init__(self):
        pass
    def sec_to_min(self, sec):
        print(sec/60)
    def min_to_sec(self, min):
        print(min*60)
    def min_to_hr(self, min):
        print(min/60)
    def hr_to_min(self, hr):
        print(hr*60)

t1 = Time()
t1.sec_to_min(147)
t1.hr_to_min(12.5)
t1.min_to_hr(345)
t1.min_to_sec(13.6)
    
