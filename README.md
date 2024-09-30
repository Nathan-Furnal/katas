# Introduction

A repo for my katas taken from https://kata-log.rocks/ . For the sake of
reproducibility, you can find the exercise copied down here. I sometimes made
tiny changes depending on the language I use.

# Katas
## Banking
### Your Task

Your bank is tired of its mainframe COBOL accounting software and they hired
both of you for a greenfield project in - what a happy coincidence.

- your favorite programming language!

Your task is to show them that your TDD-fu and your new-age programming language
can cope with good ole’ COBOL!

### Requirements

Write a class `Account` that offers the following methods `void deposit(int)`, `void withdraw(int)` `String printStatement()`

```
An example statement would be:

Date        Amount  Balance
24.12.2015   +500      500
23.8.2016    -100      400
```

## Bowling
### Bowling rules
The game consists of 10 frames. In each frame the player has two rolls to knock
down 10 pins. The score for the frame is the total number of pins knocked down,
plus bonuses for strikes and spares.

A spare is when the player knocks down all 10 pins in two rolls. The bonus for
that frame is the number of pins knocked down by the next roll.

A strike is when the player knocks down all 10 pins on his first roll. The frame
is then completed with a single roll. The bonus for that frame is the value of
the next two rolls.

In the tenth frame a player who rolls a spare or strike is allowed to roll the
extra balls to complete the frame. However no more than three balls can be
rolled in tenth frame.

### Requirements
Write a class `Game` that has two methods:

`void roll(int)` is called each time the player rolls a ball. The argument is
the number of pins knocked down. `int score()` returns the total score for that
game.
