import angr 

def solve():
    proj = angr.Project('keygen')

    state = proj.factory.entry_state()

    simgr = proj.factory.simgr(state)
    avoid_addr = [0x400000 + 0xabe, 0x400000 + 0xad7, 0x400000 + 0xaf0]

    simgr.explore(
        find=0x400000 + 0xaa0,
        avoid=avoid_addr
    )

    print(simgr)

    if simgr.found:
        f = simgr.found[-1]
        # open("data", "w+").write(str(f.posix.dumps(0)))
        print(f.posix.dumps(0))

if __name__ == "__main__":
    solve()