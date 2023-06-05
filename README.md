# 313 Sprite Sheets

Objectives
* Convert basic objects into a class
* Make use of class methods and properties within a class

Introduction
As we start to incorporate more and more objects in a canvas, keeping track of the properties of an object and how they interact with each other becomes a lot more difficult; there are too many things to keep track of.  We can start doing so with a class object

#### What is a class?
A class is a template from which we can create an object, with its own variable(properties).  It bundles a lot of the functions (methods) necessary to keep the object working.  For example, in the previous assignment, we added some functionality to update a sprite so that it was continually animated.  We can put this into a class definition to keep all of the relevant code within the class object.

##### Parts of a Class
Definition of class properties
Constructor definition
Class Methods
Destructor definition
Object instantiation

#### What is this "Self" thing?
Sometimes trying to keep track of variables that are global in scope is a problem.  Packing variables with our class definition is a way to create variables that can exist throughout the class template.  We use self to refer to the current object.

#### How do we define and instantiate a class?
Open example.1py

#### How do we incorpoate classes with a canvas and tkinter window?
Open example2.py

### Task 1
Collissions between objects
Rewrite your basic assignment that checks collisions between your main canvas actor and the obstacle.  Your new code should include an object for your actor and an object for your obstacle.  Create an interface between the two objects so that one object can retrieve information about the other object.

### Task 2
Collision betwen multiple objects
Same as task 1, but instantiate multiple obstacles in a list so that you can iterate through them.