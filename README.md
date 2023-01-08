# PortfolioProjectPython

Python code covering a number of topics can be found in this repository, each code's name should help identify what each does but I will also supply a general 
description of each upload here in the README for ease of access.

The VCF_filtering file was used in my PhD and was created to process a directory of VCF files in order to isolate and document unique variant calls across numerous
cell lines. The program can take any number of VCF files and it is possible to specify a cutoff for numer of times a mutation is present across all lines. The code
will then take the desired output and create a new excel table and write the data to it, for each cell line in the directory it will create a seperate sheet within
that table for easier comparisons. As is it is currently set to produce only the unique mutations, but can be made to pull shared mutations or higher counts.

The movie correlation data project is used as a means to practice some data manipulation and to find various correlations across the dataset. 
Numerous plots were generated from scatterplots with correlation lines as well as multiple heatmaps were created to better help visualize the data.
I also wanted to play around with modifying datatypes and make comparisons between values in datasets that were outside the realm of bioinformatics.
