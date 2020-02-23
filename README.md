# Vortex
- Natural Language Database
- NOSQL Structure with a single seek file.
- Uses a abstract storage method for fast retrieval.
- Self contained portable design for all projects.

# Usage

    import vortex.core.instance as vortex

    vdb = vortex.Instance('string_sample')

    while vdb:
        vdb.input_as_string(input('Input: '))
        print(vdb.result_as_string())