# AGENTS.md

## Purpose
This repository is the canonical, human-readable specification of Proto-Minitongue. Keep it compact, coherent, historically motivated, and easy for humans and language models to inspect.

## Branches
Use only:
- `main` — accepted canonical state.
- `experimental` — provisional or exploratory work.

Do not create, rename, or delete branches unless the user explicitly requests it.

## Sources of truth
- `README.md` — concise human orientation.
- `GRAMMAR.md` — current synchronic analysis.
- `LEXICON.tsv` — canonical lexemes and senses.
- `EXAMPLES.tsv` — examples and regression corpus.
- `HISTORY.md` — in-world diachrony: stages, ordered changes, analogy, reanalysis, grammaticalization, contact, and reconstruction.
- `STATUS.md` — current unresolved questions, provisional systems, known conflicts, and next useful tests.
- Git history — project-development history; do not duplicate a changelog elsewhere.

Read only the files and sections relevant to the task. Do not treat chat history as canonical language data.

## Canon
Use `idea → provisional → tested → canon`.

The human creator has final authority. Do not make major structural choices canonical without explicit approval. Routine consequences of established rules may be implemented without asking.

If a fact is genuinely missing, mark it `UNSPECIFIED` or record it in `STATUS.md`; do not invent a rule merely to complete an analysis.

When a proposal conflicts with canon:
1. state the conflict briefly;
2. offer 2–3 coherent reconciliations;
3. recommend one when useful;
4. let the user choose if the result materially changes the language.

Preserve stable IDs. Prefer minimal diffs. Do not reformat unrelated content.

## Decision economy
Minimize creator microdecisions and token use.

Resolve without asking when a choice is mechanically determined, a regular consequence of canon, formatting/metadata, or a reversible implementation detail.

Batch related local choices into one proposal. Escalate only choices that materially affect phonological or grammatical architecture, productive morphology, alignment, major semantic distinctions, typological character, broad diachrony, or established canon.

Prefer, in order:
1. established rule;
2. productive extension;
3. new regular rule;
4. restricted exception;
5. new subsystem.

Do not resolve an `UNSPECIFIED` point unless it blocks the current task or a useful test.

## Change workflow
Before editing, identify the smallest set of affected sources of truth.

For grammar changes, check relevant lexical entries, examples, historical derivations, and status items. For historical changes, verify that modern forms and grammar remain derivable. For lexical changes, verify forms against current phonology, morphology, and diachrony.

Update canonical statements rather than appending duplicate explanations.

Do not add, remove, rename, split, merge, or reorganize project files unless the user explicitly requests a structural change. Do not change TSV columns without explicit approval.

## Testing
Treat `EXAMPLES.tsv` as a regression corpus.

For substantive changes, test:
1. the smallest example demonstrating the rule;
2. interactions with existing rules;
3. several unseen forms or constructions;
4. relevant proto → intermediate → contemporary derivations;
5. connected text when mature enough.

A successful single example does not validate a rule.

Discovery examples may expose missing grammar. Once a rule is accepted, retain representative examples as regression cases. If connected text requires an unanticipated construction, mark it unspecified and design it deliberately rather than patching the translation.

Periodically perform a language health check for internal consistency, diachronic motivation, and productivity. Surface only meaningful problems.

## Data conventions
- UTF-8, Unicode NFC.
- Canonical rule IDs: `G-DOMAIN-NNN`.
- Lexeme IDs: `L-NNNN`; sense IDs: `L-NNNN-SNN`; example IDs: `EX-NNNN`.
- IDs are immutable once published.
- Store bare IPA in TSV fields; use delimiters only in presentation.
- Interlinear examples follow the Leipzig Glossing Rules.
- Keep TSV records one logical line each; avoid embedded tabs/newlines.
- Keep documentation compact and machine-readable where practical.

## Linguistic research
Use external linguistic evidence when it materially improves naturalism or resolves uncertainty.

Use typological databases for orientation and language discovery; consult descriptive grammars, papers, or other primary sources for mechanisms. Distinguish:
- attested parallel;
- plausible extrapolation;
- deliberate invention.

Do not copy a source language wholesale. Adapt mechanisms to Proto-Minitongue's established history and structural tendencies.

## Design priorities
Prefer systems that:
- arise from earlier structure;
- interact with other systems;
- support productive extension;
- reinforce a recognizable structural personality.

Avoid isolated novelty, unnecessary symmetry, feature accumulation, and complexity without functional or historical motivation. Preserve motivated irregularity rather than regularizing solely for elegance.

## Definition of done
A change is complete when affected sources of truth agree, relevant regression examples still work, unseen forms behave predictably, and no unresolved dependency has been silently invented.

Use concise commit messages describing the linguistic or repository change. Git is the development log.
