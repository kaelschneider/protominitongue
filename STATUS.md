# Proto-Minitongue Status

This file records current working state only. Git history is the project-development log.

## Speaker environment and culture

Accepted design context. These facts may motivate later lexical, semantic, pragmatic, and grammatical developments, but no grammatical consequence is canonical merely because it fits this setting.

- **Environment and mobility:** cool maritime coast, river-fed forest, and uplands form the main ecological zone. Communities are seasonally mobile, especially between coast and uplands through productive forest corridors.
- **Subsistence:** fishing and gathering combine with pastoralism. Semi-domesticated cervid-like herds are associated with households or cohorts but range relatively freely.
- **Social organization:** lifelong age/cohort groups cut across kin and organize labor, migration, ritual, and political obligations. Cohorts are broad age-sets formalized through initiation rather than exact universal age thresholds, and cohort-linked transitions structure life stages. Residence is flexible and may alternate seasonally between families; children can belong socially to several households.
- **Authority and prestige:** society is broadly egalitarian. Ritual specialists can gain influence through ecological, genealogical, and place-based knowledge. Prestige is deliberately plural: generosity, ecological competence, memory/eloquence, and ritual skill can all matter, limiting permanent elite formation. Recognized roles such as mediator, ritual specialist, provider, or speaker are contextual and generally non-hereditary rather than fixed ranks.
- **Assemblies:** otherwise independent communities meet at seasonal assemblies for exchange, marriage ties, dispute settlement, ritual, and intercommunity coordination. Cohort networks make wider political relationships visible without permanent central government.
- **Landscape and personhood:** personhood is graded and relational rather than a simple human/nonhuman binary. Humans are default persons; nonhuman beings may acquire stronger person-status through established reciprocity and/or communal ritual recognition. A nonhuman being can simultaneously have a domain identity (animal, water, storm, place, etc.), relational statuses such as familiar, dangerous, obligated, or ancestral, and—where culturally licensed—a collective identity such as a herd, river, or forest acting as one social being. Landscape is ancestral and agentive.
- **Sacred geography:** forests are both resource zones and ancestral corridors. Natural places can possess significance independently, while repeated visits, deposits, structures, and remembered events deepen that significance across generations.
- **Time and knowledge:** ordinary time is strongly seasonal/cyclical, while historical time is genealogical. Direct witnessing and traceable trusted testimony are privileged ways of establishing knowledge.
- **Property and exchange:** land and major resources are held collectively, while portable goods may be individually held. Circulation and generosity can generate prestige more readily than accumulation alone.
- **Ritual calendar:** herd movement, seasonal crossings, visits to ancestral sites, and cohort transitions are coordinated within one ritual cycle.
- **Guests and outsiders:** strangers may be treated cautiously, but properly received guests enter a distinct temporary relational status carrying strong protection and reciprocal obligations.
- **Death and ancestry:** the dead remain socially individuated as remembered ancestors for a time, then may gradually merge into collective ancestral and landscape presence.
- **Conflict:** compensation, mediation, and cohort diplomacy are preferred mechanisms; restoring workable relations is culturally more important than decisive victory.
- **Material culture:** domestic life emphasizes portable goods and elaborate woodworking, hide, bone, antler, and fiber crafts, while repeatedly used ritual places can accumulate durable structures.
- **Kinship and gender:** genealogy matters, but upbringing, co-residence, fostering, and reciprocal obligation can create socially genuine kin. Gender is important especially in kinship and reproduction, but cohort, household, skill, and relationship usually organize social life more strongly.
- **Recurring cultural tensions:** mobility versus attachment to ancestral places; inherited ritual authority versus practical innovation; and caution toward outsiders versus strong hospitality obligations.

## Active questions

- Remaining noun-class residue questions are the consonant of relic SOCIAL `*Ci`, the resulting person-sensitive DAT/COM allomorphs, additional LAND/WATER consonantal relic cells beyond the canonical bootstrap, additional ANIMATE high-frequency fusion relics, and the exact attributive-classifier exponents/final inventory. The bootstrap apocope set and the `nuru`/`ram` fossils are canonical.
- How is phase selected when separation and benefit coexist, as in “I remove a splinter for your benefit”? Participant-oriented, event-oriented, and class-specific analyses were offered; none was selected.
- Affected-person applicative `-r`, means applicative `-m`, CAUS `-t`, and ITER/INTENS `-s` are established. AUX is a small closed set whose members/forms remain UNSPECIFIED; lexical verbs retain `-a/-u/-i` grade and auxiliaries bear linking `-e`. The exact PART reflex in the planned `WHOLE-GEN + PART` construction remains UNSPECIFIED. The 16-verb bootstrap now has canonical active–stative assignments; broader lexical distributions and future verb-class membership remain open as the lexicon expands.
- `nuru` “river/route” and `ram` “boat” are canonical conservative PERL members; the broader lexical set of route/path nouns preserving `-mi` and any further noun-specific inherited linker vowels remain UNSPECIFIED. The pronominal and possessive paradigms are canonical.
- Ordering and disambiguation of original patient versus applied object when both have the same person are UNSPECIFIED. Patient-before-applied-object was a testing convention, not a separately accepted rule.
- Historical derivations of the EVENT/PARTICIPANT/RESULT nominalizers, participial extension, converb case constructions, `r-` valency reducer, and reciprocal `s-` remain to be developed in detail. CAUS `-t`, derivational bounded/pluractional `-s`, applicative `-r/-m`, and possessive indexing now have accepted historical sources at the current level of reconstruction.

## Provisional systems

- The creator's latest direction is that benefit would most likely use positive `i-`. Its exact scope is not settled. Do not implement retained beneficiary case as a general override making a negative transfer construction benefactive.
- Negative transfer indexing an affected person has been tested with “I take bread from you” as the default reading. Do not generalize this to all affected-person constructions without testing.
- Splinter removal was accepted as potentially source- or beneficiary-oriented depending on context. Overt retained case may clarify a relation only where its interpretation is established. Its interaction with the latest positive-phase preference for benefit remains open.

## Known conflicts

The earlier proposed negative-phase benefit reading and the later preference for positive phase for benefit are not yet reconciled for events that combine separation and benefit. The grammar records neither a universal benefactive override nor a universal phase-scope rule.

## Next useful tests

Phonology, morphophonology, nominal architecture, case, animacy, noun classes, number, nonfinite morphology, the core verbal exponent system, pronouns, inalienable possession, and the first lexical bootstrap are canonical and regression-tested. `LEXICON.tsv` now contains the core bootstrap with lexical alignment assignments, class-shift pairs, moderate historical apocope, and the first residual case forms; `EXAMPLES.tsv` contains permanent regression examples for those interactions. The next decisive morphology work is selection of the AUX inventory/forms, the GEN-based partitive construction, and the remaining SOCIAL DAT/COM residue.

| Diagnostic | Established expectation | Remaining dependency |
| --- | --- | --- |
| Dance into/out of/inside a house | Positive/negative/neutral plus INESS `-ti`; no obligatory movement derivation | Root form |
| Put onto/take off/reposition on a platform | Positive/negative/neutral plus SUPER `-ta` with a broad handling root | Root form |
| I cook bread for you | Applied second-person indexing without n; affected-person APPL `-r`; first-person agent suffix; recoverable pronouns omitted | Phase interpretation and root form |
| I take bread from you | Negative transfer can index you as applied object with affected-person APPL `-r`; bread remains unmarked | Root form |
| I cut bread with a knife | Means APPL `-m` indexes knife; bread remains unmarked; redundant instrument case need not be retained | Same-person noun ordering; root form |
| I remove a splinter for you | Source and benefit readings need testing against phase and meaningful case retention | Phase scope and licensed retained-case readings |

The table above remains a discovery queue for constructions whose missing noun vocabulary or phase scope is not yet canonical. Permanent lexical and morphophonological regression examples now live in `EXAMPLES.tsv`. The Pre-Proto → Proto phonological system specifies the required relative ordering and concrete outputs needed to derive canonical forms; absolute ordering of noninteracting historical changes is not asserted.
