
# NATO Alphabet 

You thought A for Apple, B for Ball? Well not according to the NATO Alphabet! 

![awkward](../../GIFs/giphy-b99-ThisIsAwkward.gif)

Don't make the decision to forget everything you learnt in kindergarten just yet! [NATO phonetic alphabet](https://en.wikipedia.org/wiki/NATO_phonetic_alphabet) is a series of codes assigned to letters and numbers to make them easily distinguishable from one another over radio and telephone. Try using these the next time someone has trouble understanding your name over the phone! 

### NATO Phonetic Alphabet CSV 
Contains alphabets and their Telephony codes.

The csv is read into a Dataframe. A dictionary is made from the Dataframe by iterating through the rows and making each alphabet into keys and codes being assigned as the corresponding values. 

A word is taken as the input from the user. For each letter in the word, if the letter is in the dictionary as a key, the corresponding value is added to a list. When all the letters in the word are converted into codes, the final list is printed as the output.
