# HTML Specification — 产出层规则

> 本文件对应 Slide2HTML。
> 读取时机：分析与建模完成、开始选择页面架构和编写 HTML 时；涉及设计系统、组件、搜索、语言切换、响应式与离线规则时回查。

---

# 26. HTML GENERATION PROTOCOL

## 26.1 NON-NEGOTIABLE OUTPUT RULE

The primary deliverable MUST be an actual file:

```text
slide2html.html
```

Do not merely provide HTML source code in chat when file generation is available.

The system must:

1. construct the HTML;
2. write it to a real file;
3. verify the file exists;
4. verify the HTML is non-empty;
5. perform structural validation;
6. provide the generated file to the user.

---

# 27. HTML FILE REQUIREMENTS

The generated file MUST:

- use UTF-8;
- be a complete HTML document;
- contain `<!DOCTYPE html>`;
- contain `<html>`;
- contain `<head>`;
- contain `<body>`;
- contain embedded CSS;
- contain embedded JavaScript when required;
- work when opened locally;
- require no build process;
- require no backend;
- preserve Chinese text;
- be responsive.

---

# 28. SINGLE-FILE HTML

For one file, adapt the page to its document type.

## Lecture

```text
Dashboard
→ Lecture Overview
→ Core Concepts
→ Methods
→ Formulas
→ Examples
→ Takeaways
→ Resources
→ Assessment Relevance
→ Sources
```

## Assignment

```text
Dashboard
→ Assignment Overview
→ What You Need To Do
→ Deliverables
→ Deadline
→ Rubric
→ Required Knowledge
→ Resources
→ Sources
```

## Project

```text
Dashboard
→ Project Overview
→ Requirements
→ Milestones
→ Deliverables
→ Evaluation
→ Resources
→ Sources
```

## Syllabus

```text
Dashboard
→ Course Overview
→ Grading
→ Schedule
→ Policies
→ Assessments
→ Readings
→ Sources
```

Do not display irrelevant empty sections.

When the single file contains no deadlines, policies or grading (typical for a bare
LECTURE), omit the Dashboard's Important Dates / Critical Rules / Assessment Snapshot
areas instead of showing empty cards, and consolidate those gaps in the Items to Verify /
Missing Information section (see §22–§23).

---

# 29. MULTI-FILE HTML

When enough course materials are available, generate:

```text
Dashboard
Course Overview
Assessment
    ├── Grading
    ├── Attendance
    ├── Assignments
    ├── Projects
    └── Exams
Timeline
Lectures
Knowledge Map
Assessment Mapping
Resources
Reading
Items to Verify
Missing Information
Sources
```

---

# 30. HTML DESIGN SYSTEM

The generated page must look like a polished, modern SaaS product — think Linear,
Vercel Dashboard, Notion, or Stripe — not a 2010s academic template. It should feel
crisp, calm, and premium while remaining fully offline and self-contained.

## 30.1 Design Tokens (CSS Custom Properties)

Define these variables at `:root` and reuse them everywhere:

```css
:root {
  /* Color — background layers */
  --bg-page: #f6f7fb;
  --bg-surface: #ffffff;
  --bg-surface-hover: #f8f9fd;
  --bg-subtle: #eef0f7;

  /* Color — brand accent (indigo) */
  --accent: #4f46e5;
  --accent-hover: #4338ca;
  --accent-soft: #eef2ff;
  --accent-border: #c7d2fe;

  /* Color — text */
  --text-primary: #0f172a;
  --text-secondary: #475569;
  --text-muted: #94a3b8;
  --text-on-accent: #ffffff;

  /* Color — semantic */
  --success: #059669;
  --success-soft: #ecfdf5;
  --warning: #d97706;
  --warning-soft: #fffbeb;
  --danger: #dc2626;
  --danger-soft: #fef2f2;
  --info: #0284c7;
  --info-soft: #f0f9ff;

  /* Color — borders */
  --border: #e2e8f0;
  --border-strong: #cbd5e1;

  /* Typography */
  --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    "Helvetica Neue", Arial, "Noto Sans SC", "PingFang SC",
    "Microsoft YaHei", sans-serif;
  --font-mono: "SF Mono", "Cascadia Code", "Fira Code", Consolas, monospace;

  /* Type scale */
  --fs-xs: 0.75rem;
  --fs-sm: 0.875rem;
  --fs-base: 1rem;
  --fs-lg: 1.125rem;
  --fs-xl: 1.25rem;
  --fs-2xl: 1.5rem;
  --fs-3xl: 1.875rem;

  /* Radius */
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --radius-full: 9999px;

  /* Shadows */
  --shadow-xs: 0 1px 2px rgba(15, 23, 42, 0.04);
  --shadow-sm: 0 1px 3px rgba(15, 23, 42, 0.06), 0 1px 2px rgba(15,23,42,0.04);
  --shadow-md: 0 4px 12px rgba(15, 23, 42, 0.07), 0 2px 4px rgba(15,23,42,0.04);
  --shadow-lg: 0 12px 32px rgba(15, 23, 42, 0.10), 0 4px 8px rgba(15,23,42,0.05);

  /* Spacing (4px base) */
  --sp-1: 4px;  --sp-2: 8px;  --sp-3: 12px; --sp-4: 16px;
  --sp-5: 20px; --sp-6: 24px; --sp-8: 32px; --sp-10: 40px;
  --sp-12: 48px;

  /* Layout */
  --sidebar-w: 260px;
  --content-max: 960px;

  /* Motion */
  --ease: cubic-bezier(0.4, 0, 0.2, 1);
  --dur: 200ms;
}
```

## 30.2 Visual Principles

- **Background**: soft cool off-white (`--bg-page`), not pure white.
- **Cards**: pure white (`--bg-surface`), 1px border (`--border`), radius `--radius-md`,
  and a layered shadow that grows on hover.
- **Accent**: a single restrained indigo (`--accent`) used sparingly — for primary
  buttons, active nav links, key highlights, and important callouts. Do not splash
  it everywhere.
- **Whitespace**: generous. Let content breathe. Section spacing should be at least
  `--sp-8` (32px).
- **Typography**: `--font-sans` for everything; `--font-mono` only for code,
  URLs, variable names, and source badges.
- **Hierarchy**: page title `--fs-3xl` bold; section headings `--fs-xl` semibold;
  body `--fs-base`; captions/labels `--fs-sm`; meta/source `--fs-xs`.

## 30.3 Component Styling

### Cards

```css
.card {
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: var(--sp-5);
  box-shadow: var(--shadow-sm);
  transition: box-shadow var(--dur) var(--ease), transform var(--dur) var(--ease);
}
.card:hover {
  box-shadow: var(--shadow-md);
}
```

### Buttons / Nav

- Primary: solid `--accent` background, white text, `--radius-sm`, subtle shadow.
- Ghost/secondary: transparent with `--border` border, dark text.
- Active nav item: `--accent-soft` background + `--accent` left bar or text color.

### Badges / Tags

- Pill-shaped (`--radius-full`), soft tinted backgrounds (`--*-soft`), small
  font (`--fs-xs`), semibold, 4–8px horizontal padding.
- Source badges (`[S01 p.4]`) should be `--font-mono`, `--fs-xs`, `--bg-subtle`,
  `--text-secondary`, no background fill.

### Tables

- Clean lines: only horizontal borders (`--border`), no vertical grid lines.
- Header row: `--bg-subtle`, uppercase `--fs-xs`, semibold, `--text-secondary`.
- Row hover: `--bg-surface-hover`.

### Callouts / Warning Cards

- Left accent bar (3–4px) in the semantic color; soft tinted background.
- Warning: `--warning` border on left, `--warning-soft` background.
- Danger/conflict: `--danger` left bar, `--danger-soft` background.
- Info: `--info` left bar, `--info-soft` background.

## 30.4 Micro-Interactions

- All interactive elements get a 200ms ease transition on color, background,
  shadow, and transform.
- Cards lift slightly on hover (shadow goes from sm → md).
- Nav links smoothly fade to accent on hover.
- No bouncing, no parallax, no marquee, no animated gradients.

## 30.5 What to Avoid

- Excessive gradients (at most one subtle header gradient if desired).
- Heavy drop shadows or glossy effects.
- Gaming / neon / dark-mode-by-default aesthetics.
- Decorative icons, illustrations, or emoji in the layout chrome.
- Fonts loaded from external CDNs — always use system font stack.
- Rounded-3xl cartoonish corners; keep radii restrained (6–16px).

The final result should look like a well-designed internal tool at a modern tech
company: calm, dense but not cramped, visually trustworthy, and easy to scan.

---

# 31. REQUIRED HTML COMPONENTS

Use reusable components where appropriate:

### Course Header

Course name, code, instructor, semester.

### Stat Card

Number of lectures, assignments, projects, resources.

### Assessment Card

Assessment details.

### Deadline Card

Date + requirement + source.

### Concept Card

Academic knowledge.

### Formula Card

Equation + variables + explanation.

### Resource Card

Paper / book / website / dataset / tool.

### Warning Card

Conflict or verification issue.

### Source Badge

Traceability.

---

# 32. DASHBOARD

The dashboard must answer:

> What is this course?

> What do I need to do?

> What is due?

> What matters most?

Display:

### Course Snapshot

- title;
- instructor;
- semester;
- material count;
- lecture count;
- assessment count.

### Assessment Snapshot

Grading overview.

### Important Dates

Upcoming deadlines.

### Critical Rules

Attendance, AI policy, academic integrity, late policy.

### Priority Knowledge

Core concepts.

---

# 33. SEARCH

Implement client-side search.

Search:

- concepts;
- lectures;
- assignments;
- projects;
- resources;
- policies;
- readings.

No backend required.

---

# 34. FILTERS

When useful provide:

- Lecture;
- Assignment;
- Project;
- Exam;
- Resource;
- Reading;
- High Priority.

---

# 35. LANGUAGE SWITCH

Provide:

```text
EN + 中文
English
中文
```

Default:

`EN + 中文`

Switch language client-side without page reload.

---

# 36. PROGRESS TRACKING

Optional checkboxes may track:

- lecture reviewed;
- reading completed;
- assignment completed;
- project milestone completed.

Use:

```javascript
localStorage
```

Do not alter academic source data.

---

# 37. RESPONSIVE DESIGN

Desktop:

```text
Sidebar | Main Content
```

Tablet:

```text
Compact Sidebar
```

Mobile:

```text
Collapsible Navigation
Stacked Cards
Scrollable Tables
```

Prevent horizontal page overflow.

---

# 38. ACCESSIBILITY

Use:

- semantic HTML;
- logical heading hierarchy;
- keyboard-accessible controls;
- focus states;
- readable contrast;
- meaningful labels;
- ARIA labels where appropriate.

---

# 39. JAVASCRIPT RULES

JavaScript must be:

- minimal;
- vanilla JS whenever possible;
- embedded inside the HTML;
- understandable;
- defensive against missing data.

Do not use JavaScript for functionality that can be achieved with HTML/CSS.

Required interactive functionality should work offline.

---

# 40. CSS RULES

CSS must be embedded in:

```html
<style>
...
</style>
```

Do not require a separate stylesheet.

Use CSS variables for design tokens.

Use responsive media queries.

Avoid excessive complexity.

---

# 41. EXTERNAL DEPENDENCY RULE

The HTML should work offline whenever possible.

Prefer:

- HTML;
- CSS;
- vanilla JavaScript.

Avoid:

- external frameworks;
- external fonts;
- external icon libraries;
- external JavaScript;
- external CSS.

If an external dependency is genuinely necessary, clearly indicate it.

Do not allow external dependencies to break the core page.

---

# 42. OFFLINE-FIRST RULE

The page must remain useful when opened directly as:

```text
file:///.../slide2html.html
```

Core functionality must not require:

- server;
- API;
- database;
- build system;
- login.

---

# 43. HTML STRUCTURE

The generated document should approximately follow:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>Slide2HTML — Interactive Study Page</title>

    <style>
        /* Embedded CSS */
    </style>
</head>

<body>

    <header>
        <!-- Course header -->
    </header>

    <nav>
        <!-- Navigation -->
    </nav>

    <main>
        <!-- Generated academic content -->
    </main>

    <footer>
        <!-- Source / generation information -->
    </footer>

    <script>
        /* Embedded JavaScript */
    </script>

</body>
</html>
```

---

# 44. CONTENT-TO-HTML MAPPING

Map structured information to appropriate components.

```text
Course Metadata
→ Header / Dashboard

Assessment
→ Assessment Cards / Tables

Deadline
→ Timeline / Deadline Cards

Concept
→ Concept Cards

Formula
→ Formula Cards

Resource
→ Resource Cards

Conflict
→ Warning Cards

Missing Information
→ Verification Section

Source
→ Source Badges / Source Index
```

Do not dump raw extracted text into the page.

---

# 45. TABLE RULES

Use tables for:

- grading;
- deadlines;
- assignment comparison;
- project milestones;
- reading lists;
- source index.

Tables must be responsive.

On mobile:

```css
overflow-x: auto;
```

Do not allow tables to break the page width.

---

# 46. FORMULA RULES

When mathematical notation is present:

1. preserve the original equation;
2. explain variables;
3. explain meaning;
4. explain assumptions where available;
5. provide interpretation.

Prefer self-contained rendering.

If MathJax is used, it must be explicitly treated as an external dependency.

Do not use MathJax merely for simple notation.

---

# 47. KNOWLEDGE GRAPH VISUALIZATION

If enough relationships exist, provide a visual knowledge map.

Possible implementation:

- CSS-based relationship cards;
- connected sections;
- lightweight SVG;
- vanilla JavaScript.

Do NOT introduce a large graph library solely for visualization.

If the relationship graph is too complex, use a structured hierarchy instead.

Accuracy is more important than visual sophistication.

---

# 48. INTERNAL DATA SEPARATION

The system should conceptually separate:

```text
SOURCE DATA
    ↓
NORMALIZED COURSE DATA
    ↓
GENERATED HTML
```

Do not mix unsupported interpretations into source facts.

---

# 49. SOURCE-BASED VS INFERRED CONTENT

When necessary, visually distinguish:

### Source-Based

直接来自课件 / 课程材料

### Contextual Explanation

用于帮助理解的学术解释

### Inferred

根据材料推断

The distinction should be subtle but visible.

---

# 50. DUPLICATION CONTROL

For Multi-File Mode:

If a concept appears in multiple files:

1. create one canonical explanation;
2. list all relevant sources;
3. list related lectures;
4. list related assessments.

Example:

```text
Regularization

Introduced:
Lecture 05

Applied:
Assignment 02

Revisited:
Lecture 08
```

---

# 51. CROSS-LINKING

Where appropriate, create internal links between:

```text
Lecture ↔ Concept
Concept ↔ Assignment
Assignment ↔ Lecture
Project ↔ Lecture
Paper ↔ Concept
Resource ↔ Topic
```

Every link must point to an actual generated section.

Do not create broken anchors.
