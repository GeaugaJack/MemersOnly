from Question import Question

question_prompts = [
    "What is the first pokemon Cynthia brings out in the Elite Four in Pokemon Platinum?\n(a) Lucario\n(b) Spiritomb\n(c) Garchomp\n(d) Milotic\n\n",
    "Which Pokemon is only available male?\n(a) Machamp\n(b) Gyrados\n(c) Tauros\n(d) Snorlax\n\n",   
    "Who is the second ELite Four member in the 2nd generation?\n(a) Lorelei\n(b) Blaine\n(c) Wallace\n(d) Koga\n\n",
    "The TM Lt.Surge gives you in Pokemon LeafGreen is... \n(a) Signal Beam\n(b) Thunderbolt\n(c) Volt Tackle\n(d) Shock Wave\n\n",
    "Where can you catch Sabeleye in Pokemon Ruby?\n(a) Route 110\n(b) Turnback Cave\n(c) Granite Cave\n(d) It cannot be caught in Ruby\n\n",          
    "What is the Pokemon featured for Pokemon Go's August Community Day 2019?\n(a) Gible\n(b) Ralts\n(c) Spiritomb\n(d) Baltoy\n\n",   
    "What pokemon is Whitney's gym shaped after in Pokemon Silver?\n(a) Clefairy\n(b) Miltank\n(c) Chansey\n(d) Snubbull\n\n",
    "Which item could not be sold to Marts in the Pokemon FireRed?\n(a) Rare Candies\n(b) Charcoal\n(c) Moon Stones\n(d) Poke Doll\n\n",
    "Where can you catch Pikachu in Pokemon LeafGreen?\n(a) Viridian Forest\n(b) Pokemon Mansion\n(c) Safari Zone\n(d) Mt. Moon\n\n",
    "Which Pokemon does not have a second evolution?\n(a) Gulpin\n(b) Spoink\n(c) Aipom\n(d) Spinda\n\n",
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "d"),
    Question(question_prompts[3], "d"),
    Question(question_prompts[4], "d"),
    Question(question_prompts[5], "b"),
    Question(question_prompts[6], "a"),
    Question(question_prompts[7], "c"),
    Question(question_prompts[8], "a"),
    Question(question_prompts[9], "d"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)