# Quality control and delivery

Use before delivering a new page or substantial edit. Check observable outcomes, not a ceremonial multi-pass process. For a small correction, validate affected content and interactions.

## Evidence and coverage

Confirm readable inputs are represented within scope. Reconcile every deadline, weight, policy, deliverable, and conflict against its source. Check representative core concepts/equations and uncertain extraction. A citation must support its adjacent claim; a valid-looking badge is not evidence of correctness.

Confirm real source IDs/locators, no unsupported requirements, labeled supplemental explanations, visible unresolved contradictions, and disclosed unreadable material. Do not imply full-course coverage from a partial package.

Check both languages for meaning, terminology, qualifiers, units, negation, and unchanged equations. Pay particular attention to “required” versus “recommended” and AI/collaboration rules. Translation must not strengthen a requirement.

## Artifact checks

Confirm a real, nonempty, UTF-8 HTML file with embedded assets and no unintended runtime dependency. With Python available, run:

```sh
python scripts/validate_html.py path/to/slide2html.html
```

This helper checks basic structure, IDs/anchors, and likely offline asset dependencies. It is not a full HTML/CSS/JS validator, does not execute JavaScript, and cannot establish factual or visual quality. Resolve failures; inspect unusual but intentional markup before assuming a heuristic is definitive.

## Browser and visual checks

When a browser is available, open the saved file directly with networking unavailable or blocked. Verify representative desktop and phone widths (for example 1440px and 390px), and inspect the rendered page. A hosted preview alone does not establish `file://` behavior.

- **Appearance:** strong first-screen hierarchy, course-specific identity, readable bilingual typography, deliberate spacing, no clipping/overlap, empty sections, or generic card wall. Improve visible defects instead of judging appearance from CSS.
- **Interaction:** navigation/anchors, language switching, search in both languages, zero results/reset, filters/disclosures, and any implemented tracking. Check keyboard use, focus, responsive navigation, and combined search/language behavior.
- **Offline/resilience:** no failed required asset requests or uncaught script errors. If persistence exists, check blocked storage does not break the page and session-only progress is disclosed. Core study content remains readable without JavaScript.

Repair observed problems and recheck affected behavior. If browser tooling or direct-file access is unavailable, do feasible static/syntax checks and report visual/runtime or direct-file verification as incomplete. Do not claim tests that were not performed.

## Delivery

Honor a requested filename; otherwise use `slide2html.html` or a sanitized, reliably known course-code prefix. Deliver the file with a brief content/coverage note, unreadable inputs or consequential unresolved issues, and material verification limits. Do not dump HTML in chat when an artifact can be written.

If no input is readable, request an accessible copy rather than producing a fictional guide. If artifact writing is unavailable, explain the restriction and offer complete source as a fallback. Do not generate sidecar JSON, long statistics reports, or additional files unless requested or needed.
