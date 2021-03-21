# Election Analysis

## Project Overview:
  A Colorado Board of Elections employee has given the following tasks, to complete the election audit of a recent local congressional election. 
  
  1. Calculate the total number of voters cast
  2. Get a complete list of candidates who received votes.
  3. Calculate the total number of votes each candidate received.
  4. Calculate the precentage of votes each candidate won.
  5. Determine the winner of the election based on highest votes.

## Resources

  - Data Source: election_results.csv
  - Software: Python 3.7.6

## Summary
  - Below are the observations made, after anlyzing the data provided in a csv file:
  
  ###  - Total Votes: 369,711

  ###  - Candidates who received votes:
        - Charles Casper Stockham
        - Diana DeGette
        - Raymon Anthony Doane

  ###  - Counties where the elections were held:
        - Jefferson
        - Denver
        - Arapahoe

  ### - Winner of the election:
        - Diana DeGette with 73.8% of votes, which is 272,892 votes.

  ### - Final Results as generated by this query:
  <img src=resources/Terminal_Results.png width="40%">
  
  ## Reusability
    - The query used for this analysis is attached below. 
    - This has been built to be used for any election that will be conducted in the future.
   [PyPoll.py](Election_Analysis/PyPoll.py)

   ### - Here are some guidelines to reuse this query:
    - This query points to a file that is saved in the resources folder with name: "election_results.csv". 
    - In order to resuse this for another election, new election data needs to be saved here with the same name.
    - It is also important that the columns of the new file are the same as the old one.
    
  <img src=resources/file_path.png width="70%">
  
    - In a situation where the columns are not the same, the numbers within the box brackets (indexing) must be updated 
      to match the candidate name and county name columns. (Editing Example #1)
  <img src=resources/examples.png width="50%">

    - In a situation where the elections are held for state and not county, edit the word "county" to "state" or anything 
      that is deemeed relevant in the entire query. 
      (Editing Example #2)
      
  <img src=resources/examples2.png width="50%">

   ## What actually happens:
    - After updating the path and running the query, the first for loop starts: 
        1. Counting the total votes casted in the election.
        2. Capturing the names of the candidates for whom votes were casted.
        3. Capturing the county names for which elections were held and the votes for each.

  <img src=resources/for_loop_1.png width="70%">

    - At this point, total votes casted and votes for each county will be printed to a txt file on the 'Analysis' folder.
  
  <img src=resources/save_to_txt.png width="70%">
  
    - The next for loop is written to retreive county names from earlier loop, votes casted for each county and percentage 
      of votes from the overall votes.
    - Here, the county wil largest number of vote is printed to the same txt file right below the previous analysis.
  
  <img src=resources/for_loop_2.png width="70%">
  
    - The final for loop retrieves the votes for each candidate and saves them to the txt file along with the percentage 
      for each candidate.
    - And the final results of the election is printed at the end of the txt file, along with the vote count and percentage.

  <img src=resources/for_loop_3.png width="70%">
