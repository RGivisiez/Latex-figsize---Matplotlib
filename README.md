# Matplotlib figsize for latex

  This module returns the correct figure size for Latex documents. I found this in this [site][site_ref]
  

  The first step is to get the width of the document. To do so, put the command below inside the document and compile it,
this should generate a .log file where you will find the width. It will be something like this: 345.0pt. 
  
  > If your latex document is a normal text:
  > \showthe\textwidth
  
  > If your latex document has a column:
  > \showthe\columnwidth
  
  
  
  [a][ny times]

  
[site_ref]: https://jwalton.info/Embed-Publication-Matplotlib-Latex/
