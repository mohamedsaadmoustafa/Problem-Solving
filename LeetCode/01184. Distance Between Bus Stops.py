class Solution:
    def distanceBetweenBusStops(self, distance, start, destination):
        if start > destination:
            start, destination = destination, start # swap
        
        a = sum(distance[start:destination])
        b = sum(distance) - a

        return min(a, b)
