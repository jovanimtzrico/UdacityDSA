# Run time analysis

## Task0
The run time for this task is constant **O(1)** because the access time for location in the array is constant
```
O(1)
```

## Task1
The run time for this problem is **O(n)**, this is because it needs to iterate accross the list of text wich this takes O(n), but also it needs to iterate the entire list of calls that also takes O(n).So we have:

```
 O(n) + O(n) = O(2n) = O(n)
```

## Task2
The time complexity for this task is **O(n)**, the code iterates over the list of calls and then it ask if the phone is already in the hashMap that takes constant time to lookup, all of this takes O(n). Finally it iterates accross the dictionary to find the losngest call duration and this takes O(n).

```
 O(n) + O(n) = O(2n) = O(n)
```


## Task3
The run time for this problem is **O(n log n)**, the algorithm first iterates over the list of calls and then it looks for the numbers that have the code for Bangalore which this takes O(m), m is the length of the phone number. Then the algorithm looks if the receiving call has the Bangalore code in order to get the percentage, this takes again O(m) because it looks the code over the length of the phone number. In order to get the code, the regex takes O(m). Finally, it returns the sorted unique codes which it takes O(n log n), therefore the final result is the following:

```
 O(n*m+m) + O(n log n) = O(n log n)
```

## Task4
The run time for this question is **O(n log n)**, because the code iterates 3 times over the list, the first time to get the unique numbers from the text list, the second time to get the uniques numbers from the receiving calls, and the third time to get the possible Telemarketers numbers, in this last iteration, it looks if the making call number is not in the uniques numbers, this takes constant time because set is implemented as a hash table in python. Finally, it needs to return the list in order, therefore we have the following:

```
 O(n) + O(n) +O(n) + O(n log n) = O(n log n)
```
