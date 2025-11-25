import pandas as pd

#what file to look in
inputfile = "Bible.txt"
#What characters should be replaced with spaces
trimCharacters = ".,<>/?!@#$%^&*()`~'’:;[]}{-_=+\|\n	"

# this section reads the file, and stops further code from running if this fails
content = None

try:
    with open(inputfile, 'r',encoding='utf-8') as file:
        content = file.read()

except FileNotFoundError:
    print(f"Error: The file '{inputfile}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

if(content == None):
    print(content)
    quit()

# convert to lowercase
content = content.lower()

# trim out non-alphanumeric characters
for char in trimCharacters:
    content = content.replace(char," ")

# split the content up by spaces, meaning each item in this new list will be a word theoretically
splitTokens = content.split(" ")
print("")
print("")


countedTokens = dict()

# count the ocurrences of each word
for token in splitTokens:
    countedTokens[token] = countedTokens.get(token,0) + 1
    
# sort the words by number of occurrences
sorted = dict(sorted(countedTokens.items(),key=lambda item: item[1],reverse=False))

# output the files to the console and an excel file
for item in sorted.items():
    print(item)
    pass
df = pd.DataFrame.from_dict(sorted,orient="index")
df.to_excel(inputfile + "_analysis.xlsx",index=True)