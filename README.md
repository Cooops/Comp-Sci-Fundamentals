# Computer Science Fundamentals
This will serve as a repository for publically measuring my progress learning Computer Science fundamentals.

# Why are you doing this?
I want to improve my fundamental knowledge over the course of the next 6-12 months, rounding out any core Computer Science (mainly Data Structures & Algorithms) related information I am lacking. This will be a long-term venture with plenty of notes, videos, articles, and of cousrse code samples along the way. I will start out coding in Python, but will likely blend in C-related langauges down the line. 

I am doing this for myself first and foremost; not anyone else.

> "Why waste time proving over and over how great you are, when you could be getting better? Why hide deficiencies instead of overcoming them? Why look for friends or partners who will just shore up your self-esteem instead of ones who will also challenge you to grow? And why seek out the tried and true, instead of experiences that will stretch you? The passion for stretching yourself and sticking to it, even (or especially) when it’s not going well, is the hallmark of the growth mindset. This is the mindset that allows people to thrive during some of the most challenging times in their lives"

## Inspiration (videos & text): 
* http://www.aaronsw.com/weblog/dweck
* https://medium.freecodecamp.org/why-i-studied-full-time-for-8-months-for-a-google-interview-cc662ce9bb13
* https://www.youtube.com/watch?v=YJZCUhxNCv8

## Task List (will be constantly expanded upon and updated)
- Data Structures
    <!-- - [x] Hash Map, etc ?
    - Array -->
- Algorithms
- Operating Systems
- Object-Oriented Design
- System Design (solving problems at scale)
- Database design

# 1) Low-level Knowledge
* **[How a CPU works](https://www.youtube.com/watch?v=FZGugFqdr60&feature=youtu.be)**
* **[How a CPU executes a program](https://www.youtube.com/watch?v=XM4lGflQFvA)**
    - **Work in progress, will come back to this once my C related study material arrives...**
    - INC A
    - Machine code will usually represent binary patterns in hexdecimal. Hexdecimal is an easy way for humans to remember binary patterns.
    - Fetch, Decode, Execute
    - For a microprocessor to works the program counter has to contain a memory address that it points to.
* **[How computer's calculate - ALU](https://www.youtube.com/watch?v=1I5ZMmrOfnA&feature=youtu.be)**
* **[Registers and RAM](https://www.youtube.com/watch?v=fpnE6UAfbtU&feature=youtu.be)**
* **[Instructions and Programs](https://www.youtube.com/watch?v=zltgXvg6r3k&feature=youtu.be)**

# 2) Data Structures

# 3) Algorithms
* **[Asymptotic Notation](https://www.youtube.com/watch?v=iOq5kSKqeR4)**

    Fast or efficient algorithms =/= a measurement in real time (seconds, minutes) due to how much hardware varies, or that they might be running their program through a different piece of software, etc. Thus, the uniform way compare the algorithm is to measure the Asymptotic Complexity of a program, and to use the notation (Big O (or just O)) for describing this.
    **How fast a programs runtime grows asymptotically == as the size of your inputs increase towards infinity how does the runtime of your program grow?** 
    
    Think sorting an array with a size of 1 vs one of 1,000,000.
    
    Imagine counting the number of characters in a string the simplest way by walking through the whole string letter by letter and adding 1 to a counter for each character. This algorithm is said to run in linear time with respect to the number of characters (n) in the string. In short, it runs in **O(n); the time required to traverse the entire string is proportional to the number of characters**. 20 characters take twice as long as 10 characters, etc. As you increase the number of characters, **the runtime will increase linearly with the input length**.
        
    Lets says the above method isn't fast enough, so you may chose to store the number of characters in the string in a variable _len_, which you can then compare against instead of the checkin the string itself everytime .
    
    **Accessing len() is considered an asymptotically constant time operation, or O(1)**. This doesn't have to mean your code runs in one step, if it doesn't change with the size of inputs then it is still asymptotically constant.

    There are always drawbacks though, and in this case you have to spend extra memory space on your computer to store the variable (and the storage of the variable itself).

    There are many different Big O algorithms to measure runtimes with. **O(n^2) are asymptotically slower than O(n) algorithms**, but this doesn't mean they always run faster, even in the same environment and the same hardware. Maybe for small input sizes O(n) could be faster, but **as you approach towards infinity O(n^2) will eventually overtake the O(n) algorithm; just like any quadratic mathematical function will eventually overtake any linear function, no matter how much of a head start the linear function starts off it.**

    ![Big O comparisons](https://justin.abrah.ms/static/images/runtime_comparison.png)

    ![Big O comparisons](https://i.imgur.com/np3rNEh.png)
* [Harvard Big 0 Notation - Overview](https://www.youtube.com/watch?v=V6mKVRU1evU)
* [UC Berkeley Big 0 Notation - Overview](https://archive.org/details/ucberkeley_webcast_VIS4YDpuP98)
* [Big 0 Notation (and Omega/Theta) - Mathmatical](https://www.youtube.com/watch?v=1I5ZMmrOfnA&feature=youtu.be)
* [UC Berkeley Big Omega](https://archive.org/details/ucberkeley_webcast_ca3e7UVmeUc)
* [Amortized Analysis](https://www.youtube.com/watch?v=B3SpQZaAZP4&index=10&list=PL1BaGV1cIH4UhkL8a9bJGG356covJ76qN)
* [Big 0 Cheat Sheet](http://bigocheatsheet.com/)
* [General notes from Prof Skiena](http://www3.cs.stonybrook.edu/~algorith/video-lectures/2007/lecture2.pdf)
* [A gentle introduction to Algorithm Complexity Analysis](http://discrete.gr/complexity/)
* [Computational Complexity Pt. 1](https://www.topcoder.com/community/competitive-programming/tutorials/computational-complexity-section-1/)
* [Computational Complexity Pt. 2](https://www.topcoder.com/community/competitive-programming/tutorials/computational-complexity-section-2/)

# References (raw, will properly update later):
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

If you somehow ended up here, thanks for checking it out and I hope you find it helpful :).
