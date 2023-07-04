class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_color = image[sr][sc]
        if starting_color != color:
            pixels_to_examine = [[sr, sc]]
        else:
            return image

        while pixels_to_examine:
            sr, sc = pixels_to_examine.pop()
            if image[sr][sc] == starting_color:
                image[sr][sc] = color
            else:
                continue

            if (sr - 1)>=0 and image[sr-1][sc]==starting_color:
                pixels_to_examine.append([sr-1, sc])
            if (sr + 1) < len(image) and image[sr+1][sc]==starting_color:
                pixels_to_examine.append([sr + 1, sc])
            if (sc - 1) >= 0 and image[sr][sc-1]==starting_color:
                pixels_to_examine.append([sr, sc - 1])
            if (sc + 1) < len(image[0]) and image[sr][sc+1]==starting_color:
                pixels_to_examine.append([sr, sc + 1])
        return image