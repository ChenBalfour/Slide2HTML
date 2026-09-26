# Quality Control — 质检、验证与交付规则

> 本文件对应 Slide2HTML。
> 注意：**§67 Final Execution Contract（20 步执行契约）位于 SKILL.md 正文**，是每次任务的主操作序列，此处不再重复。
> 读取时机：HTML 生成之后、交付之前，逐项执行五类质检与文件验证；处理错误、部分材料及生成最终报告时回查。

---

# 52. HTML QUALITY CONTROL — STRUCTURAL

After generating the HTML file, verify:

### Required elements

- `<!DOCTYPE html>`
- `<html>`
- `<head>`
- `<meta charset>`
- `<body>`
- `<title>`

### Assets

- CSS embedded;
- JS embedded;
- no broken internal references.

### Navigation

Every navigation target must exist.

### Content

No empty major sections.

---

# 53. HTML QUALITY CONTROL — CONTENT

Verify:

- all successfully processed files are represented;
- all major assessment components are represented;
- deadlines are represented;
- important policies are represented;
- major concepts are represented;
- resources are represented;
- conflicts are represented;
- missing information is represented.

---

# 54. HTML QUALITY CONTROL — FACTUAL

Perform a final hallucination audit.

Check:

- no fabricated deadlines;
- no fabricated percentages;
- no fabricated policies;
- no fabricated URLs;
- no unsupported requirements;
- no false instructor attribution.

---

# 55. HTML QUALITY CONTROL — BILINGUAL

Check:

- major sections bilingual;
- technical terminology accurate;
- Chinese translation natural;
- English meaning preserved;
- formulas unchanged.

---

# 56. HTML QUALITY CONTROL — UX

Check:

- dashboard understandable within 30 seconds;
- important deadlines visible;
- grading easy to locate;
- assignment requirements easy to locate;
- concepts searchable;
- navigation works;
- mobile layout works.

---

# 57. FILE VALIDATION

After writing:

```text
slide2html.html
```

perform:

1. file existence check;
2. non-zero file size check;
3. UTF-8 validity check;
4. HTML structure check;
5. internal anchor check;
6. JavaScript syntax sanity check where possible.

If validation fails:

1. fix the HTML;
2. regenerate;
3. validate again.

Do not deliver a known-invalid HTML file.

---

# 58. OUTPUT FILE NAMING

Default:

```text
slide2html.html
```

If course code is reliably available:

```text
COURSECODE_slide2html.html
```

Sanitize unsupported filename characters.

---

# 59. OPTIONAL SUPPORTING FILES

Only when useful, optionally generate:

```text
slide2html_data.json
slide2html_summary.md
```

The primary deliverable remains:

```text
slide2html.html
```

Do not generate unnecessary files.

---

# 60. ERROR HANDLING

If a document cannot be fully processed:

- continue processing other files;
- record the failed document;
- mark its information as incomplete;
- do not pretend it was processed.

Example:

> Lecture_07.pdf could not be fully processed.  
> Lecture 07 information may be incomplete.

---

# 61. PARTIAL COURSE RULE

More files do not necessarily mean complete course information.

Always distinguish:

### Available in provided materials

and:

### Not found in provided materials

Never infer:

> “Not present in this file = does not exist in the course.”

---

# 62. SINGLE-FILE RULE

One file is always a valid input.

Never refuse analysis solely because:

> “Only one file was uploaded.”

Instead:

1. identify its type;
2. perform type-specific analysis;
3. generate an adaptive HTML hub;
4. identify missing course-level information.

---

# 63. USER INTENT OVERRIDE

If the user explicitly requests a narrow scope, follow it.

Examples:

> “Only summarize this lecture.”

Do not generate unnecessary course-level sections.

> “Extract all assignments.”

Focus on assignments.

> “Build a complete course hub.”

Use full synthesis.

If no scope is specified:

> Generate the most useful adaptive HTML supported by the available evidence.

---

# 64. DEFAULT SINGLE-FILE EXPERIENCE

If the user uploads:

`Lecture_05.pdf`

generate:

```text
Lecture 05
│
├── Executive Summary
├── Core Concepts
├── Key Definitions
├── Models / Methods
├── Formulas
├── Examples
├── Important Takeaways
├── Assessment Relevance
├── Resources
├── Missing Information
└── Sources
```

Do not fabricate course-wide grading.

---

# 65. DEFAULT MULTI-FILE EXPERIENCE

If the user uploads:

```text
Syllabus
Lecture 01–12
Assignments
Project Brief
Rubric
```

generate:

```text
Slide2HTML
│
├── Course Overview
├── Grading
├── Attendance & Policies
├── Assignments
├── Projects
├── Exams
├── Timeline
├── Lecture Knowledge
├── Knowledge Map
├── Assessment Mapping
├── Resources
├── Reading
├── Items to Verify
├── Missing Information
└── Sources
```

---

# 66. FINAL USER REPORT

After successful generation, report briefly:

### Multi-File Mode

```text
Slide2HTML generated.

Mode: Multi-File
Files processed: N
Lectures: N
Assignments: N
Projects: N
Assessment components: N
Resources: N
Important dates: N
Conflicts: N
Missing information: N
```

### Single-File Mode

```text
Slide2HTML generated.

Mode: Single-File
Document type: Lecture
Source: Lecture_05.pdf
Core concepts: N
Methods / Models: N
Formulas: N
Resources: N
Assessment references: N
Missing course-level information: N
```

Then provide the actual HTML file.

Do not paste the entire HTML source into the chat.

---

# 68. ULTIMATE PRINCIPLE

Slide2HTML is not a PDF summarizer.

It is:

> **A personal academic course operating system.**

Its purpose is to transform:

```text
Documents
   ↓
Information
   ↓
Knowledge
   ↓
Relationships
   ↓
Assessment Awareness
   ↓
Actionable Academic Dashboard
```

Optimize in this order:

```text
Evidence Accuracy
        >
Completeness
        >
Traceability
        >
Academic Usefulness
        >
Information Architecture
        >
Frontend UX
        >
Visual Polish
```

Never sacrifice evidence accuracy for completeness.

Never sacrifice completeness for visual appearance.

Never invent information to make the course appear complete.

Always produce the best possible academic knowledge hub supported by the available evidence.
