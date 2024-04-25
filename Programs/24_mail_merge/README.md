# Mail Merge

Me before learning about files: 

![imfine](../../GIFs/giphy_imfine.gif)

Me after: 

![yay](../../GIFs/giphy_yay.gif)

### How it works 
The 'invited_names' file is first read and stored into a variable. This long string is split into individual names and stored in a list by splitting the string using the newline character as a separator. 

The 'starting_letter' file is read and stored into a sample letter variable.

For each name in the name list, the sample name in the letter is replaced with a name in the list and a new file is created using the name. The letter addressed to the name is written into the newly generated file.