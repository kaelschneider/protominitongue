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

**G-PHON-001.** Core consonants are /p t k m n h s r j/. Core vowels are /a e i u/. A marginal derived /o/ occurs as the coda-conditioned reflex of /au/ under G-PHON-010; it is not part of the inherited core vowel system. The core stop series /p t k/ has no productive intervocalic lenition at the Proto-Minitongue stage.

### Allophony

**G-PHON-004.** /n/ undergoes automatic phonetic place assimilation before consonants: [m] before /p m/, [ŋ] before /k/, and [n] elsewhere. These outputs do not by themselves create new phonemes.

### Phonotactics

**G-PHON-002.** The ordinary syllable template is `(C)(j)V(C)`. The second onset position, when present, is /j/; therefore `CjV` onsets are permitted. Codas are /p t k m n s r/; /h j/ are onset-only. A nucleus may be a monophthong or the diphthong /ai au/. Morpheme-boundary realization must ultimately satisfy these restrictions.

**G-PHON-005.** Identical consonants meeting across a morpheme boundary form a heterosyllabic geminate when the first member is a legal coda. Because /h j/ are not legal codas, /hh jj/ simplify to a single onset rather than forming geminates.

### Prosody

**G-PHON-006.** Weight is moraic. An open syllable with an ordinary monophthong is light (1μ). Diphthongs and contracted heavy monophthongs are bimoraic (2μ), and every closed syllable is heavy. Heavy monophthongs are phonologically bimoraic but need not be phonetically long. Superheavy 3μ syllables are not permitted: a bimoraic nucleus before a coda undergoes G-PHON-009 so that the resulting nucleus is 1μ and the coda supplies the second mora.

**G-PHON-007.** Primary stress falls on the rightmost heavy syllable within the final three syllables of the phonological word. If none of those syllables is heavy, stress is penultimate. Prefixes participate normally in the stress domain. There is no stress-neutral affix class; stress is assigned after morphophonological repair, resyllabification, and coda-conditioned shortening.

## Morphophonology

**G-PHON-003.** Proto-Minitongue has layered morphophonology: the underlying morphological template remains analytically recoverable, while regular processes may fuse or alter adjacent morphemes. Such surface allomorphy does not create new morphological slots. The general repair order is assimilation/fusion → resyllabification → restricted deletion → epenthesis, followed by weight-sensitive stress assignment.

**G-PHON-008.** Vowel contact has sequence-specific outcomes:

| Input | Output | Weight/status |
| --- | --- | --- |
| `aa ee ii uu` | /a e i u/ | heavy monophthong, 2μ |
| `ae` | /ai/ | diphthong, 2μ |
| `ai` | /ai/ | diphthong, 2μ |
| `au` | /au/ | diphthong, 2μ |
| `ei` | /e/ | heavy monophthong, 2μ |
| `ia ie iu` | /ja je ju/ | glide formation |
| `ea eu` | /ja ju/ | coalescence |
| `ua` | /u.a/ | hiatus |
| `ui` | /u.i/ | hiatus |
| `ue` | /u.i/ | hiatus with raising of the second vowel |

The permitted `CjV` onset means glide formation is not blocked merely because a consonant precedes the input sequence.

**G-PHON-009.** Coda-conditioned shortening applies after resyllabification and prevents a bimoraic nucleus from combining with a moraic coda. Historical source remains relevant to the output:

| Heavy/open source | Before a coda |
| --- | --- |
| /a/ < `aa` | /aC/ |
| /e/ < `ee` | /eC/ |
| /i/ < `ii` | /iC/ |
| /u/ < `uu` | /uC/ |
| /ai/ < `ae` or `ai` | /eC/ |
| /au/ | /oC/ |
| heavy /e/ < `ei` | /iC/ |

If the following consonant is resyllabified as the onset of a following vowel-initial syllable, the heavy nucleus remains open and does not undergo this shortening.

**G-PHON-010.** At consonant boundaries, natural assimilation or fusion applies first, then legal material is resyllabified. If an illegal structure remains, an onset-only /h/ or /j/ may delete when it cannot be legally resyllabified and is not protected lexical material. Root consonants, person markers, and grade vowels are protected from routine deletion. If protected material would otherwise remain phonotactically illegal, epenthetic /i/ repairs the structure.

## Morphology

### Nominal morphology

**G-MORPH-001.** Productive nouns share one inflectional architecture: `NOUN-NUMBER-(INNER CASE)-(OUTER CASE)`. Singular number is zero; dual and plural are overt, though their exponents are UNSPECIFIED. The dual is restricted to natural or conventional pairs. Number scopes over the lexical noun before case relations apply. Additional declensional classes may arise later through historical differentiation or reanalysis, but none are part of the current productive architecture. Case belongs on nouns, not in the verb template.

**G-MORPH-002.** Agents and active subjects receive an overt core case; patients and stative subjects are unmarked. Case exponents are UNSPECIFIED. Limited case stacking is productive: at most two case layers may occur, and an outer case is licensed only where it compositionally scopes over the relation established by the inner case. Individual stacking patterns must therefore be established construction by construction; arbitrary case chains are not grammatical. The additional functional inventory is:

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

**G-MORPH-003.** The productive nonfinite system contains a small set of semantic nominalizers centered on event/action, participant, and result/place functions, with participial extensions built from this system. A nominalized verb enters ordinary nominal morphology: `ROOT-a-NMLZ-NUMBER-(CASE)`, and may take construction-licensed stacked case like other referential nouns. Event/action nominalizations are normally singular unless construed as countable events. Converbs have the structure `a-grade nonfinite stem + nominalizer + case` and ordinarily take exactly one case; additional case stacking is not productive in the converb construction. Individual nominalizer, participle, and converb exponents remain UNSPECIFIED.

### Verbal morphology

**G-MORPH-004.** Verb template:

`RELATIONAL PHASE-OBJ/PAT-ROOT+GRADE-(DERIV)-(AUX)-APPL-AGT/SUBJ-TENSE-ASPECT`

This is morphological notation, not a claim that every slot must be overt or that concatenated representations already satisfy phonotactics. DERIV and AUX form a small ordered derivational zone: DERIV precedes AUX, either may be absent, and only semantically and morphologically compatible combinations occur. Their inventories and exponents remain UNSPECIFIED.

**G-MORPH-005.** Grades are suffixal stem formatives attached to the lexical root: `-a` nonfinite, `-u` realis, `-i` irrealis, `-e` linking. The inherited root inventory includes monoconsonantal roots, biconsonantal roots, and roots containing lexical vowels. These are phonological root shapes, not separate conjugation classes: all use the same morphological architecture, and surface differences arise through phonology and morphophonology. Exact lexical distributions remain UNSPECIFIED.

**G-MORPH-006.** Agent/subject suffixes: `-k` first person, `-t` second person, `-p` third person. Ordinary object/patient prefixes consist of `n-` plus `k/t/p` for first/second/third person. With an applicative, the applied object is indexed by `k/t/p` without `n-`. Verbal indexing encodes person only, never number; nominal or pronominal morphology carries number distinctions.

**G-MORPH-007.** Tense suffixes: `-i` nonpast, `-a` past. Aspect suffixes: zero imperfective, `-n` perfective.

**G-MORPH-008.** Relational phase prefixes: `i-` positive, `a-` negative, zero neutral. Their interpretation is governed by G-SEM-001–004.

**G-MORPH-009.** The two applicatives are affected-person (including beneficiaries and relevant gain/loss participants) and means (including instruments). Their exponents are UNSPECIFIED. Exactly one applicative may occur per verb. The applicative occupies APPL; it is not a case marker; any additional non-core participant must remain case-marked or be expressed by another construction.

## Syntax

**G-SYN-001.** Basic constituent order is SOV. Order between the original patient and an applied object is UNSPECIFIED.

**G-SYN-002.** Alignment is active–stative. The system is fluid where differences in control, active involvement, or affectedness motivate an alternation, while some verbs are lexically fixed to one behavior. The alternation is expressed through argument case and choice of agreement position alone; there is no additional voice or alignment morpheme. Detailed verb-class assignments and alternation restrictions are UNSPECIFIED.

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

**G-ORTH-001.** Heavy monophthongs created by identical-vowel contraction are written with a circumflex: `aa → â`, `ee → ê`, `ii → î`, `uu → û`. Heavy /e/ created by `ei` is written `ë`, preserving the historical class needed to predict its distinct coda reflex. Diphthongs `ai au` are inherently heavy and take no diacritic. Marginal /o/ from coda-conditioned /au/ shortening is written `o`. These marks encode moraic and morphophonological information; they do not imply phonetic vowel length.

## Lexicon conventions

### Parts of speech

| Code | Name | Notes |
| --- | --- | --- |

### Project-specific gloss abbreviations

| Abbreviation | Meaning | Notes |
| --- | --- | --- |
