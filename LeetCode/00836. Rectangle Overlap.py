class Rectangle:
    def __init__(self, rect):
         self.x1, self.y1, self.x2, self.y2 = rect

class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        rec1, rec2 = Rectangle(rec1), Rectangle(rec2)
        x1 = max(rec1.x1, rec2.x1)
        y1 = max(rec1.y1, rec2.y1)
        x2 = min(rec1.x2, rec2.x2)
        y2 = min(rec1.y2, rec2.y2)
        return max(0, x2 - x1 ) * max(0, y2 - y1) # if o then False; if number>0 then True
