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

**G-PHON-010.** At consonant boundaries, natural assimilation or fusion applies first, then legal material is resyllabified. INST `-h` has productive strengthening before ordinary consonants: `hp ht hk hm hn hs hr → pp tt kk mm nn ss rr`. Elsewhere onset-only /h j/ may delete only when unprotected and not legally resyllabifiable. Root consonants, person markers, grade vowels, and productive VOICE/INST/ASPECT exponents are protected. Protected word-final INST `-h` and IPFV `-j` therefore receive epenthetic /i/; protected MID `j-` likewise triggers the minimum /i/-epenthesis needed to preserve MID plus following U morphology. Remaining protected illegal material is repaired by /i/-epenthesis. In multi-consonant chains repair proceeds from the rightmost problematic boundary leftward.
## Morphology

### Nominal morphology

**G-MORPH-001.** Productive nouns share one inflectional architecture: `NOUN-(COLL/PCL)-NUMBER-(POSS)-(INNER CASE)-(OUTER CASE)`. COLL/PCL is an optional stem-forming derivation under G-MORPH-014; POSS is the inalienable possessive-index slot of G-MORPH-016. Singular is zero, dual is `-e`, and plural is `-u`. Number scopes over the lexical or derived nominal stem before possessive indexing and case relations apply. Four productive noun stem classes condition theme realization and limited surface allomorphy within this shared architecture; they are not four separate case paradigms. Case belongs on nouns, not in the verb template.

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

Pronouns preserve person-specific ABS stems and conservative core-case relics under G-MORPH-016. Inalienable possession is productively head-marked by possessor indexing on the possessed noun under G-MORPH-016; alienable possession uses GEN.

LOC `-t`, INESS `-ti`, and SUPER `-ta` form a synchronically recognizable `t(V)` family, and PERL/INS `-m`, conservative PERL `-mi`, and COM `-ma` form a recognizable `m(V)` family. Speakers recognize these relationships analogically, but the vowels are not independently productive morphemes. PERL and INS are normally syncretic in `-m`; `-mi` remains productively conservative on pronouns and canonical route/path nouns, whose lexical membership is UNSPECIFIED. With inanimate associates, `-m` favors functional/instrumental association while `-ma` can construe the referent as a companion or co-participant.

Before consonant-only case endings, /i/ is the generalized default theme-linker, historically extended from the ANIMATE class. Thus consonant-final stems normally show forms such as `C-k → Cik` and `C-t → Cit`, but productive class themes may override /i/ in conservative cells under G-MORPH-010–011. Vowel-bearing `-ti -ta -mi -ma -e` attach directly and undergo ordinary phonology; thus a matching stem-final consonant may form a legal heterosyllabic geminate, as in schematic `pat-ti → patti`. High-frequency nouns may preserve additional fused or fossil class-conditioned forms.

Limited case stacking is productive but narrower than the general two-slot architecture suggests. GEN may serve as an inner case before LOC, INESS, SUPER, or PERL when an outer spatial relation compositionally scopes over a possessive or referential GEN relation; abstract relational GEN resists such stacking. DAT and ESS do not stack productively. Arbitrary case chains are ungrammatical. There is no productive Reference case: affected or animate endpoint functions fall to DAT, spatial anchors and routes to the spatial cases, and abstract nominal relations to GEN.

**G-MORPH-003.** Productive predicate nominalization is built on NONFINITE `-a` and has three independently sourced domains:

| Domain | Exponent | Core interpretation | Verbal retention |
| --- | --- | --- | --- |
| STATE | `-k` | state, result, circumstance | strongly noun-like; agreement/TAM normally suppressed |
| EVENT | `-n` | event, action, process | intermediate; limited A/U may survive, but finite tense/aspect normally does not |
| FACT | `-p` | proposition, fact | most clause-like; agreement normally survives, tense usually survives, aspect survives when contrastive or constructionally required |

REL remains inside the nominalized predicate. Old PARTICIPANT `-r` and RESULT/PLACE `-t ~ -m` are lexical or fossil morphology, not productive nominalizers.

Productive converbs are conventional EVENT+CASE constructions: EVENT+ESS is simultaneous/circumstantial, EVENT+INS means/manner, and EVENT+DAT purpose. Converbs take one outer case. There is no productive ABL case; source/separation meanings use REL plus existing case, another relational construction, or lexicalized/fused morphology. Attributive and relative predicates use DEP under G-SYN-006.
**G-MORPH-010.** The productive noun stem classes are ANIMATE, GROWING, LAND/WATER, and MADE. Their inherited theme profiles are respectively `-i`, `-a`, `-u`, and `Ø/C`. These themes are stem formatives rather than independent case suffixes. Historical apocope and lexical fusion mean that ABS.SG citation forms do not always display the theme overtly. New and productively formed nouns normally follow the semantic centers of the four classes, while inherited vocabulary may preserve older mismatches. A relic SOCIAL stratum survives in limited morphology but is not a fifth productive noun class.

Class meanings are prototypes rather than exhaustive ontologies. ANIMATE contains humans and ordinary animals; GROWING centers on living plants and other growing sources; LAND/WATER centers on landscape, waters, and comparable environmental entities; MADE centers on artifacts, worked objects, and related portable products. Productive class shift is available for culturally salient changes of mode of existence, especially GROWING → extracted material → MADE. Derivational morphology may distinguish extraction/material formation from manufacture even when class morphology indicates the resulting category.

Canonical lexical contrasts demonstrate that class follows mode of existence and construal rather than dictionary identity: GROWING `pana` “tree” contrasts with MADE `pan` “wood/timber”; LAND/WATER `kasu` “wild/natural fire” with MADE `kas` “hearth/controlled fire”; and GROWING `tana` “forest vegetation” with LAND/WATER `tanu` “forest tract/woodland territory.” Living body parts are ANIMATE. Detached anatomy may remain ANIMATE, while material worked from body substances such as bone, antler, or hide may shift to MADE.

**G-MORPH-011.** Noun-class effects on case are asymmetrical historical pockets within one case system. GROWING preserves transparent `-a-` most strongly before LOC and PERL/INS, yielding productive schematic `ROOT-at` and `ROOT-am`; LAND/WATER preserves `-u-` strongly in the same domain, yielding `ROOT-ut` and `ROOT-um`. LAND/WATER also preserves older `u ~ Ø` alternation and fossil consonantal material in limited lexical/case pockets whose exact distribution is UNSPECIFIED. MADE normally follows the generalized /i/ pattern but older nouns may preserve direct/fused `-m` in PERL/INS. ANIMATE /i/ is largely obscured by its spread as the default linker, though high-frequency nouns retain a small irregular fusion pocket demonstrating its older class status; exact forms are UNSPECIFIED.

The first canonical lexical residues are `nuru` “river/route,” with ordinary INS `nurum` but conservative route PERL `nurumi`, and MADE `ram` “boat,” whose high-frequency fossil INS is syncretic with ABS as `ram` while conservative PERL is `rammi`. These are lexical survivals, not new productive case allomorphs.

Old SOCIAL morphology survives as person-sensitive allomorphy in DAT and COM. It is available to humans and to nonhuman referents construed as socially responsive persons, without changing the referent's lexical noun class. Conventionally person-like rivers, herds, ancestral places, and similar referents may favor these forms even when nonperson construal remains possible. The old SOCIAL marker is reconstructed only schematically as classifier-like `*Ci`; its consonant and the exact modern DAT/COM outputs remain UNSPECIFIED.

**G-MORPH-012.** Dual and plural use the same underlying exponents across noun classes: dual `-e`, plural `-u`. Theme + number interactions are derived by ordinary morphophonology; there are no productive class-specific number allomorphs or true number+case portmanteaux. Surface number syncretism produced by regular phonology is tolerated.

The dual marks a coherent licensed pair rather than mere cardinality. For core natural-pair lexemes, singular denotes one member, dual the coherent pair, and plural three or more members or two unmatched members. Conventional functional or cultural pairings can also license dual; a newly established functional pair may be coerced into dual once discourse treats it as a unit, but accidental physical juxtaposition alone does not suffice. When the two members are separately coordinated, each conjunct normally remains singular rather than redundantly taking dual.

The numeral TWO selects dual when the noun is dual-eligible and the two referents form a licensed pair; otherwise it selects plural. Numerals THREE and above select plural. For nouns without dual eligibility, plural therefore includes two or more. Number on collective nouns counts collectives rather than their members. Mass/substance nouns may pluralize with contextual kind, portion, or bounded-instance readings.

**G-MORPH-013.** A newer attributive classifier system may suffix to attributive stative verbs/adjectives when classification is semantically relevant; neutral descriptions may omit it. Its semantic inventory is richer than the four inherited noun classes and cross-cuts them, with centers including SOCIAL/PERSON, MOBILE-LIVING, GROWING, FLUID/LANDSCAPE, WORKED/MATERIAL, BOUNDED, and COLLECTIVE. A classifier can freely signal a contextual construal different from the noun's inherited lexical class without changing that noun's declension. Some classifiers descend from older class material and others are later innovations; their exact exponents and final inventory are UNSPECIFIED.

**G-MORPH-014.** The productive collective/paucal derivation is `-s` and precedes number: `NOUN-COLL/PCL-NUMBER-CASE`. Its semantic center is a bounded coherent subset: with count nouns it forms a small group or paucal set, with mass/substance nouns a bounded quantity, and with collective nouns a subcollective. The derived stem may itself take singular, dual, or plural; dual eligibility is recalculated for the derived collective rather than inherited from the base noun.

COLL/PCL `-s` blocks the conservative class-theme case pockets of G-MORPH-011. Before consonant-only case endings, a derived `-s` stem therefore uses the generalized `-i-` linker regardless of the base noun class, schematically `ROOT-a-s-i-t` and `ROOT-u-s-i-m`. Vowel-bearing case endings attach directly under the ordinary phonology. Consonant-final bases undergo the ordinary boundary-repair system, so schematic `C-s` surfaces as `Cis` where required by phonotactics.

### Verbal morphology

**G-MORPH-004.** Abstract predicate template:

`NEG | REL–VOICE–U–[ROOT–LEX.DERIV¹⁻²]⟨GRADE⟩–INST–VAL/APPL¹⁻²–AUX¹⁻²–A–TENSE–ASPECT`

Morphological position, morphosyntactic selection, and semantic scope are distinct. Maximal forms are licensed only when every combination is lexically and semantically compatible. One layer is ordinary in each recursive domain; at most two LEX.DERIV, VAL/APPL, or AUX operators are productive. VOICE is normally singular. Denser apparent stacks favor lexicalization or restructuring.

**G-MORPH-005.** Grades are NONFINITE `-a`, REAL/INDEPENDENT `-u`, IRREALIS `-i`, and DEPENDENT `-e`. REAL marks ordinary independent assertion; IRREALIS marks projected/nonactual status; DEP serves attributive, relative, adverbial, secondary-predicate, and young complex-predicate constructions; NF supplies nominalization and converb bases. Young AUX take DEP `-e`; older bound AUX lose independent grading.

**G-MORPH-006.** Agreement has two person-only series. A-series is post-AUX: 1 `-k`, 2 `-t`, 3 `-p`. U-series is pre-root: 1 `n-k-`, 2 `n-t-`, 3 `n-p-`. A indexes Actor/event-source; U indexes Undergoer/event-locus or another selected U-controller. Only one U marker surfaces. PO and U-controller are distinct: argument structure and valency first establish PO eligibility, then local person can override U control without changing PO. First/second persons outrank third person for U control; when 1 and 2 compete, PO breaks the tie.

**G-MORPH-007.** Tense remains NONPAST `-i` and PAST `-a`. Independent finite predicates obligatorily contrast them; DEP normally lacks tense except in licensed finite-dependent constructions. Outer aspect is `Ø` neutral, PFV `-n`, IPFV `-j`, HAB `-r`. HAB normally contrasts with rather than stacks with PFV/IPFV. IPFV descends from CONTINUE; protected final `-j` surfaces with epenthetic /i/. HAB descends from LIVE/STAY; a fuller semi-productive LIVE/STAY customary/durative construction survives outside the core AUX inventory.

**G-MORPH-008.** REL is INCREASE `i-`, MAINTAIN `Ø`, DECREASE `a-`. INCREASE marks convergence, entry, strengthening, or increasing relation; DECREASE marks divergence, exit, weakening, or decreasing relation; zero marks maintenance or lexical baseline. REL modifies the resulting voiced predicate and is construction- and lexical-class-conditioned.

**G-MORPH-009.** Three productive applicatives occupy VAL/APPL:

| Applicative | Exponent | Semantic center |
| --- | --- | --- |
| AFFECTED | `-r` | beneficiary/maleficiary, affected possessor/container/surface, affected participant |
| ORIENTEE | `-p` | addressee, recipient, perceptual target, social counterpart, comparison standard |
| GROUND | `-m` | location, path, medium, instrument |

AFF and GRD continue relational material also reflected in nominal DAT `-r` and INS/PERL `-m`; ORI `-p` grammaticalized from a TURN/FACE counterpart construction. CASE expresses participant relation; APPL integrates a participant into core event structure, so meaningful case may remain visible. An applied argument normally outranks an unapplied theme for PO. With two applicatives the outer applicative normally supplies PO; construction-specific exceptions remain possible. Applicative order may express scope.

**G-MORPH-015.** Lexical derivation precedes grade. PLACT/INT `-s` gives event-internal plurality/distribution with events and intensive lexical predicates with appropriate statives. LEX.CAUS `-m` descends from MAKE/SHAPE. Derived stems receive their own alignment properties; LEX.CAUS has only a default transitive bias. Productive syntactic CAUS is post-grade `-t`: the causer controls A by default, the highest remaining non-A is default PO, and the causee is DAT unless separately promoted. Thus pre-grade LEX.CAUS `-m` and post-grade VAL.CAUS `-t` remain distinct.

**G-MORPH-017.** VOICE is REFL `r-`, MID `j-`, RECP `s-`, ANTIP `ma-`. REFL identifies Actor and Undergoer and yields one S, which takes one agreement series by ordinary alignment. MID suppresses external-Actor construal or presents internal arising; CUT/SPLIT and BURN/COOK anticausatives use MID plus U. RECP distributes reciprocal relations across a plural/set participant. ANTIP demotes the current PO; COM `-ma` is the default demotion case, and PO is recomputed from remaining eligible arguments.

**G-MORPH-018.** INST `-h` follows grade and marks a salient particular manifestation/token of a property or event. It is not perfective, punctual, telic, completive, realis, past, nominalization, or an alignment selector. Before ordinary consonants it fuses by strengthening under G-PHON-010; otherwise protected `-h` survives through ordinary epenthesis. FACT normally restricts INST.

**G-MORPH-019.** Core AUX are BEGIN, CONTINUE, FINISH, ABLE, INTEND, NECESSARY. Zero or one AUX is ordinary; two may combine in class-based default order, with selected reversible pairs for true scope contrasts. Exact lexical forms remain UNSPECIFIED. Young AUX retain DEP `-e`; older bound AUX lose grade. CONTINUE is also the source of IPFV `-j`. LIVE/STAY is semi-productive outside the core AUX inventory beside descendant HAB `-r`. Narrow AUX negation uses a less-bound construction such as `ABLE [NEG V]`; propositional NEG precedes the whole finite predicate.

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

**G-SYN-001.** Basic constituent order is SOV. PO tends toward the immediately preverbal object position, but information structure may override this tendency.

**G-SYN-002.** Alignment is active–stative/semantic alignment constrained by lexical class. Active S and transitive A normally control A; inactive/stative S and selected non-A arguments normally control U. MOVE and BREATHE/EMIT are fluid-S but active-biased; SLEEP and LIVE/GROW are strongly U/stative-biased; BIG/MUCH, GOOD/FIT, and COLD are fixed U/stative. KNOW/REMEMBER is U/stative for possessed knowledge/memory but A-aligned for deliberate recall/attention. The bootstrap transitives remain transitive by default. CUT/SPLIT and BURN/COOK productively license MID anticausatives; JOIN/GATHER and HANDLE/TRANSFER license MID and/or REFL readings according to lexical semantics.

**G-SYN-003.** Adjectival meanings are stative verbs.

**G-SYN-004.** PO is the syntactically privileged non-A argument; U-controller is the participant realized by U agreement. Determine them in this order: establish core arguments; select constructional PO; apply valency/applicative changes; apply local-person U override; realize one U marker. Applicativization makes its participant PO-eligible. ANTIP demotes current PO and recomputes PO. A local non-PO may therefore control U without becoming PO.

**G-SYN-005.** Productive BNI is syntactic/pseudo-incorporation: the noun remains phonologically separate, is typically low-referential, theme-like, non-PO, immediately preverbal, and semantically integrated. Bare noun alone does not diagnose BNI. Genuine BNI cannot control U; indexing requires de-incorporation or promotion. ANTIP strongly favors later BNI of its demoted theme but neither requires the other. A recurrent pathway is `P-COM ANTIP-V → P ANTIP-V → [P V] → lexical complex predicate`.

**G-SYN-006.** Attributive/relative predicates use DEP `-e`. Accessibility is A/S → PO → non-PO core O → oblique. A/S and PO are freely relativizable; PO relatives may retain U indexing of the head. Non-PO core objects may relativize directly with a gap but normally leave no U trace. Obliques normally require APPL or another relational strategy. Genuine BNI resists direct relativization and normally de-incorporates/reanalyzes first.

**G-SYN-007.** Productive NEG is preverbal with default propositional scope. Narrow/focused negation uses a less-bound construction, especially with AUX: `ABLE [NEG V]` contrasts with `NEG [V-ABLE]`. Any old clause-final negator is restricted/archaic/lexicalized rather than a duplicate productive negator.
## Semantics and pragmatics

**G-SEM-001.** REL describes change or maintenance of relation, not participant role. INCREASE tends toward convergence, connection, entry, strengthening, or scalar increase; DECREASE toward divergence, separation, exit, weakening, or scalar decrease; MAINTAIN follows a stable relation or root-specific baseline. Extensions are conventional to semantic classes and roots.

**G-SEM-002.** Case domains have constructional REL tendencies rather than automatic meanings. INESS supports in/into/out-of contrasts; SUPER on/onto/off; COM accompaniment/joining/separation; ESS state/entry/exit; LOC and PERL interact productively with favored motion predicates; DAT and INS allow lexically licensed gain/loss, benefit/harm, enabling/removal interpretations. The unresolved competition between separation and benefit remains construction-specific rather than a universal REL override.

**G-SEM-003.** Spatial and gradable predicates are especially productive with REL. `house-INESS INCREASE-go`, `house-INESS go`, and `house-INESS DECREASE-go` yield go into, move/remain within, and go out of the house. With gradable states INCREASE can yield become more X and DECREASE become less X. Abstract extensions require conventionalization.

**G-SEM-004.** LEX.DERIV, INST, VAL/APPL, AUX, and outer ASPECT remain distinct. PLACT changes event type while HAB marks customary recurrence of whole events; INST selects a manifestation without supplying perfectivity/telicity; lexical CAUS creates a new predicate while productive CAUS builds argument structure; AUX phase/modality operators remain distinct from outer viewpoint aspect.

**G-PRAG-001.** Social personhood is a graded, relational construal rather than a categorical human/nonhuman feature. Humans are ordinarily treated as persons by default. Nonhuman beings may receive stronger person construal through established reciprocity and/or communal ritual recognition. Such beings can be categorized simultaneously by domain (for example animal, water, storm, or place), by relational status (for example familiar, dangerous, obligated, or ancestral), and, where culturally licensed, as a collective person such as a herd, river, or forest. Personhood is distinct from both lexical noun class and grammatical animacy.

**G-PRAG-002.** Grammatical animacy has two values, ANIMATE and INANIMATE. Ordinary animals are ANIMATE. Personhood is not a third animacy value: person-construal can instead license person-sensitive reference and the SOCIAL-derived DAT/COM allomorphy of G-MORPH-011. Some culturally prominent nonhuman referents develop a conventional tendency toward person-like treatment while retaining ordinary nonperson construals.

## Discourse

**G-DISC-001.** Recoverable indexed pronouns may be omitted. Ordinary applied second-person participants such as “you” in “I cook bread for you” need not appear as overt nouns; the verb indexes them. Agent indexing likewise permits recoverable agent omission. Indexing distinguishes persons, not multiple nouns of the same person.

**G-DISC-002.** Third-person reference is construal-sensitive: speakers may refer to the same eligible nonhuman referent in a more person-like way with independent PERSON forms based on `ri`, or in a more thing-like way with independent THING forms based on `a`, according to the discourse relation being foregrounded. Physical description does not require person-like reference, while reciprocity, intention, obligation, ritual interaction, or ancestry may favor it. Verbal and possessive 3P indexing does not encode this contrast.

## Orthography

**G-ORTH-001.** Heavy monophthongs created by identical-vowel contraction are written with a circumflex: `aa → â`, `ee → ê`, `ii → î`, `uu → û`. Heavy /e/ created by `ei` is written `ë`, preserving the historical class needed to predict its distinct coda reflex. Diphthongs `ai au` are inherently heavy and take no diacritic. Marginal /o/ from coda-conditioned /au/ shortening is written `o`. These marks encode moraic and morphophonological information; they do not imply phonetic vowel length.

## Lexicon conventions

### Parts of speech

| Code | Name | Notes |
| --- | --- | --- |
| N | noun | Includes inherited classed nouns and lexicalized nominal derivatives. |
| V | verb | Includes eventive and stative verbs; adjectives are stative verbs under G-SYN-003. |

### Project-specific gloss abbreviations

| Abbreviation | Meaning | Notes |
| --- | --- | --- |
| TH | noun-class theme | Overt inherited class theme. |
| LNK | generalized linker | Generalized /i/ before consonant-only case endings. |
| A | Actor agreement | Post-AUX 1/2/3 agreement series. |
| U | Undergoer agreement | Pre-root `n-k/t/p-`; controller need not be PO. |
| REL | relational phase | INCREASE `i-`, MAINTAIN `Ø`, DECREASE `a-`. |
| INST | instantiative | Salient manifestation/token `-h`. |
| AFF | affected applicative | `-r`. |
| ORI | orientee applicative | `-p`. |
| GRD | ground applicative | `-m`. |
| PLACT | pluractional lexical derivation | Pre-grade lexical `-s`. |