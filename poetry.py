poem = """If you are a dreamer, come in,
If you are a dreamer, a wisher, a liar,
A hope-er, a pray-er, a magic bean buyer…
If you’re a pretender, come sit by my fire
For we have some flax-golden tales to spin.
Come in!
Come in!"""

def line_printed_backwards(lines_list):
    """This function takes in a list of strings containing the 
    lines of your poem as arguments and will print the poem lines out in 
    reverse with the line numbers reversed"""
    #TODO:reverse the list
    
    lines_list.reverse()
    #print(lines_list)
    #TODO: use loop to print out items in list
    list_num = len(lines_list)
    
    for i in range(len(lines_list)):
        print(str(list_num) +" " + lines_list[i])
        list_num -= 1

    
def lines_printed_random():
    """randomly select lines from a list of strings and print them out in random order"""
    pass

def my_custom_function():
    """does somthing of my choosing 
    TODO: comment"""

#testing code
#TODO:Get poem string into list of lines
lines_list = poem.split("\n")
line_printed_backwards(lines_list)
#lines_printed_random()
#my_custom_function()