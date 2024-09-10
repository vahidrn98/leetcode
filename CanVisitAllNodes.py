class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.visited = set()
        key = 0
        self.visited = self.visit(0,rooms)
        return len(self.visited)==len(rooms)
    def visit(self,key,rooms):
        if(key in self.visited):
            return self.visited
        self.visited.add(key)
        for k in rooms[key]:
            self.visited = self.visit(k,rooms)
        return self.visited