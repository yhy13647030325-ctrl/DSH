# WCAG 2.1 新增成功准则原文摘录

> **源文件**：`_standards/wcag21.html`（W3C W3C Recommendation, https://www.w3.org/TR/WCAG21/）
> **抓取日期**：2026-11-17
> **提取方式**：`_standards/extract_sc_full.js` 按 `<section>` 配平提取，逐字未改。
> **条目来源**：本清单由 `_standards/diff_wcag.js` 比对 wcag20.html 与 wcag21.html 的条目集合算出（**17 条**），
> 与 wcag21.html 正文 "The following Success Criteria are new in WCAG 2.1" 段落列出的条目一致。

### 1.3.4 Orientation（Level AA）

Content does not restrict its view and operation to a single display orientation, such as portrait or landscape, unless a specific display orientation is essential .
Note Examples where a particular display orientation may be essential are a bank check, a piano application, slides for a projector or television, or virtual reality content where content is not necessarily restricted to landscape or portrait display orientation.

### 1.3.5 Identify Input Purpose（Level AA）

The purpose of each input field collecting information about the user can be programmatically determined when:
The input field serves a purpose identified in the Input Purposes for user interface components section ; and
The content is implemented using technologies with support for identifying the expected meaning for form input data.

### 1.3.6 Identify Purpose（Level AAA）

In content implemented using markup languages, the purpose of user interface components , icons, and regions can be programmatically determined .

### 1.4.10 Reflow（Level AA）

Content can be presented without loss of information or functionality, and without requiring scrolling in two dimensions for:
Vertical scrolling content at a width equivalent to 320 CSS pixels ;
Horizontal scrolling content at a height equivalent to 256 CSS pixels .
Except for parts of the content which require two-dimensional layout for usage or meaning.
Note 1 320 CSS pixels is equivalent to a starting viewport width of 1280 CSS pixels wide at 400% zoom. For web content which is designed to scroll horizontally (e.g., with vertical text), 256 CSS pixels is equivalent to a starting viewport height of 1024 CSS pixels at 400% zoom.
Note 2 Examples of content which requires two-dimensional layout are images required for understanding (such as maps and diagrams), video, games, presentations, data tables (not individual cells), and interfaces where it is necessary to keep toolbars in view while manipulating content. It is acceptable to provide two-dimensional scrolling for such parts of the content.

### 1.4.11 Non-text Contrast（Level AA）

The visual presentation of the following have a contrast ratio of at least 3:1 against adjacent color(s):
User Interface Components
Visual information required to identify user interface components and states , except for inactive components or where the appearance of the component is determined by the user agent and not modified by the author;
Graphical Objects
Parts of graphics required to understand the content, except when a particular presentation of graphics is essential to the information being conveyed.

### 1.4.12 Text Spacing（Level AA）

In content implemented using markup languages that support the following text style properties , no loss of content or functionality occurs by setting all of the following and by changing no other style property:
Line height (line spacing) to at least 1.5 times the font size;
Spacing following paragraphs to at least 2 times the font size;
Letter spacing (tracking) to at least 0.12 times the font size;
Word spacing to at least 0.16 times the font size.
Exception: Human languages and scripts that do not make use of one or more of these text style properties in written text can conform using only the properties that exist for that combination of language and script.

### 1.4.13 Content on Hover or Focus（Level AA）

Where receiving and then removing pointer hover or keyboard focus triggers additional content to become visible and then hidden, the following are true:
Dismissible
A mechanism is available to dismiss the additional content without moving pointer hover or keyboard focus, unless the additional content communicates an input error or does not obscure or replace other content;
Hoverable
If pointer hover can trigger the additional content, then the pointer can be moved over the additional content without the additional content disappearing;
Persistent
The additional content remains visible until the hover or focus trigger is removed, the user dismisses it, or its information is no longer valid.
Exception: The visual presentation of the additional content is controlled by the user agent and is not modified by the author.
Note 1 Examples of additional content controlled by the user agent include browser tooltips created through use of the HTML title attribute .
Note 2 Custom tooltips, sub-menus, and other nonmodal popups that display on hover and focus are examples of additional content covered by this criterion.

### 2.1.4 Character Key Shortcuts（Level A）

If a keyboard shortcut is implemented in content using only letter (including upper- and lower-case letters), punctuation, number, or symbol characters, then at least one of the following is true:
Turn off
A mechanism is available to turn the shortcut off;
Remap
A mechanism is available to remap the shortcut to include one or more non-printable keyboard keys (e.g., Ctrl, Alt);
Active only on focus
The keyboard shortcut for a user interface component is only active when that component has focus.

### 2.2.6 Timeouts（Level AAA）

Users are warned of the duration of any user inactivity that could cause data loss, unless the data is preserved for more than 20 hours when the user does not take any actions.
Note Privacy regulations may require explicit user consent before user identification has been authenticated and before user data is preserved. In cases where the user is a minor, explicit consent may not be solicited in most jurisdictions, countries or regions. Consultation with privacy professionals and legal counsel is advised when considering data preservation as an approach to satisfy this success criterion.

### 2.3.3 Animation from Interactions（Level AAA）

Motion animation triggered by interaction can be disabled, unless the animation is essential to the functionality or the information being conveyed.

### 2.5.1 Pointer Gestures（Level A）

All functionality that uses multipoint or path-based gestures for operation can be operated with a single pointer without a path-based gesture, unless a multipoint or path-based gesture is essential .
Note This requirement applies to web content that interprets pointer actions (i.e. this does not apply to actions that are required to operate the user agent or assistive technology).

### 2.5.2 Pointer Cancellation（Level A）

For functionality that can be operated using a single pointer , at least one of the following is true:
No Down-Event
The down-event of the pointer is not used to execute any part of the function;
Abort or Undo
Completion of the function is on the up-event , and a mechanism is available to abort the function before completion or to undo the function after completion;
Up Reversal
The up-event reverses any outcome of the preceding down-event;
Essential
Completing the function on the down-event is essential .
Note 1 Functions that emulate a keyboard or numeric keypad key press are considered essential.
Note 2 This requirement applies to web content that interprets pointer actions (i.e. this does not apply to actions that are required to operate the user agent or assistive technology).

### 2.5.3 Label in Name（Level A）

For user interface components with labels that include text or images of text , the name contains the text that is presented visually.
Note A best practice is to have the text of the label at the start of the name.

### 2.5.4 Motion Actuation（Level A）

Functionality that can be operated by device motion or user motion can also be operated by user interface components and responding to the motion can be disabled to prevent accidental actuation, except when:
Supported Interface
The motion is used to operate functionality through an accessibility supported interface;
Essential
The motion is essential for the function and doing so would invalidate the activity.

### 2.5.5 Target Size（Level AAA）

The size of the target for pointer inputs is at least 44 by 44 CSS pixels except when:
Equivalent
The target is available through an equivalent link or control on the same page that is at least 44 by 44 CSS pixels;
Inline
The target is in a sentence or block of text;
User Agent Control
The size of the target is determined by the user agent and is not modified by the author;
Essential
A particular presentation of the target is essential to the information being conveyed.

### 2.5.6 Concurrent Input Mechanisms（Level AAA）

Web content does not restrict use of input modalities available on a platform except where the restriction is essential , required to ensure the security of the content, or required to respect user settings.

### 4.1.3 Status Messages（Level AA）

In content implemented using markup languages, status messages can be programmatically determined through role or properties such that they can be presented to the user by assistive technologies without receiving focus.

