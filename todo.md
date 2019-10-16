Urgent
======


Open (in loose order of priority)
=================================

ID  Owner   Issued      Task
----------------------------

11  PG      15 Oct 2019 tell HR to arrange contract with MD - done
    MD      16 Oct 2019 arrange contract with HR

10  PG/MD   8 Oct 2019  fix physical meeting

9   Marina  8 Oct 2019  web [continuous_profile] app/profile_continuous.php
                        send 2-3 URLs as standard tests to discuss appearance
                        on load: zoom window to jump to data (to avoid looking at a blank zoom window)
                        zoom window: less tall, display more hours? (let's discuss)
            15 Oct 2019 max 8 activity icons vertically. If more [...] icon and show in tooltip

6   Phil    12 Sep 2019 Gender paper
            16 Oct 2019 identify top 5 activities of difference
                        difference in reporting frequency
                        difference in timing
                        difference in simultaneous activities

2   Marina  6 Sep 2019  Reading paper compare CREST and Meter profiles
                        waiting for Reading profiles
            7 Oct 2019  Timur on leave - deadline 1st of November

On Hold
=======

4   Phil    6 Sep 2019  Invite Osney to event
                        Waiting for Mim for date

1   Aven    6 Sep 2019  Source trophy for Osney winner
                        Wait for winter study TBC
                        Marina to continue??

Closed
======
12  Marina  16 Oct 2019 Update DB to have only one idHH for each WOSC contact. I chose the unique idHH to be the idHH of the latest run with good electricity (or the latest run generally, for the household that never managed to give us good electricity). I updated the idHH in the Meta and the Run table accordingly, and deleted the HH entries in the Household table belonging to the 'extra' households. In case something went wrong, we can always restored the data either from our backups or from the deposited dataset that included WOSC. The .csv file with 'idContact, oldHH, newHH' columns is pushed to the MeterData repository. It keeps track of what was renamed.

5   Marina  12 Sep 2019 Run WOSC analysis on Osney
            7 Oct 2019  MD: See Analysis [mpdev] output/Osney/Osney.md and scripts/osney_wosc_comparison_new.py

7   Phil    7 Oct 2019  MD: To arrange Skype with Marina, to talk about a) the vis, b) prelim Osney activities' analysis, c) potential visit, d) gender paper?
                        PG: email 8 Oct 2019 - suggest Mondays 3pm
8   Phil    3 Oct 2019  MD: To look at the continuous profile vis - it's a blend of profile and browser-based vis; what needs to be added/taken away, or modified?
                        PG: Looking good. Suggestions in Task 9
3   Marina  6 Sep 2019  Profile span all readings
            30 Sep 2019 Simplified version based on mobile js
            3 Oct 2019  Passed a sample version to Phil - see task 9

0   Phil    30 Sep 2019 Git to trigger notification on commit for Data repo
