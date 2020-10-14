import angr
import claripy

def solve():
    proj = angr.Project('a.out')

    flag_chars = [claripy.BVS('flag_%d' % i, 8) for i in range(15)]
    flag = claripy.Concat( *flag_chars + [claripy.BVV(b'\n')]) # Add \n for scanf() to accept the input

    state = proj.factory.full_init_state(
            args=['./a.out'],
            add_options=angr.options.unicorn,
            stdin=flag,
    )

    for k in flag_chars:
        state.solver.add(k >= ord('!'))
        state.solver.add(k <= ord('~'))

    simgr = proj.factory.simulation_manager(state)

    simgr.explore(
        find=0x400000 + 0x1124,
        avoid=0x400000 + 0x110d
    )

    print(simgr)

    if (len(simgr.found) > 0):
        for found in simgr.found:
            print(found.posix.dumps(0))

if __name__ == "__main__":
    solve()