import time
import sys

def main():
    print("------------------------------------------")
    print("Pozdravljeni! Python aplikacija se izvaja.")
    print(f"Verzija sistema: {sys.version}")
    print("------------------------------------------")
    
    # Preprosta zanka, da vsebnik ne ugasne takoj
    counter = 0
    while counter < 5:
        print(f"Aplikacija še vedno teče... (korak {counter + 1}/5)")
        time.sleep(2)
        counter += 1
    
    print("Testiranje uspešno zaključeno!")

if __name__ == "__main__":
    main()