# **Computer Science Fundamentals** (work in progress)

This will serve as a repository for publically measuring my progress both learning and brushing up on Computer Science fundamentals.

## Synopsis

I want to improve my fundamental knowledge over the course of the next 6-12 months, rounding out any core Computer Science (see Task List below for specifics) related information I am lacking. This will be a long-term venture with plenty of notes, videos, articles, and of course code samples along the way. I will start out coding in Python, but will likely blend in C-related langauges down the line.

I am doing this for myself first and foremost; not anyone else.

> "Learning is not attended by chance, it must be sought for with ardor and dilligence." - Abigail Adams

## Inspiration (videos & text)

* http://www.aaronsw.com/weblog/dweck
* https://medium.freecodecamp.org/why-i-studied-full-time-for-8-months-for-a-google-interview-cc662ce9bb13
* https://www.youtube.com/watch?v=YJZCUhxNCv8

## Task List (will be constantly expanded upon and updated)

* Low-level knowledge
* Operating Systems
* Data Structures
* Algorithms
* Object-Oriented Design
* System Design (solving problems at scale)
* Databases
* Web Apps & Servers

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
<summary><b>Hash Tables</b></summary>

### Bite Size Overview

---
Hash Tables, or more commonly dictionaries in Python, are a type of data structure that stores key-value pairs where the key is generated through a hashing function. This improves the functionality by a significant margin as the key values themselves act as the index of the array which stores the data. A picture says a thousand words:

```
dict = {'Name': 'Cooper', 'Focus': 'Comp Sci Fundamentals'}

print(dict['Name'], dict['Focus'])

>>> Cooper, Comp Sci Fundamentals
```

### Videos & Links

---

1. 

### Notes

---
A Dictionary satisfied the requirements to properly represent the implement of a Hash Table:

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

### Videos & Links

---

1. <a href="https://medium.freecodecamp.org/python-interview-question-guide-how-to-code-a-linked-list-fd77cbbd367d">Linked Lists in Python (text)</a>
2. <a href="https://www.youtube.com/watch?v=6sBsF13n5ig"> Linked Lists in Python (video)</a>
3. <a href="https://stackoverflow.com/questions/39585740/how-can-i-print-all-of-the-values-of-the-nodes-in-my-singly-linked-list-using-a">Linked Lists - StackOverflow (text)</a>
4. <a href="https://stackoverflow.com/questions/39585740/how-can-i-print-all-of-the-values-of-the-nodes-in-my-singly-linked-list-using-a">Printing a Singly-Linked List (text)</a>

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

### Videos & Links

---

1. 

### Notes

---

### Summary

---
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
Web frameworks are libraries of server-side languages that contruct the back-end structure of a site. Web frameworks aim to automate the overhead services associated with common activities performed in web application (and abstract away low-level issues like protocols and sockets).

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

There are pros and cons to all of the different web frameworks, so I would highly recommend that you spend some time detailing out the exact nature of your problem and what framework would assist you in the most efficient manner. If you just have a small application that runs locally then you do not need to over-optimize and you should likely stick with a minimimalistic web framework like Flask. If you know you need built in ORM functionality or streamlines modules that you don't have the time to create from the ground up, something more "batteries-included" would be a great choice, like Django. There are plenty of other examples, but these are the two situations that are the most straightforward.

The personal preference is slanted towards Flask, particularly with how simply one can both build, expand, and maintain API's.

**There is a spectrum between minimal functionality with easy extensibility on one end and including everything in the framework with tight integration on the other end.**

### Summary

---
Web frameworks assist developers by abstracting away low-level processes and providing libraries with modules that will aid in the development of a web application. They are meant to aid you in both quickly scaffolding an application and in managing automate away a lot of overhead services, but keep in mind that they with the "batteries-included" approach they can come with a tightly coupled internal set of packages or modules that may not be efficient for what you are trying to achieve.

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

## [8] **References** (raw, will sort and format later)

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

_If you somehow ended up here, thanks for checking it out and I hope you find it helpful <3._
