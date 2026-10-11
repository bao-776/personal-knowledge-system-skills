# Evidence labels and selective verification

Source attribution and verification are different dimensions. A cited source can be wrong.

## Attribution

Use source-claim, user-statement, user-judgment, author-opinion, or ai-inference. Preserve the original wording and a locator (page, section, timestamp, or excerpt) when needed. Existing `fact` labels mean sourced claims until checked, not proof of truth.

## Verification state

Use unchecked, supported, qualified, contradicted, unresolved, or not-applicable. Record the basis, scope, checked date, and primary-source links for checked claims. `supported` means supported under the identified conditions, not universally true. Opinions and personal experiences can be preserved without judging them true or false; empirical premises embedded in an opinion remain eligible for checking.

## Triage before searching

1. Read for the user's purpose; do not enumerate or verify every sentence. Identify the small set of factual premises that will enter maintained knowledge or support its conclusion.
2. Prioritize central premises, precise numbers, causal/generalized claims, surprising claims, high-stakes decisions, conflicts, and time-sensitive facts. Deprioritize decorative examples, repetitions, subjective preferences, and incidental facts unrelated to the requested output.
3. Default for an ordinary intake: at most three highest-priority claim groups and two search rounds per group. These are adjustable resource limits, not a promise of exhaustive verification. Combine equivalent claims and reuse evidence only when population, outcome, conditions, and date match. Critical unsupported premises beyond the budget stay unresolved; do not quietly adopt them. High-stakes advice follows applicable accuracy requirements and must not rely on unchecked premises.
4. Search available web tools for the original experiment/paper, official dataset, original record, or authoritative primary documentation. Do not send private source text, identities, credentials, or internal details to a search engine; use a generic public query or mark the claim uncheckable externally.
5. Separate the direction of an effect from its magnitude. Check what was measured, population, sample, comparison, uncertainty, timing, and whether a percentage is relative change, percentage points, or another measure. A search snippet or repeated secondary claim is not verification; inspect the primary source where accessible. An abstract supports only what it actually states; disclose unavailable full text.
6. Stop when evidence supports a bounded conclusion, contradicts it, or the search budget yields no usable primary evidence. No result does not prove falsehood. Tool or network failure is not evidence either; mark unresolved and report the limitation. Do not expand into an unrelated literature review.

## Write the result

Keep Raw unchanged. In Wiki write the defensible conclusion, original claim and locator, verification status, important limits, and supporting source. Remove unsupported precision from the maintained conclusion while retaining it as an attributed unresolved claim. Report selected, checked, deferred, and skipped claim groups with brief reasons. Full check tables are optional for short inputs.

Example: an image claims hot bathing increases sleepiness by 45%. Check separately (a) whether relevant bathing conditions affect sleep outcomes and (b) the origin and measurement of 45%. Evidence about sleep-onset latency does not by itself verify subjective sleepiness or that percentage. This is a verification example, not an asserted medical finding.
