# Benford_Stocks
Repository dedicated to my MBA's dissertation, in the topic of statistical analysis of Stocks using the Newcomb-Benford distribution as a framework

Welcome!

The usage of this code is quite simple

First of all, you'll need the following python libraries:

pandas; matplotlib; sys; math; collections

The next step is to open the 001 file, which will daily update the stocks value for most of the companies listed at B3 - the brazilian Stock Market.

Then, after it updates it, you should copy the entire column and paste it into the first row and column of 002 file (I know it could be done directly from the 001 file, but I've created it this way in order to get more flexibility with my 001 file, so I can later do some more analysis, etc. In a near future I will simplify this part).

After the row with the updated values are pasted and the 002 file is saved, all there is left to do is run the python command. It should be in the following form:

$ python 003-Newcomb.py 002-Test.xml

Then, you should enter the date you're evaluating the stocks (most likely the actual date you're doing the analysis - just remember to run these analysis after the market closes). you will be asked separately for the day, month and year (remember to use two digits for day and month and four for the year).

then, the simulation will create 5 files. 3 plots of the first, second and third digits, a counting file with all the first, second and third digits and, lastly, a file containing the differences between the first digit seen and what should be expected for a NB analysis. When you re-do the analysis, the two text files will update with the new values, keeping the previous ones.
