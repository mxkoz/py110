Rules of the game:
1. Initialize deck
2. Deal cards to player and dealer
3. Player turn: hit or stay
   - repeat until bust or stay
4. If player bust, dealer wins.
5. Dealer turn: hit or stay
   - repeat until total >= 17
6. If dealer busts, player wins.
7. Compare cards and declare winner.

Data structure:
<!-- What data structure should you use to contain the deck, the player's cards, and the dealer's cards? A dictionary, perhaps? A list? A nested list? Your decision will have consequences throughout your code but don't be afraid of choosing the wrong one. Play around with an idea, and see how far you can push it. If it doesn't work, back out and take another approach. -->

The deck as a dictionary
The individual decks as lists pulling random values from that dick