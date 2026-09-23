# Proto-Minitongue Status

This file records current working state only. Git history is the project-development log.

## Active questions

- How is phase selected when separation and benefit coexist, as in “I remove a splinter for your benefit”? Participant-oriented, event-oriented, and class-specific analyses were offered; none was selected.
- Case, number, applicative, auxiliary, and derivational exponents are UNSPECIFIED. Exact root templates and distributions, the extension of dual beyond natural pairs, and detailed active–stative verb-class assignments remain UNSPECIFIED.
- Exact phonotactic realization at morpheme boundaries is UNSPECIFIED. The architecture now favors historically motivated assimilation/fusion and sequence-specific vowel-contact outcomes, but the concrete mappings are not selected. In particular, `n + person + consonant-initial root` can violate (C)V(C).
- Ordering and disambiguation of original patient versus applied object when both have the same person are UNSPECIFIED. Patient-before-applied-object was a testing convention, not a separately accepted rule.
- Nominalizer, participle, and converb inventories and their historical derivations remain to be developed.
- The ordered Pre-Proto → Proto sound laws remain to be specified. Current canon establishes only the historical architecture: partial simplification of older clusters/hiatus, consonantal assimilation/fusion at morpheme boundaries, mixed sequence-specific vowel-contact outcomes, and substantial sound change across morpheme boundaries.

## Provisional systems

- The creator's latest direction is that benefit would most likely use positive `i-`. Its exact scope is not settled. Do not implement retained beneficiary case as a general override making a negative transfer construction benefactive.
- Negative transfer indexing an affected person has been tested with “I take bread from you” as the default reading. Do not generalize this to all affected-person constructions without testing.
- Splinter removal was accepted as potentially source- or beneficiary-oriented depending on context. Overt retained case may clarify a relation only where its interpretation is established. Its interaction with the latest positive-phase preference for benefit remains open.

## Known conflicts

The earlier proposed negative-phase benefit reading and the later preference for positive phase for benefit are not yet reconciled for events that combine separation and benefit. The grammar records neither a universal benefactive override nor a universal phase-scope rule.

## Next useful tests

Use a small coherent lexicon and actual sentences once forms are available. Do not reopen accepted architecture to resolve routine implementation details.

| Diagnostic | Established expectation | Remaining dependency |
| --- | --- | --- |
| Dance into/out of/inside a house | Positive/negative/neutral plus containment; no obligatory movement derivation | Root and case forms; phonotactics |
| Put onto/take off/reposition on a platform | Positive/negative/neutral plus position with a broad handling root | Root and case forms; phonotactics |
| I cook bread for you | Applied second-person indexing without n; first-person agent suffix; recoverable pronouns omitted | Phase interpretation and applicative exponent |
| I take bread from you | Negative transfer can index you as applied object; bread remains unmarked | Root and applicative exponent |
| I cut bread with a knife | Means applicative indexes knife; bread remains unmarked; redundant instrument case need not be retained | Same-person noun ordering; forms |
| I remove a splinter for you | Source and benefit readings need testing against phase and meaningful case retention | Phase scope and licensed retained-case readings |

These are semantic diagnostics, not fully formed regression corpus entries. `LEXICON.tsv` and `EXAMPLES.tsv` remain empty until canonical word forms and valid interlinear examples exist. A Pre-Proto → Proto historical framework is established, but no concrete word-level derivation is yet canonical.
