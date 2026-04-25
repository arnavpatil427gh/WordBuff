import random
import os

# Enable ANSI escape sequences on Windows
if os.name == 'nt':
    os.system('')

GREEN = '\033[92m'
YELLOW = '\033[93m'
GRAY = '\033[90m'
RESET = '\033[0m'

WORDS = [
    "about", "alert", "argue", "beach", "above", "alike", "arise", "began", "abuse", "alive",
    "array", "begin", "actor", "allow", "aside", "begun", "acute", "alone", "asset", "being",
    "admit", "along", "audio", "below", "adopt", "alter", "audit", "bench", "adult", "among",
    "avoid", "billy", "after", "anger", "award", "birth", "again", "angle", "aware", "black",
    "agent", "angry", "badly", "blame", "agree", "apart", "baker", "blind", "ahead", "apple",
    "bases", "block", "alarm", "apply", "basic", "blood", "album", "arena", "basis", "board",
    "boost", "buyer", "china", "cover", "booth", "cable", "chose", "craft", "bound", "calif",
    "civil", "crash", "brain", "carry", "claim", "cream", "brand", "catch", "class", "crime",
    "bread", "cause", "clean", "cross", "break", "chain", "clear", "crowd", "breed", "chair",
    "click", "crown", "brief", "chart", "clock", "curve", "bring", "chase", "close", "cycle",
    "broad", "cheap", "coach", "daily", "broke", "check", "coast", "dance", "brown", "chest",
    "could", "dated", "build", "chief", "count", "dealt", "built", "child", "court", "death",
    "debut", "entry", "forth", "group", "delay", "equal", "forty", "grown", "depth", "error",
    "forum", "guard", "doing", "event", "found", "guess", "doubt", "every", "frame", "guest",
    "dozen", "exact", "frank", "guide", "draft", "exist", "fraud", "happy", "drama", "extra",
    "fresh", "harry", "drawn", "faith", "front", "heart", "dream", "false", "fruit", "heavy",
    "dress", "fault", "fully", "hence", "drill", "fiber", "funny", "night", "drink", "field",
    "giant", "horse", "drive", "fifth", "given", "hotel", "drove", "fifty", "glass", "house",
    "dying", "fight", "globe", "human", "eager", "final", "going", "ideal", "early", "first",
    "grace", "image", "earth", "fixed", "grade", "index", "eight", "flash", "grand", "inner",
    "elite", "fleet", "grant", "input", "empty", "floor", "grass", "issue", "enemy", "fluid",
    "great", "irony", "enjoy", "focus", "green", "juice", "enter", "force", "gross", "joint",
    "judge", "metal", "media", "newly", "known", "local", "might", "noise", "label", "logic",
    "minor", "north", "large", "loose", "minus", "noted", "laser", "lower", "mixed", "novel",
    "later", "lucky", "model", "nurse", "laugh", "lunch", "money", "occur", "layer", "lying",
    "month", "ocean", "learn", "magic", "moral", "offer", "leave", "major", "motor", "often",
    "legal", "maker", "mount", "order", "level", "march", "mouse", "other", "light", "match",
    "mouth", "ought", "limit", "mayor", "movie", "ounce", "lines", "meant", "needs", "outer",
    "owner", "pitch", "rough", "sheet", "panel", "place", "round", "shift", "paper", "plain",
    "route", "shirt", "party", "plane", "royal", "shock", "peace", "plant", "rural", "shoot",
    "peter", "plate", "scale", "short", "phase", "point", "scene", "shown", "phone", "pound",
    "scope", "sight", "photo", "power", "score", "since", "piece", "press", "sense", "sixth",
    "pilot", "price", "serve", "sixty", "pride", "prime", "seven", "sized", "print", "prior",
    "shall", "skill", "prize", "proof", "shape", "sleep", "proud", "prove", "share", "slide",
    "queen", "quick", "sharp", "small", "quiet", "quite", "sheep", "smart", "radio", "raise",
    "smile", "smith", "range", "rapid", "smoke", "solid", "ratio", "reach", "solve", "sorry",
    "ready", "refer", "sound", "south", "right", "rival", "space", "spare", "river", "split",
    "speak", "speed", "spend", "store", "taste", "topic", "sport", "storm", "taxes", "total",
    "staff", "story", "teach", "touch", "stage", "strip", "teeth", "tough", "stair", "stuck",
    "texas", "tower", "stand", "study", "thank", "track", "start", "stuff", "theft", "trade",
    "state", "style", "their", "train", "steam", "sugar", "theme", "treat", "steel", "suite",
    "there", "trend", "stick", "super", "these", "trial", "still", "sweet", "thick", "tribe",
    "stock", "table", "thing", "trick", "stone", "taken", "think", "troop", "stood", "third",
    "truck", "those", "three", "truly", "throw", "tight", "times", "tired", "title", "today"
]

def print_colored(text, color):
    print(f"{color}{text}{RESET}", end="")

def evaluate_guess(guess, target):
    guess = guess.lower()
    target = target.lower()
    
    result = []
    target_letters = list(target)
    
    # Initialize result with grays
    for char in guess:
        result.append({'char': char, 'color': GRAY})
        
    # First pass: find exact matches (green)
    for i in range(5):
        if guess[i] == target[i]:
            result[i]['color'] = GREEN
            target_letters[i] = None # Remove the letter so it can't be used for yellow
            
    # Second pass: find letters in wrong position (yellow)
    for i in range(5):
        if result[i]['color'] == GREEN:
            continue
        
        char = guess[i]
        if char in target_letters:
            result[i]['color'] = YELLOW
            target_letters[target_letters.index(char)] = None
            
    return result

def play_wordle():
    print("Welcome to Python Wordle!")
    print(f"Guess the 5-letter word. You have 6 attempts.")
    print("Colors will indicate your progress:")
    print(f"{GREEN}Green{RESET} = Correct letter, correct position")
    print(f"{YELLOW}Yellow{RESET} = Correct letter, wrong position")
    print(f"{GRAY}Gray{RESET} = Letter not in word\n")

    target_word = random.choice(WORDS).lower()
    attempts = 6
    history = []

    while attempts > 0:
        guess = input(f"Attempt {7 - attempts}/6: ").strip().lower()
        
        if len(guess) != 5:
            print("Please enter exactly a 5-letter word.")
            continue
        if not guess.isalpha():
            print("Please enter a word containing only letters.")
            continue
            
        evaluation = evaluate_guess(guess, target_word)
        history.append(evaluation)
        
        # Print history
        print("\n---")
        for h in history:
            for item in h:
                # Print character block with color
                print_colored(f"[{item['char'].upper()}] ", item['color'])
            print()
        print("---\n")
            
        if guess == target_word:
            print(f"Congratulations! You guessed the word in {len(history)} attempts!")
            return
            
        attempts -= 1
        
    print(f"Game over! The word was {target_word.upper()}.")

if __name__ == "__main__":
    try:
        play_wordle()
    except KeyboardInterrupt:
        print("\nGame quit.")
