# Analysis Framework — 分析层规则

> 本文件对应 Slide2HTML。
> 读取时机：完成输入清点后、开始抽取信息前；构建证据模型、概念模型、考核模型、时间线，以及做去重与冲突检测时随时回查。

---

# 2. INPUT MODES

## 2.1 Single-File Mode

Activate when one relevant course document is available.

A single file is a complete and valid input.

The system must NOT require additional files.

Examples:

```text
Lecture_05.pdf
Assignment_02.pdf
Project_Brief.pdf
Course_Syllabus.pdf
Reading.pdf
```

The system first identifies the document type and then generates an appropriate knowledge hub.

---

## 2.2 Multi-File Mode

Activate when two or more related course documents are available.

Treat them as a unified course corpus.

Perform:

- cross-document synthesis;
- deduplication;
- timeline merging;
- grading aggregation;
- assessment mapping;
- concept mapping;
- conflict detection;
- version detection;
- resource aggregation.

Do not simply concatenate summaries.

---

# 3. DOCUMENT TYPE DETECTION

Classify every input into one of:

```text
SYLLABUS
LECTURE
LECTURE_NOTES
ASSIGNMENT
PROJECT
PROJECT_BRIEF
RUBRIC
EXAM_GUIDE
ANNOUNCEMENT
READING
RESEARCH_PAPER
TUTORIAL
LAB
REFERENCE
OTHER
```

Use:

- filename;
- title;
- headings;
- content;
- metadata;
- contextual clues.

Never rely exclusively on filenames.

---

# 4. INPUT INVENTORY

Before analysis, construct an internal inventory.

For every file record:

```text
Source ID
Filename
Document Type
Date
Version
Course
Week / Lecture
Page / Slide Count
Authority Level
Assessment Relevance
```

Example:

```text
S01 — Course Syllabus
S02 — Week 01 Lecture
S03 — Week 02 Lecture
S04 — Assignment 01
S05 — Project Brief
S06 — Course Announcement
```

---

# 5. SOURCE AUTHORITY

Use the following default authority hierarchy:

```text
Latest explicit instructor announcement
        ↓
Latest official assignment / project specification
        ↓
Official syllabus
        ↓
Official lecture material
        ↓
Tutorial / lab
        ↓
Supplementary material
        ↓
Student-created material
```

A newer explicit update overrides an older requirement when the update is clear.

If a conflict cannot be resolved confidently, expose the conflict.

Never silently select one version.

---

# 6. EVIDENCE MODEL

Classify information internally as:

### E1 — Explicit

Directly stated.

### E2 — Cross-Document Confirmed

Supported by multiple course documents.

### E3 — Inferred

Reasonably inferred from the material.

### E4 — Speculative

Insufficiently supported.

Rules:

- E1/E2 may be presented as course facts.
- E3 must be labeled as inference.
- E4 must not be presented as fact.

---

# 7. NON-HALLUCINATION RULE

Never invent:

- grading percentages;
- deadlines;
- attendance rules;
- exam dates;
- exam formats;
- project requirements;
- assignment requirements;
- instructor policies;
- required readings;
- URLs;
- datasets;
- software requirements.

If information is absent:

> Not specified in the provided materials.  
> 提供的材料中未明确说明。

If inferred:

> Inferred from the provided materials.  
> 根据提供的材料推断。

---

# 8. SOURCE TRACEABILITY

Important information must retain source references whenever possible.

Use:

```text
[S01 p.4]
[S02 slide 18]
[S05 p.2–5]
```

Never fabricate page or slide numbers.

Prioritize source references for:

- grading;
- deadlines;
- attendance;
- policies;
- assignment requirements;
- project requirements;
- exam information;
- formulas;
- definitions;
- external resources.

---

# 9. ACADEMIC ANALYSIS

For lecture material extract:

- executive summary;
- core concepts;
- definitions;
- theories;
- models;
- methods;
- algorithms;
- formulas;
- assumptions;
- examples;
- applications;
- limitations;
- important takeaways;
- related concepts.

For graduate / PhD-level material, preserve technical precision.

Do not oversimplify complex material merely for readability.

---

# 10. CONCEPT MODEL

For each major concept capture:

```text
Concept
English Name
Chinese Name
Definition
Intuition
Technical Explanation
Formula
Variables
Example
Application
Limitation
Related Concepts
Related Lectures
Related Assessments
Sources
```

Only populate fields supported by evidence.

---

# 11. CONCEPT RELATIONSHIPS

Identify:

- prerequisite → dependent concept;
- theory → method;
- method → application;
- problem → solution;
- input → process → output;
- model A → model B;
- assumption → consequence;
- concept → assignment;
- concept → project.

Create a course knowledge map when sufficient information exists.

---

# 12. ASSESSMENT INTELLIGENCE

Extract:

- attendance;
- participation;
- assignments;
- homework;
- quizzes;
- exams;
- projects;
- presentations;
- reports;
- labs;
- papers.

For each assessment capture:

```text
Name
Weight
Deadline
Format
Submission Platform
Individual / Group
Group Size
Deliverables
Rubric
Required Tools
Required Dataset
Late Policy
Resubmission Policy
Source
```

---

# 13. GRADING VALIDATION

When weights exist:

1. calculate total;
2. identify missing weights;
3. identify duplicates;
4. check whether total = 100%.

If total = 100%:

> ✓ Grading structure accounts for 100%.

If total ≠ 100%:

> ⚠ Grading structure requires verification.  
> ⚠ 当前评分结构需要核实。

Never normalize percentages.

---

# 14. ASSIGNMENT ANALYSIS

For each assignment generate:

### Assignment Overview
### 作业概览

### What You Need to Do
### 实际需要完成什么

### Deliverables
### 提交内容

### Deadline
### 截止时间

### Grading
### 评分

### Required Knowledge
### 所需知识

### Requirements & Constraints
### 要求与限制

### Source
### 来源

Do not add unsupported requirements.

---

# 15. PROJECT ANALYSIS

Extract:

- project objective;
- research question;
- group requirements;
- group size;
- proposal;
- milestones;
- implementation;
- experiment;
- presentation;
- report;
- code;
- dataset;
- evaluation;
- final deliverables;
- deadlines;
- weight.

Generate a roadmap only when supported.

---

# 16. POLICY ANALYSIS

Extract:

- attendance;
- participation;
- absence;
- lateness;
- academic integrity;
- plagiarism;
- collaboration;
- AI usage;
- citation;
- late submission;
- extensions;
- resubmission.

Policies should receive high visual priority.

---

# 17. RESOURCE EXTRACTION

Extract resources mentioned in the materials:

- papers;
- books;
- websites;
- GitHub repositories;
- datasets;
- software;
- frameworks;
- APIs;
- tutorials;
- videos;
- documentation;
- online courses.

For each resource:

```text
Name
Type
Description
Context
Related Topic
URL
Source
```

Never fabricate URLs.

---

# 18. READING CLASSIFICATION

When supported, classify:

- Required Reading;
- Recommended Reading;
- Further Reading.

Never upgrade recommended material to required reading.

---

# 19. RESEARCH LAYER

For graduate / PhD courses, identify when present:

- seminal papers;
- influential research;
- research questions;
- theoretical debates;
- methodological choices;
- limitations;
- open problems;
- datasets;
- benchmarks;
- research tools;
- research directions.

Clearly distinguish:

**Course Material**

from:

**Research Context**

Do not attribute general academic knowledge to the instructor.

---

# 20. ASSESSMENT ↔ KNOWLEDGE MAPPING

Create two-way mappings.

Example:

```text
Assignment 2
├── Lecture 04
├── Regression
├── Regularization
└── Model Evaluation
```

And:

```text
Regularization
├── Lecture 05
├── Assignment 02
└── Project
```

Only create evidence-supported relationships.

Inferred relationships must be labeled.

---

# 21. TIMELINE

Build a chronological timeline from all available dates.

Include:

- assignment deadlines;
- project milestones;
- quizzes;
- presentations;
- exams;
- proposals;
- reports.

Single-file mode:

Only include dates found in that file.

Multi-file mode:

Merge dates across documents.

---

# 22. CONFLICT DETECTION

Detect conflicts involving:

- deadlines;
- grading;
- group size;
- deliverables;
- submission requirements;
- exam format;
- attendance;
- AI policy;
- project requirements.

Create:

# Items to Verify
# 需要核实的信息

Each conflict must show:

```text
Issue
Version A
Source A
Version B
Source B
Possible Explanation
Verification Recommendation
```

---

# 23. MISSING INFORMATION

Create:

# Information Not Found
# 材料中未找到的信息

Examples:

```text
Final exam date — Not found
Attendance threshold — Not found
Project group size — Not found
Submission platform — Not found
```

Meaning:

> Not found in the provided materials.

NOT:

> No such requirement exists.

---

# 24. BILINGUAL REQUIREMENT

All major content must be bilingual.

Default format:

```text
Cross-validation
交叉验证

Cross-validation evaluates model generalization...
交叉验证用于评估模型的泛化能力……
```

English should generally appear first.

Preserve original English for:

- technical terminology;
- software;
- APIs;
- code;
- equations;
- variable names;
- paper titles.

---

# 25. PRIORITY SYSTEM

Classify information:

### P0 — Critical

- deadlines;
- grading;
- attendance;
- submission;
- academic integrity;
- project requirements.

### P1 — Core

- theories;
- definitions;
- models;
- algorithms;
- formulas.

### P2 — Supporting

- examples;
- applications;
- case studies.

### P3 — Supplementary

- optional resources;
- peripheral content.

The HTML visual hierarchy must reflect these priorities.
