# Analysis framework

Use for complex extraction, multi-document synthesis, and course requirements. The evidence rules in `SKILL.md` remain the shared baseline.

## Extraction and provenance

Track only useful metadata: source ID, filename, document type, and known course/version/date/locator. Classify from content, not filename alone. Do not infer a semester or edition from file modification time.

Extract text once with available tools. Inspect page renders when layout conveys meaning: multi-column reading order, formula symbols, chart axes, table headers, annotations, or image-only slides. Use OCR only where needed; uncertain OCR is uncertain evidence. Cite actual PDF pages or slide numbers consistently, explaining differences from printed labels if relevant. List unreadable sources as unprocessed rather than counting them as covered.

Keep a compact working record of important claims and sources; a rigid schema for every sentence is unnecessary.

| Evidence | Meaning | Presentation |
|---|---|---|
| E1 | Explicit in a source | Source fact with locator |
| E2 | Consistently supported by multiple sources | Source fact with relevant locators |
| E3 | Reasonably inferred | Visible inference label and supporting sources |
| E4 | Unsupported speculation | Exclude from factual content |

Grades describe support, not certainty: repeated outdated information can still be wrong. Prioritize citations for requirements, definitions, equations, and consequential claims; avoid badge clutter. Supplemental academic explanations or invented teaching examples may help, but label them as supplemental, never as instructor statements or source examples.

## Match extraction to the document

- **Lecture/notes:** central ideas, definitions, methods, equations with variables and assumptions, meaningful examples, limitations, and takeaways. Preserve technical precision. Avoid an empty assessment section.
- **Assignment/project/rubric/exam guide:** objective, deliverables, deadline, submission channel, format, individual/group constraints, weight, rubric, and relevant policies. Separate assessed requirements from optional study advice.
- **Syllabus/announcement:** overview, assessment structure, schedule, readings, and important rules, especially late submission, attendance, collaboration, and AI use.
- **Reading/research paper:** question, method, findings, assumptions, limitations, and its stated course relevance. Do not invent an assessment connection.

Populate only useful, supported fields. Group related ideas into one explanation with multiple citations rather than concatenating file summaries. Make supported prerequisite/application links; label inferred relationships. Use a map only when it clarifies relationships.

## Assessment weights and dates

Keep percentages as stated. Sum unique components at the same level; do not add a category and its subcomponents together. Deduplicate repeated statements, keep different courses or assessment versions separate, and do not rescale to 100%.

Claim a complete 100% grading structure only when the source establishes the full structure and totals agree. A partial package totaling 40% is partial evidence, not proof of a grading error. Treat unexplained inconsistency in an explicitly complete scheme as an item to verify. Accommodate explicit bonus credit or alternative grading schemes.

Keep original date wording when a year, timezone, or interpretation is missing. Do not silently convert “next Friday,” infer the current year, or label historical course deadlines as upcoming. Sort comparable absolute dates; present ambiguous/relative dates separately with source context.

## Versions, conflicts, and gaps

Compare documents only after confirming the course, cohort, and assessment match. A clearly applicable, explicit instructor correction may supersede an earlier requirement: show the effective value, its source, and the superseded version in a compact note. A newer filename alone is insufficient.

For unresolved conflicts, show the issue, both values and sources, and what needs confirmation. Do not choose by a universal document ranking. A possible explanation is an inference, not a resolution.

Surface gaps that affect the user's task: a missing submission channel matters in an assignment guide; an absent attendance rule usually does not matter in a lecture guide. Consolidate gaps into a concise note, not empty cards. More files do not establish complete course coverage.
