from ..doctools import document
from .geom_segment import geom_segment
from .geom_point import geom_point


@document
class geom_lollipop(geom_segment):
    '''
    lollipop plot

    {usage}

    Parameters
    ----------
    {common_parameters}
    point_color: str, optional (default: `geom_point.DEFAULT_AES['color']`
    color of the points
    point_size: float, optional (default: `geom_point.DEFAULT_AES['size']`
    size of the points
    horizontal: bool, optional (default: False)
    flag to plot the data horizontally

    See Also
    --------
    plotnine.geoms.geom_bar
    '''
    REQUIRED_AES = {'x', 'y'}
    NON_MISSING_AES = {'xend', 'yend'}
    DEFAULT_PARAMS = {**geom_point.DEFAULT_PARAMS, **geom_segment.DEFAULT_PARAMS,
                      'point_color': geom_point.DEFAULT_AES['color'],
                      'point_size': geom_point.DEFAULT_AES['size'],
                      'horizontal': False}
    DEFAULT_AES = {**geom_point.DEFAULT_AES, **geom_segment.DEFAULT_AES}

    def setup_data(self, data):
        data['yend'] = 0
        data['xend'] = data['x']

        return data

    @staticmethod
    def draw_group(data, panel_params, coord, ax, **params):

        if params["horizontal"]:
            plotting_data = data.copy()
            plotting_data["yend"] = plotting_data["y"]
            plotting_data["xend"] = 0
        else:
            plotting_data = data
        geom_segment.draw_group(plotting_data, panel_params, coord, ax, **params)
        geom_point.draw_group(
            plotting_data.assign(
                color=params['point_color'],
                size=params['point_size']
            ),
            panel_params, coord, ax, **params)
