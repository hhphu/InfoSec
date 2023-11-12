# High-stake Investigation

You have just been hired by Lucky Duck Casino as a security analyst.
- Lucky Duck has lost a significant amount of money on the roulette tables over the last month.
- The largest losses occurred on March 10, 12, and 15.
- Your manager believes there is a player working with a Lucky Duck dealer to steal money at the roulette tables.
- The casino has a large database containing data on wins and losses, player analysis, and dealer schedules.
- You are tasked with navigating, modifying, and analyzing these data files to gather evidence on the rogue player and dealer.
- You will prepare several evidence files to assist the prosecution.
- You must work quickly, as Lucky Duck can't afford any more losses.
- Lucky Duck Casino has provided you with the following files:
    - Roulette Player Data: Week of March 10
    - Employee Dealer Schedule: Week of March 10

## Setup
Run [setup.sh](setup.sh) file to download the files and setup folder strutures for the investigation.

## Correlating the Evidence
- Your next task is to correlate the large losses from the roulette tables with the dealer schedule. This will help you determine which dealer and player are colluding to steal money from Lucky Duck.

- Complete the player analysis with the following steps:
    1. Navigate to the Player_Analysis directory.
    2. Use grep to isolate all of the losses that occurred on March 10, 12, and 15.
    3. Place those results in a file called Roulette_Losses.txt.
    4. Preview the file Roulette_Losses.txt and analyze the data.
        - Record the following in the Notes_Player_Analysis.txt file:
        - The times the losses occurred on each day.
        - Whether there is a certain player who was playing during each of those times.
        - The total count of times this player was playing. > Hint: Use the wc command to find this value.

- Complete the dealer analysis with the following steps:
    1. Navigate to the Dealer_Analysis directory.
    2. This file contains the dealer schedules for the various Lucky Duck casino games: Blackjack, Roulette, and Texas Hold 'Em.
        - Preview the schedule to view the format and to understand how the data is separated.
    3. Using your findings from the player analysis, create a separate script to look at each day and time that you determined losses occurred. Use awk, pipes, and grep to isolate out the following four fields:
        - Time
        - a.m./p.m.
        - First name of roulette dealer
        - Last name of roulette dealer
        For example, if a loss occurred on March 10 at 2 p.m., you would write one script to find the roulette dealer who was working at that specific day and time.
    4. Run all of the scripts and append those results to a file called Dealers_working_during_losses.txt.
    5. Preview your file Dealers_working_during_losses.txt, and analyze the data.
        - Record the following in the Notes_Dealer_Analysis.txt file:
            - The primary dealer working at the times where losses occurred.
            - How many times the dealer worked when major losses occurred.
        - Complete the player/employee correlation.
            - In the notes file of the Player_Dealer_Correlation directory, add a summary of your findings noting the player and dealer you believe are colluding to scam Lucky Duck.
            - Make sure to document your specific reasons for this finding.

## Scripting Your Tasks
- You manager is impressed with the work you have done so far on the investigation They've now tasked you with building a shell script that can easily analyze future employee schedules. They will use this script to determine which employee was working at a given time in the case of future losses.
- Complete the following tasks:
    1. Remain in the Dealer_Analysis directory. Develop a shell script called roulette_dealer_finder_by_time.sh that can analyze the employee schedule to easily find the roulette dealer at a specific time.
        - Design the shell script to accept the following two arguments:
            - Date (four digits)
            - Time
    2. Test your script on the schedules to confirm that it outputs the correct dealer at the time specified.

## Optional Additional Challenge
- In case there is future fraud on other Lucky Duck games, create a shell script called roulette_dealer_finder_by_time_and_game.sh that has the following three arguments:
    - Specific time
    - Specific date
    - Casino game being played