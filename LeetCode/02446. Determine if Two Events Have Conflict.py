class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        l = lambda a: int(a.replace(':', ''))
        event1 = list(map(l, event1))
        event2 = list(map(l, event2))
        return event1[0] <= event2[1] and event1[1] >= event2[0]
      
      
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        return event1[0] <= event2[1] and event1[1] >= event2[0]
