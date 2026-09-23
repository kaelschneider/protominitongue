# Proto-Minitongue Status

This file records current working state only. Git history is the project-development log.

## Active questions

- How is phase selected when separation and benefit coexist, as in “I remove a splinter for your benefit”? Participant-oriented, event-oriented, and class-specific analyses were offered; none was selected.
- Number, applicative, auxiliary, derivational, nominalizer, participle, converb, and inalienable possessive-index exponents are UNSPECIFIED. Exact lexical distributions of root shapes and detailed active–stative verb-class assignments remain UNSPECIFIED.
- Exact pronominal case relics, the lexical set of canonical route/path nouns preserving PERL `-mi`, and noun-specific inherited linker vowels remain UNSPECIFIED; these do not block productive nominal inflection.
- Ordering and disambiguation of original patient versus applied object when both have the same person are UNSPECIFIED. Patient-before-applied-object was a testing convention, not a separately accepted rule.
- Historical derivations of the nominalizer, participle, and converb systems remain to be developed.

## Provisional systems

- The creator's latest direction is that benefit would most likely use positive `i-`. Its exact scope is not settled. Do not implement retained beneficiary case as a general override making a negative transfer construction benefactive.
- Negative transfer indexing an affected person has been tested with “I take bread from you” as the default reading. Do not generalize this to all affected-person constructions without testing.
- Splinter removal was accepted as potentially source- or beneficiary-oriented depending on context. Overt retained case may clarify a relation only where its interpretation is established. Its interaction with the latest positive-phase preference for benefit remains open.

## Known conflicts

The earlier proposed negative-phase benefit reading and the later preference for positive phase for benefit are not yet reconciled for events that combine separation and benefit. The grammar records neither a universal benefactive override nor a universal phase-scope rule.

## Next useful tests

Phonology, morphophonology, the high-level morphological architecture, and the productive case system are now canonical. The case module has passed a morphophonological regression pass, including consonant-final linker repair, weight-sensitive coda shortening, case-family contrasts, GEN stacking, and bimoraic-nucleus saturation before vowel-initial morphology. The next decisive morphology tests are exponent design for number, nominalization, derivation/AUX ordering, applicatives, and inalienable possessive indexing.

| Diagnostic | Established expectation | Remaining dependency |
| --- | --- | --- |
| Dance into/out of/inside a house | Positive/negative/neutral plus INESS `-ti`; no obligatory movement derivation | Root form |
| Put onto/take off/reposition on a platform | Positive/negative/neutral plus SUPER `-ta` with a broad handling root | Root form |
| I cook bread for you | Applied second-person indexing without n; first-person agent suffix; recoverable pronouns omitted | Phase interpretation and applicative exponent |
| I take bread from you | Negative transfer can index you as applied object; bread remains unmarked | Root and applicative exponent |
| I cut bread with a knife | Means applicative indexes knife; bread remains unmarked; redundant instrument case need not be retained | Same-person noun ordering; forms |
| I remove a splinter for you | Source and benefit readings need testing against phase and meaningful case retention | Phase scope and licensed retained-case readings |

These are semantic diagnostics, not fully formed regression corpus entries. `LEXICON.tsv` and `EXAMPLES.tsv` remain empty until canonical word forms and valid interlinear examples exist. The Pre-Proto → Proto phonological system now specifies the required relative ordering and concrete outputs needed to derive canonical forms; absolute ordering of noninteracting historical changes is not asserted.
