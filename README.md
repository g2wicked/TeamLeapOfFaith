TeamLeapOfFaith
===============

Team Leap of Faith's repo for BattleHackTO 2014

Breakdown of Project: Touchless Medical Interface

Synopsis: One of the biggest problems in the medical field is the issue of cross contamination. This makes computers, despite their usefulness, unreasonable to use in a surgical environment. Our hack aims to allow doctors to interface with computers without making physical contact at all. Leveraging the Leap Motion, doctors (even while wearing medical gloves) can control important visual data on existing hospital infrastructure in a way the completely avoids the issue of contact transmission of disease.

Components:
1. Leap interface - Using the Leap API, data will be provided to the main program, allowing the interface to be controlled by the hands. This controller (in C#) will proivde the correct interpretation of specific hand gestures and actions.
2. Background Application - Either in Unity or on the Windows platform. Where we actually do stuff with the controller.
3. Particular Apps - Image manipulation, document reading, other things? Please ideas people!

Talked breakdown:

The purpose it twofold:
1. Decrease the number of touched surfaces, thus decreasing the transmission of diseases in hospitals worldwide without requiring major infrastructure change (BIG GOAL)
2. Increase computer interactivity within hospitals by making interfaces usable in complex situations (during surgery, with gloves, looking at someone's xrays on a screen)
3. Something to do with financial components


Need to build
1. Backend patient database use case
2. Medical Professional interface - pretty, simple, easy graphic interface
3. Patient/Visitor interface - again, simple, pretty, full patient record accessible, can purchase elements of record


--------------------------------------------------------------------------------------------------------------------------
File Structure for User Case Patient Database

Directory contains one folder for each Patient. Patient folders have naming convention:
Patient [Patient#] - [Lastname],[Firstname]

In each Patient folder, there are a number of items.
In every Patient folder, there will be a text file named: content.txt
content.txt will contain a list of every file in the Patient's directory in a readable format, and will update every time the folder's contents are modified.

In each Patient folder, there will be two files called PatientHistory.docx, and PatientHistory.pdf. They are an up to date patient overview, that can be seen and ordered by the patient.

Additional folders may be included, indicating specific dates of record in the following format: History-[mm-dd-yyyy]
The folder for a specified date can contain any number of files, all in pdf format. These can include:
xray-[body region]-[Doctor Lastname], [Doctor Firstname]-[mm-dd-yyyy].pdf
catscan-[body region]-[Doctor Lastname],[Doctor Firstname]-[mm-dd-yyyy].pdf
notes-[Doctor Lastname],[Doctor Firstname]-[mm-dd-yyyy].pdf
ultrasound-[body region]-[Doctor Lastname],[Doctor Firstname]-[mm-dd-yyyy].pdf
mamogram-[body region]-[Doctor Lastname],[Doctor Firstname]-[mm-dd-yyyy].pdf


--------------------------------------------------------------------------------------------------------------

