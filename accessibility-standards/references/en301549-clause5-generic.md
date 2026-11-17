# EN 301 549 第 5 章 通用要求（原文摘录，PAGE 23–30）

> **源文件**：`_standards/en_301549_v3.2.1.txt`（EN 301 549 V3.2.1 (2021-03) 官方 PDF 的抽取文本，186 页）
> **原 PDF**：`_standards/en_301549_v3.2.1.pdf`
> **源 URL**：https://www.etsi.org/deliver/etsi_en/301500_301599/301549/03.02.01_60/en_301549v030201p.pdf
> **抓取日期**：2026-11-17
> **提取方式**：`_standards/build_en_refs.js` 按页码标记切取，逐字未改；`===== PAGE N =====` 为抽取脚本加的页码锚点。

## 5 Generic requirements（全章）

```
===== PAGE 23 =====
 
ETSI CEN CENELEC 
 
23
EN 301 549 V3.2.1 (2021-03)
5 
Generic requirements 
5.1 
Closed functionality 
5.1.1 
Introduction (informative) 
ICT has closed functionality for many reasons, including design or policy. Some of the functionality of products can be 
closed because the product is self-contained and users are precluded from adding peripherals or software in order to 
access that functionality. 
ICT may have closed functionality in practice even though the ICT was not designed, developed or supplied to be 
closed. 
Computers that do not allow end-users to adjust settings or install software are functionally closed. 
5.1.2 
General 
5.1.2.1 
Closed functionality 
Where ICT has closed functionality, it shall meet the requirements set out in clauses 5.2 to 13, as applicable. 
NOTE 1: ICT may close some, but not all, of its functionalities. Only the closed functionalities have to conform to 
the requirements of clause 5.1. 
NOTE 2: The requirements within this clause replace those in clauses 5.2 to 13 that specifically state that they do 
not apply to closed functionality. This may be because they relate to compatibility with assistive 
technology or to the ability for the user to adjust system accessibility settings in products with closed 
functionality (e.g. products that prevent access to the system settings control panel). 
5.1.2.2 
Assistive technology 
Where ICT has closed functionality, that closed functionality shall be operable without requiring the user to attach, 
connect or install assistive technology and shall conform to the generic requirements of clauses 5.1.3 to 5.1.6 as 
applicable. Personal headsets and personal induction loops shall not be classed as assistive technology for the purpose 
of this clause. 
5.1.3 
Non-visual access 
5.1.3.1 
Audio output of visual information 
Where visual information is needed to enable the use of those functions of ICT that are closed to assistive technologies 
for screen reading, ICT shall provide at least one mode of operation using non-visual access to enable the use of those 
functions. 
NOTE 1: Non-visual access may be in an audio form, including speech, or a tactile form such as braille for deaf-
blind users. 
NOTE 2: The visual information needed to enable use of some functions may include operating instructions and 
orientation, transaction prompts, user input verification, error messages and non-text content. 
5.1.3.2 
Auditory output delivery including speech 
Where auditory output is provided as non-visual access to closed functionality, the auditory output shall be delivered: 
a) 
either directly by a mechanism included in or provided with the ICT; or 


===== PAGE 24 =====
 
ETSI CEN CENELEC 
 
24
EN 301 549 V3.2.1 (2021-03)
b) 
by a personal headset that can be connected through a 3,5 mm audio jack, or an industry standard connection, 
without requiring the use of vision. 
NOTE 1: Mechanisms included in or provided with ICT may be, but are not limited to, a loudspeaker, a built-in 
handset/headset, or other industry standard coupled peripheral. 
NOTE 2: An industry standard connection could be a wireless connection. 
NOTE 3: Some users may benefit from the provision of an inductive loop. 
5.1.3.3 
Auditory output correlation 
Where auditory output is provided as non-visual access to closed functionality, and where information is displayed on 
the screen, the ICT should provide auditory information that allows the user to correlate the audio with the information 
displayed on the screen. 
NOTE 1: Many people who are legally blind still have visual ability, and use aspects of the visual display even if it 
cannot be fully comprehended. An audio alternative that is both complete and complementary includes all 
visual information such as focus or highlighting, so that the audio can be correlated with information that 
is visible on the screen at any point in time. 
NOTE 2: Examples of auditory information that allows the user to correlate the audio with the information 
displayed on the screen include structure and relationships conveyed through presentation. 
5.1.3.4 
Speech output user control 
Where speech output is provided as non-visual access to closed functionality, the speech output shall be capable of 
being interrupted and repeated when requested by the user, where permitted by security requirements. 
NOTE 1: It is best practice to allow the user to pause speech output rather than just allowing them to interrupt it. 
NOTE 2: It is best practice to allow the user to repeat only the most recent portion rather than requiring play to start 
from the beginning. 
5.1.3.5 
Speech output automatic interruption 
Where speech output is provided as non-visual access to closed functionality, the ICT shall interrupt current speech 
output when a user action occurs and when new speech output begins. 
NOTE: 
Where it is essential that the user hears the entire message, e.g. a safety instruction or warning, the ICT 
may need to block all user action so that speech is not interrupted. 
5.1.3.6 
Speech output for non-text content 
Where ICT presents non-text content, the alternative for non-text content shall be presented to users via speech output 
unless the non-text content is pure decoration or is used only for visual formatting. The speech output for non-text 
content shall follow the guidance for "text alternative" described in WCAG 2.1 [5] Success Criterion 1.1.1. 
5.1.3.7 
Speech output for video information 
Where pre-recorded video content is needed to enable the use of closed functions of ICT and where speech output is 
provided as non-visual access to closed functionality, the speech output shall present equivalent information for the 
pre-recorded video content. 
NOTE: 
This speech output can take the form of an audio description or an auditory transcript of the video 
content. 


===== PAGE 25 =====
 
ETSI CEN CENELEC 
 
25
EN 301 549 V3.2.1 (2021-03)
5.1.3.8 
Masked entry 
Where auditory output is provided as non-visual access to closed functionality, and the characters displayed are 
masking characters, the auditory output shall not be a spoken version of the characters entered unless the auditory 
output is known to be delivered only to a mechanism for private listening, or the user explicitly chooses to allow 
non-private auditory output.  
NOTE 1: Masking characters are usually displayed for security purposes and include, but are not limited to 
asterisks representing personal identification numbers. 
NOTE 2: Unmasked character output might be preferred when closed functionality is used, for example, in the 
privacy of the user's home. A warning highlighting privacy concerns might be appropriate to ensure that 
the user has made an informed choice. 
5.1.3.9 
Private access to personal data 
Where auditory output is provided as non-visual access to closed functionality, and the output contains data that is 
considered to be private according to the applicable privacy policy, the corresponding auditory output shall only be 
delivered through a mechanism for private listening that can be connected without requiring the use of vision, or 
through any other mechanism explicitly chosen by the user. 
NOTE 1: This requirement does not apply in cases where data is not defined as being private according to the 
applicable privacy policy or where there is no applicable privacy policy. 
NOTE 2: Non-private output might be preferred when closed functionality is used, for example, in the privacy of 
the user's home. A warning highlighting privacy concerns might be appropriate to ensure that the user has 
made an informed choice. 
5.1.3.10 
Non-interfering audio output 
Where auditory output is provided as non-visual access to closed functionality, the ICT shall not automatically play, at 
the same time, any interfering audible output that lasts longer than three seconds. 
5.1.3.11 
Private listening volume 
Where auditory output is provided as non-visual access to closed functionality and is delivered through a mechanism for 
private listening, ICT shall provide at least one non-visual mode of operation for controlling the volume. 
5.1.3.12 
Speaker volume 
Where auditory output is provided as non-visual access to closed functionality and is delivered through speakers on 
ICT, a non-visual incremental volume control shall be provided with output amplification up to a level of at least 
65 dBA (-29 dBPaA). 
NOTE: 
For noisy environments, 65 dBA may not be sufficient. 
5.1.3.13 
Volume reset 
Where auditory output is provided as non-visual access to closed functionality, a function that resets the volume to be at 
a level of 65 dBA or less after every use, shall be provided, unless the ICT is dedicated to a single user. 
NOTE: 
A feature to disable the volume reset function may be provided in order to enable the single-user 
exception to be met.  


===== PAGE 26 =====
 
ETSI CEN CENELEC 
 
26
EN 301 549 V3.2.1 (2021-03)
5.1.3.14 
Spoken languages 
Where speech output is provided as non-visual access to closed functionality, speech output shall be in the same human 
language as the displayed content provided, except: 
a) 
for proper names, technical terms, words of indeterminate language, and words or phrases that have become 
part of the vernacular of the immediately surrounding text; 
b) 
where the content is generated externally and not under the control of the ICT vendor, the present clause shall 
not be required to apply for languages not supported by the ICT's speech synthesizer; 
c) 
for displayed languages that cannot be selected using non-visual access; 
d) 
where the user explicitly selects a speech language that is different from the language of the displayed content. 
5.1.3.15 
Non-visual error identification 
Where speech output is provided as non-visual access to closed functionality and an input error is automatically 
detected, speech output shall identify and describe the item that is in error.  
5.1.3.16 
Receipts, tickets, and transactional outputs 
Where ICT is closed to visual access and provides receipts, tickets or other outputs as a result of a self-service 
transaction, speech output shall be provided which shall include all information necessary to complete or verify the 
transaction. In the case of ticketing machines, printed copies of itineraries and maps shall not be required to be audible. 
NOTE: 
The speech output may be provided by any element of the total ICT system. 
5.1.4 
Functionality closed to text enlargement 
Where any functionality of ICT is closed to the text enlargement features of platform or assistive technology, the ICT 
shall provide a mode of operation where the text and images of text necessary for all functionality is displayed in such a 
way that a non-accented capital "H" subtends an angle of at least 0,7 degrees at a viewing distance specified by the 
supplier. 
The subtended angle, in degrees, may be calculated from: 
 
Ψ = (180 x H) / (π x D) 
Where: 
• 
ψ is the subtended angle in degrees 
• 
H is the height of the text 
• 
D is the viewing distance 
• 
D and H are expressed in the same units 
NOTE 1: The intent is to provide a mode of operation where text is large enough to be used by most users with low 
vision. 
NOTE 2: Table 5.1 and Figure 1 illustrate the relationship between the maximum viewing distance and minimum 
character height at the specified minimum subtended angle. 


===== PAGE 27 =====
 
ETSI CEN CENELEC 
 
27
EN 301 549 V3.2.1 (2021-03)
Table 5.1: Relationship between maximum design viewing distance and 
minimum character height at the limit of subtended angle 
Minimum 
subtended 
angle 
Maximum design 
viewing distance 
Minimum character 
height 
0,7 degrees 
100 mm 
1,2 mm 
200 mm 
2,4 mm 
250 mm 
3,1 mm 
300 mm 
3,7 mm 
350 mm 
4,3 mm 
400 mm 
4,9 mm 
450 mm 
5,5 mm 
500 mm 
6,1 mm 
550 mm 
6,7 mm 
600 mm 
7,3 mm 
 
 
Figure 1: Relationship between minimum character height and maximum design viewing distance 
5.1.5 
Visual output for auditory information 
Where auditory information is needed to enable the use of closed functions of ICT, the ICT shall provide visual 
information that is equivalent to the auditory output. 
NOTE: 
This visual information can take the form of captions or text transcripts. 
5.1.6 
Operation without keyboard interface 
5.1.6.1 
Closed functionality 
Where ICT functionality is closed to keyboards or keyboard interfaces, all functionality shall be operable without vision 
as required by clause 5.1.3. 


===== PAGE 28 =====
 
ETSI CEN CENELEC 
 
28
EN 301 549 V3.2.1 (2021-03)
5.1.6.2 
Input focus 
Where ICT functionality is closed to keyboards or keyboard interfaces and where input focus can be moved to a user 
interface element, it shall be possible to move the input focus away from that element using the same mechanism, in 
order to avoid trapping the input focus. 
5.1.7 
Access without speech 
Where speech is needed to operate closed functions of ICT, the ICT shall provide at least one mode of operation using 
an alternative input mechanism that does not require speech. 
5.2 
Activation of accessibility features 
Where ICT has documented accessibility features, it shall be possible to activate those documented accessibility 
features that are required to meet a specific need without relying on a method that does not support that need. 
5.3 
Biometrics 
Where ICT uses biological characteristics, it shall not rely on the use of a particular biological characteristic as the only 
means of user identification or for control of ICT. 
NOTE 1: Alternative means of user identification or for control of ICT could be non-biometric or biometric. 
NOTE 2: Biometric methods based on dissimilar biological characteristics increase the likelihood that individuals 
with disabilities possess at least one of the specified biological characteristics. Examples of dissimilar 
biological characteristics are fingerprints, eye retinal patterns, voice, and face. 
5.4 
Preservation of accessibility information during conversion 
Where ICT converts information or communication it shall preserve all documented non-proprietary information that is 
provided for accessibility, to the extent that such information can be contained in or supported by the destination 
format. 
5.5 
Operable parts 
5.5.1 
Means of operation 
Where ICT has operable parts that require grasping, pinching, or twisting of the wrist to operate, an accessible 
alternative means of operation that does not require these actions shall be provided. 
5.5.2 
Operable parts discernibility 
Where ICT has operable parts, it shall provide a means to discern each operable part, without requiring vision and 
without performing the action associated with the operable part. 
NOTE: 
One way of meeting this requirement is by making the operable parts tactilely discernible. 


===== PAGE 29 =====
 
ETSI CEN CENELEC 
 
29
EN 301 549 V3.2.1 (2021-03)
5.6 
Locking or toggle controls 
5.6.1 
Tactile or auditory status 
Where ICT has a locking or toggle control and the status of that control is visually presented to the user, the ICT shall 
provide at least one mode of operation where the status of the control can be determined either through touch or sound 
without operating the control. 
NOTE 1: Locking or toggle controls are those controls that can only have two or three states and that keep their 
state while being used. 
NOTE 2: An example of a locking or toggle control is the "Caps Lock" key found on most keyboards. Another 
example is the volume button on a pay telephone, which can be set at normal, loud, or extra loud volume. 
5.6.2 
Visual status 
Where ICT has a locking or toggle control and the status of the control is non-visually presented to the user, the ICT 
shall provide at least one mode of operation where the status of the control can be visually determined when the control 
is presented. 
NOTE 1: Locking or toggle controls are those controls that can only have two or three states and that keep their 
state while being used. 
NOTE 2: An example of a locking or toggle control is the "Caps Lock" key found on most keyboards. An example 
of making the status of a control determinable is a visual status indicator on a keyboard. 
5.7 
Key repeat 
Where ICT has a key repeat function that cannot be turned off: 
a) 
the delay before the key repeat shall be adjustable to at least 2 seconds; and 
b) 
the key repeat rate shall be adjustable down to one character per 2 seconds. 
5.8 
Double-strike key acceptance 
Where ICT has a keyboard or keypad, the delay after any keystroke, during which an additional key-press will not be 
accepted if it is identical to the previous keystroke, shall be adjustable up to at least 0,5 seconds. 
5.9 
Simultaneous user actions 
Where ICT has a mode of operation requiring simultaneous user actions for its operation, such ICT shall provide at least 
one mode of operation that does not require simultaneous user actions to operate the ICT. 
NOTE: 
Having to use both hands to open the lid of a laptop, having to press two or more keys at the same time or 
having to touch a surface with more than one finger are examples of simultaneous user actions.
```

