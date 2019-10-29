# Backwards Poetry

## Description
In this project we will write a Python program to print out poetry backwards, randomly, and any way you can rearrange!
By reading a poem in news ways we can discover new meanings or invite new interpretations.

Credit to Mark D. LeBlanc for their project posted on EngageCSEdu

## Learning Outcomes
By completing this project, you should be able to…

1. Implement functions
1. Practice storing items in lists and reading from them
1. Implement loops
1. String manipulation and formatting
1. Apply the random module to your programs
1. Make connections to fields outside of CS

## Schedule

From the day this project is assigned, you will have approximately **1 week** to complete this project. A sample daily outline is provided to assist you in planning your project.

**Important note:** “Day 01” refers to the first calendar day of the project being assigned, and subsequent days will follow this reference:

- Day 01: Project assigned, read the project spec, ask any clarifying questions you may have, begin designing how you would implement the project, set up your repo
- Day 03: Build lines_printed_backwards() function
- Day 05: Build lines_printed_random() function
- Day 06: Build a rearrange function of your choice
- Day 07: Fix any remaining bugs, make sure your code has helpful comments, and submit the project!

## Requirements

1. You can store your poem as a multi line string in Python, you do not need to read from a file.

2. Your code should implement the lines_printed_backwards() function. This function takes in a list of strings containing
the lines of your poem as arguments and will print the poem lines out in reverse with the line numbers reversed. For example, if you poem is Invitation by Shel Silverstein:

If you are a dreamer, come in,\
If you are a dreamer, a wisher, a liar,\
A hope-er, a pray-er, a magic bean buyer…\
If you’re a pretender, come sit by my fire\
For we have some flax-golden tales to spin.\
Come in!\
Come in!

then your function will print:

7 Come in!\
6 Come in!\
5 For we have some flax-golden tales to spin.\
4 If you’re a pretender, come sit by my fire\
3 A hope-er, a pray-er, a magic bean buyer…\
2 If you are a dreamer, a wisher, a liar,\
1 If you are a dreamer, come in,

3. Your code should implement the lines_printed_random() function which will randomly select lines from a list of strings and
print them out in random order. Repeats are okay and the number of lines printed should be equal to the original number of lines
in the poem (line numbers don't need to be printed). Hint: try using a loop and randint()

4. Your code should implement a function of your choice that rearranges the poem in a unique way, be creative! Make sure that you carefully comment your custom function so it's clear what it does.

5. Feel free to use any poem of your choice.
