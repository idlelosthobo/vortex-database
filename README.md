# Vortex
Natural Language Database

# Usage

    import vortex.core.instance as vortex

    vdb = vortex.Instance('string_sample')

    while vdb:
        vdb.input_as_string(input('Input: '))
        print(vdb.result_as_string())