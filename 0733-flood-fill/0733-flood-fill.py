class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def lookAround(image, sr, sc, color, OldColor):
            if sr in range(0, len(image)) and sc in range(0, len(image[0])):
                if image[sr][sc] == color:
                    return image
                if image[sr][sc] == OldColor:
                    print(sr, sc)
                    image[sr][sc] = color
                    if sr+1 in range(-1, len(image)):
                        lookAround(image, sr+1, sc, color, OldColor )
                    if sr-1 in range(-1, len(image)):
                        lookAround(image, sr-1, sc, color, OldColor )
                    if sc+1 in range(-1, len(image[0])):
                        lookAround(image, sr, sc+1, color, OldColor )
                    if sc-1 in range(-1, len(image[0])):
                        lookAround(image, sr, sc-1, color, OldColor )

                return image
            else:
                return image        
        return lookAround(image, sr, sc, color, image[sr][sc])
				
