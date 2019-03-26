
chorus1 = "bottles of bear on the wall"
chorus2 = "bottles of beer"
chorus3 = "Take one down pass it around"
chorus4 = "last bottle of beer on the wall"
chorus5 = "last bottle of beer"
chorus6 = "Take it down, pass it around"
    
for i in range (99,0,-1):
    
        beercount = i
        if i > 1:
            print (beercount,chorus1,beercount,chorus2)

            print (chorus3,beercount - 1, chorus1)
        else:
            print (beercount,chorus4,beercount,chorus5)

            print (chorus6,beercount - 1, chorus1)
    