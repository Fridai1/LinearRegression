# Linear Regression

We created a simple python script, implementing sklearn libraries to perform the AI functions.


We had some issues parsing the *.xlsx file, so we converted it to .csv and used that. 
That in itself caused its own errors.
First off we had $ signs in front of money values, we attempted to remove these with code, so that we didn't have to modify the document itself, though due to the way the document was read and stored in the variable this proved to be harder than we thought. We ended up removing the $ sings manually, the reason being that we would rather spend time trying to work with the AI part of the assignment and not the fundamentals of python.

Our second issue arose when having to deal with large numbers in a csv file, as they were separated with commas. like so: "102,232,000". we attempted to have pandas convert this to fullstops "." when imported into the variable, but due to the fact there were multiple commas this wouldn't work. Our solution where to remove the last three zeros, as all the large numbers in that column had that in common, so removing them shouldn't change the importance of the each value and the predictions should be the same regardless.

When running the code we measure the success with 