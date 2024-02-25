def createTextFile(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

"""function takes a filename as input, reads the file line by line, 
and counts the occurrences of each word. 
It returns a dictionary."""
def wordCount(t):
    word_dict = {} # Create an empty dictionary to store the word counts
    with open(t, 'r') as file:
        for line_num, line in enumerate(file, start=1): # enumerate built-in function is used to iterate over the lines of a file and simultaneously get both the line number and the content of each line
            words = line.split() # line.split() is used to split the content of each line into a list of words.
            for word in words:
                if word not in word_dict:
                    word_dict[word] = [line_num]
                else:
                    word_dict[word].append(line_num) 
    return word_dict

sample_content = """
This is a sample text file.
It contains some words for testing the wordCount function.
Let's see how it works. This is the last line.
"""
sample_filename = 'sample_text.txt'
createTextFile(sample_filename, sample_content)

result = wordCount(sample_filename)

print(result)