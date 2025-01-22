JOIN is left/right: combines columns with same number of rows
UNION is top/bottom: combines rows with same number of columns   

we want union for combining the wildfire csv files  

gameplan:  
- new script to read in csv files, perform a union, and save into a) an excel sheet and b) a pickle file. this script shouldnt have to be run very often. pickle file can be uploaded to github. 
- when beginning to work with the model: can load in the pickle files instead of the excel file to shorten load time?  

back to UNION (with pandas): actually really easy
`union_df = pd.concat([df1, df2], ignore_index=True)`
  
cool