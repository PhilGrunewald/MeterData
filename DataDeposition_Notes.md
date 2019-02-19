We are depositing data with the **UK Data Archive**. The processes happens through the **UK Data Service**. We will use their **ReShare** repository.

**ReShare** uses institutional login.

Our data is
[**here**](https://reshare.ukdataservice.ac.uk/cgi/users/home?screen=EPrint::Edit&eprintid=853483).


### 1. What Data?

#### 1.1 Tables to include
+ Activities
+ Legend
+ Meta
+ Household
+ Individual
+ Electricity, Electricity_1min, Electricity_10min

#### 1.2 Fields to exclude
+ From **Household**: ``security_code``, ``comment``, ``referee``
+ From **Meta**: ``uploaded``
+ From **Activities**: ``key``
+ From **Electricity**: -
+ From **Individual**: ``TimeOfDiary``, ``Rushed``, ``UnusualDay``, ``DifficultyMeter``, ``ConsentShare``


#### 1.4 Records to exclude
- none

### 2. Which files?

- Meter App files: I downloaded the repository as of 4 Dec and included it in a separate folder
- Do we include our publications? Or do we anticipate that any researcher would have access to them anyway?


## Q for Phil:
- Do we keep an online version of the documentation (that is not the just the .rst files, but the compiled .html)? If so, where? Further action for me: update the link at the main ReShare deposition page
- We talk about about the Hour View - but I didn't think we're depositing views?
- We *are* depositing WOSC..
- per Phil's email (30 Jan 2019): "FYI, I added a timestamp column in the meta table, so that we can see when people got the app (might be nice to track in future whether a campaign was successful or not). All the 'old' ones I made 2000-01-01 again." Can we exclude that field?
- On the website, we say *'You owning the data also means that we will not share data without your consent.'* Should we not ask participants before depositing the data? On a related note, does that mean that we ignore all the ``ConsentShare`` fields in the Individual surveys? Currently the fact there is also individual consent is not mentioned in the data documentation.

## Changes to data needed (MD to do once we have copy of DB):
1. Delete app-entered activities?
2. Clean up activities using the proposed schema
3. Delete idHH = 0 and idMeta = 0 and all related data
4. Study should not be zero: after 2, the study should be 3, excluding WOSC
5. Update intervention to 0 for after WOSC, check Quality is assigned correctly, and check CollectionDate is assigned correctly
6. Start and end dates of collection?
7. CHECK that the range of possible values for the tables is what we say it is (so for example serial number -1 should be excluded), i.e. that there are no undescribed values

# Instructions from ReShare
#### Accepted format
For tables, *.csv* or *.tab*. For documentation, *.rtf* or *.hml*.

#### Documentation needed
+ A *ReadMe.txt* with:     
``
for each filename a short description of what data it includes
any relationships between the data files
for tabular data definitions of column headings and row labels, data codes (including missing data) and measurement units
``

+ To include apart from the ReadMe file:  
  ```
  + clear variable descriptions and code labels in each data file
  + questionnaire form or data dictionary for surveys
  + consent form and information sheet used
  + methods description
  + PDF of website materials
  ```

#### For the actual deposition (on ReShare):
-  **Data description** (abstract)
-  Start and end date of collection
-  **Data collection method**: Describe the methodology used to create this data collection (e.g. interviews, measurements, surveys, mapping, modelling, focus groups etc.). Describe sampling procedure and studied population.
-  **Data sourcing, processing and preparation**:
Information about the source of the data collection, e.g. if derived from existing data resources. List any available data resources under Related resources. Any quality assessment, improvement processes or changes (e.g. anonymisation) that were applied to the data should be summarised here.
- **Notes on access**:
Describe any access, ethical, legal or other issues which may influence the re-use of the data by other researchers, e.g. any informed consent or confidentiality agreements that may influence data re-use, sensitive information in the data collection, or data quality aspects. Also detail whether commercial use of the data is allowed or not. This information will be considered by the ReShare administrator during the review process. If applicable, an example consent form should be uploaded as documentation.
-  To include publications and data doc in the 'Related resources'




#UPLOADED TEXT
##Abstract

The METER dataset is a text-based version of a relational database containing the current results of the METER project. It consists of data tables that store electricity readings on the household level (at varying resolution), simultaneous activities of household members, socio-demographic and appliance information about the household, and results of individual questionnaires. Additional data tables provide meta information linking these different types of data, as well as give code labels. This is supplemented by extensive documentation both in static files and through links to online resources.



##Data Collection Method
METER data combines high resolution UK household electricity readings with simultaneous activity records of household members, providing a platform for new analytical insights. The data has been collected in an ongoing process for over two years. Household sign up on a opt-in basis on the project website (energy-use.org), completing a Household survey as an integral part of the process. This survey solicits socio-demographic and appliance-related information. No explicit rewards are offered, but each year one participating household can win the cash equivalent of one year of their electricity bill. Prior to their chosen date the household receives an envelope with all the devices necessary to take part. These include:
1) an "eMeter", a standard mobile device preconfigured to record electricity over a particular set period. Participants need to attach the current clamp beneath their mains electricity meter prior to the study period. Instructions are printed on the case. The eMeter is fully automated and has no switches or other feedback mechanisms
2) an "aMeter" for each household member. These are budget smart phones with a pre-installed app. All other phone features are disabled, except the power button, which can toggle the device on/off. These devices are thus configured to only provide two functions: the `Individual Survey` and the `Activity Recording`. The interface is specifically designed to be fail save and intuitive. No sliders, gestures or nested menus exist. All operations are a choice of 6 large buttons on a 2 by 3 grid. The only exception is the home screen where reported activities are chronologically listed in scrollable form. Before January 2017 participants received a paper diary instead
3) instruction booklet
Activity and electricity recordings are taken over a 28 hour period starting at 5pm, thus capturing two of the typically most energy intensive periods between 5pm and 7pm. After returning the devices, households receive a link to an interactive visualisation of their electricity profile and activities. The hour of highest electricity consumption is annotated and brought into focus on loading the page.  Participants have the opportunity to provide additional information about appliances that may have been in use during this hour.

##Data sourcing, processing and preparation
The shared data forms an anonymised subset of the collected data. Any contact details, or information by which a participant could in principle be identified (such as the referee), were removed. The quality of the electricity readings in conjunction with activity records has been assessed in "The  electricity  footprint  of  household  activities  -  implications  for demand  models" through examining the accuracy of the power signature of making a cup of tea. The functionality and technology behind the eMeter is described in "Measuring the relationship between time-use and electricity consumption". The functionality of the aMeter app is assessed on an ongoing basis. Though both electricity and activity records are assigned a "Quality" field that forms part of the dataset, no data is excluded on this basis. We leave it up to the individual researcher to decide which records to include.

##Notes on access
METER's participants agree to take part in the study under the condition that their anonymised data will be used for research purposes. This data is therefore only available for research purposes; any commercial use is not allowed. See documentation for the full consent information.
Potential issues with the data relate to whether it is possible to identify either the household or the individual. This danger has been minimised by excluding any contact or other uniquely-characterising information from the dataset.
Since participants can at any time ask for their data to be deleted, use of this dataset is conditional upon agreeing to comply with any such request that might be relayed by the METER team. Consequently the METER team needs to have functioning contact details of any users of this dataset.

Meter's `data privacy policy <http://energy-use.org/data_policy.php>`_
is available from the final screen of the Household Survey.




## We do not include:

.. csv-table::
   :header: "Property"
   :widths: 30, 20

   Households, Number
   Individuals, Number
   Adults, Number
   Children 0-8, Number
   Activities, Number
   Activities reported at home, Number

[TO DO: once we have the dataset]

[TO DO: make a pie with all household that have taken part, to understand what proportion have good e-meter readings, etc.]


.. _representativity:








Representativity
----------------

Participation in the study is voluntary (see :ref:`Participant Recruitment`) and the sample is therefore not representative of the general UK population.

The study was promoted online, via radio, and through campaigns at selected community events.

Here we give a comparison between the socio-economic composition of the dataset's households, as well as the respective numbers for the entire population.

.. csv-table::
   :header: Feature, Group, "Sample [%]", "National* [%]"
   :widths: 30, 30, 30, 30

	Home, Ownership, 85, 64
	Income, "<15,000 ", 6, 7
	, "<25,000 ", 13, 13
	, "<35,000 ", 9, 24
	, "<50,000 ", 21, 21
	, "<70,000 ", 23, 14
	, ">70,000 ", 28, 11
	Occupants, "1-2", 57, 64
	, "3-4", 37, 30
	, ">4", 2, 7
	Age, "Under 18s", 26, 23
	, "19-50", 47, 44
	, "Over 50", 24, 35
	Pets, "Dogs", 10, 24
	, "Cats", 24, 17
	, "Fish", 6, 8
	Appliances, "PV", 14, 4
	, "Electric Vehicle", 4, 0.4
	, "Washing machine/dryer", 99, 97
	, "Dishwasher", 51, 45


* Selected characteristics of study participants. National figures for 2017 based on ONS data.

The dataset thus consists of highly energy-literate, economically comfortable households. In particular high income groups are over-represented, as well as adopters of solar PV and electric vehicles.
