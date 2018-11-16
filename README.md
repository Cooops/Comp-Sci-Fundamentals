# **Computer Science Fundamentals** (work in progress)

This will serve as a repository for publicly measuring my progress both learning and brushing up on Computer Science fundamentals.

## Synopsis

I want to improve my fundamental knowledge over the course of the next 6-12 months, rounding out any core Computer Science (see Task List below for specifics) related information I am lacking. This will be a long-term venture with plenty of notes, videos, articles, and of course code samples along the way. I will start out coding in Python, but will likely blend in C-related languages down the line.

I am doing this for myself first and foremost; not anyone else.

> "Learning is not attended by chance, it must be sought for with ardor and diligence." - Abigail Adams

## Inspiration (videos & text)

* <a href="http://www.aaronsw.com/weblog/dweck">Fixed vs. Growth Mindset</a>
* <a href="https://medium.freecodecamp.org/why-i-studied-full-time-for-8-months-for-a-google-interview-cc662ce9bb13">The blueprint I am basing this guide off</a>
* <a href="https://www.youtube.com/watch?v=YJZCUhxNCv8">Getting a Job at the Big 4 _(sensational title, but solid talk)_</a>

## Task List (will be constantly expanded upon and updated)

* Low-level knowledge
* Operating Systems
* Data Structures
* Algorithms
* Object-Oriented Design
* System Design (solving problems at scale)
* Databases
* Web Apps & Servers
* Math

## Language Breakdown

<details>
    <summary><b>Python
    </b></summary>
Python is an example of high-level language (as opposed to a low-level language). Before we move any further, let's break down the different between a high and low level language:

* High-level language
    * Python, C++, Java

* Low-level language
    * **Machine language**
        * The process of encoding instructions in binary so that a computer can directly execute them.
    * **Assembly language**
        * Uses a slightly easier format to refer to the low level instructions (abstracts things a bit).

</details>

## General Definitions

<details>
<summary><b>Algorithm
</b></summary>
"If problem solving is a central part of computer science, then the solutions that you create through the problem solving process are also important. In computer science, we refer to these solutions as <b>algorithms</b>. An algorithm is a step by step list of instructions that if followed exactly will solve the problem under consideration.


Our goal in computer science is to take a problem and develop an algorithm that can serve as a general solution. Once we have such a solution, we can use our computer to automate the execution. As noted above, programming is a skill that allows a computer scientist to take an algorithm and represent it in a notation (a program) that can be followed by a computer. These programs are written in programming languages." - <a href="https://interactivepython.org/runestone/static/thinkcspy/GeneralIntro/Algorithms.html">source</a>

</details>
<details>
<summary><b>Lambda
</b></summary>

In computer programming, an anonymous function (or <b>lambda</b> expression) is a function that has no identifier <a href="https://thepythonguru.com/python-lambda-function/">(source).</a>

* Usually not more than a single line in length.
* Can't contain more than one expression.

    * Lets check out an example:
        ```
        The function version:

        def multiply(x, y):
            return x * y
        ```

        This verison is too small, so let's convert it to a lambda. To create a lambda function, first denote the keyword `lambda` followed by one of more arguments separated by comma and followed by colon sign ( : ), which is then followed by a single line expression. See below:

        ```
        The lambda version:

        r = lambda x, y: x * y

        r(12, 3)  # call the lambda function
        >>> 36
        ```

        We can even call the lambda function without assigning it to a variable:

        ```
        (lambda x, y: x * y)(12, 3)
        >>> 36
        ```
</details>
<details>
<summary><b>Recursion
</b></summary>

A recursive function is essentially just a function that will continue to call itself until it some condition is met to return a result <a href="https://realpython.com/python-thinking-recursively/">(source).</a>

Let's say we wanted to recursively calculate n! (factorial) in Python:

```
def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)  # recursively call function while subtracting 1 from n each time (will continue until we reach 0)
>>> 120
```

```
# adding stack frame to call stack
# factorial_recursive(1)
# factorial_recursive(2)
# factorial_recursive(3)
# factorial_recursive(4)
# factorial_recursive(5)

# 5*4*3*2*1

# unwinding call stack
# 1 * 2
# 2 * 3
# 6 * 4
# 24 * 5
# hit end of call stack, returns 120
```

Each recursive call will add a stack frame to the call stack until we reach the base case. Then, the stack begins to unwind as each call returns the result (as you can see in the above example, or a much better one on <a href="https://realpython.com/python-thinking-recursively/">this page</a>).

#### State

Each recursive call contains its own execution context, so in order to maintain state we need to do a few things:

1. Thread the state through each recursive call so that the current state is part of the current call's execution content.
2. Keep the state in a global scope.

Let's say we had to calculate 1+2+3...+10 using recursion. We need to maintain the state -- the current number we are adding & the accumulate sum until now.

Let's look at an example where we pass (thread) the updated current state to each recursive call as arguments:

```
def sum_recursive(current_number, accumulated_sum):
    # return the final state
    if current_number == 11:  # base case
        return accumulated_sum

    # recursive case
    # thread the state through the recursive call
    else:
        return sum_recursive(current_number + 1, accumulated_sum + current_number)

print(sum_recursive(1, 0))
>>> 55
```

![control flow with threaded state](https://files.realpython.com/media/state_3.3e8a68c4fde5.png)

and similarly, here's how you would maintain by utilizing a global scope:

```
# global mutable state
current_number = 1
accumulated_sum = 0

def sum_recursive_global():
    global current_number
    global accumulated_sum
    if current_number == 11:  # base case
        return accumulated_sum
    # recursive case
    else:
        accumulated_sum = accumulated_sum + current_number
        current_number = current_number + 1
        return sum_recursive_global()

print(sum_recursive_global())
>>> 55
```

In general, threading will keep your code much cleaner, less bug prone and more maintainable for others.

#### Recursive Data Structures

A data structure is defined as recursive if it can be defined in smaller terms of a smaller version of itself. One example is a list, as explained below.

If we were to start with an empty list and were only able to perform the following operation...

```
# return a new list that is the result of
# adding element to the head (i.e. front) of input_list
def attach_head(element, input_list):
    return [element] + input_list
```

...we could use the `attach_head` function to generate any list of any size. For example, if we wanted to return the list `[1, 46, -31, 'hello']`:

```
attach_head(1, attach_head(46, attach_head(-31, attach_head("hello", []))))

# unwinding the call stack
# ['hello']
# [-31, 'hello']
# [46, -31, 'hello']
# [1, 46, -31, 'hello']
```

We can also perform the following recursive implementations with other data structures like sets, trees, dictionaries and more.

These recursive data functions and recursive data structures balance each-other perfectly; like yin and yang.

The recursive function’s structure can often be modeled after the definition of the recursive data structure it takes as an input. Let's see how the writer implemented this example of calculating the sum of all lists recursively:

```
def list_sum_recursive(input_list):
    # base case
    if input_list == []:
        return 0
    # recursive case
    # decompose the original problem into simpler instances of the same problem
    # by making use of the fact that the input is a recursive data structure
    # and can be deﬁned in terms of a smaller version of itself
    else:
        head = input_list[0]
        smaller_list = input_list[1:]
        return head + list_sum_recursive(smaller_list)

print(list_sum_recursive([1,2,3]))
>>> 6
```

#### Naive recursion

Let's look at an example for creating a function to calculate the nth Fibonacci number:

```
def fibonacci_recursive(n):
    print("Calculating F", "(", n, ")", sep="", end=", ")

    # base case
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # becursive case
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

fibonnaci_recursive(5)
>>> Calculating F(5), Calculating F(4), Calculating F(3), Calculating F(2), Calculating F(1), Calculating F(0), Calculating F(1), Calculating F(2), Calculating F(1), Calculating F(0), Calculating F(3), Calculating F(2), Calculating F(1), Calculating F(0), Calculating F(1), 5
```

As we can see in the above example, we are unnecessarily recomputing values. Let's try to improve this function by caching the results of each computation:

```
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_recursive_cache(n):
    print("Calculating F", "(", n, ")", sep="", end=", ")

    # base case
    if n < 2:
        return n

    # recursive case
    else:
        return fibonacci_recursive_cache(n-1) + fibonacci_recursive_cache(n-2)

print(fibonacci_recursive_cache(5))
>>> 5
```

More about memoization and caching <a href="https://mike.place/2016/memoization/">here</a>, but `lru` essentially stands for least-recently-used and it is a FIFO approach to managing the size of a cache. Fundamentally, this is the same as manually incorporating a memoize function but instead allows you to just import it and wrap your function in the respective decorator.

The only thing to keep is mind is that `lru_cache` utilizes a dictionary to cache results, so positional and keyword arguments (keys) to the function must be hashable.

#### Corner cases/details

Python doesn't have built-in support for a <a href="https://en.wikipedia.org/wiki/Tail_call">tail-call elimination</a>. This means you can cause a stack overflow if you end up adding more stack frames than the default call stack depth:

```
import sys
sys.getrecursionlimit()
>>> 3000
```

This limitation is important to keep in mind if you are working with a program that requires deep recursion.

</details>

## [1] **Low-level Knowledge**

<details>
<summary><b>CPU & RAM
</b></summary>

### Bite Size Overview

---

### Videos & Links

---

1. **[How a CPU works](https://www.youtube.com/watch?v=FZGugFqdr60&feature=youtu.be)**
2. **[How a CPU executes a program](https://www.youtube.com/watch?v=XM4lGflQFvA)**
3. **[How computer's calculate - ALU](https://www.youtube.com/watch?v=1I5ZMmrOfnA&feature=youtu.be)**
4. **[Registers and RAM](https://www.youtube.com/watch?v=fpnE6UAfbtU&feature=youtu.be)**
5. **[Instructions and Programs](https://www.youtube.com/watch?v=zltgXvg6r3k&feature=youtu.be)**


### Notes

---
* *INC A
* Machine code will usually represent binary patterns in hexadecimal. Hexadecimal is an easy way for humans to remember binary patterns.
* Fetch, Decode, Execute
* For a microprocessor to works the program counter has to contain a memory address that it points to.

### Summary

---
</details>
   
## [2] **Data Structures**

<details>
<summary><b>Hash Tables (Hash Maps)</b></summary>

### Time Complexity

| Algorithm     | Average       | Worst Case  |
| ------------- |:-------------:| -----------:|
| Space         | O(1)          | O(n)        |
| Search        | O(n)          | O(n)        |
| Insert        | O(n)          | O(n)        |
| Delete        | O(n)          | O(n)        |


### Bite Size Overview

---
Hash Tables, or more commonly implemented as dictionaries in Python, are a type of data structure that stores key-value pairs where the key is generated through a hashing function. This improves the functionality of lookups by a significant margin as the key values themselves act as the index of the array which stores the data. A picture says a thousand words:

```
>>> a = dict(one=1, two=2, three=3)
>>> b = {'one': 1, 'two': 2, 'three': 3}
>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
>>> d = dict([('two', 2), ('one', 1), ('three', 3)])
>>> e = dict({'three': 3, 'one': 1, 'two': 2})
>>> a == b == c == d == e
True


dict = {'Name': 'Cooper', 'Focus': 'Comp Sci Fundamentals'}

print(dict['Name'], dict['Focus'])

>>> Cooper, Comp Sci Fundamentals
```

**When dealing with space vs time tradeoffs, keep Hash Tables at the top of your mind.** On average, Hash Tables will out-perform search trees or any other table lookup structure.

### Videos & Links

---

1. <a href="https://en.wikipedia.org/wiki/Hash_table">What is a Hash Table? (text)</a>
2. <a href="https://stackoverflow.com/questions/114830/is-a-python-dictionary-an-example-of-a-hash-table">Is a Python Dictionary an example of a Hash Table (text)</a>
3. <a href="http://www.laurentluce.com/posts/python-dictionary-implementation/">Why doesn't Python have a real hashing function?</a>
4. <a href="http://www.wellho.net/mouth/3934_Multiple-identical-keys-in-a-Python-dict-yes-you-can-.html">Multiple Dict Keys in Python</a>
5. <a href="https://stackoverflow.com/questions/19588290/python-equivalent-for-hashmap">Python Equivalent for Hash Map (text)</a>
6. <a href="https://stackoverflow.com/questions/2548000/how-to-sort-a-dictionary-having-keys-as-a-string-of-numbers-in-python">Sort Dict by Key (Python)</a>

### Notes

---
Hash Tables are widely used in many kinds of computer software, primarily for associate arrays, database indexing, caching, and sets.

A Dictionary in Python, like a hash in Perl or an associative array in PHP, satisfied the requirements to properly represent the implement of a Hash Table:

    * The keys of the dictionary are hashable (produces unique values, are not lists).
    * The order of the data elements are not fixed.

### Summary

---
</details>

<details>
<summary><b>Linked Lists</b></summary>

### Bite Size Overview

---
On the simplest level, a Linked List is really just a bunch of connected nodes (sub-data structures). The nodes link together to form a list and contain two attributes:

* a value (int, str, objects, etc)
* a pointer to the next node in the sequence

Python lists are resizable, C++ arrays are not
C++ arrays are a contiguous allocation of objects in memory, Python lists are a contiguous allocation of references in memory

### Videos & Links

---

1. <a href="https://medium.freecodecamp.org/python-interview-question-guide-how-to-code-a-linked-list-fd77cbbd367d">Linked Lists in Python (text)</a>
2. <a href="https://www.youtube.com/watch?v=6sBsF13n5ig"> Linked Lists in Python (video)</a>
3. <a href="https://stackoverflow.com/questions/39585740/how-can-i-print-all-of-the-values-of-the-nodes-in-my-singly-linked-list-using-a">Linked Lists - StackOverflow (text)</a>
4. <a href="https://stackoverflow.com/questions/39585740/how-can-i-print-all-of-the-values-of-the-nodes-in-my-singly-linked-list-using-a">Printing a Singly-Linked List (text)</a>
5. <a href="https://stackoverflow.com/questions/280243/python-linked-list">Python Linked List (text)</a>

### Notes

---
To start off, let's define a few terms:
* **Head Node**
    * The head node is simply the first (root) node in a linked list.
* **Tail Node**
    * The tail node is simply the last node in a linked list. Since it's the last node in the linked list, it must point to NULL as there is no other node in the sequence.
* **Singly Linked**
    * Each node points to a single node in front of it.
* **Doubly Linked**
    * each node can point to two other nodes; one in front and one behind.

With some terminology out of the way, it's almost time to jump into some code examples, but first it's important to touch on the fact that Linked Lists can be as simple or complex as you desire (and the example below is simple).

#### Creating a Linked List

Since a Linked List is made up of a series of nodes, lets first start by creating a Class for the node:

```
class Node():
    def __init__(self, value, nextNode=None):
        self.value = None
        self.nextNode = nextNode
```

If we want to actually populate a node, we simply pass in a value:

```
firstNode = Node('5')
secondNode = Node('13')
thirdNode = Node('2')
```

We have created three individual nodes, but now we need to link them together:

```
firstNode.nextNode = secondNode
secondNode.nextNode = thirdNode
```

While an extremely simple example, this does provide the basis for understanding what a Linked List in Python looks like on the most basic level.

#### Traversing a Linked List

We may be asked to get the rest of the nodes in the Linked List when provided only with the head, so we would need to find a way to iterate over the list and find what each node is pointing to, and the corresponding node that is pointing to, all the way down the structure until we hit the end (`NULL`).

```
currentNode = firstNode

# if the current node is not NULL, move to the next node
while currentNode:
    print(currentNode.value)
    currentNode = currentNode.nextNode
```

This is a _very_ basic implementation of a Linked List and how to traverse it, but it's a great way to understand how things work on a simple level.

#### Inserting values into a Linked List

Unless you are told otherwise, always insert a new element into the tail (last) node in a Linked List.

The simplest way to insert a new value is just like how we create one; by binding the new element to the tail node:

```
fourthNode = Node('4')
thirdNode.nextNode = fourthNode
```

Lets jump back to our example a few steps ago that only provides the head node. In order to traverse this list, we can utilize the aforementioned methods to find the tail.

First, lets traverse through the list and check if the node is `NULL` or populated. If it's not, we stop on the last populated node and set the nextNode equal to the value we wish to insert:

```
def insertNode(head, value):
    currentNode = head
    while currentNode:
        while not currentNode.nextNode:
            currentNode.nextNode = Node(value)
            return head
        currentNode = currentNode.nextNode
```

#### Deleting values from a Linked List

Deleting within a Linked List can get a bit tricky, so let's look at a few examples.

If we wanted to "delete" the `13`, all we would need to do is point the `5` to the `2` so that the `13` is never referenced:

```
5 -> 13 -> 2 -> NULL

becomes

5 -> 2 -> NULL
```

In order to do implement this process in a streamlined manner we now need to keep track of not just the currentNode but also the previousNode. This also means accounting for the head node being the node we wish to delete.

There are very many ways to accomplish this task and this implementation is not the most optimal, but the example I have chosen is easy to understand. See the code below:

```
def deleteNode(head, valueToDelete):
    currentNode = head
    previousNode = None
    while currentNode:
        if currentNode.value == valueToDelete:
            if not previousNode:
                newHead = currentNode.nextNode
                currentNode.nextNode = None
                return newHead
            previousNode.nextNode = currentNode.nextNode
            return head
        previousNode = currentNode
        currentNode = currentNode.nextNode
    return head
```

In the above block of code, after finding the node we wish to delete, we set the previous node's `nextNode` to the deleted node's `nextNode` to once again effectively remove it from the list.

#### Time Complexities

Let's evaluate the time complexities surrounding the above example (which is something you would implement in an interview, in more real-world scenarios you can store attribuets in a LinkedList class to lower the complexities).

Lets state _n_ is equal to the number of elements inside a Linked List.

What are the following time complexities?

1. **Traversing**
    * O(n)
        * Traversing a list will always require iterating over _n_ elements.
        * Theta(n). (?)
2. **Tail insertion**
    * O(n)
        * Requires traversing the list to insert our new node.
        * Theta(n).
3. **Head insertion**
    * O(1)
        * We always know where the index of head is within the list, so the best case time complexity is O(1).
        * Theta(1).
4. **Deleting**
    * O(n)
        * Requires traversing the list to delete our new node.
        * Omega(1), worst case O(n).

This should act as a rough introduction to Linked Lists in Python; thanks for checking it out :).

### Summary

---
In summary, Linked Lists are just a bunch of connected nodes that point to one other node (singly-linked) or up to two other nodes (doubly-linked). A node within a Linked List can only contain two attributes: a value (int, str, etc) and a pointer to the next node in the sequence. Linked Lists seem to be commonplace in technical interviews, so this section is likely one I will come back to often.

The benefit of a linked list is that it can provide list insertion and deletions of a node in O(1) instead of O(n).
</details>

<details>
<summary><b>Matrices (2D Arrays)</b></summary>

### Time Complexity

---

### Bite Size Overview

---
Put simply, a matrix is a two-dimensional data structure where the numbers are divided into rows and columns:

```
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0

A 3x5 ("three by five") Matrix, as it has 3 rows and 5 columns.
```

You are most commonly going to see these implement in the form of questions surrounding 2D arrays (which is basically a matrix).

### Videos & Links

---
1. <a href="https://www.programiz.com/python-programming/matrix">Overview of a Matrix in Python (text)</a>

### Notes

---
Python doesn't have built in matrices, however for basic tasks we can implement this using a list of lists:

```
x = [[0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]]
```

When diving into more complex computational tasks, the proper way to implement a Matrix is through the ![NumPy](https://www.numpy.org/) package. NumPy is basically the defacto package for scientific computing and it has great support for a powerful N-dimensional array object.

NumPy provides a multidimensional array of numbers (which is actually just an object). See the example below:

```
import numpy as np
a = np.array([1, 2, 3])
print(a)               # Output: [1, 2, 3]
print(type(a))         # Output: <class 'numpy.ndarray'>
```

You can see in the above that the NumPy array class is called ndarray. Utilizing NumPy to create matrices will allow a massive amount of computational efficiency vs lists, along with a higher degree of control.

Similarly to lists, we can traverse matrices using an index. See the below example of a 1 dimensional NumPy array:

```
import numpy as np
A = np.array([2, 4, 6, 8, 10])

print("A[0] =", A[0])     # First element
print("A[2] =", A[2])     # Third element
print("A[-1] =", A[-1])   # Last element
```

Now, let's say we need to traverse a 2D array (matrix).

First, let's see how we would extract the elements:

```
import numpy as np

A = np.array([[1, 4, 5, 12],
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]])

#  First element of first row
print("A[0][0] =", A[0][0])  

# Third element of second row
print("A[1][2] =", A[1][2])

# Last element of last row
print("A[-1][-1] =", A[-1][-1])  

>>> A[0][0] = 1
>>> A[1][2] = 9
>>> A[-1][-1] = 19
```

And the rows:

```
import numpy as np

A = np.array([[1, 4, 5, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]])

print("A[0] =", A[0]) # First Row
print("A[2] =", A[2]) # Third Row
print("A[-1] =", A[-1]) # Last Row (3rd row in this case)

>>> A[0] = [1, 4, 5, 12]
>>> A[2] = [-6, 7, 11, 19]
>>> A[-1] = [-6, 7, 11, 19]
```

The columns:

```
import numpy as np

A = np.array([[1, 4, 5, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]])

print("A[:,0] =",A[:,0]) # First Column
print("A[:,3] =", A[:,3]) # Fourth Column
print("A[:,-1] =", A[:,-1]) # Last Column (4th column in this case)

>>> A[:,0] = [ 1 -5 -6]
>>> A[:,3] = [12  0 19]
>>> A[:,-1] = [12  0 19]
```

The above array manipulation is known as **slicing** matrices and is essentially the same thing as how <a href="https://stackoverflow.com/questions/509211/understanding-pythons-slice-notation">slicing for lists in Python work</a>. See the brief snapshot below:

```
a[start:end]        # items start through end-1
a[start:]           # items start through the rest of the array
a[:end]             # items from the beginning through end-1
a[:]                # a copy of the whole array

a[start:end:step]   # start through not past end, by step
--------------------------------------------------------------------
a[-1]               # last item in the array
a[-2:]              # last two items in the array
a[:-2]              # everything except the last two items

a[::-1]             # all items in the array, reversed
a[1::-1]            # the first two items, reversed
a[:-3:-1]           # the last two items, reversed
a[-3::-1]           # everything except the last two items, reversed
```

One way to remember how slices work is to think of the indices as pointing between characters, with the left edge of the first character numbered 0. Then the right edge of the last character of a string of n characters has index n.

If we wanted to slice a matrix, we would do as follows:

```
import numpy as np

A = np.array([[1, 4, 5, 12, 14], 
    [-5, 8, 9, 0, 17],
    [-6, 7, 11, 19, 21]])

print(A[:2, :4])  # two rows, four columns

''' Output:
[[ 1  4  5 12]
 [-5  8  9  0]]
'''


print(A[:1,])  # first row, all columns

''' Output:
[[ 1  4  5 12 14]]
'''

print(A[:,2])  # all rows, second column

''' Output:
[ 5  9 11]
'''

print(A[:, 2:5])  # all rows, third to fifth column

'''Output:
[[ 5 12 14]
 [ 9  0 17]
 [11 19 21]]
'''
```
This is just a high level overview, but it still provides a good baseline for working with matrices in Python.

### Summary

---
Matrices are two-dimensional data structures that allow us to store data in the forms of columns and rows. The most common place to encounter matrices are in the form of questions surrounding 2D arrays (which is basically a matrix).

</details>

<details>
<summary><b>Binary Trees</b></summary>
</details>

<details>
<summary><b>Graphs</b></summary>
</details>

<details>
<summary><b>Stacks</b></summary>
</details>

<details>
<summary><b>Queues</b></summary>
</details>

<details>
<summary><b>Heaps</b></summary>
</details>

## [3] **Algorithms**

<details>
<summary><b>Asymptotic Notation (Big O)</b></summary>

### Bite Size Overview

---
Asymptotic Notation, aka Big O notation, is the most common metric for calculating time complexity. In simpler terms, Big O notation is how programmers talk about algorithms. A functions Big O notation is determined by how it responds to different inputs. How much slower is it if we feed in a list of 1,000,000 elements instead of 1? Big O describes the number of steps it takes to reach the base case.

### Videos & Links

---

1. <a href="https://www.youtube.com/watch?v=iOq5kSKqeR4">The best high-level explanation I've seen to date.</a>
2. More later...

### Notes

---
Fast or efficient algorithms =/= a measurement in real time (seconds, minutes) due to how much hardware varies, or that a user might be running their program through a different piece of software, etc. Thus, the uniform way compare the algorithm is to measure the Asymptotic Complexity of a program, and to use the notation (Big O (or just O)) for describing this.
**How fast a programs runtime grows asymptotically == as the size of your inputs increase towards infinity, how does the runtime of your program grow?**

Imagine counting the number of characters in a string the simplest way by walking through the whole string, letter by letter, and adding 1 to a counter for each character.

```
def string_length(strng):
    counter = 0
    for character in strng:
        counter += 1
    return counter
```

This algorithm is said to run in linear time with respect to the number of characters (n) in the string. In short, it runs in **O(n); the time required to traverse the entire string is proportional to the number of characters**. 20 characters take twice as long as 10 characters, etc. As you increase the number of characters, **the runtime will increase linearly with the input length**.

Lets says the above method isn't fast enough, so you may chose to store the number of characters in the string in a variable _len_, which you can then compare against instead of the checking the string itself everytime.

```
def string_length(strng):
    counter = len(strng)
    return counter
```

**Accessing len() is considered an asymptotically constant time operation, or O(1)**. What this means is no matter how big your input is it will always take you the same amount of time to compute things. This doesn't have to mean your code runs in one step; if it doesn't change with the size of inputs then it is still asymptotically constant. There are always drawbacks though and in this case you have to spend extra memory space on your computer to store the variable (and the storage of the variable itself). **Constant time is considered the best case scenario for a function.**

![Big O comparisons](https://justin.abrah.ms/static/images/runtime_comparison.png)

There are many different Big O runtimes to measure algorithms with. One area you may run into **O(n^2)** notations is with combinations and it is especially useful when it comes to data structures. See the following code example which would match every item in the list with every other item in the list:

```
def all_combinations(array):
    results = []
    for item in array:
        for inner_item in array:
            results.append((item, inner_item))
    return results
```

This function (algorithm) is considered O(n^2) as every input requires us to do n more operations; n*n == n^2. Thus, **O(n^2) are asymptotically slower than O(n) algorithms**, but this doesn't mean O(n) algorithms will always run faster, even in the same environment and the same hardware; maybe for small input sizes O(n) could be faster, but **as you approach towards infinity O(n^2) will eventually overtake O(n)**; just like any quadratic mathematical function will eventually overtake any linear function, no matter how much of a head start the linear function starts off with.

Another asymptotic complexity is logarithmic time; **O(log n)**. An example of an algorithm that runs this quickly is the classic **Binary Search Algorithm** for finding an element in an already sorted list on elements.

Let's say we are looking for the number 3 in the following array of integers [1, 2, 3, 4, 5, 6, 7].

The Binary Search Algorithm looks at the middle element of the array and asks: is the element greater than, less than, or equal to the element we are looking for?

If it finds the desired element, then you are done. If it's greater than the desired element, then it has to be in the right side of the array and you can only look at that in the future. If it's less than the desired element, you would do the same for the left side. This process is then repeated with the smaller size array until the desired element is found.

To further expand on the point, let's say we had an array with the below sizes:

`size 8 -> 3 operations (log₂8)`

`size 16 -> 4 operations (log₂16)`

If we were to **double the size of the array then the runtime would only be increased by a single chunk of the code** (splitting the middle element and checking) and is therefore said to run in **logarithmic time**.

Because an algorithm could potentially find the match on the first operation regardless of the input size, Computer Scientists have established a practice of measuring the upper and lower bounds of a runtime (the best and worst case performances of an algorithm), or **Omega**.

Continuing with the above notation of O(log n), our best case scenario is one where the element is right in the middle and thus one of constant time; we get the element in one operation no matter how big the array is. Thus, the best possible runtime for this algorithm is said to run in **Omega(1) time**. In the worst case scenario, it will run in O(log n) time as it has to perform O(log n) split-checks of the array to find the correct element.

By contrast, a **Linear Search Algorithm** (like the first string example) is one where we step through each individual character in the string, which means at best it is Omega(1) and at worst it is O(n).

The last keyword to touch on is **Theta**, which is used when the **best and the worst case scenario runtimes are the same**. Our second string problem is an example of this. No matter what number we store in the variable _len_, we will have to look at it. **The best case is we look at it and find the element. The worst case is we look at it and find the element. Therefore the runtime would be labeled as Theta(1),** as both the best and worse case scenarios are O(1) (constant time).

### Summary

---
In summary, we have good ways to reason about code's efficiency without knowing anything about the real world time they take the run (which is affected by an incredible number of different factors). It also allows us to reason well about what will happen when the size of the inputs increases towards infinity.

![Big O comparisons](https://i.imgur.com/np3rNEh.png)
</details>

<!-- [Harvard Big 0 Notation - Overview](https://www.youtube.com/watch?v=V6mKVRU1evU)
[UC Berkeley Big 0 Notation - Overview](https://archive.org/details/ucberkeley_webcast_VIS4YDpuP98)
[Big 0 Notation (and Omega/Theta) - Mathmatical](https://www.youtube.com/watch?v=1I5ZMmrOfnA&feature=youtu.be)
[UC Berkeley Big Omega](https://archive.org/details/ucberkeley_webcast_ca3e7UVmeUc)
[Amortized Analysis](https://www.youtube.com/watch?v=B3SpQZaAZP4&index=10&list=PL1BaGV1cIH4UhkL8a9bJGG356covJ76qN)
[Big 0 Cheat Sheet](http://bigocheatsheet.com/)
[General notes from Prof Skiena](http://www3.cs.stonybrook.edu/~algorith/video-lectures/2007/lecture2.pdf)
[A gentle introduction to Algorithm Complexity Analysis](http://discrete.gr/complexity/)
[Computational Complexity Pt. 1](https://www.topcoder.com/community/competitive-programming/tutorials/computational-complexity-section-1/)
[Computational Complexity Pt. 2](https://www.topcoder.com/community/competitive-programming/tutorials/computational-complexity-section-2/) -->

## [4] **Operating Systems**

## [5] **Object-Oriented Design**

## [6] **System Design**

## [7] **Databases & Database Architecture**

<details>
<summary><b>ERD
</b></summary>

### Bite Size Overview

---
In order to understand how the many elements of a database interact with eachother can be a daunting task, which is why Engineeers build Entity Relationship Diagrams, or ERD's for short.

### Videos & Links

---
1. <a href="https://www.youtube.com/watch?v=QpdhBUYk7Kk&vl=en">ERD Tutorial (video)</a>

### Notes

---
First off, let's define a few terms:
* **Entity**
    * An entity is an object, such a person, place, or thing to be tracked in the database. These are the **rows** in your database.
        * For example, if you purchase an item on Amazon then an entity can be an order, a customer, or the product itself.
* **Attributes**
    * Each entity is going to have a series of attributes, which are various properties or traits and are represented as the **columns** in your database.
        * Customer_ID, FirstName, LastName, etc.
* **Relationships**
    * Dscribes how the entities will interact with eachother (if they can). This is usually done by drawing a line in between them, denoting that there is some sort of interaction or sonnection in some way.
* **Cardinality**
    * Expands on the measuring the relationships, particularly in a numerical context; particularly within minimum and maximums.

        ![test](https://qph.fs.quoracdn.net/main-qimg-29c3a0080fe2fe1969e8e61a46de4b45)

Now, in the above example if we were asked to measure the cardinality between a customer and an order, we would ask ourselves:

* **What is the min/max number of orders that a customer could have?**
    * Min: Zero
        * A customer can exist but not have placed an order yet.
    * Max: Many
        * A customer could theoretically place an infinite number of orders.
    * **Result: Zero or Many**

Let's do the same for the order: 

* **What is the min/max number of customers that an order could have?**
    * Min: One
        * In order for an order to exist it has to have at least one customer.
    * Max: One
        * An order can only have at most one customer.
    * **Result: One (and only one)**

Now we need to do the other side, the cardinality between orders and products:

* **What is the min/max numbers of products that an order could have?**
    * Min: One
        * In order for an order to exist it has to have at least one product.
    * Max: Many
        * An order can contains an infinite number of products.
    * **Result: One to Many**

* **What is the min/max numbers of orders that a product can be a part of?**
    * Min: Zero
        * A product could simply not exist in an order, therefore an order can have zero of a product.
    * Max: Many
        * Conversely, it could also be a part of many orders.
    * **Result: Zero to Many**

![ERD](https://i.imgur.com/03uh619.png)

The above picture shows our resulting ERD and the cardinality between the tables (notice the crow's foot notation).

As we move into the next part of these notes a few more definitions need to be outlined (remember, each entity represents a table in your database):
* **Primary Key**
    * An attribute (or field) that uniquely identifies every record in a certain table.
    * There is one primary key per entity.
    * Unique.
    * Never changes.
    * Never NULL.

For the customer table in our above example, the primary key would be one that can allow us to easily distinguish between each customer.

Following along with the above constraints, we can quickly identify that the Customer_ID is the only unique identifier that we can use as a primary key. By design, a primary key is supposed to auto-increment for each record that is added to the table.

If we then jump over to the order table, it's pretty clear to see that Order_number is best utilized as our primary key.

And finally, Product_ID is our primary key for the product table.

Now, you may have noticed that there is a Customer_ID field in the orders table, yet it is now the primary key for the orders table. What an astute observation ;).

This is what is referred to as a:
* **Foreign Key**
    * The exact same as a primary key, just located in a foreign place (different entity (table)).
    * Doesn't have to be unique.
    * Can be repeated in a table.
    * Can have multiple foreign keys in one entry.

Suppose you have a primary key in one entity but it would be very helpful to pull that data into another entity; enter the foreign key. Taking note of our foreign keys can help us ascertain how our entities relate to eachother.

So, why is Customer_ID a foreign key in the orders table? Because for each order we place we need to know exactly which customer placed that order. The order entity is simply referencing the Customer_ID from the foreign entity.

This also means we need to adjust our crow's feet to reinforce the fact that our foreign key is referencing our primary key.

Let's for each order we also wanted to know which product is being purchased. We would add the Product_ID as a field into our orders table as a foreign key pointing to Product_ID in the products table, and then update our ERD as follows:

![Updated ERD](https://i.imgur.com/Lk3bbzY.png)

There's another term to touch on which is:
* **Composite Primary Key**
    * Used when two or more attributes are necessary to uniquely identify every record in a table.
    * Use the fewest number of attributes possible.
    * Don't use attributes that are likely to change.

If we were to create a shipment entity, we would have a foreign key referencing the Product_ID and another foriegn key referencing the Order_number. The problem with this table is that there is no way to uniquely identify a row, as the Product_ID is duplicated whenever another person purchases the same item, and the order could be split into a couple different shipments giving us a non-unique amount of Order_numbers.

This is when we need to combine the two foreign keys and create a composite key; both the Product_ID and the Order_number when squashed together provide us with a value that will not be repeated. This is technically called a **Compound Key** as we are using two foriegn keys, but usually people use composite key as an umbrella term.

Some people argue that you should just create a primary key in the shipments table (which I prefer), Shipment_ID for example, instead of using a compound key, but it all depends on how the database is created and whether or not incorporating a composite key makes sense.

Whenever you are creating your ER diagrams it is important to ask yourself "Is there anything else I should be recording into the database?". Sometimes you will have two entities connected to eachother, but there is more going on between them than you are accounting for. This is when you need to use a **Bridge Table**, which we will define after we outline the example below.

With our current setup, let's strip down our diagram to just compare the customer and product tables. You might ask if we could just create a direct connection between these two entities; a customer can purchase Zero or Many products, and a certain product can be purchased by Zero or Many customers. Ceonceptually, yes this does work, but the way this is set up you are not going to know a few important points:

* When did this person purchase the product?
* How many of them did they purchase at once?
* Did they return to purchase more at seperate times?

You are going to be in the dark about the relationship between many of these entities, and this is most common to occur in Many to Many relationships. In order to remedy this, we need to utilzie the:
* **Bridge Table**.
    * Allows for an intermediary one to many relationship and gets you the information you are lacking.

If we included the order entity back into our diagram, we can quickly see that this is acting as our bridge table. This breaks up the Many to Many relationship between the customer and product entities, and now whenever a cusomter purchases a product we will have a record of that interaction in our order table.

This is why you should always ask yourself if there is more data that you need to capture between the various entities.

### Summary

---
ERD's allow us to visualize the relationships between the entities in our database. We can utilize the crow's foot notation to map out relations when creating ERD's, and we always need to keep how and what potential data needs to be tracked within our desired system.

</details>

<details>
<summary><b>Normalization (1NF - 4NF)
</b></summary>

### Bite Size Overview

---
In simplest terms, normalization is the process of restructing a relational database through a series of "normal-forms" (1NF, 2NF, etc.) in an order to reduce data redundancy and improve data integrity.

### Videos & Links

---

1. <a href="https://www.youtube.com/watch?v=oexOYUUyQik&list=PL08dDdrkMLGrz67nBPbfX8KsGW-MUXU2G&index=47">What is Database Normalization?</a>
2. <a href="https://www.youtube.com/watch?v=UrYLYV7WSHM&list=PL08dDdrkMLGrz67nBPbfX8KsGW-MUXU2G&t=0s&index=49">Database Normalization, 1NF - 4NF (run at 1.25x speed)</a>

### Notes

---

### Summary

---
</details>

<details>
<summary><b>PostgreSQL
</b></summary>

### Bite Size Overview

---
PostgreSQL, more commonly referred to as Postgres, is a powerful and open source object-relational database management system (RDBMS). Postgres offers substantial additional power by leveraging **classes, inheritence, types, functions**, which is why we refer to Postgers as object-relational.

### Videos & Links

---
1. <a href="https://www.postgresql.org/docs/6.3/c0101.htm
">What is Postgres?</a>
2. <a href="https://www.postgresql.org/download/linux/ubuntu/">Install Postgres using apt</a>
3. <a href="https://www.tecmint.com/install-postgresql-from-source-code-in-linux/">Install Postgres from source code</a>
4. <a href="http://blog.shippable.com/why-we-moved-from-nosql-mongodb-to-postgressql">Why we moved from NoSQL MongoDB to PostgreSQL</a>

### Notes

---
In the past, traditional DBMS's only support a data model consisting of a collection of named relations which contain a small option of specific types (float, int, char string, money, date), but as you can see this model can quickly become inadequate for future data processing applications <a href="https://www.postgresql.org/docs/6.3/c0101.htm">source</a>. This is where the relational aspect of DMBS's comes into play due to their "Spartan simplicity", however the simplicity is still a double-edged sword as it makes implementation of certain application very difficult. As we touched on in the Bite Size Overview, this is where Postgres really shines; by leveraging those 4 basic concepts in addition to things like **constraints, triggers, rules, transactional integrity** and more it allows users to easily extend their system and deal with more complex processes.

### Summary

---
</details>

## [8] **Web Apps and Servers**

<details>
<summary><b>HTTP Protocol
</b></summary>

### Bite Size Overview

---
Designed to enable communications between clients and their servers. HTTP works as a request -> response protocol where the web browser is the client and an application on a computer that hosts the web site may be the server.

Chrome Dev Tools is a great way to watch how the browser interacts with a server backend (Chrome Dev Tools -> Network -> XHR).

### Videos & Links

---

1. <a href="https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Client-Server_overview">Client Side Programming</a>
2. <a href="https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Introduction">Server Side Programming</a>
3. <a href="https://www.telerik.com/download/fiddler">Fiddler (HTTP debugging software)</a>

### Notes

---
Clients (web browers) communicate by sending HTTP requests to the server and they can request a basic number of actions to be performed:
* `GET`
    * Fetch a specific resource.
        * _This could be returning a relevant HTML file or a list of products._
* `POST`
    * Create a specific resource.
        * _This could be whenever a user signs up for a website._
* `HEAD`
    * Fetch the metadata information about a specific resource without getting the body.
        * _This could be fetching a resource to check when it was last updated. Then we could use the expensive `GET` request to download the resource when it has changed._
* `PUT`
    * Update an existing resource (or create one if it doesn't exist).
        * _This could be whenever you click "update" to change your username on a website._
* `DELETE`
    * Delete the specified resource.
        * _This could be whenever you click "remove item" from your shopping cart._

Other terms you may come across are `TRACE`, `OPTIONS`, `CONNECT` and `PATCH`, but those are uncommon enough that they aren't worth touching on right now.

Web servers will wait (listen) for requests from the client, process them when they arrive, provide the correct HTTP response message and a HTTP response status code (200, 404, etc). Any corresponding JavaScript or CSS will be requested and downloaded during this time as well.

This is how both dynamic and static website communicate, so it is crucial to understand these communication protocols.

<details>
<summary>Let's take a look at an example of a <b>`GET` request</b>:</summary>

```
GET https://developer.mozilla.org/en-US/search?q=client+server+overview&topic=apps&topic=html&topic=css&topic=js&topic=api&topic=webdev HTTP/1.1
Host: developer.mozilla.org
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Referer: https://developer.mozilla.org/en-US/
Accept-Encoding: gzip, deflate, sdch, br
Accept-Charset: ISO-8859-1,UTF-8;q=0.7,*;q=0.7
Accept-Language: en-US,en;q=0.8,es;q=0.6
Cookie: sessionid=6ynxs23n521lu21b1t136rhbv7ezngie; csrftoken=zIPUJsAZv6pcgCBJSCj1zU6pQZbfMUAT; dwf_section_edit=False; dwf_sg_task_completion=False; _gat=1; _ga=GA1.2.1688886003.1471911953; ffo=true
```

The first and second lines contain most of the information we talked about above:

* The type of request (GET).
* The target resource URL (/en-US/search).
* The URL parameters (q=client%2Bserver%2Boverview&topic=apps&topic=html&topic=css&topic=js&topic=api&topic=webdev).
* The target/host website (developer.mozilla.org).
* The end of the first line also includes a short string identifying the specific protocol version (HTTP/1.1).
* The final line contains information about the client-side cookies — you can see in this case the cookie includes an id for managing sessions (Cookie: sessionid=6ynxs23n521lu21b1t136rhbv7ezngie; ...).

The remaining lines contain information about the browser used and the sort of responses it can handle. For example, you can see here that:

* My browser (User-Agent) is Mozilla Firefox (Mozilla/5.0).
* It can accept gzip compressed information (Accept-Encoding: gzip).
* It can accept the specified set of characters (Accept-Charset: ISO-8859-1,UTF-8;q=0.7,*;q=0.7) and languages (Accept-Language: de,en;q=0.7,en-us;q=0.3).
* The Referer line indicates the address of the web page that contained the link to this resource (i.e. the origin of the request, https://developer.mozilla.org/en-US/).

HTTP requests can also have a body, but it is empty in this case (<a href="https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Client-Server_overview">source for above</a>).

</details>

<details>
<summary>And the same for a <b>`GET` response</b>:</summary>

```
HTTP/1.1 200 OK
Server: Apache
X-Backend-Server: developer1.webapp.scl3.mozilla.com
Vary: Accept,Cookie, Accept-Encoding
Content-Type: text/html; charset=utf-8
Date: Wed, 07 Sep 2016 00:11:31 GMT
Keep-Alive: timeout=5, max=999
Connection: Keep-Alive
X-Frame-Options: DENY
Allow: GET
X-Cache-Info: caching
Content-Length: 41823


<!DOCTYPE html>
<html lang="en-US" dir="ltr" class="redesign no-js"  data-ffo-opensanslight=false data-ffo-opensans=false >
<head prefix="og: http://ogp.me/ns#">
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=Edge">
  <script>(function(d) { d.className = d.className.replace(/\bno-js/, ''); })(document.documentElement);</script>
  ...
```

The first part of the response for this request is shown below. The header contains information like the following:

* The first line includes the response code 200 OK, which tells us that the request succeeded.
We can see that the response is text/html formatted (Content-Type).
* We can also see that it uses the UTF-8 character set (Content-Type: text/html; charset=utf-8).
The head also tells us how big it is (Content-Length: 41823).
* At the end of the message we see the body content — which contains the actual HTML returned by the request.

The remainder of the truncated response header includes information like when it was generated, the server, how it expect to handle the page and more (<a href="https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Client-Server_overview">source for above</a>).

</details>

<details>
<summary>Now let's check out a <b>`POST` request</b>:</summary>

```
POST https://developer.mozilla.org/en-US/profiles/hamishwillee/edit HTTP/1.1
Host: developer.mozilla.org
Connection: keep-alive
Content-Length: 432
Pragma: no-cache
Cache-Control: no-cache
Origin: https://developer.mozilla.org
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Referer: https://developer.mozilla.org/en-US/profiles/hamishwillee/edit
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.8,es;q=0.6
Cookie: sessionid=6ynxs23n521lu21b1t136rhbv7ezngie; _gat=1; csrftoken=zIPUJsAZv6pcgCBJSCj1zU6pQZbfMUAT; dwf_section_edit=False; dwf_sg_task_completion=False; _ga=GA1.2.1688886003.1471911953; ffo=true

csrfmiddlewaretoken=zIPUJsAZv6pcgCBJSCj1zU6pQZbfMUAT&user-username=hamishwillee&user-fullname=Hamish+Willee&user-title=&user-organization=&user-location=Australia&user-locale=en-US&user-timezone=Australia%2FMelbourne&user-irc_nickname=&user-interests=&user-expertise=&user-twitter_url=&user-stackoverflow_url=&user-linkedin_url=&user-mozillians_url=&user-facebook_url=
```

The biggest difference you may have noticed is that the URL doesn't contain any paramaters. At the bottom of the request you can see that that the information from the form is encoded as a body in the request (`&user-fullname=Hamish+Willee`)
 (<a href="https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Client-Server_overview">source for above</a>).

</details>

<details>
<summary>And the same for a <b>`POST` response</b>:</summary>

```
HTTP/1.1 302 FOUND
Server: Apache
X-Backend-Server: developer3.webapp.scl3.mozilla.com
Vary: Cookie
Vary: Accept-Encoding
Content-Type: text/html; charset=utf-8
Date: Wed, 07 Sep 2016 00:38:13 GMT
Location: https://developer.mozilla.org/en-US/profiles/hamishwillee
Keep-Alive: timeout=5, max=1000
Connection: Keep-Alive
X-Frame-Options: DENY
X-Cache-Info: not cacheable; request wasn't a GET or HEAD
Content-Length: 0
```

Short and sweet :). The response status code of `302 FOUND` let's us know that the `POST` succeeded, and that it must issue a second request to load the page specified in the `Location` field (<a href="https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Client-Server_overview">source for above</a>).
</details>


A static site will only ever need to process `GET` requests as the server does not store any modifiable data, nor does it change its data based on the contents of an HTTP request (URL paramaters or cookies).

Dynamic sites handle requests for static files in the exact same way static sites sites do, but have the added bonus of allowing you to create HTML templates and insert the dynamic content into them whenever necessary. This means you can have one "Product" template that was used to render whatever product a user searched, eliminating the need to create potentially thousands of individual HTML files for each product.

This was just a brief overview of how a web client and a server communicate, but it should prove a decent foundation for now.

### Summary

---
Web clients and servers communicate through a series of HTTP requests, most commonly `GET`, `HEAD`, `POST`, `UPDATE` and `DELETE`. The server performs an action based on what the client is requesting of it, be it creating a new account, deleting a user, changing your username or something else entirely.

Chrome Dev Tools or Fiddler are both good options for exploring how websites interact in more detail.

</details>
    
<details>
<summary><b>MVC
</b></summary>

### Bite Size Overview

---
The MVC, or **Model-View-Controller**, is really just a design pattern for organizing code in an application to improve maintanability.

MVC is a general design pattern that outlines the structure of the system. It seperates the domain/application/business/etc logic from the rest of the User Interface.

Or in more technical terms, the primary purpose is to seperate "internal representations of information from the ways that information is presented to and accepted from the user", which **allows us to increase modularity for simultaneous development and code reuse** <a href="https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller">(source)</a>.

### Videos & Links

---

1. <a href="https://softwareengineering.stackexchange.com/questions/127624/what-is-mvc-really">What is a MVC really?</a>
2. <a href="https://alysivji.github.io/flask-part2-building-a-flask-web-application.html">Building an MVC with Flask</a>

### Notes

---
In a MVC design pattern each of the components [M, V, C] are defined as follows:

* **Model**
    * Handles application data and data-management
    * Includes your data structures, storage systems, etc. This is the data and data-management part of the structure
* **View**
    * Any output representation of information to the user (html, json, etc)
    * Renders data from model into form that is suitable for displaying in user interface
* **Controller**
    * Accepts inputs and converts commands for model and view (API layer)
    * A controller should **never** contain domain/business logic or be able to communicate directly to the database

The **model** stores data that is retrieved according to commands from the **controller**.

The **view** generates output for the user based on changed in the model.

The **controller** acts on both the **model** (to update state) and the **view** (to render changes).



### Summary

---
</details>

<details>
<summary><b>Web Frameworks
</b></summary>

### Bite Size Overview

---
Server-side Web Frameworks exist to make writing code and operations like we covered in the HTTP protocal section _much_ easier.

One of the most important operations they perform is simply mapping URLs to different resources/pages with special handler functions.

This makes it easier to keep the code associated with each type of resource separate. It also has benefits in terms of maintenance, because you can change the URL used to deliver a particular feature in one place, without having to change the handler function.

### Videos & Links

---
1. <a href="https://www.oreilly.com/learning/python-web-frameworks">Short online book by O'Reilly</a>
2. <a href="https://www.quora.com/Why-did-Pinterest-move-from-Django-to-Flask">Why did Pinterest move to Flask from Django?</a>

### Notes

---
The majority of web frameworks are exclusively server-side technologies (rendering the page on the server before sending it to the client).

Below are a few of the more common tasks that web frameworks can handle for you:

* Routing (URL)
* HTML, XML, and JSON (output format)
* Database manipulation
* Security against CSRF attacks
* Session storage and retrieval

Depending on the size of your application, you may end up outright removing or simply creating your own versions of the functions. The point is that some web frameworks come as "battery-included" libraries like Django, which means they come bundled with every feature off the bat, and others like Flask, which are light-weight and tend to only give you what you need.

<details>
<summary>Django Example</summary>

For example, consider the following Django code that maps two URL patterns to two view functions. The first pattern ensures that an HTTP request with a resource URL of /best will be passed to a function named index() in the views module. A request that has the pattern "/best/junior", will instead be passed to the junior() view function.

```
# file: best/urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
    # example: /best/
    url(r'^$', views.index),
    # example: /best/junior/
    url(r'^junior/$', views.junior),
]
```

The web framework also makes it easy for a view function to fetch information from the database. The structure of our data is defined in models, which are Python classes that define the fields to be stored in the underlying database. If we have a model named Team with a field of "team_type" then we can use a simple query syntax to get back all teams that have a particular type.

The example below gets a list of all teams that have the exact (case sensitive) team_type of "junior" — note the format: field name (team_type) followed by double underscore, and then the type of match to use (in this case exact). There are many other types of matches and we can daisy chain them. We can also control the order and the number of results returned.

```
# file: best/views.py

from django.shortcuts import render

from .models import Team


def junior(request):
    list_teams = Team.objects.filter(team_type__exact="junior")
    context = {'list': list_teams}
    return render(request, 'best/index.html', context)
```

After the junior() function gets the list of junior teams, it calls the render() function, passing the original HttpRequest, an HTML template, and a "context" object defining the information to be included in the template. The  render() function is a convenience function that generates HTML using a context and an HTML template, and returns it in an HttpResponse object.

Obviously web frameworks can help you with a lot of other tasks. We discuss a lot more benefits and some popular web framework choices in the next article (<a href="https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Client-Server_overview">source</a>).

</details>


There are pros and cons to all of the different web frameworks so I would highly recommend that you spend some time detailing out the exact nature of your problem and what framework would assist you in the most efficient manner. If you just have a small application that runs locally then you do not need to over-optimize and you should likely stick with a minimimalistic web framework like Flask. If you know you need built in ORM functionality or streamlines modules that you don't have the time to create from the ground up, something more "batteries-included" would be a great choice, like Django. There are plenty of other examples, but these are the two situations that are the most straightforward.

My personal preference is slanted towards Flask, particularly with how simply one can both build, expand, and maintain API's.

**There is a spectrum between minimal functionality with easy extensibility on one end and including everything in the framework with tight integration on the other end.**

### Summary

---
Web frameworks assist developers by abstracting away low-level processes and providing libraries with modules that will aid in the development of a web application. They are meant to aid you in both quickly scaffolding an application and in managing automate away a lot of overhead services, but keep in mind that those with the "batteries-included" approach can come with a tightly coupled internal set of packages or modules that may not be efficient for what you are trying to achieve.
</details>

<details>
<summary><b>API
</b></summary>

### Bite Size Overview

---

### Videos & Links

---

1. 

### Notes

---

### Summary

---
</details>

## [9] **Math**

<details>
<summary><b>Modulo
</b></summary>
Modulo returns the remainder (modulus), not the quotient, between two values.

```
4 % 2; <- returns 0
4 % 3; <- returns 1

This is commonly used in combination with a comparison operator:

4 % 2 == 0; <- returns True
4 % 3 == 0; <- returns False
```

* One common place to use Modulo (or the % operator) is when checking whether a number is divisible by another number.
    * For example, is 3 even or odd? If it is even it will produce a remainder of 0 when divided by 2, if it is odd it can't be evenly divided by 2.
* Great little short explanation (<a href="https://www.omnicalculator.com/math/modulo#what-are-modulo-operations">here</a>).
</details>
* Long-term TODO: Learn about set theory, finite-state machines, regular expressions, matrix multiplication, bitwise operations, solving linear equations, important combinatorics concepts such as permutations, combinations, pigeonhole principle.

## **References** (raw, will sort and format later)

* https://github.com/jwasham/coding-interview-university
* https://www.amazon.com/Write-Great-Code-Understanding-Machine/dp/1593270038
* https://www.amazon.com/Programming-Interviews-Exposed-Secrets-Programmer/dp/047012167X
* https://www.amazon.com/Structures-Algorithms-Python-Michael-Goodrich/dp/812656217X/
* https://startupnextdoor.com/want-to-work-at-amazon/
* https://startupnextdoor.com/retaining-computer-science-knowledge/
* https://github.com/jwasham/computer-science-flash-cards
* https://github.com/jwasham/code-catalog-python
* https://ankiweb.net/shared/info/25173560
* https://github.com/jwasham/practice-python
* https://www.amazon.com/Programming-Language-Brian-W-Kernighan/dp/0131103628
* https://github.com/lekkas/c-algorithms
* https://justin.abrah.ms/computer-science/big-o-notation-explained.html
* https://labs.spotify.com/2013/03/20/how-we-use-python-at-spotify/
* http://www.ironpythoninaction.com/magic-methods.html
* http://www.postgresqltutorial.com/postgresql-foreign-key/
* https://stackoverflow.com/questions/18211694/data-structure-model-of-score-keeping-app-for-games-avoiding-many-to-many-to-ma
* https://static.simonwillison.net/static/2010/redis-tutorial/
* https://docs.python.org/3/library/collections.html#collections.deque
* https://medium.com/coderbyte/how-to-get-good-at-algorithms-data-structures-d33d5163353f
* https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/
* https://techdevguide.withgoogle.com/
* https://interactivepython.org/runestone/static/thinkcspy/index.html
* https://onedrive.live.com/redir?resid=8D59514B5DBE9460%21171239&authkey=%21AAYudHw4Jy57cpY&page=View&wd=target%28README.one%7C7913485d-edef-4437-a685-c7deb73218aa%2FAbout%20this%20notebook%7C81ffa585-e123-47fd-b5a8-0b721f8aa357%2F%29
* https://realpython.com/python-thinking-recursively/
* https://realpython.com/python-memcache-efficient-caching/
* https://mike.place/2016/memoization/

_If you somehow ended up here, thanks for checking it out and I hope you find it helpful <3._
