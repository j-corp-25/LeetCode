class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # x is the row y is the column
        # loop through each regular array [...] and possibly reverse method
        # loop through it again and then inverse the number based on what it is
        # the number is 1 then it will 0 and vice versa
        # then return the inverted image

        for i in range(len(image)):
            image[i] = [1 - x for x in image[i][::-1]]
        return image
           
                





        
        