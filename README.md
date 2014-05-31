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
