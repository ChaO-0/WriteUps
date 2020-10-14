import angr

def solve():
    proj = angr.Project('angrmanagement')

    state = proj.factory.entry_state()

    simgr = proj.factory.simgr(state)

    simgr.explore(
        find=0x400000 + 0x2360,
        avoid=0x400000 + 0x23b9
    )

    print(simgr)

    if simgr.found:
        f = simgr.found[-1]
        open("data", "w+").write(str(f.posix.dumps(0)))
        # print()

if __name__ == "__main__":
    solve()