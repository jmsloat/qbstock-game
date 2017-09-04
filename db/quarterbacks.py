class QuarterbackRepository(object):
    qbs_by_tier = {
        1: [
            {
                'name': 'Matt Ryan',
                'team': 'ATL',
                'tier': '1',
                'prior_tier': '-',
                'qbr': 83.3,
                'wl_diff': 0,
                'ipo': 8.33
            },
            {
                'name': 'Tom Brady',
                'team': 'NE',
                'tier': '1',
                'prior_tier': '-',
                'qbr': 83.0,
                'wl_diff': 0,
                'ipo': 8.30
            },
            {
                'name': 'Dak Prescott',
                'team': 'DAL',
                'tier': '1',
                'prior_tier': '-',
                'qbr': 81.5,
                'wl_diff': 0,
                'ipo': 8.15
            }],
        2: [
            {
                'name': 'Tyrod Taylor',
                'team': 'DAL',
                'tier': '2',
                'prior_tier': '-',
                'qbr': 68.2,
                'wl_diff': 0,
                'ipo': 6.82
            },
            {
                'name': 'Ben Roethlisberger',
                'team': 'PIT',
                'tier': '2',
                'prior_tier': '-',
                'qbr': 66.3,
                'wl_diff': 0,
                'ipo': 6.63
            }],

        3: [
            {
                'name': 'Russel Wilson',
                'team': 'SEA',
                'tier': '3',
                'prior_tier': '-',
                'qbr': 63.2,
                'wl_diff': 0,
                'ipo': 6.32
            },
            {
                'name': 'Derek Carr',
                'team': 'OAK',
                'tier': '3',
                'prior_tier': '-',
                'qbr': 62.1,
                'wl_diff': 0,
                'ipo': 6.21
            },
        ],
    }

    def __init__(self):
        pass

    def get_all(self):
        return self.qbs_by_tier
