This implementation defines a token as a maximal sequence of 
ASCII letters (A–Z, a–z) and digits (0–9), normalized to 
lowercase. All other characters, including punctuation, 
and non-English characters, act as delimiters. Files 
are decoded as UTF-8, and malformed byte sequences are 
replaced with delimiter characters so processing can continue. 
Part B counts distinct tokens shared by both files. 
repeated occurrences do not increase the count.
Files are read in chunks, with incomplete tokens preserved across chunk boundaries. 
Part A returns the required token list
Part B streams tokens and stores the first file’s unique vocabulary. 

AI declaration:
ChatGPT helped generate the initial code structure.
