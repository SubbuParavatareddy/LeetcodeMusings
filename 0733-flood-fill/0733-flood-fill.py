class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]

        if (image[sr][sc] == color):
            return image

        def bfs(r, c):
            if (r < 0) or (r >= len(image)) or (c < 0) or (c >= len(image[0])) or (image[r][c] != original_color): 
                return
            
            image[r][c] = color

            bfs( r + 1, c )
            bfs( r - 1, c )
            bfs( r, c +1 )
            bfs( r, c - 1 )

        bfs(sr, sc)
        return image