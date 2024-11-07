#!/usr/bin/env python
# coding: utf-8

# # Q1.print poem twinkle twinkle little star

# In[2]:


print("""Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star.""")


# # Q2. use repl and print table of 5

# In[3]:


# done in terminal


# # Q3. Install an external module and use it to perform an operation of your interest.

# In[4]:


pip install pyttsx3


# In[6]:


import pyttsx3
engine = pyttsx3.init()
engine.say('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.''')
engine.runAndWait()


# # Q4. Write a python program to print the contents of a directory using the os module.Search online for the function which does that.

# In[11]:


import os

def print_directory_contents(path):
    try:
        # Get the list of all files and directories in the specified path
        dir_contents = os.listdir(path)
        
        print(f"Contents of '{path}':")
        for item in dir_contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{path}'.")

# Specify the directory path
directory_path = '/'  # Replace with the actual directory path

print_directory_contents(directory_path)


# In[ ]:




