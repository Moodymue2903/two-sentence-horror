"""Draft + validate 20 two-sentence horror candidates for
u-suroto-two-sentence-horror-acea9253.

Validates each candidate: exactly 2 sentences, 1-400 chars, single line,
no abbreviation periods that could confuse a sentence count.
Writes candidates.md with real char counts.
"""
import re

CANDIDATES = [
    "My wife kisses me goodbye every morning, always on the left cheek, before the kettle boils. This morning she kissed my right cheek, and when I laughed and asked why, she said, 'Because I have never once kissed you on the left.'",
    "The baby monitor crackled, and my daughter whispered, 'Mummy, there's a man standing in my room.' I was already standing in her doorway, so I whispered back, 'Then who just took my hand?'",
    "Every night at three in the morning my dog stands at the foot of my bed and growls at the empty corner of the room. Last night the growling stopped, because the corner growled back.",
    "I found my own obituary in this morning's paper, printed neatly under a photograph of me smiling at a party I never attended. The date of death was tomorrow.",
    "My phone's voice assistant has started answering questions I only think, never say aloud. Tonight it whispered, 'You should stop thinking about the basement.'",
    "The lift in my building only ever goes to the basement, and it has done that for ten years. Yesterday it stopped at the thirteenth floor, and the doors opened onto my own flat, where I was already asleep in my own bed.",
    "Every night my son asks me to check under his bed for monsters, and every night I find nothing. Tonight I found my son under the bed, and the thing in his bed asked me why I was staring.",
    "My grandmother's clock has chimed thirteen times at midnight for as long as I can remember, and we all pretended not to hear it. Last night it chimed twelve, and every other clock in the house stopped at the same time.",
    "I sleep with the bedroom door locked, because my husband sleepwalks and I am afraid of what he might do. Last night I woke to the sound of the lock turning from the outside, and his voice said, 'You locked the wrong one in.'",
    "The new neighbours moved in across the street, and every evening they stand at their window waving at me, always in perfect unison. This morning I waved back, and they all stopped at once, as if someone had switched them off.",
    "My sister died three years ago, but her phone still sends me a goodnight text every evening at nine. Tonight the text said, 'Stop replying \u2014 he can see the light from your screen.'",
    "I took a photograph of my daughter's birthday party, and in the background, through the kitchen window, a man was watching us from the garden. We do not have a garden, and the house has no kitchen window.",
    "The doctor told me the tumour was gone, and for the first time in a year I slept without dreaming. This morning I found a note in my own handwriting that said, 'It did not die \u2014 it moved.'",
    "I have lived alone for six years, and every night I bolt the front door twice, once for the lock and once for luck. Tonight I found the second bolt already drawn, and a second set of footprints in the dust leading from my bedroom to the door.",
    "My daughter drew our family this morning: me, her mother, and a tall man with no face standing behind us. When I asked who he was, she said, 'He is the one who holds the crayon when I sleep.'",
    "The recording from my doorbell camera shows me coming home at six, hanging up my coat, and sitting down to dinner. I did not get home until midnight, and I have never owned a coat.",
    "I told my therapist that the voice in my head had finally gone quiet, and she smiled and said that was wonderful progress. On the way home I realised the voice had not gone quiet at all; it had simply learned to sound like her.",
    "The last train home always arrives at 11:40, and I have caught it every night for three years. Tonight it arrived at 11:40, on time, full of passengers, and every one of them was me.",
    "My reflection has been a half-second late for a week, and I have been telling myself it is the light in the bathroom. This morning it blinked first, and then it smiled.",
    "There is a knocking in the walls of my flat, three knocks, always at the same hour, and the landlord swears the building has no pipes there. Last night the knocking answered me, in my own rhythm, from inside the room.",
]

SENT_END = re.compile(r"[.!?]['\"]?(?=\s+[A-Z]|\s*$)")


def sentence_count(text):
    return len(SENT_END.findall(text))


def main():
    problems = []
    lines = ["# Two-Sentence Horror — candidates\n",
             "Bounty: u-suroto-two-sentence-horror-acea9253 ($2, deadline 2026-11-27T08:00:00Z).",
             "Each candidate: exactly two sentences, at most 400 characters, single line.",
             "Char counts below are measured by this script, not estimated.\n"]
    for i, c in enumerate(CANDIDATES, 1):
        n = sentence_count(c)
        chars = len(c)
        ok = (n == 2 and 1 <= chars <= 400 and "\n" not in c and "\r" not in c)
        flag = "" if ok else "  <-- FAIL"
        if not ok:
            problems.append((i, n, chars))
        print(f"{i:2d}. sentences={n} chars={chars}{flag}")
        lines.append(f"## {i}. ({chars} chars)\n\n{c}\n")
    with open("/home/hatch/workspace/makefun/two-sentence-horror/candidates.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print()
    if problems:
        print("FAILURES:", problems)
    else:
        print("ALL 20 PASS: exactly 2 sentences, 1-400 chars, single line.")


if __name__ == "__main__":
    main()
