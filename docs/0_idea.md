# Course project idea

Yanqiao Chen

## Title

Simple but automatic cat fight

## Description of project

* What I want to show is a battle bewteen two 1 level normal type monsters, so they only have 1 move, smash. I want to create 4 systems just like pokemon. Fight, Bag, Pokemon or capture, and Run.
each of these 2 monsters have 100HP
* ?die will decide who moves first
* Run: when your monster's HP is lower than 30, it may try to run. You have half chan to succeed to quit
* Bag: Heal 50Hp ? I want to achieve this by using a asumpable, which means you can only heal 1 time.
* Pokemon or Capture: your monster will try to capture the enemy when the enemy's HP is lower than 50. The success rate = HP enemy lost/100
* Fight: deal 20-30 demage, but you have 30%  chance to deal 150% of the original demage!
### If you plan to use any data sources, what are they and why?

First, I want to imoprt random and catname.json as monsters' names. So that will becomes a cat battle. Since we have four systems, I will use 4 functions. two dictionaries to store two monsters' information. And then a for loop  as a battle process.

### Tentative description of ideal output

A list that describes this battle just like:  
battle begins  
Ulysses v.s. British shorthair  
Ulysses deals 20 demages   
Bs deals 30 demages  
Critical hit! Ulysses deals 40 demage     
Bs uses item, it heals 50 HP   
Ulysses deals 25 demage  
Bs deals 30 demage  
Ulysses trys to capture.  
....  
He succeeds! 
Battle ends  
tip: they will all be automatic
## Statement of motivation/interest

I believe that will be coooool if I can create a game by programming. Now after I know a few knowledgements of Python, I sometimes think of how a game achieves something in code. So then when the turn-based battles came to my mind, I thought I can do it myself by using what I've learned. So I want it to be my project.

## Perceived or realized challenges

How to make sure you can only use item once. How to use die to decide who moves first. 