class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in range(len(image)):
            image[row] = [1 - x for x in image[row][::-1]]
        return image

        
     

        