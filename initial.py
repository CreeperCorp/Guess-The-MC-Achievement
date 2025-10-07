import random
import textwrap

# Sample data: Add more as desired!
advancements = [
    {
        "name": "Monster Hunter",
        "desc": "Kill any hostile monster",
        "type": "Java & Bedrock",
        "icon": "🗡️",
        "requirements": "Kill any hostile mob (e.g., zombie, skeleton, etc.)"
    },
    {
        "name": "Stone Age",
        "desc": "Mine stone with your new pickaxe",
        "type": "Java & Bedrock",
        "icon": "⛏️",
        "requirements": "Mine any stone block with a pickaxe"
    },
    {
        "name": "We Need to Go Deeper",
        "desc": "Build, light and enter a Nether Portal",
        "type": "Java & Bedrock",
        "icon": "🔥",
        "requirements": "Enter the Nether through a nether portal"
    },
    {
        "name": "Diamonds!",
        "desc": "Acquire diamonds",
        "type": "Java & Bedrock",
        "icon": "💎",
        "requirements": "Obtain diamonds by mining or from chests"
    },
    {
        "name": "A Seedy Place",
        "desc": "Plant a seed and watch it grow",
        "type": "Java & Bedrock",
        "icon": "🌱",
        "requirements": "Plant any seed in farmland"
    },
    {
        "name": "Suit Up",
        "desc": "Protect yourself with a piece of iron armor",
        "type": "Java & Bedrock",
        "icon": "🦺",
        "requirements": "Equip any piece of iron armor"
    },
    {
        "name": "The End?",
        "desc": "Enter the End portal",
        "type": "Java & Bedrock",
        "icon": "🐉",
        "requirements": "Enter the End dimension"
    },
    {
        "name": "Sweet Dreams",
        "desc": "Change your respawn point",
        "type": "Java & Bedrock",
        "icon": "🛏️",
        "requirements": "Sleep in a bed to set spawn"
    },
    {
        "name": "Adventure Time",
        "desc": "Discover every biome",
        "type": "Java",
        "icon": "🌍",
        "requirements": "Visit all of the overworld biomes"
    },
    {
        "name": "Getting an Upgrade",
        "desc": "Construct a better pickaxe",
        "type": "Java & Bedrock",
        "icon": "🪓",
        "requirements": "Craft a stone pickaxe"
    },
    # Add more advancements as you wish!
]

print("="*40)
print("Welcome to Minecraft: Guess the Advancement!")
print("="*40)
print("I will describe a Minecraft advancement or achievement. Can you guess its name?")
print("Type 'quit' to exit at any time.")
print()

score = 0
rounds = 0

while True:
    achievement = random.choice(advancements)
    print("\n--- New Challenge! ---")
    print("Advancement/Achievement type:", achievement["type"])
    print("Description:", textwrap.fill(achievement["desc"], width=60))

    guess = input("\nWhat is the name of this advancement/achievement? ").strip()
    if guess.lower() == "quit":
        print("\nThanks for playing!")
        break

    rounds += 1

    if guess.lower() == achievement["name"].lower():
        print("Correct! 🎉")
        score += 1
    else:
        print("Incorrect.")

        # Provide hints
        print("\nHint 1: Icon:", achievement["icon"])
        guess2 = input("Guess again: ").strip()
        if guess2.lower() == "quit":
            print("\nThanks for playing!")
            break
        if guess2.lower() == achievement["name"].lower():
            print("Correct! 🎉")
            score += 1
            continue

        print("\nHint 2: Requirements:", achievement["requirements"])
        guess3 = input("Last try: ").strip()
        if guess3.lower() == "quit":
            print("\nThanks for playing!")
            break
        if guess3.lower() == achievement["name"].lower():
            print("Correct! 🎉")
            score += 1
        else:
            print(f"Sorry! The correct answer was: '{achievement['name']}'.")

    print(f"Score: {score}/{rounds}")

print(f"\nFinal Score: {score}/{rounds} rounds played.")
print("Goodbye!")
