# Hybrid Sort
The hybrid sort algorithm uses 3-way merge sort for lengthy inputs and uses selection sort (instead of continuing to recurse) if the input sublist length is below a certain threshold. This hybrid approach (merge sort with threshold) is more efficient then pure merge sort. The overall complexity is 𝑂(𝑁𝑙𝑜𝑔3(𝑁)).

## steps comparison
<img width="373" alt="Screen Shot 2022-10-01 at 7 31 33 PM" src="https://user-images.githubusercontent.com/49523649/193430680-904356cf-f6ee-4721-bf96-58dd3fce2e46.png">

## runtime comparison
<img width="360" alt="Screen Shot 2022-10-01 at 7 32 02 PM" src="https://user-images.githubusercontent.com/49523649/193430688-1a182dd4-25a9-41eb-8772-c072edf455b6.png">

