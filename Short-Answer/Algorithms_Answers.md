#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
first we have a while loop what will run as long as 'a' is less than 'n^3'(O(n^3). during the while loop we will 
increase 'a' by 'n^2' and since 'a' starts as 0 'a' is 'n^2'. when looking at the runtime of this it is O(n^3-n^2)
which equates to O(n) making the overall runtime O(n). 

b)
first we have a for loop the length of n (O(n). for each position of the loop we have a while loop that will continue
as long as j is less than n (O(n)). inside the inner while loop j gets doubled or j = j^2. this changes the while 
runtime to O(log_n). we then times each position of the outer for loop with the inner while loop runtime making the
total runtime O(n^log_n).

c)
first we have a function that looks at bunnies and determines if bunnies equals 0. if does we stop. if it doesn't
then run the function again but with one less bunnies. continue until bunnies equals 0. based on this we can tell
that the runtime is O(n) because we only run the function however many times the original bunnies value is.

## Exercise II
i would choose a binary search algorithm. we begin by picking the middle floor of our building and drop an egg. if it 
breaks we know we are too high and if it doesn't we are too low. if you were high then your current floor would 
become the new top floor and we would cut the number of floors from the bottom to the new top floor in half and drop
another egg. if you were low you would make your current floor your new bottom floor and find the middle floor between
your new bottom floor and the top floor and drop another egg. we continue this until we reach the floor that the next
highest floor would break the egg.

n = total floors of building
bottom = buildings bottom floor
top = buildings top floor
middle = n's middle floor rounded down if number of floors is odd
f = highest floor that won't break the egg

while f not found:
    if drop and egg breaks:
        middle = floors from current to bottom divided by half
        go to middle and do it again
    if drop and egg doesn't break:
        middle = floors from current to top divided by half
        got to middle and do it again
    if egg doesn't break and there is no floor above it that wouldn't break it:
        we found f!
        stop the while loop
        
we found f by halving the number of floors we needed to search each time we dropped an egg. this tells us the runtime 
of this algorithm is however many times we had to drop an egg. this is shown as O(log_n).