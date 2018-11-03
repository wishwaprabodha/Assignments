# Machine Learning Assignment 01

## Information Retrieval

### Task - Preprocess 20NewsGroupsData dataset

### Steps

```
01. Import packages.
02. Create a function to get all filenames to a list.
03. Check the filepath and categorize those accordingly.
04. Train/Test split. (filenames)
05. Get the tokenized and cleaned wordlist for respective category. (List of lists)
06. Convert category list to one dimemsional list. (Flatten the list)
07. Convert lists to dictionaries with respective occurance frequencies.
08. Print the wordlists to CSV files.
09. Combine all lists to 02 train/test separate lists.
10. Create a sample list with few file names.
11. Create a dataframe of all training words vs each comp file content.
12. Create functions to generate respective dataframes and CSV files. 

```

### Tokenizing Process

```
1. Read files using utf-8 file encoding to avoid complications.
2. Get the english stopWords list.
3. Tokenize words and use a regular expression (Regex) to avoid numbers and non-alphabetic words.
4. Remove punctuation marks from words.
5. Convert all words to lower case for convienience.
6. Append words to a list.

```

### Libraries Used

* **codecs** - *file reading*
* **os** - *directory access*
* **nltk** - *processing toolkit for NLP tasks*
* **pandas** - *writing to csv*
* **collections** - *Flat multidimensional Lists*

### Imporatant

* **Last two functions are not executed** - * Due to less processing power for the computation*

*-Completed for submission-*

## Thank You!
