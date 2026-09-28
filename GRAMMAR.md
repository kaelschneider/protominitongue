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

The language has SOV order and lexical-class-constrained active–stative alignment. Its predicate is layered into REL, VOICE, U agreement, lexical stem formation and grade, INST, VAL/APPL, AUX, A agreement, tense, and viewpoint aspect. PO syntax and U agreement are related but explicitly non-identical.

## Conventions

- Canonical rule IDs: `G-DOMAIN-NNN`, with domains `PHON`, `ORTH`, `MORPH`, `SYN`, `SEM`, `PRAG`, `DISC`, `LEX`.
- Lexeme IDs: `L-NNNN`; sense IDs: `L-NNNN-SNN`; example IDs: `EX-NNNN`.
- Store canonical pronunciation/transcription in IPA. TSV IPA fields contain bare IPA without slash or bracket delimiters.
- Interlinear examples follow the Leipzig Glossing Rules.
- Ordinary orthography never marks morpheme boundaries. Pedagogical materials may additionally show a segmented analysis such as `n-p-h-u-p-i` beside the ordinary form `niphupi`; segmentation is explanatory, not a second spelling system.
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

**G-PHON-007.** Primary stress falls on the rightmost heavy syllable within the final three syllables of the phonological word. If none of those syllables is heavy, stress is penultimate. Prefixes participate normally in the stress domain. There is no stress-neutral affix class. For G-PHON-011, a pre-syncope application of this prosodic pattern identifies protected stressed vowels; after syncope, repair, resyllabification, and coda-conditioned shortening, stress is recalculated on the resulting surface word.

## Morphophonology

**G-PHON-003.** Proto-Minitongue has layered morphophonology: the underlying morphological template remains analytically recoverable, while regular processes may fuse or alter adjacent morphemes. Such surface allomorphy does not create new morphological slots. The general repair cycle is assimilation/fusion → resyllabification → pre-syncope prosodic evaluation → G-PHON-011 syncope/reduction → any newly fed assimilation/fusion and resyllabification → restricted deletion → epenthesis → coda-conditioned shortening → final weight-sensitive stress assignment.

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

**G-PHON-010.** At consonant boundaries, natural assimilation or fusion applies first, then legal material is resyllabified. INST `-h` has productive strengthening before ordinary consonants: `hp ht hk hm hn hs hr → pp tt kk mm nn ss rr`. Elsewhere onset-only /h j/ may delete only when unprotected and not legally resyllabifiable. Root consonants, person markers, grade vowels, and productive VOICE/INST/ASPECT exponents are protected. Protected word-final INST `-h` and IPFV `-j` therefore receive epenthetic /i/; protected MID `j-` likewise triggers the minimum /i/-epenthesis needed to preserve MID plus following U morphology. Remaining protected illegal material is repaired by /i/-epenthesis. In multi-consonant chains repair proceeds from the rightmost problematic boundary leftward.

**G-PHON-011.** Medial high-vowel syncope is a historical reduction pattern with a narrow productive residue. Synchronically, productive deletion is restricted to unstressed epenthetic /i/ and the generalized nominal linker /i/. Root vowels, stored noun-class themes (including themes hidden by ABS.SG apocope), grade vowels, agreement/TAM material, and the vowels of productive grammatical exponents are protected. Older reductions of other /i u/ and of /a e/ survive only in stored lexical or formulaic forms.

Eligible /i/ is tested right-to-left. Each successful deletion is followed by ordinary assimilation/fusion and resyllabification before the next candidate is considered. Deletion applies only if the whole output can be exhaustively syllabified under G-PHON-002: ordinary medial clusters must parse as legal coda + legal onset, and a three-consonant sequence is permitted only as `C.Cj` where the final `Cj` is independently licensed. Thus repair-vowel reduction still licenses forms such as `nipitiruki → niptiruki` and `nipisjupi → nipsjupi`, but blocks `panit → *pant`, `panasit → *panast`, `nipitiruki → *niptruki`, and `nipikinui → *nipknui`. A newly created closed syllable does not itself halt the current scan; after reduction and repair, G-PHON-007 is reapplied. Productive syncope is written in ordinary orthography.

## Morphology

### Nominal morphology

**G-MORPH-001.** Productive nouns share one inflectional architecture: `NOUN-(COLL/PCL)-NUMBER-(POSS)-(INNER CASE)-(OUTER CASE)`. COLL/PCL is an optional stem-forming derivation under G-MORPH-014; POSS is the inalienable possessive-index slot of G-MORPH-016. Singular is zero, dual is `-e`, and plural is `-u`. Number scopes over the lexical or derived nominal stem before possessive indexing and case relations apply. Four productive noun stem classes condition lexical stem-theme realization within this shared architecture; they are not four separate case paradigms. Case belongs on nouns, not in the verb template.

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
| PERL | `-mi` | Route/path through or along |
| INS | `-m` | Instrument, means, or enabling medium |
| COM | `-ma` | Companion or co-participant association |
| ESS | `-e` | Temporary state, role, life-stage, circumstance, or temporary function/material construal |

Pronouns preserve person-specific ABS stems and conservative core-case relics under G-MORPH-016. Inalienable possession is productively head-marked by possessor indexing on the possessed noun under G-MORPH-016; alienable possession uses GEN.

LOC `-t`, INESS `-ti`, and SUPER `-ta` form a synchronically recognizable `t(V)` family. INS `-m`, PERL `-mi`, and COM `-ma` form a recognizable `m(V)` family. The endings are synchronically indivisible: `-mi` is the productive PERL on ordinary nouns as well as pronouns, while `-m` is INS. Vowel-bearing `-ti -ta -mi -ma -e` attach directly to the stem and undergo ordinary phonology.

Stored noun-class themes are part of the lexical stem rather than case allomorphs. A theme visible in the lexical stem remains before case, and a theme hidden by ABS.SG apocope resurfaces under suffixation. A truly theme-less consonant-final stem uses generalized linker `-i-` before consonant-only case endings when required by the productive paradigm: thus apocopated ANIMATE `nar < *nar-i` gives `nar-i-k`, apocopated LAND/WATER `mur < *mur-u` gives `mur-u-t`, while theme-less MADE `pan` gives `pan-i-t`. High-frequency lexical fossils may preserve individually listed fused forms, notably boat `ram` INS.

Limited case stacking remains productive but narrower than the general two-slot architecture suggests. GEN may serve as an inner case before LOC, INESS, SUPER, or PERL when an outer spatial relation compositionally scopes over a possessive or referential GEN relation; abstract relational GEN resists such stacking. DAT and ESS do not stack productively. Arbitrary case chains are ungrammatical. There is no productive Reference case: affected or animate endpoint functions fall to DAT, spatial anchors and routes to the spatial cases, and abstract nominal relations to GEN.

**G-MORPH-003.** Productive predicate nominalization is built on NONFINITE `-a` and has three independently sourced domains:

| Domain | Exponent | Core interpretation | Verbal retention |
| --- | --- | --- | --- |
| STATE | `-k` | state, result, circumstance | strongly noun-like; agreement/TAM normally suppressed |
| EVENT | `-n` | event, action, process | intermediate; limited A/U may survive, but finite tense/aspect normally does not |
| FACT | `-p` | proposition, fact | most clause-like; agreement normally survives, tense usually survives, aspect survives when contrastive or constructionally required |

REL remains inside the nominalized predicate. Old PARTICIPANT `-r` and RESULT/PLACE `-t ~ -m` are lexical or fossil morphology, not productive nominalizers.

Productive converbs are conventional EVENT+CASE constructions: EVENT+ESS is simultaneous/circumstantial, EVENT+INS means/manner, and EVENT+DAT purpose. Converbs take one outer case. There is no productive ABL case; source/separation meanings use REL plus existing case, another relational construction, or lexicalized/fused morphology. Attributive and relative predicates use DEP under G-SYN-006.
**G-MORPH-010.** The productive noun stem classes are ANIMATE, GROWING, LAND/WATER, and MADE. Their inherited theme profiles are respectively `-i`, `-a`, `-u`, and `Ø/C`. Themes are lexical stem formatives, not case suffixes. Historical ABS.SG apocope may hide a stored theme in the citation form, but suffixation reveals that same stored theme; case does not independently choose or resurrect a class vowel. Theme-less MADE stems instead use the generalized linker required by G-MORPH-002. New and productively formed nouns normally follow the semantic centers of the four classes, while inherited vocabulary may preserve older mismatches. A relic SOCIAL stratum survives in limited morphology but is not a fifth productive noun class.

Class meanings are prototypes rather than exhaustive ontologies. ANIMATE contains humans and ordinary animals; GROWING centers on living plants and other growing sources; LAND/WATER centers on landscape, waters, and comparable environmental entities; MADE centers on artifacts, worked objects, and related portable products. Productive class shift is available for culturally salient changes of mode of existence, especially GROWING → extracted material → MADE. Derivational morphology may distinguish extraction/material formation from manufacture even when class morphology indicates the resulting category.

Canonical lexical contrasts demonstrate that class follows mode of existence and construal rather than dictionary identity: GROWING `pana` “tree” contrasts with MADE `pan` “wood/timber”; LAND/WATER `kasu` “wild/natural fire” with MADE `kas` “hearth/controlled fire”; and GROWING `tana` “forest vegetation” with LAND/WATER `tanu` “forest tract/woodland territory.” Living body parts are ANIMATE. Detached anatomy may remain ANIMATE, while material worked from body substances such as bone, antler, or hide may shift to MADE.

**G-MORPH-011.** Noun-class effects in ordinary case forms are consequences of stored stem themes, not productive case-conditioned theme alternations. Overt-theme stems retain their theme before case (`pana-t → panat`, `ratu-mi → ratumi`); apocopated stems reveal their stored theme under suffixation (`mur < *mur-u → murut`, `nar < *nar-i → narik`); truly theme-less stems use the generalized linker where G-MORPH-002 requires it (`pan → panit`). Forms such as `tanun`, `karun`, `narje`, and `pirje` are therefore regular consequences of stored theme plus ordinary phonology, not separate case residues.

The remaining nominal irregularities are genuinely lexical. MADE `ram` “boat” preserves fossil INS `ram` from an older fused instrumental, while productive PERL is regular `rammi`. Other high-frequency lexical fusions may be listed individually but do not create productive case subclasses.

Old SOCIAL morphology survives as person-sensitive allomorphy in DAT and COM. The old SOCIAL marker is `*ri`, historically related to independent PERSON `ri`. Modern SOCIAL DAT is `-rir` and SOCIAL COM is `-rima`; these case allomorphs suppress the ordinary theme/linker in their cell. They are available to humans by default. For nonhuman referents they require an overtly established PERSON construal under G-PRAG-001/G-DISC-002; lexical noun class does not change. Possessive indexing blocks these SOCIAL case allomorphs under G-MORPH-016.

**G-MORPH-012.** Dual and plural use the same underlying exponents across noun classes: dual `-e`, plural `-u`. Theme + number interactions are derived by ordinary morphophonology; there are no productive class-specific number allomorphs or true number+case portmanteaux. Surface number syncretism produced by regular phonology is tolerated.

The dual marks a coherent licensed pair rather than mere cardinality. For core natural-pair lexemes, singular denotes one member, dual the coherent pair, and plural three or more members or two unmatched members. Conventional functional or cultural pairings can also license dual; a newly established functional pair may be coerced into dual once discourse treats it as a unit, but accidental physical juxtaposition alone does not suffice. When the two members are separately coordinated, each conjunct normally remains singular rather than redundantly taking dual.

The numeral TWO selects dual when the noun is dual-eligible and the two referents form a licensed pair; otherwise it selects plural. Numerals THREE and above select plural. For nouns without dual eligibility, plural therefore includes two or more. Number on collective nouns counts collectives rather than their members. Mass/substance nouns may pluralize with contextual kind, portion, or bounded-instance readings.

**G-MORPH-013.** The attributive classifier system suffixes to DEP stative verbs/adjectives when classification is semantically relevant; neutral descriptions may omit it. The seven productive classifiers are PERSON `-ri`, MOBILE-LIVING `-i`, GROWING `-a`, FLUID/LANDSCAPE `-u`, WORKED/MATERIAL `-t`, BOUNDED `-k`, and COLLECTIVE `-s`. The system cross-cuts inherited noun class: a classifier may signal a contextual construal different from the head noun's declensional class without changing that noun's inflection. PERSON, the three class-vowel classifiers, and COLLECTIVE continue older material; WORKED/MATERIAL and BOUNDED are later innovations. Ordinary vowel contact applies after DEP, including `e+i > ë`, `e+a > ja`, and `e+u > ju`.

**G-MORPH-014.** The productive collective/paucal derivation is `-s` and precedes number: `NOUN-COLL/PCL-NUMBER-CASE`. Its semantic center is a bounded coherent subset: with count nouns it forms a small group or paucal set, with mass/substance nouns a bounded quantity, and with collective nouns a subcollective. The derived stem may itself take singular, dual, or plural; dual eligibility is recalculated for the derived collective rather than inherited from the base noun.

COLL/PCL `-s` creates the outer derived stem for case inflection. Before consonant-only case endings, a derived `-s` stem therefore uses the generalized `-i-` linker regardless of the base noun class, schematically `ROOT-a-s-i-t` and `ROOT-u-s-i-m`. Vowel-bearing case endings attach directly under the ordinary phonology. Consonant-final bases undergo the ordinary boundary-repair system, so schematic `C-s` surfaces as `Cis` where required by phonotactics.

**G-MORPH-020.** The productive partitive is `WHOLE-GEN + sa`. `sa` is a light nominal PART head historically related to the bounded GROUP/PORTION source of COLL/PCL `-s`, but it is synchronically a separate word. The GEN phrase identifies the whole and `sa` denotes an unspecified bounded portion or subset. When the partitive phrase itself bears case, the outer case is realized on `sa`; the whole remains GEN.

### Verbal morphology

**G-MORPH-004.** Abstract predicate template:

`NEG | REL–VOICE–U–[ROOT–LEX.DERIV¹⁻²]⟨GRADE⟩–INST–VAL/APPL¹⁻²–AUX¹⁻²–A–TENSE–ASPECT`

Morphological position, morphosyntactic selection, and semantic scope are distinct. Maximal forms are licensed only when every combination is lexically and semantically compatible. One layer is ordinary in each recursive domain; at most two LEX.DERIV, VAL/APPL, or AUX operators are productive. VOICE is normally singular. Denser apparent stacks favor lexicalization or restructuring.

**G-MORPH-005.** Grades are NONFINITE `-a`, REAL/INDEPENDENT `-u`, IRREALIS `-i`, and DEPENDENT `-e`. REAL marks ordinary independent assertion; IRREALIS marks projected/nonactual status; DEP serves attributive, relative, adverbial, secondary-predicate, and young complex-predicate constructions; NF supplies nominalization and converb bases. Young AUX take DEP `-e`; older bound AUX lose independent grading.

**G-MORPH-006.** Agreement has two person-only series. A-series is post-AUX: 1 `-k`, 2 `-t`, 3 `-p`. U-series is pre-root: 1 `n-k-`, 2 `n-t-`, 3 `n-p-`. A indexes Actor/event-source; U indexes Undergoer/event-locus or another selected U-controller. Only one U marker surfaces. PO and U-controller are distinct: argument structure and valency first establish PO eligibility, then local person can override U control without changing PO. First/second persons outrank third person for U control; when 1 and 2 compete, PO breaks the tie. When a local non-PO overrides a third-person PO for U control, that local participant normally remains overt and bears its independently licensed case; U indexing alone does not recover its grammatical relation.

**G-MORPH-007.** Tense remains NONPAST `-i` and PAST `-a`. Independent finite predicates obligatorily contrast them; DEP normally lacks tense except in licensed finite-dependent constructions. Outer aspect is `Ø` neutral, PFV `-n`, IPFV `-j`, HAB `-r`. HAB normally contrasts with rather than stacks with PFV/IPFV. IPFV descends from CONTINUE; protected final `-j` surfaces with epenthetic /i/. HAB descends from LIVE/STAY; a fuller semi-productive LIVE/STAY customary/durative construction survives outside the core AUX inventory.

**G-MORPH-008.** REL is INCREASE `i-`, MAINTAIN `Ø`, DECREASE `a-`. INCREASE marks convergence, entry, strengthening, or increasing relation; DECREASE marks divergence, exit, weakening, or decreasing relation; zero marks maintenance or lexical baseline. REL modifies the resulting voiced predicate and is construction- and lexical-class-conditioned.

**G-MORPH-009.** Three productive applicatives occupy VAL/APPL:

| Applicative | Exponent | Semantic center |
| --- | --- | --- |
| AFFECTED | `-r` | beneficiary/maleficiary, affected possessor/container/surface, affected participant |
| ORIENTEE | `-p` | addressee, recipient, perceptual target, social counterpart, comparison standard |
| GROUND | `-m` | location, path, medium, instrument |

AFF and GRD continue relational material also reflected in nominal DAT `-r` and INS/PERL `-m`; ORI `-p` grammaticalized from a TURN/FACE counterpart construction. CASE expresses participant relation; APPL integrates a participant into core event structure, so meaningful case may remain visible. An applied argument normally outranks an unapplied theme for PO. With two applicatives, the inner applicative applies first and the outer applicative scopes over the resulting event; the outer applicative supplies PO. This outer-PO rule is productive and has no constructional exception. Local-person U override applies only after that PO has been established under G-MORPH-006.

**G-MORPH-015.** Lexical derivation precedes grade. PLACT/INT `-s` gives event-internal plurality/distribution with events and intensive lexical predicates with appropriate statives. LEX.CAUS `-m` descends from MAKE/SHAPE. Derived stems receive their own alignment properties; LEX.CAUS has only a default transitive bias. Productive syntactic CAUS is post-grade `-t`: the causer controls A by default, the highest remaining non-A is default PO, and the causee is DAT unless separately promoted. Thus pre-grade LEX.CAUS `-m` and post-grade VAL.CAUS `-t` remain distinct.

Within lexical derivation, `ROOT-s-m` (PLACT/INT → LEX.CAUS) is productively compositional when semantics permit: the causative scopes over the pluralized/intensified predicate. Reverse `ROOT-m-s` is not a productive scope reversal and survives only in lexicalized stems. The canonical residue is `r-m-s` < MOVE-LEX.CAUS-PLACT, lexicalized as `rimisa` “herd; drive a mobile group about”; it is a stored stem, not a template licensing new `ROOT-m-s` formations. Voice and applicative morphology are otherwise compositionally available whenever their participant structures remain coherent; individual lexemes may record blocking or narrower lexical licensing.

**G-MORPH-017.** VOICE is REFL `r-`, MID `j-`, RECP `s-`, ANTIP `ma-`. REFL identifies Actor and Undergoer and yields one S, which takes one agreement series by ordinary alignment. MID suppresses external-Actor construal or presents internal arising; CUT/SPLIT and BURN/COOK anticausatives use MID plus U. RECP distributes reciprocal relations across a plural/set participant. ANTIP demotes the current PO; COM `-ma` is the default demotion case, and PO is recomputed from remaining eligible arguments.

**G-MORPH-018.** INST `-h` follows grade and marks a salient particular manifestation/token of a property or event. It is not perfective, punctual, telic, completive, realis, past, nominalization, or an alignment selector. Before ordinary consonants it fuses by strengthening under G-PHON-010; otherwise protected `-h` survives through ordinary epenthesis. FACT normally restricts INST.

**G-MORPH-019.** Core AUX are BEGIN, CONTINUE, FINISH, ABLE, INTEND, NECESSARY. The phase AUX are the older bound forms BEGIN `-ke`, CONTINUE `-je`, and FINISH `-te`; they have lost independent grading. The younger modal AUX retain DEP forms of lexical predicates: ABLE `sine` < KNOW/REMEMBER, INTEND `re` < MOVE/GO, and NECESSARY `sene` < GOOD/FIT. CONTINUE `-je` is also the source of IPFV `-j`.

Zero or one AUX is ordinary. Two-AUX words remain structurally productive, but are favored when the relative scope of both operators is discourse-relevant; otherwise speakers normally use one AUX plus an ordinary lexical or paraphrastic clause. No special restructuring construction is obligatory. Within a two-AUX word, the AUX closest to the lexical predicate has narrowest scope. The default inner-to-outer class order is PHASE – ABLE – INTEND – NECESSARY. Two scope pairs may productively reverse when both readings are semantically coherent: BEGIN↔ABLE and CONTINUE↔INTEND. Thus `V-BEGIN-ABLE` means ABLE(BEGIN(V)), while `V-ABLE-BEGIN` means BEGIN(ABLE(V)); the CONTINUE/INTEND pair behaves in parallel. Other inverse scopes require a less-bound construction.

Narrow AUX negation uses a less-bound construction such as `ABLE [NEG V]`; propositional NEG precedes the whole finite predicate. LIVE/STAY remains semi-productive outside the core AUX inventory beside descendant HAB `-r`.

**G-MORPH-016.** Independent pronouns preserve a conservative person/number subsystem. Strong ABS forms are:

| Person | SG | DU | PL |
| --- | --- | --- | --- |
| 1 inclusive | — | `mai` | `mâ` |
| 1 exclusive | `na` | `nai` | `nâ` |
| 2 | `si` | `sî` | `sja` |
| 3 PERSON | `ri` | `rî` | `rja` |
| 3 THING | `a` | `ai` | `â` |

The 1P inclusive stem descends from older comitative material, while the exclusive series continues the ordinary 1P stem. The 2P and both 3P series preserve old pronominal DU `-i` and PL `-a`; ordinary morphophonology produces the surface forms above. PERSON 3P `ri` is an old SOCIAL pronoun, whereas THING 3P `a` descends from a distal demonstrative. The PERSON/THING contrast is available only in independent reference: verbal indexing and possessive indexing have a single 3P value.

Core pronominal cases preserve relic endings ERG `-ik`, GEN `-un`, and DAT `-ar`; other cases use the productive nominal case system, with conservative PERL `-mi`. Ordinary phonology applies to all combinations and may create syncretism, including 2SG~2PL and 3.PERSON.SG~PL in DAT. Pronouns do not take the separate SOCIAL DAT/COM noun allomorphy of G-MORPH-011.

Inalienable possession is head-marked in the slot `NOUN-(COLL/PCL)-NUMBER-POSS-CASE` by 1P `-i`, 2P `-a`, and 3P `-u`. Possessive indexing marks person only, never possessor number, and the ancient possessive series is historically independent of both modern pronouns and verbal `k/t/p` indexing. Possession is suffixing. POSS blocks inherited noun-class case pockets and SOCIAL DAT/COM allomorphy; subsequent case inflection is uniform. Regular vowel contact and coda shortening may therefore create possessive-number syncretism, including SG~DU with 1POSS and SG~PL with 3POSS before some consonant-only cases. Alienable possession uses a GEN possessor instead. An overt possessor may accompany an indexed inalienable noun; GEN on such a co-occurring possessor is marked/emphatic rather than required.

## Syntax

**G-SYN-001.** Basic constituent order is SOV. PO tends toward the immediately preverbal object position. A discourse topic is normally clause-initial, while contrastive focus occupies the immediately pre-predicate field and may displace the ordinary PO preference. With genuine BNI, the incorporated noun remains obligatorily adjacent to the verb, so a separate focused constituent precedes the whole `[BNI V]` unit rather than intervening inside it.

**G-SYN-002.** Alignment is active–stative/semantic alignment constrained by lexical class. In ordinary finite intransitives, nominal S case and verbal controller covary: active/controlled S takes ERG and controls A, while inactive/affected/stative S takes ABS and controls U. Transitive A remains ERG+A.

Only MOVE and BREATHE/EMIT are productively fluid-S: controlled/volitional uses are active-biased ERG+A, while spontaneous motion/emission, weather motion, and the transformed subject of the ESS + INCREASE MOVE construction are ABS+U. Other predicates with more than one alignment pattern use lexically listed sense defaults rather than free contextual fluidity. STAND is A-aligned for deliberately assuming/maintaining a standing role and U-aligned for inactive posture/state. KNOW/REMEMBER is U-aligned for possessed knowledge or memory and A-aligned specifically for deliberate recall/attention. HEAR/LISTEN/HEED, SMELL, TOUCH/FEEL, and BEAT/PULSE likewise follow their lexically listed intentional versus nonintentional sense defaults. SLEEP and LIVE/GROW remain strongly U/stative-biased; BIG/MUCH, GOOD/FIT, and COLD are fixed U/stative. The bootstrap transitives remain transitive by default. CUT/SPLIT and BURN/COOK productively license MID anticausatives; JOIN/GATHER and HANDLE/TRANSFER license MID and/or REFL readings according to lexical semantics.

**G-SYN-003.** Adjectival meanings are stative verbs.

**G-SYN-004.** PO is the syntactically privileged non-A argument; U-controller is the participant realized by U agreement. Determine them in this order: establish core arguments; select constructional PO; apply valency/applicative changes; apply local-person U override; realize one U marker. Applicativization makes its participant PO-eligible. ANTIP demotes current PO and recomputes PO. A local non-PO may therefore control U without becoming PO.

**G-SYN-005.** Productive BNI is syntactic/pseudo-incorporation: the noun remains phonologically separate but is obligatorily immediately preverbal, low-referential, backgrounded/noncontrastive, theme-like, and non-PO. Bare noun alone does not diagnose BNI. Genuine BNI cannot control U; indexing requires de-incorporation or promotion. An applied PO precedes the BNI constituent, giving the schematic order `... APPLIED.PO [BNI V]`. Topic status, contrastive focus, U-indexing, or the need to establish a robust continuing discourse referent normally forces de-incorporation. ANTIP strongly favors later BNI of its demoted theme but neither requires the other. A recurrent pathway is `P-COM ANTIP-V → P ANTIP-V → [P V] → lexical complex predicate`.

**G-SYN-006.** Attributive/relative predicates use DEP `-e`. Accessibility is A/S → PO → non-PO core O → oblique. A/S and PO are freely relativizable. When a relativized PO is the U-controller, U indexing of that head is obligatory; if some other participant controls U under G-MORPH-006, the relative retains that controller instead. Non-PO core objects may relativize directly with a gap but do not acquire U indexing merely by being the relative head. Obliques normally require APPL or another relational strategy. Genuine BNI resists direct relativization and normally de-incorporates/reanalyzes first. There is no productive resumptive-pronoun or switch-reference subsystem: ordinary agreement, gaps, and discourse continuity track recoverable reference, with an overt NP or PERSON/THING pronoun used when ambiguity would otherwise result.

**G-SYN-007.** Productive NEG is the independent preverbal particle `an` with default propositional scope. It immediately precedes the predicate complex it negates. Narrow/focused negation uses a less-bound construction, especially with AUX: `ABLE [an V]` contrasts with `an [V-ABLE]`. Any old clause-final negator is restricted/archaic/lexicalized rather than a duplicate productive negator.

**G-SYN-008.** Connected syntax is converb-heavy and matrix-final. EVENT+ESS supplies simultaneous or background clauses, EVENT+INS manner/means, and EVENT+DAT purpose. FACT nominalizations supply proposition and complement clauses. These dependent constructions normally precede their matrix predicate. Equally foregrounded sequential events are ordinarily expressed as separate finite clauses rather than as an unlimited dependent chain.

**G-SYN-009.** Content questions use interrogative stem `mi`, which occupies the ordinary constituent position and takes case directly without a noun-class theme: `mik` ERG, `min` GEN, `mir` DAT, `mit` LOC, and so on. No additional question particle is required in a content question. Polar questions use clause-final `he`; `he` is not used merely because a content interrogative is present.

The linker/coordinator `ja` spans an additive → sequential → consequential cline: between clauses it may mean “and”, “and then”, or contextually “and so”. It does not unambiguously mark a causal reason; ordinary explicit cause uses G-SYN-016 `hapim`. Ordinary clause juxtaposition remains available. Sentence-initial `ja` is especially characteristic of narrative, sacred, and other elevated discourse; ordinary prose more often keeps it between linked clauses. Nominal coordination follows G-SYN-013.

**G-SYN-010.** Generic and gnomic nominal classification permits zero copula: `tam tinak` “hands are crossings/junctions.” Specific nominal identification likewise permits zero copula when two ordinary nominals are equated in discourse. Established-name statements use the possessive nominal `X-GEN hat NAME`, as in `samin hat Masi` “Masi is the herd-animal's name” and `ratun hat Masi` “Masi is the path's name”; productive naming itself follows G-SYN-015. PERSON/THING pronouns `ri/a` are referential forms, not productive nominal predicates: construal must be shown by ordinary reference, SOCIAL case, or a lexical predicate rather than `X ri/a`. GEN may appear as a zero-copular predicate only in tightly elliptical question-answer discourse, such as `hanu narin he?` “the world—of the people?”; ordinary assertions keep GEN inside a nominal relation. Temporally bounded, embodied, or deliberately assumed roles use ESS with an independently appropriate posture/state predicate, especially STAND `pn`: `narik tinake pinupi` “a person stands/serves as a crossing.” Zero copula does not replace ordinary verbal predication.

**G-SYN-011.** Explicit contrastive quantification uses pre-nominal `uru` ALL and `mau` NONE. The quantified noun bears any required case; the quantifiers themselves do not inflect. A generic morphologically singular noun may denote the quantified set (`uru nar` “all people”, `mau nar` “no person/people”), while ordinary number remains available when independently relevant. Generic singular/plural reference also remains available without a quantifier, so `uru/mau` are favored when exhaustive contrast matters, especially in ritual parallelism. With `uru X ... an V`, ordinary propositional NEG scopes over ALL by default, yielding “not all X V” rather than “no X V”; NONE uses `mau`. `mau` supplies negative quantification and does not require an additional `an` unless the predicate itself is independently negated.

**G-SYN-012.** Open and generic conditionals may use a DEP predicate as a protasis followed by a REAL matrix apodosis. The older compact construction is bare `X V-DEP, Y V-REAL` and remains especially frequent in customary, legal, gnomic, and elevated speech.

Ordinary contemporary prose usually makes the relation overt with clause-initial `matut` IF/WHEN, historically LOC `matu-t` “at the time/turn”: `matut X V-DEP, Y V-REAL`. In connector use `matut` is a fixed clause linker; lexical `matu-t` “in/at the season” remains independently available and is disambiguated by syntactic position and content. Neither construction by itself marks counterfactuality: projected or nonactual status continues to use the independently motivated IRREALIS system.

**G-SYN-013.** `ja` coordinates overt nominal phrases that bear the same grammatical relation. Each conjunct independently bears the case required by that relation; case is repeated on every conjunct rather than realized once over the whole coordination. In a single finite clause, overt same-role NP coordination requires `ja` in ordinary, sacred, and assembly registers. Coordinated singular conjuncts establish syntactically plural discourse reference, not dual reference: the dual remains the number of a single nominal construed as a coherent pair. Verbal agreement remains person-only under G-MORPH-006, but a later overt independent pronoun referring jointly to two or more PERSON conjuncts uses plural `rja` (or the corresponding plural form of another pronominal series). `ja` does not create mixed-role coordination. Sacred and early assembly recitation may preserve paired parallel juxtaposition only when each conjunct forms its own clause, typically with the predicate repeated; this is rhetorical clause parallelism, not asyndetic NP coordination.

**G-SYN-014.** Proto-Minitongue has no productive verbless existential clause. Ecological or living availability uses ordinary LIVE/GROW `n`: `mau suma nipinua` “no fungi were present/available.” Bounded presence of people or objects uses SIT/REMAIN `kn`. The contrast is constructional rather than a dedicated existential verb: LIVE foregrounds ecological/living availability, while SIT foregrounds bounded presence. Temporal frame nouns are overtly case-marked: recurrent or calendrical periods such as `matu` “season” take LOC (`hure matut` “in the cold season”), while temporary environmental or circumstantial states may take ESS.

**G-SYN-015.** Productive naming uses a restricted impersonal SAY+ORIENTEE construction. The generic speaker/source is suppressed and has no A-series exponent; the named participant is the applied ORIENTEE and U-controller, and the spoken NAME is a non-PO designation/content expression. The ORIENTEE participant is normally recoverable and omitted, so its SOCIAL DAT is implicit in the construction. For a third-person namee, `Masi niphupi` may parse `Masi n-p-h-u-p-i` “Masi U-3-SAY-REAL-ORI-NPST” = “they are called Masi.” This is surface-homophonous with ordinary 3A `niphupi` “they say it”; argument structure and discourse distinguish the naming construction. Established designation remains the zero-copular possessive construction of G-SYN-010.

**G-SYN-016.** Ordinary explicit causal linkage uses clause-initial `hapim` BECAUSE before a dependent cause clause: schematically `hapim X V-DEP, Y V-REAL`. The linker grammaticalized from `h-a-p-i-m`, literally SAY-NF-FACT-LNK-INS “by/given the fact”; synchronically connector `hapim` is fixed and does not inflect. Productive FACT nominalizations and EVENT+INS converbs remain independent constructions. Elevated narrative may instead leave causality implicit or use consequential `ja` when the reason relation is recoverable.

**G-SYN-017.** Ordinary comparison is relational rather than a dedicated comparative degree morphology. The standard is construed as the separated reference point, while the gradable predicate itself remains in its ordinary MAINTAIN form: schematically `X STANDARD-DECREASE.REL X-PROPERTY`, “X is PROPERTY relative to/away from STANDARD.” DECREASE on the gradable predicate itself retains G-SEM-003 “become less X” and is not a comparative exponent. Equality uses ordinary NEG DIFFERENT/CHANGED or an appropriate shared-state construction rather than a dedicated equative morpheme.

**G-SYN-018.** Commands do not introduce a dedicated imperative slot. An ordinary directive uses the minimally marked finite predicate with the addressee recoverable from discourse; IRREALIS supplies a stronger projected/emphatic directive when required. Prohibition is transparently `an + command`; no productive fused prohibitive is posited.

**G-SYN-019.** Disjunction uses `mi` in a grammaticalized interrogative-derived coordinator construction between alternatives. This OR use is distinguished from content-question `mi` by coordination position and parallel alternatives; it does not require clause-final `he`.

**G-SYN-020.** Cardinal numerals follow the noun in the ordinary NP. ONE is compatible with morphologically singular reference; TWO selects plural unless the referent is a conventional coherent natural pair, where established dual morphology remains available; THREE and higher select plural. Ordinals are attributive predicates derived from the corresponding numeral and therefore precede the noun in their DEP attributive form rather than creating a separate ordinal inflectional slot.

**G-SYN-021.** Demonstratives form a proximal/distal contrast and are attributive elements preceding the noun. When another attributive predicate is present, the ordinary order is `ATTR–DEM–N`; demonstrative focus may move the demonstrative to the left edge of the NP without creating a second paradigm. Proximal `hira` continues an expanded PRESENT/HERE stem based on old presentative *`hi`; distal `ara` is an expanded descendant of old distal *`a`, whose reduced form survives independently as the THING pronoun `a` under G-MORPH-016. The corresponding place adverbs are transparently LOC-marked `hirat` “here” and `arat` “there”.

**G-SYN-022.** Cardinal numerals are `pe` ONE, `tu` TWO, `juk` THREE, `sem` FOUR, `hu` FIVE, `hup` SIX, `hut` SEVEN, `hujuk` EIGHT, `husem` NINE, and `jun` TEN. ONE–FIVE and TEN are inherited roots. SIX–NINE are synchronically ordinary numeral lexemes but retain increasingly transparent traces of older FIVE+N composition (`*hu+pe`, `*hu+tu`, `*hu+juk`, `*hu+sem`). Higher decades are multiplicative: `tu jun` 20, `juk jun` 30; a following unit is additive, so `tu jun juk` is 23. The general NP rules of G-SYN-020 continue to govern noun number.

**G-SYN-023.** Fractions use the existing PART head `sa`. A substantivized denominator numeral bears GEN, with the generalized linker before consonant-only GEN where phonotactics require it; the numerator counts `sa` in ordinary postnominal numeral order. Thus `jukin sa pe` is 1/3 and `jukin sa tu` is 2/3. This is productive PART syntax, not a special fractional paradigm. Distributives use postnumeral `pari` EACH: `N NUM pari` means “NUM each/apiece”.

**G-SYN-024.** Approximation uses preverbal/preconstituent particle `hami` ABOUT/AROUND with semantic scope over the following quantity, measure, time expression, or gradable proposition. It is not restricted to numerals. Excess and sufficiency are explicit threshold constructions: gradable `X` plus `tuma` EXCEED/GO-BEYOND a contextual or overt limit yields “too X”, while `pura` REACH/MEET a contextual or overt requirement yields “X enough”. Bare gradable predicates remain neutral for absolute versus context-relative interpretation; the comparison class is normally supplied by discourse.

**G-SYN-025.** Superlatives are compositional extensions of G-SYN-017: the comparison standard is the exhaustive set marked by `uru` ALL, yielding the sense “X is PROPERTY beyond all relevant Y”. The set noun is recoverable and may be omitted when unambiguous. There is no dedicated superlative exponent.

## Semantics and pragmatics

**G-SEM-001.** REL describes change or maintenance of relation, not participant role. INCREASE tends toward convergence, connection, entry, strengthening, or scalar increase; DECREASE toward divergence, separation, exit, weakening, or scalar decrease; MAINTAIN follows a stable relation or root-specific baseline. Extensions are conventional to semantic classes and roots.

**G-SEM-002.** Case domains have constructional REL tendencies rather than automatic meanings. INESS supports in/into/out-of contrasts; SUPER on/onto/off; COM accompaniment/joining/separation; ESS state/entry/exit; LOC and PERL interact productively with favored motion predicates; DAT and INS allow lexically licensed gain/loss, benefit/harm, enabling/removal interpretations. When an event simultaneously encodes separation and benefit, the event trajectory determines REL: actual separation, removal, departure, or weakening remains DECREASE `a-`, while the beneficiary is expressed independently by DAT and/or AFFECTED. Benefit does not override a separative REL.

**G-SEM-003.** Spatial and gradable predicates are especially productive with REL. `house-INESS INCREASE-go`, `house-INESS go`, and `house-INESS DECREASE-go` yield go into, move/remain within, and go out of the house. With gradable states INCREASE can yield become more X and DECREASE become less X. Several lexical classes conventionalize especially transparent REL profiles. HANDLE/TRANSFER `k` has INCREASE “receive/take toward oneself,” MAINTAIN “handle/transfer,” and DECREASE “give/send away.” MAINTAIN can extend to immediate keeping/control of a manipulable theme, but alienable ownership remains a nominal GEN relation rather than an independent HAVE predicate. RECP is licensed on HANDLE/TRANSFER only with MAINTAIN, where it yields reciprocal transfer/exchange; the deictically anchored INCREASE and DECREASE transfer senses are blocked under RECP because one reciprocal event contains both transfer directions. Stative posture SIT `kn` and STAND `pn` each use MAINTAIN for the posture, INCREASE for entry into it, and DECREASE for exit from it. KNOW/REMEMBER `sn` has MAINTAIN “know/remember,” INCREASE “learn/realize/come to understand,” and DECREASE “forget/lose knowledge.” SEARCH/TRACK `sr` has MAINTAIN “seek/track,” INCREASE “find/come upon,” and DECREASE “lose the trail/lose track of.” LIVE/GROW `n` conventionalizes INCREASE “sprout/be born/come alive,” MAINTAIN “live/grow,” and DECREASE “die/wither/cease living”; with PATH as a conventional metaphorical subject, INCREASE LIVE/GROW can mean that a reciprocal relation lengthens or strengthens. DIFFERENT/CHANGED `rs` has MAINTAIN “be different/changed,” INCREASE “become more/differently changed,” and DECREASE “become alike/converge in kind”; propositional NEG `an` on the stative yields “not different/same/unchanged” where context licenses that opposition. SEE/WITNESS plus LEX.CAUS `se-m` conventionalizes a visibility profile: MAINTAIN “show/make visible,” INCREASE “reveal/bring into view,” and DECREASE “hide/conceal/remove from view.” Bare SEE retains its ordinary perception semantics. RETURN/RESTORE `nr` instead lexicalizes reversal/restoration itself and ordinarily blocks INCREASE/DECREASE REL; its unprefixed predicate covers return, restore, repay, and give back.

ESS result complements also support a conventional change-of-state strategy with selected roots. `N-ESS INCREASE-MOVE` presents a referent as entering a landscape, route, role, or comparable state, while `N-ESS INCREASE-LIVE/GROW` presents emergence as living or growing material. In the MOVE construction the transformed subject is an inactive undergoer and therefore realizes ABS+U under G-SYN-002, not active ERG+A. Where both construals are plausible, noun-class construal distinguishes them: for example, LAND/WATER forest tract favors MOVE, while GROWING forest vegetation favors LIVE/GROW. These are lexical-semantic extensions of REL plus ESS, not a general-purpose copular BECOME morpheme.

**G-SEM-005.** Physical CARRY is ordinarily expressed by the conventionalized but still analyzable serial-converb construction `THEME HANDLE-EVENT-ESS MOVE`: `hat kane rupi` “they go while handling the name / carry the name.” The HANDLE component supplies continued control of the carried theme and MOVE supplies transport; either predicate may still occur independently. In ritual and ordinary metaphor, the same construction with NAME means preserve and transmit a remembered name. Productive SAY nominalizations remain distinct: `han` is a telling/utterance event and `hap` a proposition/fact, while lexical `sapa` means story/narrative. When an uttered proposition is entrusted or transmitted, `hap` may contextually denote message-content; this is ordinary FACT semantics and does not lexicalize a separate MESSAGE noun.

**G-SEM-006.** Practical teaching and route guidance extend the existing visibility system without a new general GUIDE or TEACH root. SEE/WITNESS + LEX.CAUS is SHOW; with overt PATH `ratu` as the shown theme and an ORIENTEE learner/traveler, `PATH ... SHOW-ORI` is the conventional construction “show the path to; guide.” PATH remains overt in this conventional construction, so SHOW has not lexicalized an unrestricted GUIDE sense. Practical ecological instruction may use SHOW+ORIENTEE more broadly for visible places, foods, plants, fungi, and procedures. Propositional or knowledge teaching instead uses productive syntactic CAUS on KNOW/REMEMBER: the learner is the ordinary causee (DAT by default under G-MORPH-015), while an overt FACT/NAME/STORY content argument retains KNOW/REMEMBER's ordinary non-PO content status. Rescue has no dedicated lexical verb at this stage; FIND followed by contextually appropriate aid such as FOOD transfer and PATH-guidance remains compositional.

**G-SEM-004.** LEX.DERIV, INST, VAL/APPL, AUX, and outer ASPECT remain distinct. PLACT changes event type while HAB marks customary recurrence of whole events; INST selects a manifestation without supplying perfectivity/telicity; lexical CAUS creates a new predicate while productive CAUS builds argument structure; AUX phase/modality operators remain distinct from outer viewpoint aspect.

**G-PRAG-001.** Social personhood is a graded, relational construal rather than a categorical human/nonhuman feature. Humans are persons by default. A nonhuman referent may be construed as a social person, but ordinary discourse must overtly establish that construal before person-sensitive SOCIAL DAT/COM is licensed. Establishment may be made by an independent PERSON-series reference based on `ri` that resumes an already identifiable lexical referent, or by a PERSON classifier `-ri` on an overt description. Once established, the license persists through the coherent topic chain until a topic break, a competing same-type referent forces re-establishment, or explicit THING reference resets the construal. Lexical noun class and grammatical animacy do not change.

**G-PRAG-002.** Grammatical animacy has two values, ANIMATE and INANIMATE. Ordinary animals are ANIMATE. Personhood is not a third animacy value: an overtly established PERSON construal licenses PERSON-series reference and the SOCIAL-derived DAT/COM allomorphy of G-MORPH-011. Some culturally prominent nonhuman referents are especially easy to establish as persons, but cultural salience does not remove the overt establishment requirement.

**G-PRAG-003.** Several metaphors from the sacred cycle are conventional in ordinary discourse but remain semantically compositional rather than grammaticalized. PATH may denote an ongoing reciprocal or social relation: INCREASE/LIVE-GROW of PATH can describe strengthening or extension of that relation, while CUT or DECREASE-MOVE of PATH can describe rupture or withdrawal. HANDLE/TRANSFER with NAME can mean carry/transmit a remembered name; RETURN with a changed-state complement can describe appropriate non-identical reciprocity; and the approach/return of MIST can metaphorically describe social or epistemic opacity. Literal readings remain fully available and context determines the metaphorical construal.

## Discourse

**G-DISC-001.** Recoverable indexed pronouns may be omitted. Ordinary applied second-person participants such as “you” in “I cook bread for you” need not appear as overt nouns; the verb indexes them. Agent indexing likewise permits recoverable agent omission. Indexing distinguishes persons, not multiple nouns of the same person.

**G-DISC-002.** Third-person reference is construal-sensitive. Eligible nonhuman referents may be resumed with independent PERSON forms based on `ri` or THING forms based on `a`. For nonhumans, the first overt PERSON resumption (or an overt PERSON-classified description under G-PRAG-001) establishes the PERSON discourse license; explicit THING reference resets it. While the PERSON chain remains established, later PERSON reference and SOCIAL DAT/COM may continue without repeating the establishment. Verbal and possessive 3P indexing do not encode the PERSON/THING contrast.

**G-DISC-003.** Reference tracking uses ordinary argument omission, agreement, lexical semantics, topic continuity, and discourse prominence rather than dedicated tracking morphology. At a switch between plausible third-person referents, at least an overt independent pronoun is required. If PERSON/THING choice does not uniquely identify the intended referent, the lexical NP is repeated. Once the switched referent is re-established, recoverable arguments may again be omitted. Mere mention of a nonprominent referent does not by itself force a switch. BNI material is normally backgrounded and poor at establishing persistent reference; later robust anaphora therefore favors earlier de-incorporation or subsequent overt reintroduction. Topic and contrastive focus follow G-SYN-001 and do not break strict BNI–verb adjacency.

**G-DISC-004.** Formal sacred recitation uses ordinary grammar with a limited conservative register. Narrative episodes normally use PAST; transformation or revelation pivots may switch briefly to mythic REAL.NONPAST, and inherited refrains/gnomic teachings favor REAL.NONPAST. Prophecy begins predominantly in IRREALIS and shifts to REAL at the canonical restoration hinge when the child finds the seed. Parallelism freely uses topic fronting, narrative sentence-initial `ja`, explicit `uru/mau` contrasts, and denser recoverable argument omission, but never relaxes G-DISC-003's discourse-prominence threshold or BNI adjacency. `ja` may carry additive, sequential, or contextually consequential force; the younger ordinary causal linker `hapim` is optional in sacred recitation, which often preserves the older implicit/consequential strategy. Memorized ritual formulas may preserve individually listed pre-syncope vowels or older case/pronominal residues; these are stored formulaic variants and do not license productive suspension of G-PHON-011. Primordial figures have three naming layers: ordinary prose relative descriptions, fixed lexical epithets `Kumakar` Flesh-Giver, `Hatkar` Name-Keeper, and `Raturar` Path-Walker, and archaic ceremonial invocations using fossil PARTICIPANT forms `kumi akar`, `hat kar`, and `ratu rar`. Old PARTICIPANT `-r` remains nonproductive outside these listed fossils. True personal names Kimi, Nemi, and Tasi are primarily recitational. Sacred descriptions may shift the same landscape referent between THING reference in physical description and PERSON reference/SOCIAL case in reciprocal interaction.

**G-DISC-005.** Testimony source is expressed lexically and constructionally rather than by a grammatical evidential series. Direct witnessing uses SEE/WITNESS `se`; received testimony uses ordinary SAY with a source Actor and an ORIENTEE recipient and may carry FACT content; later retelling uses SAY with FACT or STORY according to whether a proposition or a narrative package is foregrounded. When source is contrastive, the relevant source predicate is overt rather than inferred from agreement alone. Direct speech is an independent finite clause juxtaposed with ordinary SAY; quotation marks are editorial and do not create a separate quotative complement type. Nested stories obey the ordinary reference-tracking requirements of G-DISC-003.

**G-DISC-006.** Early assembly/customary recitation uses ordinary grammar in a compressed conservative register. Parallel reciprocal pairs such as TAKE/RETURN, RECEIVE/KEEP, DAMAGE/RESTORE, and HEAR/KEEP-KNOW are favored, and G-SYN-012 bare-DEP protases are especially frequent. Same-role nominal conjuncts use `ja` under G-SYN-013; older paired formulas may instead repeat the predicate in juxtaposed clauses, preserving rhetorical parallelism without creating a separate coordination grammar. Gnomic/customary declarations conventionally carry normative force in this register, so the ten principles do not require NECESSARY morphology. NECESSARY remains available when a speaker explicitly contrasts obligation with mere custom, possibility, or description. A very small set of memorized legal formulas preserves individually listed pre-syncope verbal shapes, including `nipitire` beside ordinary `niptire` “if/when it is cut” and `jinipitire` beside ordinary `jiniptire` “if/when it breaks.” These are formulaic archaisms and do not suspend productive G-PHON-011 elsewhere. The register does not introduce a separate imperative, evidential, debt, liability, or legal case system; ordinary transfer, promise, testimony, custody, RETURN/RESTORE, and the PATH relation metaphor supply those meanings.

## Orthography

**G-ORTH-001.** Heavy monophthongs created by identical-vowel contraction are written with a circumflex: `aa → â`, `ee → ê`, `ii → î`, `uu → û`. Heavy /e/ created by `ei` is written `ë`, preserving the historical class needed to predict its distinct coda reflex. Diphthongs `ai au` are inherently heavy and take no diacritic. Marginal /o/ from coda-conditioned /au/ shortening is written `o`. These marks encode moraic and morphophonological information; they do not imply phonetic vowel length.

## Lexicon conventions

### Parts of speech

| Code | Name | Notes |
| --- | --- | --- |
| N | noun | Includes inherited classed nouns and lexicalized nominal derivatives. |
| V | verb | Includes eventive and stative verbs; adjectives are stative verbs under G-SYN-003. |
| NUM | numeral | Cardinal numeral lexeme; may be substantivized for constructions such as fractional denominators. |
| DEM | demonstrative | Attributive deictic stem; LOC derives the corresponding place adverb. |
| PART | particle | Function word, coordinator, quantifier-like operator, or discourse/semantic particle. |

### Project-specific gloss abbreviations

| Abbreviation | Meaning | Notes |
| --- | --- | --- |
| TH | noun-class theme | Overt inherited class theme. |
| PART | partitive head | Light nominal `sa` in `WHOLE-GEN + PART`. |
| SOC | SOCIAL residue | Person-sensitive DAT/COM allomorphy. |
| CLF | attributive classifier | Classifier suffix on a DEP stative predicate. |
| BNI | bare-noun incorporation | Backgrounded immediately preverbal pseudo-incorporation. |
| LNK | generalized linker | Generalized /i/ before consonant-only case endings. |
| A | Actor agreement | Post-AUX 1/2/3 agreement series. |
| U | Undergoer agreement | Pre-root `n-k/t/p-`; controller need not be PO. |
| REL | relational phase | INCREASE `i-`, MAINTAIN `Ø`, DECREASE `a-`. |
| INST | instantiative | Salient manifestation/token `-h`. |
| AFF | affected applicative | `-r`. |
| ORI | orientee applicative | `-p`. |
| GRD | ground applicative | `-m`. |
| PLACT | pluractional lexical derivation | Pre-grade lexical `-s`. |
| Q | interrogative | `mi`, case-bearing content-question stem. |
| POLQ | polar question | Clause-final `he`. |
| CONJ | linker/coordinator | `ja` “and/and then/and so”; required for overt same-role NP coordination. |
| ALL | exhaustive quantifier | Pre-nominal `uru`. |
| NONE | negative quantifier | Pre-nominal `mau`. |
