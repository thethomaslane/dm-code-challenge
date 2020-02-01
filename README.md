# dm-code-challenge
### Thomas Lane's code challenge for UCSD

## Use instructions:
### dosing.py
In order to use this command line script call it with the following parameters:

  "dosing.py -v \<viscode\> -s \<svdose\> -e \<ecsdstxt\> -o \<outputdirectory\>

viscode: The viscode you want to filtered results to have 

svdose: The svdose you want the filtered results to have 

ecsdstxt: The ecsdstxt you want to exclude from the filtered results 

outputdirectory: (Optional) The output directory you want the results.csv file exported to. Defaults to the current directory.


Sample call used to generate results.csv:

  "python dosing.py -v w02 -s Y -e 280"


### test_dosing.py
In order to run this test, you must have pytest installed.

With pytest installed, to run the tests call:

  "pytest"
