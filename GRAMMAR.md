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

The permitted `CjV` onset means glide formation is not blocked merely because a consonant precedes the input sequence. Vowel-contact processes in this rule apply only when the preceding nucleus is monomoraic. A bimoraic nucleus—whether a diphthong or a contracted heavy monophthong—is saturated: a following vowel-initial morpheme begins a new syllable and remains in hiatus (for example, `pâ-e → pâ.e` and `pai-e → pai.e`).

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

**G-MORPH-001.** Productive nouns share one inflectional architecture: `NOUN-(COLL/PCL)-NUMBER-(INNER CASE)-(OUTER CASE)`. COLL/PCL is an optional stem-forming derivation under G-MORPH-014. Singular is zero, dual is `-e`, and plural is `-u`. Number scopes over the lexical or derived nominal stem before case relations apply. Four productive noun stem classes condition theme realization and limited surface allomorphy within this shared architecture; they are not four separate case paradigms. Case belongs on nouns, not in the verb template.

**G-MORPH-002.** The productive case inventory and ordinary nominal exponents are:

| Case | Exponent | Core scope |
| --- | --- | --- |
| ABS | `Ø` | Patient and stative/inactive S; ordinary nouns are unmarked |
| ERG | `-k` | Transitive A and active/agentive S |
| GEN | `-n` | Alienable possession and broader nominal relation |
| DAT | `-r` | Recipient, beneficiary/maleficiary, experiencer, affected animate participant |
| LOC | `-t` | General location |
| INESS | `-ti` | Interior/containment |
| SUPER | `-ta` | Surface contact/support |
| PERL | `-m`; conservative `-mi` | Route/path, especially motion through or along |
| INS | `-m` | Instrument or means |
| COM | `-ma` | Companion or co-participant association |
| ESS | `-e` | Temporary state, role, life-stage, circumstance, or temporary function/material construal |

Pronouns preserve person-specific ABS stem alternations and several conservative core-case forms; their exact paradigm is UNSPECIFIED. Inalienable possession is productively head-marked by possessor indexing on the possessed noun, with older/high-frequency nouns permitted to preserve irregular indexed stems; the possessive exponents themselves remain UNSPECIFIED.

LOC `-t`, INESS `-ti`, and SUPER `-ta` form a synchronically recognizable `t(V)` family, and PERL/INS `-m`, conservative PERL `-mi`, and COM `-ma` form a recognizable `m(V)` family. Speakers recognize these relationships analogically, but the vowels are not independently productive morphemes. PERL and INS are normally syncretic in `-m`; `-mi` remains productively conservative on pronouns and canonical route/path nouns, whose lexical membership is UNSPECIFIED. With inanimate associates, `-m` favors functional/instrumental association while `-ma` can construe the referent as a companion or co-participant.

Before consonant-only case endings, /i/ is the generalized default theme-linker, historically extended from the ANIMATE class. Thus consonant-final stems normally show forms such as `C-k → Cik` and `C-t → Cit`, but productive class themes may override /i/ in conservative cells under G-MORPH-010–011. Vowel-bearing `-ti -ta -mi -ma -e` attach directly and undergo ordinary phonology; thus a matching stem-final consonant may form a legal heterosyllabic geminate, as in schematic `pat-ti → patti`. High-frequency nouns may preserve additional fused or fossil class-conditioned forms.

Limited case stacking is productive but narrower than the general two-slot architecture suggests. GEN may serve as an inner case before LOC, INESS, SUPER, or PERL when an outer spatial relation compositionally scopes over a possessive or referential GEN relation; abstract relational GEN resists such stacking. DAT and ESS do not stack productively. Arbitrary case chains are ungrammatical. There is no productive Reference case: affected or animate endpoint functions fall to DAT, spatial anchors and routes to the spatial cases, and abstract nominal relations to GEN.

**G-MORPH-003.** The productive nonfinite system is built on the `-a` grade and three semantic nominalizers:

| Function | Exponent | Core interpretation |
| --- | --- | --- |
| EVENT/ACTION | `-n` | event, action, process |
| PARTICIPANT | `-r` | participant in the event; role is construction-dependent |
| RESULT/PLACE | `-t ~ -m` | `-t` for resulting state/place, `-m` for resulting object/means |

The ordinary nominalized-verb template is `PHASE-(OBJ/PAT)-ROOT-a-(DERIV)-(AUX)-(APPL)-NMLZ-NUMBER-(CASE)`. Nonfinites suppress AGT/SUBJ indexing, tense, and finite aspect. Pre-root person indexing may survive only for a distinct internal patient/object or applied object; when a pre-root `r-` or `s-` valency marker is retained in a nonfinite and its associated participant is the nonfinite subject, the person consonant is suppressed with the other subject indexing. Referential event nominalizations normally express their subject as GEN. Productive nonfinite derivatives use the generalized /i/ linker before consonant-only case suffixes and do not enter an inherited noun class unless lexicalized. Event/action nominalizations are normally singular unless construed as countable events.

Participles are attributive extensions of PARTICIPANT `-r`; they do not have separate active/passive morphology. The relativized participant's role follows the active–stative argument structure of the construction. If the relativized participant is the patient/object, its object indexing is suppressed as the participial gap.

Converbs are EVENT `-n` plus exactly one case and do not productively stack further case. The core constructions are EVENT+ESS for simultaneous/circumstantial “while doing,” EVENT+INS for means/manner “by doing,” and EVENT+DAT for purpose “in order to do.” Converbs are normally controlled by a matrix argument; a different overt subject is permitted in ordinary case. Schematic outputs include `ROOT-a-n-e` EVENT+ESS, `ROOT-a-n-i-m` EVENT+INS, and `ROOT-a-n-i-r` EVENT+DAT.

**G-MORPH-010.** The productive noun stem classes are ANIMATE, GROWING, LAND/WATER, and MADE. Their inherited theme profiles are respectively `-i`, `-a`, `-u`, and `Ø/C`. These themes are stem formatives rather than independent case suffixes. Historical apocope and lexical fusion mean that ABS.SG citation forms do not always display the theme overtly. New and productively formed nouns normally follow the semantic centers of the four classes, while inherited vocabulary may preserve older mismatches. A relic SOCIAL stratum survives in limited morphology but is not a fifth productive noun class.

Class meanings are prototypes rather than exhaustive ontologies. ANIMATE contains humans and ordinary animals; GROWING centers on living plants and other growing sources; LAND/WATER centers on landscape, waters, and comparable environmental entities; MADE centers on artifacts, worked objects, and related portable products. Productive class shift is available for culturally salient changes of mode of existence, especially GROWING → extracted material → MADE. Derivational morphology may distinguish extraction/material formation from manufacture even when class morphology indicates the resulting category.

**G-MORPH-011.** Noun-class effects on case are asymmetrical historical pockets within one case system. GROWING preserves transparent `-a-` most strongly before LOC and PERL/INS, yielding productive schematic `ROOT-at` and `ROOT-am`; LAND/WATER preserves `-u-` strongly in the same domain, yielding `ROOT-ut` and `ROOT-um`. LAND/WATER also preserves older `u ~ Ø` alternation and fossil consonantal material in limited lexical/case pockets whose exact distribution is UNSPECIFIED. MADE normally follows the generalized /i/ pattern but older nouns may preserve direct/fused `-m` in PERL/INS. ANIMATE /i/ is largely obscured by its spread as the default linker, though high-frequency nouns retain a small irregular fusion pocket demonstrating its older class status; exact forms are UNSPECIFIED.

Old SOCIAL morphology survives as person-sensitive allomorphy in DAT and COM. It is available to humans and to nonhuman referents construed as socially responsive persons, without changing the referent's lexical noun class. Conventionally person-like rivers, herds, ancestral places, and similar referents may favor these forms even when nonperson construal remains possible. The old SOCIAL marker is reconstructed only schematically as classifier-like `*Ci`; its consonant and the exact modern DAT/COM outputs remain UNSPECIFIED.

**G-MORPH-012.** Dual and plural use the same underlying exponents across noun classes: dual `-e`, plural `-u`. Theme + number interactions are derived by ordinary morphophonology; there are no productive class-specific number allomorphs or true number+case portmanteaux. Surface number syncretism produced by regular phonology is tolerated.

The dual marks a coherent licensed pair rather than mere cardinality. For core natural-pair lexemes, singular denotes one member, dual the coherent pair, and plural three or more members or two unmatched members. Conventional functional or cultural pairings can also license dual; a newly established functional pair may be coerced into dual once discourse treats it as a unit, but accidental physical juxtaposition alone does not suffice. When the two members are separately coordinated, each conjunct normally remains singular rather than redundantly taking dual.

The numeral TWO selects dual when the noun is dual-eligible and the two referents form a licensed pair; otherwise it selects plural. Numerals THREE and above select plural. For nouns without dual eligibility, plural therefore includes two or more. Number on collective nouns counts collectives rather than their members. Mass/substance nouns may pluralize with contextual kind, portion, or bounded-instance readings.

**G-MORPH-013.** A newer attributive classifier system may suffix to attributive stative verbs/adjectives when classification is semantically relevant; neutral descriptions may omit it. Its semantic inventory is richer than the four inherited noun classes and cross-cuts them, with centers including SOCIAL/PERSON, MOBILE-LIVING, GROWING, FLUID/LANDSCAPE, WORKED/MATERIAL, BOUNDED, and COLLECTIVE. A classifier can freely signal a contextual construal different from the noun's inherited lexical class without changing that noun's declension. Some classifiers descend from older class material and others are later innovations; their exact exponents and final inventory are UNSPECIFIED.

**G-MORPH-014.** The productive collective/paucal derivation is `-s` and precedes number: `NOUN-COLL/PCL-NUMBER-CASE`. Its semantic center is a bounded coherent subset: with count nouns it forms a small group or paucal set, with mass/substance nouns a bounded quantity, and with collective nouns a subcollective. The derived stem may itself take singular, dual, or plural; dual eligibility is recalculated for the derived collective rather than inherited from the base noun.

COLL/PCL `-s` blocks the conservative class-theme case pockets of G-MORPH-011. Before consonant-only case endings, a derived `-s` stem therefore uses the generalized `-i-` linker regardless of the base noun class, schematically `ROOT-a-s-i-t` and `ROOT-u-s-i-m`. Vowel-bearing case endings attach directly under the ordinary phonology. Consonant-final bases undergo the ordinary boundary-repair system, so schematic `C-s` surfaces as `Cis` where required by phonotactics.

### Verbal morphology

**G-MORPH-004.** Finite verb template:

`RELATIONAL PHASE-PRE-ROOT PARTICIPANT-ROOT+GRADE-(ITER/INTENS)-(CAUS)-(AUX)-APPL-AGT/SUBJ-TENSE-ASPECT`

This is morphological notation, not a claim that every slot must be overt or that concatenated representations already satisfy phonotactics. PRE-ROOT PARTICIPANT contains the indexing/valency series of G-MORPH-006. Post-root derivation is deliberately small: productive iterative/intensive morphology precedes CAUS, which precedes AUX. Thus CAUS scopes over a modified iterative/intensive base. Only semantically and morphologically compatible combinations occur. Exact ITER/INTENS, CAUS, and AUX exponents remain UNSPECIFIED.

**G-MORPH-005.** Grades are suffixal stem formatives attached to the lexical root: `-a` nonfinite, `-u` realis, `-i` irrealis, `-e` linking. The inherited root inventory includes monoconsonantal roots, biconsonantal roots, and roots containing lexical vowels. These are phonological root shapes, not separate conjugation classes: all use the same morphological architecture, and surface differences arise through phonology and morphophonology. Exact lexical distributions remain UNSPECIFIED.

**G-MORPH-006.** Agent/subject suffixes are `-k` first person, `-t` second person, and `-p` third person. The pre-root participant series combines a relation/valency marker with the same person consonants:

| Series | Form | Function |
| --- | --- | --- |
| ordinary PAT/OBJ | `n-k/t/p-` | indexed patient/object |
| VAL.RED | `r-k/t/p-` | reflexive, middle, or anticausative participant according to verb class |
| RECIP | `s-k/t/p-` | reciprocal participant |
| applied object | `k/t/p-` | applied participant selected by an applicative |

In finite `r-` forms, the person consonant indexes the sole/core affected participant; reflexive clauses may therefore index the same person pre-root as patient and post-root as agent. Reciprocal clauses behave analogously for the reciprocal participants. The inherited reciprocal `s-` is synchronically independent of nominal COLL/PCL `-s`. Verbal indexing encodes person only, never number; nominal or pronominal morphology carries number distinctions.

**G-MORPH-007.** Tense suffixes: `-i` nonpast, `-a` past. Aspect suffixes: zero imperfective, `-n` perfective.

**G-MORPH-008.** Relational phase prefixes: `i-` positive, `a-` negative, zero neutral. Their interpretation is governed by G-SEM-001–004.

**G-MORPH-009.** The two applicatives are affected-person (including beneficiaries and relevant gain/loss participants) and means (including instruments). Their exponents are UNSPECIFIED. Exactly one applicative may occur per verb. The applicative occupies APPL; it is not a case marker; any additional non-core participant must remain case-marked or be expressed by another construction. Because applied-object indexing uses the same pre-root participant position as the `r-` valency-reducing and `s-` reciprocal series, applicatives do not combine with `r-` or `s-` forms.

**G-MORPH-015.** Productive verbal derivation is intentionally compact. A single CAUS derivation increases valency; its exponent is UNSPECIFIED. In a causative of a transitive base, the original patient remains ABS/PAT and the causee is DAT. Iterative/intensive derivation occupies the preceding DERIV position and may combine with finite PERF `-n`, so event-internal iteration/intensity remains distinct from grammatical perfectivity. The exact ITER/INTENS exponent or internal subdivision is UNSPECIFIED.

The pre-root `r-` series is a general valency reducer rather than a literal-reflexive-only marker: verb class and construction determine reflexive, middle, or anticausative interpretation. The `s-` series marks reciprocal valency. When either combines with CAUS, CAUS scopes over the already derived `r-/s-` base: schematically `r-ROOT-CAUS` means “cause [REFL/MID/ANTICAUS ROOT]” and `s-ROOT-CAUS` means “cause [RECIP ROOT].”

## Syntax

**G-SYN-001.** Basic constituent order is SOV. Order between the original patient and an applied object is UNSPECIFIED.

**G-SYN-002.** Alignment is active–stative. The system is fluid where differences in control, active involvement, or affectedness motivate an alternation, while some verbs are lexically fixed to one behavior. The alternation is expressed through argument case and choice of agreement position alone; there is no additional voice or alignment morpheme. Detailed verb-class assignments and alternation restrictions are UNSPECIFIED.

**G-SYN-003.** Adjectives are stative verbs.

**G-SYN-004.** An applicative selects its applied participant for object indexing. The original patient remains unmarked and is not indexed in that slot. An overt applied noun is unmarked when its case would add nothing; it may retain case when case contributes a meaningful distinction. Individual retained-case interpretations must be licensed by the construction, not invented from the intended translation.

## Semantics and pragmatics

**G-SEM-001.** Positive phase tends toward connecting, building, or advancing; negative phase toward separating, reducing, or reversing. Actual oppositions are conventional to semantic classes and roots. Spatial, contact, relational, and alteration classes are examples, not an exhaustive classification. Neutral phase follows a root-specific baseline rather than universally marking either a state or an activity.

**G-SEM-002.** Phase interpretation is construction- and verb-class-conditioned, but several case domains have productive tendencies:

| Case | Neutral phase | Positive `i-` | Negative `a-` |
| --- | --- | --- | --- |
| DAT | neutral involvement/experience | gain, benefit, or orientation toward the affected participant | loss, harm, or orientation away/from the affected participant |
| LOC | location | toward/arrival at for motion and location predicates | away/departure from for motion and location predicates |
| INESS | in/interior | into or establishment of interior relation | out of or removal of interior relation |
| SUPER | on/surface relation | onto or establishment of surface relation | off or removal of surface relation |
| PERL | route/along | enter or continue along a path with directional motion predicates | leave or reverse from a path with directional motion predicates |
| INS | means/instrument | acquisition/use or enabling means, by verb class | relinquishing/removal or obstructive means, by verb class |
| COM | accompaniment | joining or co-participation | separation or withdrawal |
| ESS | be/as a temporary state or role | become/enter the state or role | cease/leave the state or role |

Outside the favored motion/location classes, LOC and PERL allow root-specific phase interpretations rather than mechanically directional ones. DAT experiencer and other stative predicates may conventionalize phase as affect or intensity, or lexicalize another contrast, rather than directly expressing gain versus loss. PERL and INS are normally distinguished by construction and lexical semantics despite their shared `-m` exponent; conservative PERL `-mi` can overtly preserve the path reading.

**G-SEM-003.** INESS and SUPER can express phase-sensitive changes of topological relation, while LOC and PERL interact compositionally with phase in their favored motion/location constructions. A separate movement derivation is not required for a manner verb to express a path. Ordinary motion roots favor direction-neutral lexical meanings, with direction supplied by the construction. Accepted semantic patterns, using English placeholders rather than canonical lexemes, are:

| Construction | Positive | Negative | Neutral |
| --- | --- | --- | --- |
| dance + house-INESS | dance into the house | dance out of the house | dance inside the house |
| position/handle + platform-SUPER | put onto the platform | take off the platform | reposition on the platform |
| move + road-PERL | enter/continue along the road | leave/reverse from the road | move along the road |

Abstract spatial-case uses develop as conventional extensions, not unrestricted productive metaphor.

**G-SEM-004.** Contact verbs have an engage/withdraw tendency with root-specific contrasts. Alteration supports distinct class patterns of degree increase/decrease, establishing/undoing, and applying/removing. These patterns do not by themselves establish roots or assign their alignment.

**G-PRAG-001.** Social personhood is a graded, relational construal rather than a categorical human/nonhuman feature. Humans are ordinarily treated as persons by default. Nonhuman beings may receive stronger person construal through established reciprocity and/or communal ritual recognition. Such beings can be categorized simultaneously by domain (for example animal, water, storm, or place), by relational status (for example familiar, dangerous, obligated, or ancestral), and, where culturally licensed, as a collective person such as a herd, river, or forest. Personhood is distinct from both lexical noun class and grammatical animacy.

**G-PRAG-002.** Grammatical animacy has two values, ANIMATE and INANIMATE. Ordinary animals are ANIMATE. Personhood is not a third animacy value: person-construal can instead license person-sensitive reference and the SOCIAL-derived DAT/COM allomorphy of G-MORPH-011. Some culturally prominent nonhuman referents develop a conventional tendency toward person-like treatment while retaining ordinary nonperson construals.

## Discourse

**G-DISC-001.** Recoverable indexed pronouns may be omitted. Ordinary applied second-person participants such as “you” in “I cook bread for you” need not appear as overt nouns; the verb indexes them. Agent indexing likewise permits recoverable agent omission. Indexing distinguishes persons, not multiple nouns of the same person.

**G-DISC-002.** Third-person reference is construal-sensitive: speakers may refer to the same eligible nonhuman referent in a more person-like or more thing-like way according to the discourse relation being foregrounded. Physical description does not require person-like reference, while reciprocity, intention, obligation, ritual interaction, or ancestry may favor it. The exact pronominal or referential forms realizing this contrast are UNSPECIFIED.

## Orthography

**G-ORTH-001.** Heavy monophthongs created by identical-vowel contraction are written with a circumflex: `aa → â`, `ee → ê`, `ii → î`, `uu → û`. Heavy /e/ created by `ei` is written `ë`, preserving the historical class needed to predict its distinct coda reflex. Diphthongs `ai au` are inherently heavy and take no diacritic. Marginal /o/ from coda-conditioned /au/ shortening is written `o`. These marks encode moraic and morphophonological information; they do not imply phonetic vowel length.

## Lexicon conventions

### Parts of speech

| Code | Name | Notes |
| --- | --- | --- |

### Project-specific gloss abbreviations

| Abbreviation | Meaning | Notes |
| --- | --- | --- |
