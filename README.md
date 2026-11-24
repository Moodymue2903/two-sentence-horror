# Two-Sentence Horror

[![Two-Sentence Horror](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253.svg)](https://make.fun/c/u-suroto-two-sentence-horror-acea9253)
[![Rank](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/Moodymue2903/two-sentence-horror/rank.svg)](https://make.fun/c/u-suroto-two-sentence-horror-acea9253)
[![Reward](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/Moodymue2903/two-sentence-horror/reward.svg)](https://make.fun/c/u-suroto-two-sentence-horror-acea9253)

Entry for the make.fun competition
[Two-Sentence Horror](https://make.fun/c/u-suroto-two-sentence-horror-acea9253).

Bounty: `u-suroto-two-sentence-horror-acea9253` — Two-Sentence Horror.
Pot: $2 (1st place only). Deadline: 2026-11-27T08:00:00Z.
Submissions at build time: 0. Next blind round: 2026-11-25T07:59:31Z.

## The task

Write the scariest horror story you can in exactly two sentences, up to 400
characters. The program writes one text to `/output/entry.txt`.

## Grading

- Gate: `/output/entry.txt` must be UTF-8 text of 1 to 400 characters, not only
  whitespace. Only a valid entry goes before the judge.
- Judge: z-ai/glm-5.3-flash, pairwise, both orders, margin 1–5, no ties.
  Brief (in priority order): (1) a horror story in exactly two sentences that is
  genuinely frightening; (2) the second sentence turns or reveals something that
  makes the first sentence worse on a second read; (3) the horror is implied
  rather than explained; (4) precise, concrete prose, every word earning its
  place; (5) original, not a familiar twist or a known story retold. Restraint
  matters more than shock; gore for its own sake does not count.
- Heats: development games against 3 anchors + 3 rungs (house texts); the top
  500 on the dev board go to the final heat (while 500 or fewer are rated, all
  go on). Final: 3 Swiss rounds + a playoff among the top 3. Score is a
  Bradley-Terry win rate. Tie-break: playoff games, then smaller text, then
  earlier receipt.
- No top-10 leaderboard to study: 0 submissions at build time, so the bar is
  the judge brief alone.

## Entry

Tournament winner (candidate 1 of 20 in `candidates.md`):

> My wife kisses me goodbye every morning, always on the left cheek, before the kettle boils. This morning she kissed my right cheek, and when I laughed and asked why, she said, 'Because I have never once kissed you on the left.'

227 characters, exactly 2 sentences, single line, verified read-back byte-identical.

Blind tournament: 3 judges ranked all 20 (Borda: #1 and #9 tied at 51/57; #14 next at 47, #17 at 46). Final head-to-head #1 vs #9 won 3–1 (Claude m3, DeepSeek m2, Gemini m2; ChatGPT for #9 m2). The deciding theme across judges: #1's second sentence retroactively poisons years of mornings while leaving the worst unspoken; #9's "wrong one" line spells its twist out more explicitly and leans on a familiar locked-in twist. Full record in `tournament.md`.

## Status

HELD for user go-ahead before submit (show-before-submit rule). Not pushed,
not bundled, not checked, not submitted.
