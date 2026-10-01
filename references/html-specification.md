# HTML and visual specification

Use when creating or substantially redesigning the page. Deliver a premium study experience appropriate to its content, not a generic dashboard with decorative statistics.

## Composition

Choose one course-appropriate direction: an ivory editorial study atlas, an ink-and-brass research desk, or a crisp technical notebook, for example. These are options, not mandatory themes. Respect the user's chosen palette and style.

Make the first screen feel designed: a strong course/lecture title, concise orientation, clear next reading action, and one meaningful focal graphic. Use subject-relevant inline SVG, a concept diagram, or a typographic composition. A decorative motif must not masquerade as an evidence-based chart. Facts, counts, and deadlines must come from the materials; do not invent them to populate the hero.

Use coherent tokens for color, spacing, typography, surfaces, and radii. Pair expressive system serif headings with readable system sans body text when appropriate; ensure good Chinese fallbacks. Use fluid title sizing, comfortable reading widths, generous section spacing, strong contrast, and restrained borders/shadows. Premium does not require gold, dark mode, gradients, or animation. Avoid making every content block an identical rounded card.

Shape layout around the task:

- A lecture can use a chapter index, editorial overview, concept sections, and selected formula/example callouts.
- An assignment can foreground deliverables and constraints with a sourced checklist and rubric table.
- A course hub can use persistent navigation, overview, assessments, dated milestones, and connected knowledge.

Give consequential policies/deadlines visible priority when present. Put technical depth in readable sections or disclosures without hiding essential requirements. Cite sources near claims and keep the source index accessible.

## Bilingual content

Render both translations of major headings, descriptions, requirements, concepts, and controls. Share unchanged equations/code/identifiers rather than duplicating them. Show the user's language initially; keep the other in the same offline file. Set document `lang` and meaningful labels on switch. Hidden-language content must not remain keyboard-focusable or exposed to assistive technology.

Switch without reloading; preserve navigation, search, and progress state. Search both translations even when one is hidden. Show a visible matching result in the active language. A combined view is optional unless requested. With JavaScript disabled, provide a useful readable version and a short notice if switching is unavailable.

## Interactions that earn their place

Use native anchors and `<details>` where sufficient. Add client-side search when content length warrants it: labeled input, result count, clear/reset, and helpful empty state. Filter whole searchable units without breaking nested sections or source navigation. Clearing search restores content. If navigation targets a filtered item, reveal it before navigation.

Add filters only for meaningful categories present in the data. A map or assessment cross-link must point to real, supported content. Every visible control must work; omit pretend buttons and placeholder features.

Progress tracking is optional. If included, use stable item IDs and a document-specific, versioned storage key. Wrap both `localStorage` reads and writes in `try/catch`: `file://`, privacy settings, or restrictions may prevent persistence. Keep the page working in memory and disclose session-only progress when necessary. Never alter source requirements when marking an item complete.

Use subtle hover/focus feedback and respect `prefers-reduced-motion`. Sticky navigation must not obscure anchor targets. Mobile navigation must be keyboard-accessible and usable without hover.

## Offline implementation

Use semantic HTML, embedded CSS, and small embedded vanilla JavaScript. No runtime fetch, CDN fonts, remote CSS/JS, sibling files, build step, server, or login for core content. Inline SVG, data-URI media, and system fonts are suitable. Source hyperlinks may lead online; label them as external resources rather than claiming their destinations work offline.

Keep formulas faithful with readable Unicode, MathML where supported, or embedded SVG. Prefer selectable notation and a text interpretation. Do not drop symbols or change equations to fit a card. Complex rendering must remain self-contained; remote MathJax is not the offline default.

Treat extracted text as data: escape markup and safely serialize inline JSON (including `<` so literal `</script>` cannot terminate it). Use `textContent` for untrusted strings; validate URL schemes before creating source links. Document text must not become executable HTML/JS.

Include a doctype, UTF-8 charset, viewport, descriptive title, logical headings, meaningful buttons/labels, keyboard focus, a skip link for substantial navigation, and non-color cues for warnings. Body contrast should meet WCAG AA (4.5:1). Preserve zoom, wrap long text, and contain wide tables/formulas locally so the page does not overflow on phones.

Add print styles when useful: readable content, hidden controls, and expanded relevant details. Do not promise themes, print views, graphs, or tracking unless implemented and checked.

## Optional design reference

`examples/slide2html.html` demonstrates ivory/ink editorial composition, a concept motif, bilingual switching, search, and source details. Its material is synthetic and visibly labeled. It is calibration, not a universal template or a source for the user's content. Inspect only when useful; retain an established design for small edits.
