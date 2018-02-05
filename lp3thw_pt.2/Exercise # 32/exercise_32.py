random_count_by_twos = [2,4 ,6, 8,10, 12]
good_food = ['tacos, cheese, oreos, cherries, cake, pomegrante']
trash_food = [1, 'dressing', 2,'manwiches' , 3, 'celery']
# this first kind of for-loop goes through list
for number in random_count_by_twos:
    print(f"This is count {number}")

#same as above
for good in good_food:
    print(f" These foods are good as heck: {good}")

#also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for trash in trash_food:
    print(f" This food belongs in the garbage. Let's rate them from bad to worst:{trash}")

#we can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 50 counts
for i in range(0,6):
    print(f"Adding {trash} to the list.")
    #append is a function that lists understand.
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")
        
