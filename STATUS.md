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

- The historical conditioning of REFL-related `r- > j-` in MID, the deeper source of INST `-h`, and exact lexical sources for STATE/FACT grammaticalization remain to be reconstructed in HISTORY.md without changing their canonical synchronic functions.
- Lexeme-specific exceptions to otherwise compositional voice/applicative licensing remain a lexical-growth priority. The first genuine blocker is now canonical: HANDLE/TRANSFER licenses RECP only under neutral MAINTAIN; directional INCREASE RECEIVE and DECREASE GIVE are blocked under RECP. Further exceptions should be discovered from text rather than invented abstractly.
- Conservative route PERL `-mi` is now lexically listed on `nuru` RIVER/river-route, `ram` BOAT, and `ratu` PATH/TRAIL. The licensing principle is settled; further members require independently conventional route senses rather than contextual coercion.

## Provisional systems

No unresolved provisional subsystem remains from AUX lexicalization, residual nominal/discourse morphology, connected syntax, or high-vowel syncope. The syncope system is canonical: medial unstressed /i u/ reduction is constrained by morphological protection and exhaustive syllabifiability under `(C)(j)V(C)`; epenthetic /i/ is most reducible, candidates are tested right-to-left, and stress is recalculated after reduction. New lexical exceptions found by regression testing should remain provisional until independently supported.

## Known conflicts

No unresolved structural contradiction is known. Benefit plus separation now follows event trajectory for REL (separation remains DECREASE) while beneficiary status is encoded independently by DAT/AFFECTED.

## Regression coverage

The permanent corpus now additionally tests constrained high-vowel syncope against nominal linkers, U-indexed verbal chains, `Cj` onsets, blocked illegal outputs (`*pant`, `*panast`, `*niptruki`, `*nipknui`), and post-syncope stress, alongside strict outer-PO two-applicative stacks in both orders, local-person U override against a third-person PO, obligatory U traces in PO relatives, non-PO relatives that preserve the actual U-controller, the lexicalized `r-m-s` reverse-order residue contrasted with an illicit productive `ROOT-m-s`, transfer and posture REL triplets, information-structure/BNI interaction, PERSON/THING pronoun disambiguation, and connected stress texts. The creation-myth pass adds neutral-only reciprocal TRANSFER, the causativized SEE visibility triplet SHOW/REVEAL/HIDE, ESS+INCREASE transformation with MOVE versus LIVE/GROW, a third conservative route noun `ratu`, compositional FOLLOW as `X-GEN PATH-PERL MOVE`, an applied route relative, and a six-clause three-referent discourse regression. No structural contradiction surfaced.

## Next useful tests

The highest-value next pass remains lexical rather than architectural. The creation myth can now express its transfer, visibility, transformation, route-following, and core reference-tracking spine, but a full translation would still require ad hoc vocabulary for several recurrent concepts: sibling/kin, mist, body substances, find/search, possession/control, promise/obligation, sow/plant, return/repay, fruit/food, several animal subclasses, and understand/realize. These should be bootstrapped as lexical fields and immediately retested in the myth.

The next dense text should extend the current six-clause myth regression to repeated social exchange and mixed PO/non-PO relatives over the same three PERSON referents, while checking whether PROMISE/RETURN-type predicates introduce further voice/applicative restrictions. Additional conservative `-mi` route nouns should be admitted only if the new lexicon develops independently conventional route senses.

Permanent regression examples live in `EXAMPLES.tsv`. New connected text should continue to expose missing lexical coverage without creating ad hoc grammar; any genuinely new construction should be marked UNSPECIFIED and designed deliberately.
