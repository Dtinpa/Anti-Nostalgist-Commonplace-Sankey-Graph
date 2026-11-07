import plotly.graph_objects as go
import re
import os
import random

topoi = []
recordedTopoi = dict()

books = []
recordedBooks = dict()
topoiToBooks = dict()

chapters = []
recordedChapters = dict()
chaptersToBooks = dict()

labels = []

# builds the data relations that the sankey chart needs to map topoi to the books, and the books to their place in the commonplace
# read the first line, make sure that the header contains the 4 set attributes and that the length matches.  Any derivation and we exit
with open('DataSet.txt', 'r') as file:
    firstLine = file.readline()
    headers = re.split(r'\t+', firstLine.rstrip('\t\n'))

    if(len(headers) != 4):
        print("Missing headers.  Undo any edits to Dataset.txt")
        os._exit(os.X_OK)
    if(headers[0] != "topoi" or headers[1] != "book" or headers[2] != "chapter" or headers[3] != "volume"):
        print("Invalid headers detected.  Undo any edits to Dataset.txt")
        os._exit(os.X_OK)

    lineNumberInFile = 2;
    for line in file:
        dataset = re.split(r'\t+', line.rstrip('\t\n'))

        # if any line of the data set text file is malformed, exit the program
        if(len(dataset) != 4):
            print("Missing dataset attributes on line " + str(lineNumberInFile) + ".  4 attributes are expected for each entry according to the header at the top of the file")
            os._exit(os.X_OK)
        if(not dataset[2].isdigit() or not dataset[3].isdigit()):
            print("Invalid data point for chapter or volume field.  Ensure entries are whole numbers, and that each entry is seperated by a tab")
            os._exit(os.X_OK)

        lineNumberInFile += 1

        # parse out each attribute and assign it to its relational associate array
        # the order of extraction goes: topoi, books, chapter, and volume

        topic = dataset[0]
        book = dataset[1]
        chapter = dataset[2]
        vol = dataset[3]

        chapterVolString = str(chapter) + " " + str(vol)

        if(topic not in recordedTopoi):
            topoi.append(topic)
            recordedTopoi[topic] = len(topoi) - 1
            topoiToBooks[recordedTopoi[topic]] = []

        if(book not in recordedBooks):
            books.append(book)
            recordedBooks[book] = len(books) - 1

        topoiToBooks[recordedTopoi[topic]].append(recordedBooks[book])

        if(chapterVolString not in recordedChapters):
            chapters.append(chapterVolString)
            recordedChapters[chapterVolString] = len(chapters) - 1

        chaptersToBooks[recordedBooks[book]] = recordedChapters[chapterVolString]

# define the offsets for the sankey graph now, since the data source and target references the index of the label array
topoiOffset = len(topoi)
bookOffset = len(books)
chapterOffset = len(chapters)

# build out the individual chapter and volume array and dictionary to append the correct amount of chapter and volume nodes
chap = []
vol = dict()
sourceVol = []
targetVol = []
for val in chapters:
    chapterVol = val.split()
    chap.append("Chapter " + chapterVol[0])
    vol["Volume " + chapterVol[1]] = "Volume " + chapterVol[1]

    sourceVol = sourceVol + [topoiOffset + bookOffset + recordedChapters[val]]
    targetVol = targetVol + [topoiOffset + bookOffset + chapterOffset + int(chapterVol[1]) - 1]

label = topoi + books + chap + list(vol.values())

#build the source and target arrays so we can finally populate the chart
source = []
target = []

# first build the topoi book relations.  After this for loop is finished, we'll create the mapping of books to chapters
for idx, node in enumerate(topoi):
    bookList = [topoiOffset+x for x in topoiToBooks[idx]]
    sourceLabel = [idx] * len(bookList)
    
    source = source + sourceLabel
    target = target + bookList

# link each book to their respective chapter per volume
for idx, node in enumerate(books):
    chapterIndex = topoiOffset + bookOffset + chaptersToBooks[recordedBooks[node]]
    source = source + [topoiOffset + idx]
    target = target + [chapterIndex]

source = source + sourceVol
target = target + targetVol

# delete uneeded data structures
del topoi
del recordedTopoi

del books
del recordedBooks
del topoiToBooks

del chapters
del recordedChapters
del chaptersToBooks

# construct the color and value arrays.  value is what gives weight to the different nodes in the graph
linkColor = ["rgba(0,0,96,0.2)"] * len(source)
hoverColor = ["midnightblue"] * len(source)
value = [1] * len(source)

# finally call the library that instantiates the sankey graph and draw the connections between the nodes
fig = go.Figure(data=[go.Sankey(
        # Define nodes
	node = dict(
		pad = 15,
		thickness = 15,
		line = dict(color = "black", width = 0.5),
		label = label
	),
	link = dict(
		source = source,
		target = target,
                value = value,
                hovercolor = hoverColor,
		color = linkColor
))])


fig.update_layout(title_text="Anti-Nostalgist Index", font_size=10)
fig.show()
