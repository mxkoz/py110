- Remove the spaces from the "input string".
- Initialize a "maximum consonants count" to zero.
- Initialize an "adjacent consonants string" to an empty string.
- For each "letter" in the "input string":
    - If the "letter" is a consonant:
        - Concatenate it to the "adjacent consonants string".
    - If the "letter" is a vowel:
        - If the "adjacent consonants string" has a length
          greater than the current "maximum consonants count":
            - If the "adjacent consonants string" has a length
              greater than 1:
                - Set the "maximum consonants count" to the length
                  of the "adjacent consonants string".

        - Reset the "adjacent consonants string" to an empty string.

- Return the "maximum consonants count".

