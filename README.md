# **Computer Science Fundamentals**

This will serve as a repository for publically measuring my progress learning Computer Science fundamentals.

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
* Data Structures
* Algorithms
* Operating Systems
* Object-Oriented Design
* System Design (solving problems at scale)
* Database Architecture

## [1] **Low-level Knowledge**

1. **[How a CPU works](https://www.youtube.com/watch?v=FZGugFqdr60&feature=youtu.be)**
2. **[How a CPU executes a program](https://www.youtube.com/watch?v=XM4lGflQFvA)**
    * **Work in progress, will come back to this once my C related study material arrives...**
    * *INC A
    * Machine code will usually represent binary patterns in hexadecimal. Hexadecimal is an easy way for humans to remember binary patterns.
    * Fetch, Decode, Execute
    * For a microprocessor to works the program counter has to contain a memory address that it points to.
3. **[How computer's calculate - ALU](https://www.youtube.com/watch?v=1I5ZMmrOfnA&feature=youtu.be)**
4. **[Registers and RAM](https://www.youtube.com/watch?v=fpnE6UAfbtU&feature=youtu.be)**
5. **[Instructions and Programs](https://www.youtube.com/watch?v=zltgXvg6r3k&feature=youtu.be)**

## [2] **Data Structures**


## [3] **Algorithms**

<details>
<summary><b>Asymptotic Notation (Big O)</b></summary>

### Bite Size Overview

---
Asymptotic Notation, aka Big O notation, is the most common metric for calculating time complexity. In simpler terms, Big O notation is how programmers talk about algorithms. A functions Big O notation is determined by how it responds to different inputs. How much slower is it if we feed in a list of 1,000,000 elements instead of 1? Big O describes the number of steps it takes to reach the base case.

### Videos

---

1. <a href="https://www.youtube.com/watch?v=iOq5kSKqeR4">The best high-level explanation I've seen to date.</a>
2. More later...

### Notes

---
Fast or efficient algorithms =/= a measurement in real time (seconds, minutes) due to how much hardware varies, or that a user might be running their program through a different piece of software, etc. Thus, the uniform way compare the algorithm is to measure the Asymptotic Complexity of a program, and to use the notation (Big O (or just O)) for describing this.
**How fast a programs runtime grows asymptotically == as the size of your inputs increase towards infinity, how does the runtime of your program grow?**.

I magine counting the number of characters in a string the simplest way by walking through the whole string, letter by letter, and adding 1 to a counter for each character.

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
    strngLen = len(strng)
    return strngLen
```

**Accessing len() is considered an asymptotically constant time operation, or O(1)**. What this means is no matter how big your input is it will always take you the same amount of time to compute things (one step). This doesn't have to mean your code runs in one step; if it doesn't change with the size of inputs then it is still asymptotically constant. There are always drawbacks though and in this case you have to spend extra memory space on your computer to store the variable (and the storage of the variable itself). **Constant time is considered the best case scenario for a function.**

![Big O comparisons](https://justin.abrah.ms/static/images/runtime_comparison.png)

There are many different Big O runtimes to measure algorithms with. One area you may run into **O(n^2)** notations is with combinations and is especially useful when it comes to data structures. See the following code example which would match every item in the list with every other item in the list:

```
def all_combinations(array):
    results = []
    for item in array:
        for inner_item in array:
            results.append((item, inner_item))
    return results
```

This function (algorithm) is considered O(n^2) as every input requires us to do n more operations; n*n == n^2. Thus, **O(n^2) are asymptotically slower than O(n) algorithms**, but this doesn't mean they always run faster, even in the same environment and the same hardware. Maybe for small input sizes O(n) could be faster, but **as you approach towards infinity O(n^2) will eventually overtake the O(n) algorithm**; just like any quadratic mathematical function will eventually overtake any linear function, no matter how much of a head start the linear function starts off with.

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

By contrast, a **Linear Search Algorithm** is one where we step through each individual character in the string, which means at best it is Omega(1) and at worst it is O(n).

The last keyword to touch on is **Theta**, which is used when the best and the worst case scenario runtimes are the same. Our first string problem is an example of this. No matter what number we store in the variable we will have to look at it. **The best case is we look at it and find the element. The worst case is we look at it and find the element. Therefore the runtime would be labeled as Theta(1),** as both the best and worse case scenarios are O(1) (constant time).

In summary, we have good ways to reason about code's efficiency without knowing anything about the real world time they take the run (which is affected by an incredible number of different factors). It also allows us to reason well about what will happen when the size of the inputs increases.

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

## [7] **Database Architecture**

## References (raw, will properly update later)

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

_If you somehow ended up here, thanks for checking it out and I hope you find it helpful <3._
