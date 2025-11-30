import time
import os

# ANSI colors for terminal output
RESET = "\033[0m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_table(dp, highlight_index=None):
    """Print DP table with one index highlighted."""
    row = ""
    for i, val in enumerate(dp):
        if i == highlight_index:
            row += f"{YELLOW}{BOLD}[{val}]{RESET} "
        else:
            row += f"[{val}] "
    print(row)

def climb_stairs_simulation(n, mode="step"):
    """
    mode = 'step' → requires Enter to go to next step
    mode = 'auto' → runs automatically
    """
    clear()
    print(CYAN + BOLD + "CLIMBING STAIRS — Dynamic Programming Simulation" + RESET)
    print(f"\nGoal: Compute number of ways to climb {n} steps.\n")

    # Base DP array
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    if mode == "step":
        input("\nPress ENTER to begin...")

    # Show initial state
    for i in range(2, n + 1):
        clear()
        print(CYAN + BOLD + "CLIMBING STAIRS — DP Simulation" + RESET)
        print(f"Step {i}: Computing dp[{i}]")

        print("\nCurrent DP Table:")
        show_table(dp, highlight_index=i)

        print("\nExplanation:")
        print(f"- dp[{i}] = dp[{i-1}] + dp[{i-2}]")
        print(f"- dp[{i-1}] = {GREEN}{dp[i-1]}{RESET}")
        print(f"- dp[{i-2}] = {GREEN}{dp[i-2]}{RESET}")

        dp[i] = dp[i - 1] + dp[i - 2]

        print(f"\nUpdating dp[{i}] to {YELLOW}{dp[i]}{RESET}")

        if mode == "step":
            input("\nPress ENTER for next step...")
        else:
            time.sleep(1.5)

    clear()
    print(GREEN + BOLD + "COMPLETED!" + RESET)
    print("\nFinal DP Table:")
    show_table(dp)
    print(f"\nTotal ways to climb {n} steps = {YELLOW}{dp[n]}{RESET}\n")


# -------------------------------
# RUN EXAMPLES
# -------------------------------
if __name__ == "__main__":
    print("Choose mode:")
    print("1. Step-by-step (press ENTER each step)")
    print("2. Auto-run (slow animation)")
    choice = input("\nEnter 1 or 2: ").strip()

    mode = "step" if choice == "1" else "auto"
    climb_stairs_simulation(6, mode)
