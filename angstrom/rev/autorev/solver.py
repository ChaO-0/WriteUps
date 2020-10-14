import angr

def main():
    proj = angr.Project('autorev_assemble')

    state = proj.factory.entry_state()

    simgr = proj.factory.simgr(state)

    simgr.explore(
        find=0x408953,
        avoid=0x408961
    )

    print(simgr)

    if simgr.found:
        f = simgr.found[-1]
        print(f.posix.dumps(0))

if __name__ == "__main__":
    main()