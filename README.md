# Philip_ProgrammingExercise_7
This program will allow the user to enter a paragraph, which also includes the sentences beginning with a number, to display each sentence of that given paragraph. It will also show the number of sentences that the user has given.

## Function: get_sentences
When the user is typing their paragraph, this code will break each sentence apart on a separate line depending on if they either use a “.”, “!”, or a “?”. Each sentence must start off with a capital letter or number.

Parameters:
s (This receives the paragraph that the user has written.)

Variables:
pat (Gives a pattern to the program to locate its sentences.)
s (Reassigns the sentences it can find to its list.)

Logic:
1. The program will locate all of the sentences in the paragraph given by the user’s input.
2. After the program finishes its scan, it will become set as the results when displayed.

Returns:
s

## Function: main
The program will ask the user to write a paragraph. For each sentence, it is separated on a specific line using the code above. Once the user finishes their paragraph, the program will display the results while also counting the total of sentences the user had written.

Parameters:
None

Variables:
s (Stores the paragraph that the user had inputted from the start.)
sentences (Shows the total number of sentences in that paragraph.)
i (Loops each variable from each sentence that was in the given paragraph.)

Logic:
1. The program will ask the user to input a paragraph they wrote.
2. Once the paragraph was given, the program will check each sentence that was written by the user.
3. After checking every sentence, the program will display the results while also adding the total of every sentence that was in the paragraph.

Returns:
None
