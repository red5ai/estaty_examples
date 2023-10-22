from estaty.analysis.action import Analyzer
from estaty.data_source.action import DataSource
from estaty.main import EstateModel
from estaty.preprocessing.action import Preprocessor

import warnings
warnings.filterwarnings('ignore')


def launch_proximity_analysis_for_bars_objects():
    point_for_analysis = {'lat': 52.5171411, 'lon': 13.3857187}
    osm_source = DataSource('osm', params={'category': 'bar'})

    osm_reprojected = Preprocessor('reproject', params={'to': 'auto'}, from_actions=[osm_source])

    analysis = Analyzer('distance', params={'network_type': 'walk', 'visualize': True, 'color': 'orange',
                                            'edgecolor': 'black', 'title': 'Bars'},
                        from_actions=[osm_reprojected])

    model = EstateModel().for_property(point_for_analysis, radius=2000)
    founded_routes = model.compose(analysis)

    print(founded_routes.lines)
    print(f'Min length: {founded_routes.lines["Length"].min():.2f}, m')
    print(f'Mean length: {founded_routes.lines["Length"].mean():.2f}, m')
    print(f'Max length: {founded_routes.lines["Length"].max():.2f}, m')


if __name__ == '__main__':
    launch_proximity_analysis_for_bars_objects()
