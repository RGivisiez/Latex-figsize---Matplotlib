# Matplotlib figsize for latex

  - This module returns the correct figure size for a Latex document. 
  - I used this [site][site_ref] as a reference.
  

  The first step is to get the width of the document. To do so, put the command below inside the document and compile it
  
- If your latex document is a normal text: **\showthe\textwidth**
- If your latex document has a column: **\showthe\columnwidth**
 
this should generate a .log file where you will find the width. It will be something like this: 345.0pt. This number is used as a entry
for the function.
 
[site_ref]: https://jwalton.info/Embed-Publication-Matplotlib-Latex/
