from estaty.analysis.action import Analyzer
from estaty.data_source.action import DataSource
from estaty.main import EstateModel
from estaty.preprocessing.action import Preprocessor

import warnings
warnings.filterwarnings('ignore')


def launch_parks_proximity_analysis():
    point_for_analysis = {'lat': 59.944843895537566, 'lon': 30.294778398601856}
    # 1 Stage - define data sources and get data from them
    osm_source = DataSource('osm', params={'category': 'park'})

    # 2 Stage - re project layers obtained from OSM: UTM zone 33N - EPSG:32633
    osm_reprojected = Preprocessor('reproject', params={'to': 'auto'}, from_actions=[osm_source])

    # 4 Stage - calculate distances from open source
    analysis = Analyzer('distance', params={'network_type': 'walk', 'visualize': True, 'color': 'green',
                                            'title': 'Parks'},
                        from_actions=[osm_reprojected])

    # Launch model for desired location
    model = EstateModel().for_property(point_for_analysis, radius=2000)
    founded_routes = model.compose(analysis)

    print(founded_routes.lines)
    print(f'Min length: {founded_routes.lines["Length"].min():.2f}, m')
    print(f'Mean length: {founded_routes.lines["Length"].mean():.2f}, m')
    print(f'Max length: {founded_routes.lines["Length"].max():.2f}, m')


if __name__ == '__main__':
    launch_parks_proximity_analysis()
