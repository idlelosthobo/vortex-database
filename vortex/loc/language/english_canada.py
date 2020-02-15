from vortex.loc.intention import Intention as In
from vortex.loc.quantify import Quantify as Qu
from vortex.loc.action import Action as Ac

intentions = [
    In('i want', 'store'),
    In('how many', 'retrieve'),
]

# We use 0 to 10 on abstract quantification
quantifies = [
    Qu('good', 5, 'rating'),
    Qu('worst', 0, 'rating'),
    Qu('like', 7, 'rating'),
    Qu('amazing', 10, 'rating'),
    Qu('hate', 0, 'rating'),
    Qu('a', 1, 'object'),
    Qu('dozen', 12, 'object'),
    Qu('bunch', 6, 'object'),
    Qu('barrel', 200, 'litre'),
    Qu('feet', 12, 'inch'),
    Qu('some', 5, 'object'),
    Qu('spectacular', 9, 'rating'),
]

actions = [
    Ac('total', 'sum')
]