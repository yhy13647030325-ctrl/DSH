# WCAG 2.2 新增成功准则原文摘录

> **源文件**：`_standards/wcag22.html`（W3C Recommendation, https://www.w3.org/TR/WCAG22/）
> **抓取日期**：2026-11-17
> **提取方式**：同上，`extract_sc_full.js` 配平提取。
> **条目来源**：`diff_wcag.js` 比对 wcag21.html 与 wcag22.html 算出，**9 条**，与正文清单一致。

### 2.4.11 Focus Not Obscured (Minimum)（Level AA）

New
When a user interface component receives keyboard focus, the component is not entirely hidden due to author-created content.
Note 1 Where content in a configurable interface can be repositioned by the user, then only the initial positions of user-movable content are considered for testing and conformance of this success criterion.
Note 2 Content opened by the user may obscure the component receiving focus. If the user can reveal the focused component without advancing the keyboard focus, the component with focus is not considered visually hidden due to author-created content.

### 2.4.12 Focus Not Obscured (Enhanced)（Level AAA）

New
When a user interface component receives keyboard focus, no part of the component is hidden by author-created content.

### 2.4.13 Focus Appearance（Level AAA）

New
When the keyboard focus indicator is visible, an area of the focus indicator meets all the following:
is at least as large as the area of a 2 CSS pixel thick perimeter of the unfocused component or sub-component, and
has a contrast ratio of at least 3:1 between the same pixels in the focused and unfocused states.
Exceptions:
The focus indicator is determined by the user agent and cannot be adjusted by the author, or
The focus indicator and the indicator's background color are not modified by the author.
Note 1 What is perceived as the user interface component or sub-component (to determine the perimeter) depends on its visual presentation . The visual presentation includes the component's visible content , border, and component-specific background. It does not include shadow and glow effects outside the component's content, background, or border.
Note 2 Examples of sub-components that may receive a focus indicator are menu items in an opened drop-down menu, or focusable cells in a grid.
Note 3 Contrast calculations can be based on colors defined within the technology (such as HTML , CSS, and SVG). Pixels modified by user agent resolution enhancements and anti-aliasing can be ignored.

### 2.5.7 Dragging Movements（Level AA）

New
All functionality that uses a dragging movement for operation can be achieved by a single pointer without dragging, unless dragging is essential or the functionality is determined by the user agent and not modified by the author.
Note This requirement applies to web content that interprets pointer actions (i.e., this does not apply to actions that are required to operate the user agent or assistive technology).

### 2.5.8 Target Size (Minimum)（Level AA）

New
The size of the target for pointer inputs is at least 24 by 24 CSS pixels , except when:
Spacing
Undersized targets (those less than 24 by 24 CSS pixels) are positioned so that if a 24 CSS pixel diameter circle is centered on the bounding box of each, the circles do not intersect another target or the circle for another undersized target;
Equivalent
The function can be achieved through a different control on the same page that meets this criterion;
Inline
The target is in a sentence or its size is otherwise constrained by the line-height of non-target text;
User Agent Control
The size of the target is determined by the user agent and is not modified by the author;
Essential
A particular presentation of the target is essential or is legally required for the information being conveyed.
Note 1 Targets that allow for values to be selected spatially based on position within the target are considered one target for the purpose of the success criterion. Examples include sliders, color pickers displaying a gradient of colors, or editable areas where you position the cursor.
Note 2 For inline targets the line-height should be interpreted as perpendicular to the flow of text. For example, in a language displayed vertically, the line-height would be horizontal.

### 3.2.6 Consistent Help（Level A）

New
If a web page contains any of the following help mechanisms , and those mechanisms are repeated on multiple web pages within a set of web pages , they occur in the same order relative to other page content, unless a change is initiated by the user:
Human contact details;
Human contact mechanism;
Self-help option;
A fully automated contact mechanism.
Note 1 Help mechanisms may be provided directly on the page, or may be provided via a direct link to a different page containing the information.
Note 2 For this success criterion, "the same order relative to other page content" can be thought of as how the content is ordered when the page is serialized. The visual position of a help mechanism is likely to be consistent across pages for the same page variation (e.g., CSS break-point). The user can initiate a change, such as changing the page's zoom or orientation, which may trigger a different page variation. This criterion is concerned with relative order across pages displayed in the same page variation (e.g., same zoom level and orientation).

### 3.3.7 Redundant Entry（Level A）

New
Information previously entered by or provided to the user that is required to be entered again in the same process is either:
auto-populated, or
available for the user to select.
Except when:
re-entering the information is essential ,
the information is required to ensure the security of the content, or
previously entered information is no longer valid.

### 3.3.8 Accessible Authentication (Minimum)（Level AA）

New
A cognitive function test (such as remembering a password or solving a puzzle) is not required for any step in an authentication process unless that step provides at least one of the following:
Alternative
Another authentication method that does not rely on a cognitive function test.
Mechanism
A mechanism is available to assist the user in completing the cognitive function test.
Object Recognition
The cognitive function test is to recognize objects.
Personal Content
The cognitive function test is to identify non-text content the user provided to the website.
Note 1 "Object recognition" and "Personal content" may be represented by images, video, or audio.
Note 2 Examples of mechanisms that satisfy this criterion include:
support for password entry by password managers to reduce memory need, and
copy and paste to reduce the cognitive burden of re-typing.

### 3.3.9 Accessible Authentication (Enhanced)（Level AAA）

New
A cognitive function test (such as remembering a password or solving a puzzle) is not required for any step in an authentication process unless that step provides at least one of the following:
Alternative
Another authentication method that does not rely on a cognitive function test.
Mechanism
A mechanism is available to assist the user in completing the cognitive function test.

