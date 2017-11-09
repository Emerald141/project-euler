from getch import getch

def peresult(probnumber, solution, time):
        print("The solution to Project Euler problem", probnumber, "is", solution)
        print("Answer took", time, "seconds")
        print()
        print("Press any key to exit")
        getch()

