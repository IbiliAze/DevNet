devices = [
    {
        'name': 's1',
        'ports': [
            'ssss.bb', 'ssss.cc', 'ssss.ee'
        ],
        'connections': [
            {'ssss.bb':'rrrr.aa'},
            {'ssss.cc':'rrrr.dd'},
            {'ssss.ee':'rrrr.ff'}
        ]
    },
    {
        'name': 'r1',
        'ports': [
            'rrrr.aa'
        ],
        'connections': [
            {'rrrr.aa':'ssss.bb'}
        ]
    },
    {
        'name': 'r2',
        'ports': [
            'rrrr.dd', 'rrrr.nn'
        ],
        'connections': [
            {'rrrr.dd':'ssss.cc'},
            {'rrrr.nn':'rrrr.mm'}
        ]
    },
    {
        'name': 'r3',
        'ports': [
            'rrrr.ff', 'rrrr.gg'
        ],
        'connections': [
            {'rrrr.ff':'ssss.ee'},
            {'rrrr.gg':'rrrr.hh'}
        ]
    },
    {
        'name': 'r4',
        'ports': [
            'rrrr.hh', 'rrrr.ii'
        ],
        'connections': [
            {'rrrr.hh':'rrrr.gg'},
            {'rrrr.ii':'rrrr.jj'}
        ]
    },
    {
        'name': 'r5',
        'ports': [
            'rrrr.jj', 'rrrr.kk'
        ],
        'connections': [
            {'rrrr.jj':'rrrr.ii'},
            {'rrrr.kk':'rrrr.ll'}
        ]
    },
    {
        'name': 'r6',
        'ports': [
            'rrrr.ll', 'rrrr.mm'
        ],
        'connections': [
            {'rrrr.ll':'rrrr.kk'},
            {'rrrr.mm':'rrrr.nn'}
        ]
    }
]