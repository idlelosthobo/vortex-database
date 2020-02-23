# Vortex
- Natural Language Database
- NOSQL Structure with a single seek file.
- Uses a abstract storage method for fast retrieval.
- Self contained portable design for all projects.

# Why
- Provide database technology that is more accessible to all projects.
- Lower the barrier to entry into formatted data storage.

# Usage

    import vortex.core.instance as vortex

    vdb = vortex.Instance('string_sample')

    while vdb:
        vdb.input_as_string(input('Input: '))
        print(vdb.result_as_string())