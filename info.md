


Further information
===================

Data Processing
---------------

**Processing electricity data**

The electricity data is collected by the eMeter at 1 second resolution. For faster data processing the data is downsampled to 1 minute and 10 minute readings and stored in two additional tables:

- **Electricity_1min**
- **Electricity_10min**

An even coarser resolution is available from a View named **El_hour**. This is computed on the fly from **Electricity_10min**.

Faulty readings can in most cases be removed by excluding values where ``Watt`` < 20 Watt

.. _activities:

**Processing activity data**

Activity records are stored as a json record and consist of the following data:

- Key: constructed from the time of the activity (for sorting purposes) and a unique component (to distinguish activities performed at the same time)
- Time use code: 4 digit code from 144 pre-coded activities
- Time of reporting: when the record was created
- Time of activity: when the activity is reported to have taken place
- Location
- Number of other people
- Enjoyment
- Path: a comma separated list of all buttons pressed as part of the entry sequence.


Participants enter activities using a dedicated app. Processing involves deconstructing the information received about an activity from the app, and populating the fields in the Activities table. Each record in the **Activities** table corresponds to an activity entry by the user.

An activity entry consists of specifying location, time, actual activity, enjoyment, and people. Users either enter new activities, or edit/delete/rename existing ones. The possible sequence of button presses allowed by the app are given by the app files *screens.json* and *activities.json*.

The corresponding activity record in the **Activities** table is a result of processing the activity entry. The app outputs the following information about an activity entry: the time of entering or modifying the activity, and the sequence of buttons the user pressed to record it. The former is the *time of recording*, and it is stored in the ``dt_recorded`` field. The latter corresponds to the raw, unprocessed *path*, and is stored in ``path``. These two fields are taken from the app without processing. All the other fields in the Activities table are derived from the original sequence of buttons that is subsequently stored in *path*. These fields are ``dt_activity``, ``tuc``, ``activity``, ``category``, ``location``, ``people``, and ``enjoyment``. The final TUC associated with the actual activity is given under ``tuc``, its description from *activities.json* is shown under ``activity``, and its category from *activities.json* under ``category``.

A path can be thought of as a sequence of Time-Use Codes (TUCs), each of which corresponds to a button. Some TUCs are app-specific, like the code used to set the activity time back 10 minutes. Others are more universal, and shared in the time-use literature, like the TUC for Personal activities ('0'). The exact correspondence between the TUC and what it means, and also how it appears to user in the app, can be found in *activities.json*. It is using this file that the python code converts relevant parts of the activity entry into appropriate fields of the database record.


The ``activity`` field entry can sometimes contain one or more *(end)* at the end of it. Each *(end)* corresponds to the participant pressing the `END` button in the app in order to report that that activity has ended. Note that the ending of the activity gets a separate record in the **Activities** table.

Some activities, whose ``Meta_idMeta`` appears as ``idMeta`` in the **Meta** table with the corresponding ``DataType`` = *E*, correspond to a participant entering information about the possible appliances in use during a particular hour associated with that household's electricity reading (as part of the Follow-up survey). These activities by definition pertain only to some limited set of appliances, and therefore cannot have meaningful data in the fields of ``path``, ``enjoyment``, ``location``, ``people``. The time of the appliance these activities reference is meant to represent the *hour* at which these were (switched) on, rather than the exact time. As such these are qualitatively different activities to those whose ``Meta_idMeta`` is associated with an *A* in the **Meta** table. Without the **Meta** table it is impossible to tell these appliance-related activities from activities entered through the diary/app.




Data Validation
---------------

**Household Survey**

We take what is reported as a given. While it is theoretically possible to use the electricity readings to infer the presence (from use) of this or that particular type of appliance, METER's project aim is *not* to give appliance-related descriptions of households; the role of the Household Survey is to give a necessary, rather than a sufficient, description. Thus, if a participant reports their household having washing machine, this is taken to be the ground truth.

The survey answers admit one self-consistency check. The sum of people across all the different age-groups should be the same as the `total number of people` question.




**Cross-validation of activity and electricity data**
Verifying the accuracy of self reported activities is inherently difficult. @Gershuny17a claim that their validity is not in doubt and use objective instruments, including video footage, to support this assertion by comparing the total duration of activities reported and observed. For their sample of 131 people, only TV, eating and reading diverge between the video footage and the diaries. Surprisingly, the amount of time watching TV is over-reported and reading is under-reported, each by nearly 10%. This is contrary to the expectation that non-desirable activities get under-reported and more desirable ones over-reported.

Reporting of 'hot drink' related activities, when carried out at home, lends themselves to testing the accuracy of the activity records used here. Such activities are reported frequently and the performance of the activity is broadly neutral in terms of social desirability. 53% of individuals and 73% of households report making a hot drink or use of a kettle during their day at least once.

Coincidence of electrical load signature of a kettle with the reporting of a 'hot drink' like activity

.. figure:: images/kettle_profiles.png
   :scale: 40 %

The electricity signature of a kettle is very distinct and usually short lived, such that it provides a helpful marker for temporal accuracy, as shown in the illustrative examples in Figure 2. It is less suitable as a test for false negatives. If a hot drink has been reported and no kettle signature can be detected it could either be that the activity was reported wrongly or too inaccurately time-wise, or that the hot drink did not involve an electric kettle, but for instance a gas fired kettle. This is the case for 26% of events.

For all other cases the time difference *d_t* of the reported activity and the corresponding kettle signature can be compared. A histogram of the error between the two events is shown in Figure 3.

Error between reporting of kettle signature in load profile (N=130)

.. figure:: images/hist_kettle_reporting_N130.png
   :scale: 40 %

In over 67% of cases the reporting accuracy is within 10 minutes of the observed electricity signature. Narrowing the scope to explicit reporting of the appliance 'kettle' itself improves this figure to 80%.

The high quality of temporal alignment between activities and their associated appliances arising from this collection method allows us to broaden the analysis to activities that are less directly associated with an easy to identify appliance. Kettles have a very prominent signature due to their high power and short use periods. In energy terms they are rather less significant and we therefore consider more energy intensive activities and appliances in the following section.




Missing Data
-------------------

* It is possible to check whether the household survey has been filled in by comparing entries to the default values of the fields - a most likely example is that the number of people home at 6pm should not be '-1'.

* Electricity consumption on the raw, 1 second resolution, contains some missing datapoints, leading the corresponding lower resolution tables to have missing data as well.

* Individual survey:  individual surveys are accessed through the a-meter. Consequently, it is possible that some individuals do not fill in their surveys. At this point it is impossible to say whether they are missing completely at random, and indeed, some correlation between the diligence in entering activities, and in filling in the individual survey, is somewhat expected.

* Activities entered as part of the follow-up survey. Entering these is not a requirement, and consequently some households will not do so.


Possible errors
---------------

**Electricity**

* An improperly attached current clamp, leading to incorrect electricity readings.

  It is the responsibility of the participants to properly attach the e-meter to the correct cable. In most cases it is a straight-forward task, particularly if the electricity meter is easy to access. However, METER has already noted the following exceptions:

	 - existence of more than one electricity meter per household
	 - cables tied together, or there being more or fewer cables than 4

  The participant could then attach the e-meter to the wrong cable, the wrong meter, or not close the current clamp properly - all of which would lead to wrong, low, or incomplete electricity readings.

  Incomplete or low readings are hard to monitor. The METER team assesses the *correctness* of the readings by eye, and if they look too low, then the usual procedure is to follow that up with the participants. However, since this criteria is a matter of judgement, it is possible that some low readings which the team took to be correct, are actually underestimating the usage.

  In the majority of cases, however, a wrong reading looks obvious, and such data is set the quality of 0.

* An integrated PV setup, leading to electricity readings that are *net* of usage and production.

* A short electricity household reading, resulting from attaching the current clamp too late, or removing it too early.

* A faulty e-meter that consistently under/over-estimates the actual values.

* The e-meter does not take into account the appliance's power factor. This might lead to slight over/under-estimation of the power used by that appliance. It would also be correct to say that, since the power factor is appliance-dependent, the readings are not strictly a faithful representation of the relative electricity consumption within a household. We accept this potential source of error as at the time of the study such lack of correctives for the power factor is not only typical of commercial-standard smart meters, but is also the standard of the industry, featuring in smart meters distributed by large scale electricity providers. Thus, METER's e-meter represents the latest standard.

* Multiple readings for any given time, for any given e-Meter. Such readings will still appear as different entries each with its own idElectricity. This has been known to happen, and identical entries exist for households whose e-Meter data had been entered (transferred into the database) twice by mistake. It should *not* be possible to have *different* readings for the same households. _Please let the METER team know should you happen to find any such cases._

* The assignment of Quality to a household's electricity record is fundamentally subjective. Consequently, some records that might be valid electricity readings can have a Quality of 0, and vice versa.

**Household Survey**

* Wrong answers entered by mistake or lack of knowledge

  Apart from the number of people mentioned above, there is no general procedure to catch this.

* Subsequent modifications of the household information by participants

  Participants might modify their answers to the Household questionnaire at any time by clicking on the original link sent to the by email, and going backwards in the questionnaire. The version given with the data therefore corresponds to the version of the answers at the date of data download, rather than the day the household filled in the questionnaire originally.

**Activities**

  * Some, particularly the earlier paper diary-related records, might have erroneous values like -1 in the enjoyment and number of people fields




Limitations to interpretation of Activity data
----------------------------------------------

* Each adult over the age of 8 is assigned a meta ID. Before the app, when activities were entered using paper diaries, this meta ID was written on top of the diary sent to the participants. If diaries were returned empty, no record of that meta ID was deposited into the database - unlike a complete empty app, which will show up as a record in the Meta table, but not in the Activities table.

* Number of activities carried out.
  Care should be taken before drawing direct relation between the number of reported and actual activities carried out by the participants. Experimental tiredness, a decrease in reporting frequency in the duration of the study is a known effect in these types of study.

* Activity duration.
  Meter takes the analytic approach to Time Use collection. The self-reported activities collected by the study are localised in time. The setup makes no suggestions as to the type and frequency of activities that should be reported, implying that activities can potentially overlap. Consequently, there is no case to be made to associate the time between successively reported activities and their duration. Some durations, of course, are obvious: the first activity in the morning puts an upper limit on the duration of sleep (if going to bed had been reported); similarly, boiling the kettle can only take so long; and some activities are fundamentally exclusive (having a shower and watching TV). The only explicit duration that can be inferred without looking at the particulars of the activity is if the activity has been reported to have ended. However, this has its limits, since the 'end' is specified only by activity name, and not by any activity id.

* Recording time.
  The interpretation of the `dt_recording`, the time of the recording of the activity, varies depending on whether that activity was recorded by the participant in the app or in the paper diary. In case of the latter, it is the METER researchers that later transcribed the user's activity using the app. Therefore, for paper diaries, time of recording refers to the time in which that activity was transcribed. If plotted, they will appear to be clustered.


* Path for paper diaries.
  The path for paper diaries is the sequence of buttons pressed by the METER researchers when entering that activity. Because of the way paper diaries were transcribed, such paths would contain a lot of 10K (time setting) codes.

While the spirit of the study remained consistent, the actual app files underwent several modifications throughout. The result is that the possible paths available to the user changed in time. In addition to that, the data processing functions have also been modified. Therefore care should be taken when comparing activities in time. We detail these legacy limitations below.

* The categorisation of the final TUC, and the subsequent entry into the `category` field in the Activities table, is done based on the categorisation of that TUC in the activities.json file in use at the time, and hence might change depending on the version of the file used.

* The 'EDIT' mode allows users to report ending an activity. Activating it creates a separate line in a list of already reported activities visible to the user, except for this activity is clearly denoted with an ('end' or 'END'). Consequently, only the existing activities could be reported to have ended. However, because the design of the app makes this into an activity in its own right, it becomes delinked from the original 'starting' activity. It is therefore theoretically possible that users delete the original activity, leaving only the 'end'-type activity. Furthermore, since the use of the button is voluntary, whether or not to use it becomes an individual preference. Furthermore, the 'end' button had only become available to users in March 2017.

* The number of character allowed for storing path in the activity record gradually increased from 100, to 300, and finally to 600 on 2/3/17 (accommodating around 80 entries).

* Prior to 3/3/17, on importing data into the database, paths for edited activities were discarded, with only the [EDIT code + possible 10K codes] remaining. The missing data has been partially reconstructed, but such 'lone' paths can still be found in the database.

* It might still be possible to find some activities that were deleted by the user, but did not get deleted in the database.

* Prior to 3/3/17, an activity can be an END-type activity, and yet not have an end code of 11005 in the path, its path with an end-code being overwritten by a new edit.

* Another change had been made sometime in early 2017. When pressing 'repeat', whether 'now' or 'recently', users could enter new ENJ and PPL. Therefore, some paths with EDIT tucs will contain one or more ENJ and PPL codes.

* For older experiments where participants used a paper diary, each activity was subsequently entered into the app, and uploaded onto the database in the usual manner. Since it is possible that a single handwritten activity was encoded using two activities in the app, thereby producing two distinct records in the database, these records in **Activities** do not necessarily correspond one to one with each activity written down in the diary.




Nuances and Sample Usage
------------------------

1. How many households took part in the study? For the purpose of these questions, we associate each household with a single run (study day).

  The surest way to find out if a household took part in the study is to check the number of household IDs that have an electricity metaID and at least one activity metaID associated with them. The answer is the number of records returned as a result of the following query:

    .. code-block:: sql

      SELECT *
      FROM (
        SELECT distinct Household_idHousehold as idHH
        FROM Meta
        WHERE DataType = 'A'
      ) as hh_with_a
      WHERE idHH IN
      (
        SELECT distinct Household_idHousehold as idHH
        FROM Meta
        WHERE DataType = 'E'
      );


2. How many of these households are actually the same physical household, just taking part multiple times?

  Households are the same physical household if they have the same contact ID. To find out how many contact IDs took part more than once, we count the number of such IDs that have more than 1 household ID associated with them. A simple query that does not take into account whether the household took part, but simply looks at the entries in the database, is the following:

  .. code-block:: sql

    SELECT Contact_idContact, count(idHousehold) as num_runs
    FROM Household as H
    GROUP BY Contact_idContact
    HAVING count(idHousehold) > 1;

  If we want to know which contacts actually *took part* more than once, we combine the above with the query from part 1:

  .. code-block:: sql

    SELECT Contact_idContact, count(idHousehold) as num_runs
    FROM Household as H
    WHERE idHousehold IN
    (
      SELECT *
      FROM (
        SELECT distinct Household_idHousehold as idHH
        FROM Meta
        WHERE DataType = 'A'
      ) as hh_with_a
      WHERE idHH IN
      (
        SELECT distinct Household_idHousehold as idHH
        FROM Meta
        WHERE DataType = 'E'
      )
    )
    GROUP BY Contact_idContact
    HAVING count(idHousehold) > 1;

3. How many households a) returned good electricity readings, b) and reported at least one activity?

  3.a) We look for the number of households whose electricity record has a ``Quality`` > 0. A 'good' electricity record is by its very nature a subjective notion, since for some purposes even a single 'valid' electricity hour is good enough. The ``Quality`` field, when referring to ``DataType`` that is not 'A', gives the number of full hours whose every ten minute average is a valid reading, i.e. looking like an electricity reading, and being >= 20 Watts. Note that strictly speaking the *distinct* qualification is not needed, since we do not expect households to have more than one e-meter.

  .. code-block:: sql

    SELECT distinct Household_idHousehold as idHH
    FROM Meta
    WHERE DataType = 'E'
    AND Quality > 0;

  3.b) The ``Quality`` field, when referring to 'A', gives the number of activities reported on that device. In the statement below the *distinct* qualification is now crucial, since now households can have more than one participant, and hence more than one 'A' meta ID.

  .. code-block:: sql

    SELECT distinct Household_idHousehold as idHH
    FROM Meta
    WHERE DataType = 'A'
    AND Quality > 0;

  Combining the two queries we get the same query as in part 1, but with Quality qualifications added to each of the activities/electricity subclauses.

4. Find electricity records for households that have electric vehicles

  We first need to identify IDs of households that have electricity vehicles, and then retrieve their electricity records.

  The presence/absence/number of a particular appliance in a household x is given by the value in the relevant appliance field of a record with ``idHousehold`` = x in the **Household** table. We need to find out what is the relevant appliance field, and be able to interpret its entry. The meaning of fields in **Household** that come directly out of the questionnaire are given under the ``col`` field in the **Legend** table with the ``tab`` set to *Household*. The meaning of non self-explanatory fields is described in the **Legend** table where ``value`` is *q*. We therefore look for a record in **Legend** with the ``tab`` set to *Household*, ``value`` is *q*, and ``meaning`` includes the words *electric car*. The corresponding `col` field in that record gives the name of the relevant field in **Household**, which in this case is ``appliance_b11``. The possible answers and their meaning are again given by the field ``value`` in the record in **Legend** with the ``tab`` set to *Household*, and ``col`` to *appliance_b1*.

  .. code-block:: sql

    SELECT * FROM Legend WHERE value = 'q' AND meaning like '%electric car%';

  Alternatively, we use the Household table descriptor to find the name of the field that holds the answer to the question that asks about the electric car. This saves the effort of knowing that, for example, the meaning in **Legend** is transcribed as *car*, not *vehicle*.

  The final query needs to link information from the **Household** table with the **Electricity** table, and the link is the **Meta** table:

  .. code-block:: sql

    SELECT H.idHousehold, E.*
    FROM Electricity_10min AS E
    JOIN Meta as M
    JOIN Household as H
    ON E.Meta_idMeta = M.idMeta
    AND M.Household_idHousehold = H.idHousehold
    WHERE H.appliance_b11 > 0;


5. How many participants reported activities?

  We look for the number of meta IDs with ``DataType`` 'A', with ``Quality`` > 0:

  .. code-block: sql

    SELECT idMeta
    FROM Meta
    WHERE DataType = 'A'
    AND Quality > 0;

6. Find all activities entered using paper diaries, or the Meter app

  The solution involves querying the **Meta** and/or the **Household** table alongside the **Activities** table, because the **Activities** table alone does not provide such information. Consequently the process if to first narrow down the relevant 'A' meta IDs.
  There are several ways to answer this:

  1. Paper diaries correspond to meta IDs with ``DataType`` 'A' that have ``SerialNumber`` of 0 in the **Table**, whereas a-meters have a non-zero ``SerialNumber``.
  2. Another method is to look at when the household took part (given by the ``date_choice`` field in the **Household** table). With two exceptions, from the start of 2017 only the apps were used. The exceptions are the study runs done on the 9 and 10 of December 2016, which used the app; and, conversely, the 10 and 11 of January 2017 households used paper diaries.
  3. Paper diaries were used in the earlier period the Meter study. Households that took part then were assigned ``study`` of *1* and *2*. ``study`` with the value *3* and above are app-based. A possible issue with this approach is that some households have a default ``study`` value of *0*, which does not give us relevant info.

7. Find all instances of washing machine use

  This involves looking through the **Activities** table for entries whose ``activity`` field is related to washing machine use. There are many ways this activity could be reported, but the following query should catch most of them:

  .. code-block:: sql

    SELECT * FROM Meter.Activities
    WHERE activity like '%Washing machine%';

8. Find all activities reported by women

  The way to retrieve gender information related to an activity meta ID is through the **Individual** table. We can look up the correspondence between the questions in the Individual survey and the fields in the table using this documentation; alternatively, we look for the rows in the **Legend** table where ``col`` is *Gender*. The ``meaning`` of *Female* corresponds to the ``value`` of *1*.

  .. code-block:: sql

    SELECT A.*
    FROM Activities as A
    JOIN Meta as M
    JOIN Individual as I
    ON A.Meta_idMeta = M.idMeta
    AND M.idMeta = I.Meta_idMeta
    WHERE Gender = 1;



|

For further information, please contact:

Phil Grunewald

philipp.grunewald@ouce.ox.ac.uk

|
