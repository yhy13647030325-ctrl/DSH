# EN 301 549 v3.2.1 结构与适用范围（原文摘录）

> **源文件**：`_standards/en_301549_v3.2.1.txt`（EN 301 549 V3.2.1 (2021-03) 官方 PDF 的抽取文本，186 页）
> **原 PDF**：`_standards/en_301549_v3.2.1.pdf`
> **源 URL**：https://www.etsi.org/deliver/etsi_en/301500_301599/301549/03.02.01_60/en_301549v030201p.pdf
> **抓取日期**：2026-11-17
> **提取方式**：`_standards/build_en_refs.js` 按页码标记切取，逐字未改；`===== PAGE N =====` 为抽取脚本加的页码锚点。

## 一、封面与文档标识（PAGE 1–2）

```
===== PAGE 1 =====
 
 
EN 301 549 V3.2.1 (2021-03) 
HARMONISED EUROPEAN STANDARD 
Accessibility requirements for ICT products and services 


===== PAGE 2 =====
 
ETSI CEN CENELEC 
 
2
EN 301 549 V3.2.1 (2021-03)
 
Reference 
REN/HF-00301549v321 
Keywords 
accessibility, HF, ICT, procurement 
 
CEN 
Rue de la science, 23 
B-1040 Brussels 
 - BELGIUM 
Tel: + 32 2 550 08 11 
Fax: + 32 2 550 08 19 
CENELEC 
Rue de la science, 23 
B-1040 Brussels 
 - BELGIUM 
Tel.: +32 2 519 68 71 
Fax: +32 2 519 69 19 
ETSI 
650 Route des Lucioles 
F-06921 Sophia Antipolis Cedex - 
FRANCE 
Tel.: +33 4 92 94 42 00 
Fax: +33 4 93 65 47 16 
Siret N° 348 623 562 00017 - NAF 742 C 
 Association à but non lucratif enregistrée à la 
 Sous-Préfecture de Grasse (06) N° 7803/88 
Important notice 
Individual copies of the present document can be downloaded from: 
ETSI Search & Browse Standards 
The present document may be made available in electronic versions and/or in print. The content of any electronic and/or 
print versions of the present document shall not be modified without the prior written authorization of ETSI. In case of any 
existing or perceived difference in contents between such versions and/or in print, the prevailing version of an ETSI 
deliverable is the one made publicly available in PDF format at ETSI Deliverables. 
Users of the present document should be aware that the document may be subject to revision or change of status. 
Information on the current status of this and other ETSI documents is available at 
ETSI deliverable status 
If you find errors in the present document, please send your comment to one of the following services: 
ETSI Committee Support Staff 
Copyright Notification 
No part may be reproduced or utilized in any form or by any means, electronic or mechanical, including photocopying and microfilm 
except as authorized by written permission of ETSI. 
The content of the PDF version shall not be modified without the written authorization of ETSI. 
The copyright and the foregoing restriction extend to reproduction in all media. 
© European Telecommunications Standards Institute 2021. 
© Comité Européen de Normalisation 2021. 
© Comité Européen de Normalisation Electrotechnique 2021. 
All rights reserved. 
 
DECT™, PLUGTESTS™, UMTS™ and the ETSI logo are trademarks of ETSI registered for the benefit of its Members. 
3GPP™ and LTE™ are trademarks of ETSI registered for the benefit of its Members and 
of the 3GPP Organizational Partners. 
oneM2M™ logo is a trademark of ETSI registered for the benefit of its Members and 
of the oneM2M Partners. 
GSM® and the GSM logo are trademarks registered and owned by the GSM Association.
```

## 二、第 1 章 Scope（PAGE 11–12）

```
===== PAGE 11 =====
 
ETSI CEN CENELEC 
 
11
EN 301 549 V3.2.1 (2021-03)
1 
Scope 
The present document specifies the functional accessibility requirements applicable to ICT products and services, 
together with a description of the test procedures and evaluation methodology for each accessibility requirement in a 
form that is suitable for use in public procurement within Europe. The present document is intended to be used with web 
based technologies, non-web technologies and hybrids that use both. It covers both software and hardware as well as 
services. It is intended for use by both providers and procurers, but it is expected that it will also be of use to many 
others as well. 
The relationship between the present document and the essential requirements of Directive 2016/2102 on the 
accessibility of the websites and mobile applications of public sector bodies [i.28] is given in Annex A. 
The present document contains the necessary functional requirements and provides a reference document such that if 
procedures are followed by different actors, the results of testing are similar and the interpretation of those results is 
clear. The test descriptions and evaluation methodology included in the present document are elaborated to a level of 
detail compliant with ISO/IEC 17007:2009 [i.14], so that conformance testing can give conclusive results. 
2 
References 
2.1 
Normative references 
References are either specific (identified by date of publication and/or edition number or version number) or 
non-specific. For specific references, only the cited version applies. For non-specific references, the latest version of the 
referenced document (including any amendments) applies.  
Referenced documents which are not found to be publicly available in the expected location might be found at ETSI 
References in docbox. 
NOTE: 
While any hyperlinks included in this clause were valid at the time of publication, ETSI cannot guarantee 
their long term validity. 
The following referenced documents are necessary for the application of the present document. 
[1] 
ETSI ETS 300 381 (Edition 1) (December 1994): "Telephony for hearing impaired people; 
Inductive coupling of telephone earphones to hearing aids". 
[2] 
ETSI ES 200 381-1 (V1.2.1) (October 2012): "Telephony for hearing impaired people; Inductive 
coupling of telephone earphones to hearing aids; Part 1: Fixed-line speech terminals". 
[3] 
ETSI ES 200 381-2 (V1.1.1) (October 2012): "Telephony for hearing impaired people; Inductive 
coupling of telephone earphones to hearing aids; Part 2: Cellular speech terminals". 
[4] 
W3C Recommendation (December 2008)/ISO/IEC 40500:2012: "Web Content Accessibility 
Guidelines (WCAG) 2.0". 
NOTE: 
Available at WCAG 2.0. 
[5] 
W3C Recommendation (June 2018): "Web Content Accessibility Guidelines (WCAG) 2.1". 
NOTE: 
Available at WCAG 2.1.
```

## 三、第 14 章 Conformance（PAGE 88–89）

```
===== PAGE 88 =====
 
ETSI CEN CENELEC 
 
88
EN 301 549 V3.2.1 (2021-03)
14 
Conformance 
Conformance to the present document is achieved by meeting all the applicable requirements, these are clauses 
containing the word "shall". Those clauses containing the word "should" are recommendations and are not required for 
conformance.  
All clauses except those in clause 12 are self-scoping. This means they are introduced with the phrase 'Where ICT <pre 
condition>'. A requirement is met when the pre-condition is true and the corresponding test (in Annex C) is passed. 
When one of the pre-conditions is false the requirement is not applicable. Consequently, the result of the tests in 
Annex C can be: not applicable, pass, fail, or (in exceptional circumstances) not testable. 
ICT is often comprised of an assembly of two or more items of ICT. In some cases, two or more interoperable items of 
ICT may together meet more requirements of the standard when one item complements the functionality of the other 
and the sum together meets more of the accessibility requirements. However, combining two items of ICT, both of 
which fail to meet any particular requirement, will not lead to a combined ICT system that meets that requirement. 
The present document does not prioritize requirements.  
NOTE 1: Conformance with the accessibility requirements could be affected by subsequent implementation or 
maintenance. 
NOTE 2: Sampling is frequently required on complex ICT when there are too many instances of the object to be 
tested. The present document cannot recommend specific ICT evaluation sampling techniques as these 
are context specific. 
The inherent nature of certain situations makes it impossible to make reliable and definitive statements that accessibility 
requirements have been met. In those situations therefore, the requirements in the present document are not applicable: 
• 
when the product is in a failure, repair or maintenance state where the ordinary set of input or output functions 
are not available; 
• 
during those parts of start-up, shutdown, and other state transitions that can be completed without user 
interaction. 
NOTE 3: Even in the above situations, it is best practice to apply requirements in the present document wherever it 
is feasible and safe to do so.
```

