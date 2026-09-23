# Proto-Minitongue Grammar

This file is the canonical synchronic specification of Proto-Minitongue. Record accepted rules here; keep unresolved or provisional systems in `STATUS.md` until they are ready for canon.

## Metadata

| Key | Value |
| --- | --- |
| language_name | Proto-Minitongue |
| language_tag | x-minitongue-proto |
| metalanguage | en |
| project_version | 0.1.0 |
| status | draft |

## Design brief

The language has SOV order, active–stative alignment, relational phase prefixes, and two applicatives. Case and verbal indexing jointly express participant relations. Semantic classes organize phase contrasts without forming a closed inventory.

## Conventions

- Canonical rule IDs: `G-DOMAIN-NNN`, with domains `PHON`, `ORTH`, `MORPH`, `SYN`, `SEM`, `PRAG`, `DISC`, `LEX`.
- Lexeme IDs: `L-NNNN`; sense IDs: `L-NNNN-SNN`; example IDs: `EX-NNNN`.
- Store canonical pronunciation/transcription in IPA. TSV IPA fields contain bare IPA without slash or bracket delimiters.
- Interlinear examples follow the Leipzig Glossing Rules.
- Standard Leipzig abbreviations are accepted without duplication below. Add only project-specific abbreviations to the dedicated table.

## Phonology

### Phoneme inventory

**G-PHON-001.** Consonants: /p t k m n h s r j/. Vowels: /a e i u/.

### Allophony

### Phonotactics

**G-PHON-002.** Syllable structure is (C)V(C). Morpheme-boundary realization must respect this structure; repair processes are UNSPECIFIED.

### Prosody

## Morphophonology

**G-PHON-003.** Proto-Minitongue has layered morphophonology: the underlying morphological template remains analytically recoverable, while regular phonological processes may fuse or alter adjacent morphemes at their boundaries. Such surface allomorphy does not create new morphological slots. Exact boundary-repair mappings are UNSPECIFIED.

## Morphology

### Nominal morphology

**G-MORPH-001.** Noun template: `NOUN-NUMBER-CASE`. Number categories are singular, dual, and plural. The dual is used with natural pairs; its extension beyond natural pairs is UNSPECIFIED. Number exponents are UNSPECIFIED. Case belongs on nouns, not in the verb template.

**G-MORPH-002.** Agents and active subjects receive an overt core case; patients and stative subjects are unmarked. Case exponents are UNSPECIFIED. The additional functional inventory is:

| Case function | Scope |
| --- | --- |
| Reference | Endpoint or anchor across compatible semantic classes |
| Location | General location; detailed contrasts remain UNSPECIFIED |
| Recipient/beneficiary | Recipient, gain/loss participant, or beneficiary as licensed by construction and phase |
| Companion | Accompaniment |
| Means/instrument | Means or instrument |
| Possessor | Possession |
| Containment | Physical interior |
| Position | Surface contact or support |

**G-MORPH-003.** The design includes rich nominalizer and participle systems. Converbs have the structure `a-grade nonfinite stem + nominalizer + case`. Individual forms and functions are UNSPECIFIED.

### Verbal morphology

**G-MORPH-004.** Verb template:

`RELATIONAL PHASE-OBJ/PAT-ROOT+GRADE-AUX/DERIV-APPL-AGT/SUBJ-TENSE-ASPECT`

This is morphological notation, not a claim that every slot must be overt or that concatenated representations already satisfy phonotactics. Auxiliary and derivational inventories are UNSPECIFIED.

**G-MORPH-005.** Grades are suffixal stem formatives attached to the lexical root: `-a` nonfinite, `-u` realis, `-i` irrealis, `-e` linking. The inherited root inventory includes monoconsonantal roots, biconsonantal roots, and roots containing lexical vowels, with unequal productivity across these types. Exact root templates and distributions remain UNSPECIFIED.

**G-MORPH-006.** Agent/subject suffixes: `-k` first person, `-t` second person, `-p` third person. Ordinary object/patient prefixes consist of `n-` plus `k/t/p` for first/second/third person. With an applicative, the applied object is indexed by `k/t/p` without `n-`. These distinctions do not establish person-number paradigms beyond person.

**G-MORPH-007.** Tense suffixes: `-i` nonpast, `-a` past. Aspect suffixes: zero imperfective, `-n` perfective.

**G-MORPH-008.** Relational phase prefixes: `i-` positive, `a-` negative, zero neutral. Their interpretation is governed by G-SEM-001–004.

**G-MORPH-009.** The two applicatives are affected-person (including beneficiaries and relevant gain/loss participants) and means (including instruments). Their exponents are UNSPECIFIED. The applicative occupies APPL; it is not a case marker.

## Syntax

**G-SYN-001.** Basic constituent order is SOV. Order between the original patient and an applied object is UNSPECIFIED.

**G-SYN-002.** Alignment is active–stative. The system is fluid where differences in control, active involvement, or affectedness motivate an alternation, while some verbs are lexically fixed to one behavior. Detailed verb-class assignments and alternation restrictions are UNSPECIFIED.

**G-SYN-003.** Adjectives are stative verbs.

**G-SYN-004.** An applicative selects its applied participant for object indexing. The original patient remains unmarked and is not indexed in that slot. An overt applied noun is unmarked when its case would add nothing; it may retain case when case contributes a meaningful distinction. Individual retained-case interpretations must be licensed by the construction, not invented from the intended translation.

## Semantics and pragmatics

**G-SEM-001.** Positive phase tends toward connecting, building, or advancing; negative phase toward separating, reducing, or reversing. Actual oppositions are conventional to semantic classes and roots. Spatial, contact, relational, and alteration classes are examples, not an exhaustive classification. Neutral phase follows a root-specific baseline rather than universally marking either a state or an activity.

**G-SEM-002.** Case and phase interact by construction. Some cases receive interpretation from phase; others retain their relation. Reference extends across compatible semantic classes. Reference and recipient/beneficiary may overlap, with reference emphasizing an endpoint or anchor and recipient/beneficiary emphasizing gain, loss, or benefit. Negative transfer with a reference participant can identify a source and can imply loss; reference alone does not entail ownership or harm.

**G-SEM-003.** Containment and position can express phase-sensitive changes of spatial relation where the whole construction licenses them. A separate movement derivation is not required for a manner verb to express a path. Otherwise spatial case locates the event. Ordinary motion roots favor direction-neutral meanings. Accepted semantic patterns, using English placeholders rather than canonical lexemes, are:

| Construction | Positive | Negative | Neutral |
| --- | --- | --- | --- |
| dance + house-CONTAINMENT | dance into the house | dance out of the house | dance inside the house |
| position/handle + platform-POSITION | put onto the platform | take off the platform | reposition on the platform |

Abstract spatial-case uses develop as conventional extensions, not unrestricted productive metaphor.

**G-SEM-004.** Contact verbs have an engage/withdraw tendency with root-specific contrasts. Alteration supports distinct class patterns of degree increase/decrease, establishing/undoing, and applying/removing. These patterns do not by themselves establish roots or assign their alignment.

## Discourse

**G-DISC-001.** Recoverable indexed pronouns may be omitted. Ordinary applied second-person participants such as “you” in “I cook bread for you” need not appear as overt nouns; the verb indexes them. Agent indexing likewise permits recoverable agent omission. Indexing distinguishes persons, not multiple nouns of the same person.

## Orthography

## Lexicon conventions

### Parts of speech

| Code | Name | Notes |
| --- | --- | --- |

### Project-specific gloss abbreviations

| Abbreviation | Meaning | Notes |
| --- | --- | --- |
