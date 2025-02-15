Understanding GPS
Principles and Applications
Second Edition
<!----Page-1---->
Understanding GPS
Principles and Applications
Second Edition
<!----Page-1---->
For a listing of recent titles in the Artech House
Mobile Communications Series, turn to the back of this book.
<!----Page-2---->
For a listing of recent titles in the Artech House
Mobile Communications Series, turn to the back of this book.
<!----Page-2---->
Understanding GPS
Principles and Applications
Second Edition

Elliott D. Kaplan
Christopher J. Hegarty

Editors

ARTECH
HOUSE
BOSTON | LONDON
artechhouse.com
<!----Page-3---->
Understanding GPS
Principles and Applications
Second Edition

Elliott D. Kaplan
Christopher J. Hegarty
Editors

ARTECH
HOUSE
BOSTON | LONDON
artechhouse.com
<!----Page-3---->
Library of Congress Cataloging-in-Publication Data
Understanding GPS: principles and applications/[editors], Elliott Kaplan,
Christopher Hegarty.—2nd ed.
p. cm.
Includes bibliographical references.
ISBN 1-58053-894-0 (alk. paper)
1. Global Positioning System. I. Kaplan, Elliott D. II. Hegarty, C. (Christopher J.)

G109.5K36 2006
623.89'3-dc22
2005056270

British Library Cataloguing in Publication Data
Kaplan, Elliott D.
Understanding GPS: principles and applications.—2nd ed.
1. Global positioning system
I. Title II. Hegarty, Christopher J.
629'.045

ISBN-10: 1-58053-894-0

Cover design by Igor Valdman

Tables 9.11 through 9.16 have been reprinted with permission from ETSI. 3GPP TSs and TRs
are the property of ARIB, ATIS, ETSI, CCSA, TTA, and TTC who jointly own the copyright
to them. They are subject to further modifications and are therefore provided to you “as is”
for informational purposes only. Further use is strictly prohibited.

© 2006 ARTECH HOUSE, INC.
685 Canton Street
Norwood, MA 02062

All rights reserved. Printed and bound in the United States of America. No part of this book
may be reproduced or utilized in any form or by any means, electronic or mechanical, includ-
ing photocopying, recording, or by any information storage and retrieval system, without
permission in writing from the publisher.

All terms mentioned in this book that are known to be trademarks or service marks have
been appropriately capitalized. Artech House cannot attest to the accuracy of this informa-
tion. Use of a term in this book should not be regarded as affecting the validity of any trade-
mark or service mark.

International Standard Book Number: 1-58053-894-0

10 9 8 7 6 5 4 3 2 1
<!----Page-4---->
```md
Library of Congress Cataloging-in-Publication Data
Understanding GPS: principles and applications/[editors], Elliott Kaplan,
Christopher Hegarty.—2nd ed.
p. cm.
Includes bibliographical references.
ISBN 1-58053-894-0 (alk. paper)
1. Global Positioning System. I. Kaplan, Elliott D. II. Hegarty, C. (Christopher J.)

G109.5K36 2006
623.89'3-dc22
2005056270

British Library Cataloguing in Publication Data
Kaplan, Elliott D.
Understanding GPS: principles and applications.—2nd ed.
1. Global positioning system
I. Title II. Hegarty, Christopher J.
629'.045

ISBN-10: 1-58053-894-0

Cover design by Igor Valdman

Tables 9.11 through 9.16 have been reprinted with permission from ETSI. 3GPP TSs and TRs
are the property of ARIB, ATIS, ETSI, CCSA, TTA, and TTC who jointly own the copyright
to them. They are subject to further modifications and are therefore provided to you “as is”
for informational purposes only. Further use is strictly prohibited.

© 2006 ARTECH HOUSE, INC.
685 Canton Street
Norwood, MA 02062

All rights reserved. Printed and bound in the United States of America. No part of this book
may be reproduced or utilized in any form or by any means, electronic or mechanical, includ-
ing photocopying, recording, or by any information storage and retrieval system, without
permission in writing from the publisher.

All terms mentioned in this book that are known to be trademarks or service marks have
been appropriately capitalized. Artech House cannot attest to the accuracy of this informa-
tion. Use of a term in this book should not be regarded as affecting the validity of any trade-
mark or service mark.

International Standard Book Number: 1-58053-894-0

10 9 8 7 6 5 4 3 2 1
<!----Page-4---->
```md
To my wife Andrea, whose limitless love and support enabled
my contribution to this work. She is my shining star.
—Elliott D. Kaplan

To my family—Patti, Michelle, David, and Megan—
for all their encouragement and support
—Christopher J. Hegarty
<!----Page-5---->
```md
To my wife Andrea, whose limitless love and support enabled
my contribution to this work. She is my shining star.
—Elliott D. Kaplan

To my family—Patti, Michelle, David, and Megan—
for all their encouragement and support
—Christopher J. Hegarty
<!----Page-5---->
```md
Contents
Preface
Acknowledgments
CHAPTER 1
Introduction
1.1 Introduction
1.2 Condensed GPS Program History
XV
xvii

1
1
2

1.3 GPS Overview
3
1.3.1 PPS
4
1.3.2 SPS
4
1.4 GPS Modernization Program
5
1.5 GALILEO Satellite System
6
1.6 Russian GLONASS System
7
1.7 Chinese BeiDou System
8
1.8 Augmentations
10
1.9 Markets and Applications
10
1.9.1 Land
11
1.9.2 Aviation
12
1.9.3 Space Guidance
13
1.9.4 Maritime
14
1.10 Organization of the Book
14
References
19
CHAPTER 2
Fundamentals of Satellite Navigation
21
2.1 Concept of Ranging Using TOA Measurements
21
2.1.1 Two-Dimensional Position Determination
21
2.1.2 Principle of Position Determination Via
Satellite-Generated Ranging Signals
24
2.2 Reference Coordinate Systems
26
2.2.1 Earth-Centered Inertial Coordinate System
27
2.2.2 Earth-Centered Earth-Fixed Coordinate System
28
2.2.3 World Geodetic System
29
2.2.4 Height Coordinates and the Geoid
32
2.3 Fundamentals of Satellite Orbits
34
2.3.1 Orbital Mechanics
34
2.3.2 Constellation Design
43
2.4 Position Determination Using PRN Codes
50
2.4.1 Determining Satellite-to-User Range
51
2.4.2 Calculation of User Position
54
vii
<!----Page-6---->
```md
Contents
2.5 Obtaining User Velocity
viii
58
2.6 Time and GPS
61
2.6.1 UTC Generation
61
2.6.2 GPS System Time
62
2.6.3 Receiver Computation of UTC (USNO)
62
References
63
CHAPTER 3
GPS System Segments
67
3.1 Overview of the GPS System
67
3.1.1 Space Segment Overview
67
3.1.2 Control Segment (CS) Overview
68
3.1.3 User Segment Overview
68
3.2 Space Segment Description
68
3.2.1 GPS Satellite Constellation Description
69
3.2.2 Constellation Design Guidelines
71
3.2.3 Space Segment Phased Development
71
3.3 Control Segment
87
3.3.1 Current Configuration
88
3.3.2 CS Planned Upgrades
100
3.4 User Segment
103
3.4.1 GPS Set Characteristics
103
3.4.2 GPS Receiver Selection
109
References
110
CHAPTER 4
GPS Satellite Signal Characteristics
113
4.1 Overview
113
4.2 Modulations for Satellite Navigation
113
4.2.1 Modulation Types
113
4.2.2 Multiplexing Techniques
115
4.2.3 Signal Models and Characteristics
116
4.3 Legacy GPS Signals
123
4.3.1 Frequencies and Modulation Format
123
4.3.2 Power Levels
133
4.3.3 Autocorrelation Functions and Power Spectral Densities
135
4.3.4 Cross-Correlation Functions and CDMA Performance
140
4.4 Navigation Message Format
142
4.5 Modernized GPS Signals
145
4.5.1 L2 Civil Signal
145
4.5.2 L5
147
4.5.3 M Code
148
4.5.4 L1 Civil Signal
150
4.6 Summary
150
References
150
<!----Page-7---->
```md
Contents
CHAPTER 5
Satellite Signal Acquisition, Tracking, and Data Demodulation
5.1 Overview
5.2 GPS Receiver Code and Carrier Tracking
5.2.1 Predetection Integration
ix

153
153
155
158
5.2.2 Baseband Signal Processing
159
5.2.3 Digital Frequency Synthesis
161
5.2.4 Carrier Aiding of Code Loop
162
5.2.5 External Aiding
164
5.3 Carrier Tracking Loops
164
5.3.1 Phase Lock Loops
165
5.3.2 Costas Loops
166
5.3.3 Frequency Lock Loops
170
5.4 Code Tracking Loops
173
5.5 Loop Filters
179
5.6 Measurement Errors and Tracking Thresholds
183
5.6.1 PLL Tracking Loop Measurement Errors
184
5.6.2 FLL Tracking Loop Measurement Errors
192
5.6.3 C/A and P(Y) Code Tracking Loop Measurement Errors
194
5.6.4 Modernized GPS M Code Tracking Loop Measurement Errors
199
5.7 Formation of Pseudorange, Delta Pseudorange, and Integrated Doppler
200
5.7.1 Pseudorange
201
5.7.2 Delta Pseudorange
216
5.7.3 Integrated Doppler
218
5.8 Signal Acquisition
219
5.8.1 Tong Search Detector
223
5.8.2 M of N Search Detector
227
5.8.3 Direct Acquisition of GPS Military Signals
229
5.9 Sequence of Initial Receiver Operations
231
5.10 Data Demodulation
232
5.11 Special Baseband Functions
233
5.11.1 Signal-to-Noise Power Ratio Meter
233

5.11.2 Phase Lock Detector with Optimistic and Pessimistic Decisions 233
5.11.3 False Frequency Lock and False Phase Lock Detector
235
5.12 Use of Digital Processing
235
5.13 Considerations for Indoor Applications
237
5.14 Codeless and Semicodeless Processing
239
References
240
CHAPTER 6
Interference, Multipath, and Scintillation
243
6.1 Overview
243
6.2 Radio Frequency Interference
243
6.2.1 Types and Sources of RF Interference
244
6.2.2 Effects of RF Interference on Receiver Performance
247
6.2.3 Interference Mitigation
278
6.3 Multipath
279
<!----Page-8---->
```md
Contents
CHAPTER 5
Satellite Signal Acquisition, Tracking, and Data Demodulation
5.1 Overview
5.2 GPS Receiver Code and Carrier Tracking
5.2.1 Predetection Integration
viii

153
153
155
158
5.2.2 Baseband Signal Processing
159
5.2.3 Digital Frequency Synthesis
161
5.2.4 Carrier Aiding of Code Loop
162
5.2.5 External Aiding
164
5.3 Carrier Tracking Loops
164
5.3.1 Phase Lock Loops
165
5.3.2 Costas Loops
166
5.3.3 Frequency Lock Loops
170
5.4 Code Tracking Loops
173
5.5 Loop Filters
179
5.6 Measurement Errors and Tracking Thresholds
183
5.6.1 PLL Tracking Loop Measurement Errors
184
5.6.2 FLL Tracking Loop Measurement Errors
192
5.6.3 C/A and P(Y) Code Tracking Loop Measurement Errors
194
5.6.4 Modernized GPS M Code Tracking Loop Measurement Errors
199
5.7 Formation of Pseudorange, Delta Pseudorange, and Integrated Doppler
200
5.7.1 Pseudorange
201
5.7.2 Delta Pseudorange
216
5.7.3 Integrated Doppler
218
5.8 Signal Acquisition
219
5.8.1 Tong Search Detector
223
5.8.2 M of N Search Detector
227
5.8.3 Direct Acquisition of GPS Military Signals
229
5.9 Sequence of Initial Receiver Operations
231
5.10 Data Demodulation
232
5.11 Special Baseband Functions
233
5.11.1 Signal-to-Noise Power Ratio Meter
233

5.11.2 Phase Lock Detector with Optimistic and Pessimistic Decisions 233
5.11.3 False Frequency Lock and False Phase Lock Detector
235
5.12 Use of Digital Processing
235
5.13 Considerations for Indoor Applications
237
5.14 Codeless and Semicodeless Processing
239
References
240
CHAPTER 6
Interference, Multipath, and Scintillation
243
6.1 Overview
243
6.2 Radio Frequency Interference
243
6.2.1 Types and Sources of RF Interference
244
6.2.2 Effects of RF Interference on Receiver Performance
247
6.2.3 Interference Mitigation
278
6.3 Multipath
279
<!----Page-8---->
```md
ix
Contents
6.3.1 Multipath Characteristics and Models
281
6.3.2 Effects of Multipath on Receiver Performance
285
6.3.3 Multipath Mitigation
292
6.4 Ionospheric Scintillation
295
References
297
CHAPTER 7
Performance of Stand-Alone GPS
301
7.1 Introduction
301
7.2 Measurement Errors
302
7.2.1 Satellite Clock Error
304
7.2.2 Ephemeris Error
305
7.2.3 Relativistic Effects
306
7.2.4 Atmospheric Effects
308
7.2.5 Receiver Noise and Resolution
319
7.2.6 Multipath and Shadowing Effects
319
7.2.7 Hardware Bias Errors
320
7.2.8 Pseudorange Error Budgets
321
7.3 PVT Estimation Concepts
322
7.3.1 Satellite Geometry and Dilution of Precision in GPS
322
7.3.2 Accuracy Metrics
328
7.3.3 Weighted Least Squares (WLS)
332
7.3.4 Additional State Variables
333
7.3.5 Kalman Filtering
334
7.4 GPS Availability
334
7.4.1 Predicted GPS Availability Using the Nominal 24-Satellite
GPS Constellation
335
7.4.2 Effects of Satellite Outages on GPS Availability
337
7.5 GPS Integrity
343
7.5.1 Discussion of Criticality
345
7.5.2 Sources of Integrity Anomalies
345
7.5.3 Integrity Enhancement Techniques
346
7.6 Continuity
360
7.7 Measured Performance
361
References
375
CHAPTER 8
Differential GPS
379
8.1 Introduction
379
8.2 Spatial and Time Correlation Characteristics of GPS Errors
381
8.2.1 Satellite Clock Errors
381
8.2.2 Ephemeris Errors
382
8.2.3 Tropospheric Errors
384
8.2.4 Ionospheric Errors
387
8.2.5 Receiver Noise and Multipath
390
8.3 Code-Based Techniques
391
8.3.1 Local-Area DGPS
391
<!----Page-9---->
```md
ix
Contents
6.3.1 Multipath Characteristics and Models
281
6.3.2 Effects of Multipath on Receiver Performance
285
6.3.3 Multipath Mitigation
292
6.4 Ionospheric Scintillation
295
References
297
CHAPTER 7
Performance of Stand-Alone GPS
301
7.1 Introduction
301
7.2 Measurement Errors
302
7.2.1 Satellite Clock Error
304
7.2.2 Ephemeris Error
305
7.2.3 Relativistic Effects
306
7.2.4 Atmospheric Effects
308
7.2.5 Receiver Noise and Resolution
319
7.2.6 Multipath and Shadowing Effects
319
7.2.7 Hardware Bias Errors
320
7.2.8 Pseudorange Error Budgets
321
7.3 PVT Estimation Concepts
322
7.3.1 Satellite Geometry and Dilution of Precision in GPS
322
7.3.2 Accuracy Metrics
328
7.3.3 Weighted Least Squares (WLS)
332
7.3.4 Additional State Variables
333
7.3.5 Kalman Filtering
334
7.4 GPS Availability
334
7.4.1 Predicted GPS Availability Using the Nominal 24-Satellite
GPS Constellation
335
7.4.2 Effects of Satellite Outages on GPS Availability
337
7.5 GPS Integrity
343
7.5.1 Discussion of Criticality
345
7.5.2 Sources of Integrity Anomalies
345
7.5.3 Integrity Enhancement Techniques
346
7.6 Continuity
360
7.7 Measured Performance
361
References
375
CHAPTER 8
Differential GPS
379
8.1 Introduction
379
8.2 Spatial and Time Correlation Characteristics of GPS Errors
381
8.2.1 Satellite Clock Errors
381
8.2.2 Ephemeris Errors
382
8.2.3 Tropospheric Errors
384
8.2.4 Ionospheric Errors
387
8.2.5 Receiver Noise and Multipath
390
8.3 Code-Based Techniques
391
8.3.1 Local-Area DGPS
391
<!----Page-9---->
```md
X
Contents
6.3.1 Multipath Characteristics and Models
281
6.3.2 Effects of Multipath on Receiver Performance
285
6.3.3 Multipath Mitigation
292
6.4 Ionospheric Scintillation
295
References
297
CHAPTER 7
Performance of Stand-Alone GPS
301
7.1 Introduction
301
7.2 Measurement Errors
302
7.2.1 Satellite Clock Error
304
7.2.2 Ephemeris Error
305
7.2.3 Relativistic Effects
306
7.2.4 Atmospheric Effects
308
7.2.5 Receiver Noise and Resolution
319
7.2.6 Multipath and Shadowing Effects
319
7.2.7 Hardware Bias Errors
320
7.2.8 Pseudorange Error Budgets
321
7.3 PVT Estimation Concepts
322
7.3.1 Satellite Geometry and Dilution of Precision in GPS
322
7.3.2 Accuracy Metrics
328
7.3.3 Weighted Least Squares (WLS)
332
7.3.4 Additional State Variables
333
7.3.5 Kalman Filtering
334
7.4 GPS Availability
334
7.4.1 Predicted GPS Availability Using the Nominal 24-Satellite
GPS Constellation
335
7.4.2 Effects of Satellite Outages on GPS Availability
337
7.5 GPS Integrity
343
7.5.1 Discussion of Criticality
345
7.5.2 Sources of Integrity Anomalies
345
7.5.3 Integrity Enhancement Techniques
346
7.6 Continuity
360
7.7 Measured Performance
361
References
375
CHAPTER 8
Differential GPS
379
8.1 Introduction
379
8.2 Spatial and Time Correlation Characteristics of GPS Errors
381
8.2.1 Satellite Clock Errors
381
8.2.2 Ephemeris Errors
382
8.2.3 Tropospheric Errors
384
8.2.4 Ionospheric Errors
387
8.2.5 Receiver Noise and Multipath
390
8.3 Code-Based Techniques
391
8.3.1 Local-Area DGPS
391
<!----Page-10---->
```md
xi
Contents
8.3.2 Regional-Area DGPS
394
8.3.3 Wide-Area DGPS
395
8.4 Carrier-Based Techniques
397
8.4.1 Precise Baseline Determination in Real Time
398
8.4.2 Static Application
418
8.4.3 Airborne Application
420
8.4.4 Attitude Determination
423
8.5 Message Formats
425
8.5.1 Version 2.3
425
8.5.2 Version 3.0
428
8.6 Examples
429
8.6.1 Code Based
429
8.6.2 Carrier Based
450
References
454
CHAPTER 9
Integration of GPS with Other Sensors and Network Assistance
459
9.1 Overview
459
9.2 GPS/Inertial Integration
460
9.2.1 GPS Receiver Performance Issues
460
9.2.2 Inertial Sensor Performance Issues
464
9.2.3 The Kalman Filter
466
9.2.4 GPSI Integration Methods
470
9.2.5 Reliability and Integrity
488
9.2.6 Integration with CRPA
489
9.3 Sensor Integration in Land Vehicle Systems
491
9.3.1 Introduction
491
9.3.2 Review of Available Sensor Technology
496
9.3.3 Sensor Integration Principles
515
9.4 Network Assistance
522
9.4.1 Historical Perspective of Assisted GPS
526
9.4.2 Requirements of the FCC Mandate
528
9.4.3 Total Uncertainty Search Space
535
9.4.4 GPS Receiver Integration in Cellular Phones—Assistance Data
from Handsets
540
9.4.5 Types of Network Assistance
543
References
554
CHAPTER 10
GALILEO
559
10.1 GALILEO Program Objectives
559
10.2 GALILEO Services and Performance
559
10.2.1 Open Service (OS)
560
10.2.2 Commercial Service (CS)
562
10.2.3 Safety of Life (SOL) Service
562
10.2.4 Public Regulated Service (PRS)
562
10.2.5 Support to Search and Rescue (SAR) Service
563
<!----Page-11---->
```md
Contents
8.3.2 Regional-Area DGPS
394
8.3.3 Wide-Area DGPS
395
8.4 Carrier-Based Techniques
397
8.4.1 Precise Baseline Determination in Real Time
398
8.4.2 Static Application
418
8.4.3 Airborne Application
420
8.4.4 Attitude Determination
423
8.5 Message Formats
425
8.5.1 Version 2.3
425
8.5.2 Version 3.0
428
8.6 Examples
429
8.6.1 Code Based
429
8.6.2 Carrier Based
450
References
454
CHAPTER 9
Integration of GPS with Other Sensors and Network Assistance
459
9.1 Overview
459
9.2 GPS/Inertial Integration
460
9.2.1 GPS Receiver Performance Issues
460
9.2.2 Inertial Sensor Performance Issues
464
9.2.3 The Kalman Filter
466
9.2.4 GPSI Integration Methods
470
9.2.5 Reliability and Integrity
488
9.2.6 Integration with CRPA
489
9.3 Sensor Integration in Land Vehicle Systems
491
9.3.1 Introduction
491
9.3.2 Review of Available Sensor Technology
496
9.3.3 Sensor Integration Principles
515
9.4 Network Assistance
522
9.4.1 Historical Perspective of Assisted GPS
526
9.4.2 Requirements of the FCC Mandate
528
9.4.3 Total Uncertainty Search Space
535
9.4.4 GPS Receiver Integration in Cellular Phones—Assistance Data
from Handsets
540
9.4.5 Types of Network Assistance
543
References
554
CHAPTER 10
GALILEO
559
10.1 GALILEO Program Objectives
559
10.2 GALILEO Services and Performance
559
10.2.1 Open Service (OS)
560
10.2.2 Commercial Service (CS)
562
10.2.3 Safety of Life (SOL) Service
562
10.2.4 Public Regulated Service (PRS)
562
10.2.5 Support to Search and Rescue (SAR) Service
563
<!----Page-11---->
```md
xii
10.3 GALILEO Frequency Plan and Signal Design
10.3.1 Frequencies and Signals
Contents

563
563
10.3.2 Modulation Schemes
565
10.3.3 SAR Signal Plan
576
10.4 Interoperability Between GPS and GALILEO
577
10.4.1 Signal in Space
577
10.4.2 Geodetic Coordinate Reference Frame
578
10.4.3 Time Reference Frame
578
10.5 System Architecture
579
10.5.1 Space Segment
581
10.5.2 Ground Segment
585
10.6 GALILEO SAR Architecture
591
10.7 GALILEO Development Plan
592
References
594
CHAPTER 11
Other Satellite Navigation Systems
595
11.1 The Russian GLONASS System
595
11.1.1 Introduction
595
11.1.2 Program Overview
595
11.1.3 Organizational Structure
597
11.1.4 Constellation and Orbit
597
11.1.5 Spacecraft Description
599
11.1.6 Ground Support
602
11.1.7 User Equipment
604
11.1.8 Reference Systems
605
11.1.9 GLONASS Signal Characteristics
606
11.1.10 System Accuracy
611
11.1.11 Future GLONASS Development
612
11.1.12 Other GLONASS Information Sources
614
11.2 The Chinese BeiDou Satellite Navigation System
615
11.2.1 Introduction
615
11.2.3 Program History
616
11.2.4 Organization Structure
617
11.2.5 Constellation and Orbit
617
11.2.6 Spacecraft
617
11.2.7 RDSS Service Infrastructure
618
11.2.8 RDSS Navigation Services
621
11.2.9 RDSS Navigation Signals
622
11.2.10 System Coverage and Accuracy
623
11.2.11 Future Developments
623
11.3 The Japanese QZSS Program
625
11.3.1 Introduction
625
11.3.2 Program Overview
625
11.3.3 Organizational Structure
626
11.3.4 Constellation and Orbit
626
11.3.5 Spacecraft Development
627
<!----Page-12---->
```md
xii
10.3 GALILEO Frequency Plan and Signal Design

10.3.1 Frequencies and Signals
Contents
563
563
10.3.2 Modulation Schemes
565
10.3.3 SAR Signal Plan
576
10.4 Interoperability Between GPS and GALILEO
577
10.4.1 Signal in Space
577
10.4.2 Geodetic Coordinate Reference Frame
578
10.4.3 Time Reference Frame
578
10.5 System Architecture
579
10.5.1 Space Segment
581
10.5.2 Ground Segment
585
10.6 GALILEO SAR Architecture
591
10.7 GALILEO Development Plan
592
References
594
CHAPTER 11
Other Satellite Navigation Systems
595
11.1 The Russian GLONASS System
595
11.1.1 Introduction
595
11.1.2 Program Overview
595
11.1.3 Organizational Structure
597
11.1.4 Constellation and Orbit
597
11.1.5 Spacecraft Description
599
11.1.6 Ground Support
602
11.1.7 User Equipment
604
11.1.8 Reference Systems
605
11.1.9 GLONASS Signal Characteristics
606
11.1.10 System Accuracy
611
11.1.11 Future GLONASS Development
612
11.1.12 Other GLONASS Information Sources
614
11.2 The Chinese BeiDou Satellite Navigation System
615
11.2.1 Introduction
615
11.2.3 Program History
616
11.2.4 Organization Structure
617
11.2.5 Constellation and Orbit
617
11.2.6 Spacecraft
617
11.2.7 RDSS Service Infrastructure
618
11.2.8 RDSS Navigation Services
621
11.2.9 RDSS Navigation Signals
622
11.2.10 System Coverage and Accuracy
623
11.2.11 Future Developments
623
11.3 The Japanese QZSS Program
625
11.3.1 Introduction
625
11.3.2 Program Overview
625
11.3.3 Organizational Structure
626
11.3.4 Constellation and Orbit
626
11.3.5 Spacecraft Development
627
<!----Page-12---->
```md
xiii
Contents
11.3.6 Ground Support
628
11.3.7 User Equipment
628
11.3.8 Reference Systems
628
11.3.9 Navigation Services and Signals
628
11.3.10 System Coverage and Accuracy
629
11.3.11 Future Development
629
Acknowledgments
630
References
630
CHAPTER 12
GNSS Markets and Applications
635
12.1 GNSS: A Complex Market Based on Enabling Technologies
635
12.1.1 Market Scope, Segmentation, and Value
638
12.1.2 Unique Aspects of GNSS Market
639
12.1.3 Market Limitations, Competitive Systems, and Policy
640
12.2 Civil Navigation Applications of GNSS
641
12.2.1 Marine Navigation
642
12.2.2 Air Navigation
645
12.2.3 Land Navigation
646
12.3 GNSS in Surveying, Mapping, and Geographical Information Systems 647
12.3.1 Surveying
648
12.3.2 Mapping
648
12.3.3 GIS
649
12.4 Recreational Markets for GNSS-Based Products
650
12.5 GNSS Time Transfer
650
12.6 Differential Applications and Services
650
12.6.1 Precision Approach Aircraft Landing Systems
651
12.6.2 Other Differential Systems
651
12.6.3 Attitude Determination Systems
652
12.7 GNSS and Telematics and LBS
652
12.8 Creative Uses for GNSS
654
12.9.