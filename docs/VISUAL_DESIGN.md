# Profile design implementation: Karan Mahalik

This adaptation follows the earlier cleaned-up Bhagabata Brahma GitHub profile: professional navy background, restrained cyan accents, consistent card dimensions, locally stored SVG graphics and **clickable cards**.

## Content hierarchy

1. Linked header and recruiter-facing summary
2. Analytics-first skills
3. Two prominent, independently linked analytics case-study cards
4. Supporting software-development repositories and a distinctly labeled planned AI lab
5. Experience and education with certificate-based role/date precision
6. Credential evidence summary and analytics workflow
7. Portfolio call to action and contact

Original analytical project descriptions, source links and case-study documents are retained. No project datasets, execution code, Vercel deployment or underlying project repositories were edited.

## Layout and accessibility

- Each project SVG is exactly 720 x 226 with two text rows separated from a right icon panel.
- The icon panel is from x=582 to x=692, and the icon local drawing area is offset inward to x=604..668. No text may enter the panel.
- No CSS animation, JavaScript, external SVG dependencies or animated positioning.
- All SVGs contain accessible title/description and are accompanied by alt text in the profile.
- Project cards point to actual GitHub repositories. The planned AI card points to a planning document and clearly states **not implemented**.
- Image descriptions do not substitute for original text; recruiters can use the readable Markdown tables.

## Certificate evidence

The provided GATS internship document validates the title "Trainee Software Engineer" and dates June 1 to September 5, 2025. The original PDF is not automatically uploaded because it exposes a family name, an employee identifier and signature details. The [public evidence summary](../credentials/gats-internship.md) contains the document-supported facts, with all qualifications.

## Maintenance

- Ensure every image and link still resolves before merging edits.
- Do not relabel ideas as finished generative-AI projects.
- Update the role/date claim only if stronger documentation is supplied.
- Keep architecture notes in each project repo, not in the profile README.
- Do not show numerical metrics without source evidence.
- Run `python3 scripts/validate_profile.py` after graphics changes.
