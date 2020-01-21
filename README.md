# Vortex
Vortex Natural Language Database

# Usage

    import vortex.core

    vdb = vortex.core.Core('testing')

    while vdb:
        vdb.string_input(input('Input: '))