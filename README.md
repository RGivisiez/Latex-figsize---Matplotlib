# Matplotlib figure size for latex

  - This module returns the correct figure size for a Latex document. 
  - I used this [site][site_ref] as a reference.
  

  The first step is to get the width of the document. To do so, put the command below inside the document and compile it
  
- If your latex document is a normal text: **\showthe\textwidth**
- If your latex document has a column: **\showthe\columnwidth**
 
this should generate a `.log` file where you will find the width. It will be something like this:

> \> 455.0pt.
>
> l.45 \showthe\textwidth

or

> \> 695.55pt
>
> l.28 \showthe\columnwidth

The first number is used as a entry for the function. For example, if the width found is 455.0pt, the entry in the python function
will be 455.0.
 
My configurations:

 Thesis: 455.0pt **==>** (,)
 
 Banner: 695.55pt **==>** (,)
 
[site_ref]: https://jwalton.info/Embed-Publication-Matplotlib-Latex/
