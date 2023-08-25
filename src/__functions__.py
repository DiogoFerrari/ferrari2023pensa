
print(f"Loading modules...", flush=True)


from pandasci import ds
from pandasci import webscraping as wb
import pandas as pd
import numpy as np
import re
from scipy.stats import norm as dnorm
from pandasci import models as dm
from datetime import datetime
from datetime import timedelta  
from scipy.stats import chi2_contingency as x2

# * R packages

import rpy2.robjects as robj
import rpy2.rlike.container as rlc
import rpy2.robjects.lib.ggplot2 as gg
from rpy2.robjects import r, FloatVector, pandas2ri, StrVector
from rpy2.robjects.packages import importr
from rpy2.robjects.packages import data as datar
from rpy2.interactive import process_revents # to refresh graphical device
try:
    process_revents.start()                      # to refresh graphical device
except (OSError, IOError, BaseException) as e:
    pass
# import data from package: datar(pkg as loaded into python).fetch('data name')['data name']
# 
pandas2ri.activate()
stats = importr('stats')
base = importr('base')
utils = importr("utils")
ggtxt = importr("ggtext")
nnet=importr("nnet")
broom=importr("broom")
car=importr("car")
edar=importr("edar")
grid=importr('grid')

# * Functions
# ** Summary

def get_data_frame(df):
    tabr = df
    tabp = (
        ds.eDataFrame(df)
        .t() 
        .drop_cols(names=0)
    )
    tab=(
        tabp
        .rename_cols(columns={old:new for old, new in zip(tabp.columns,
                                                          tabr.colnames)})
    )
    return tab


# ** Plot

def ggtheme():
    g =gg.theme(
             ## ------
             ## legend
             ## ------ 
             # legend_position = "top",
             # # legend_position = [0.12, .96],
             # legend_justification = FloatVector([0, .9]),
             # legend_direction='horizontal',
             # # legend_direction='horizontal',
             # legend_title = gg.element_text( size=11),
        #
        legend_direction  = "horizontal",
        legend_position   = FloatVector([0.08,.95]),
        legend_key        = gg.element_rect(size=21),
        # legend_key_size   = grid.unit(.5, "cm"),
        # legend_key_height = grid.unit(.01, "cm"),
        # legend_key_width  = grid.unit(.8, "cm"),
        legend_text       = gg.element_text(size=10),
             # legend_text  = gg.element_text( size=10),
             # legend_text_legend=element_text(size=10),
             # legend_text_colorbar=None,
             # legend_box=None,
             # legend_box_margin=None,
             # legend_box_just=None,
             # legend_key_width=None,
             # legend_key_height=None,
             # legend_key_size=None,
             # legend_margin=None,
             # legend_box_spacing=None,
             # legend_spacing=None,
             # legend_title_align=None,
             # legend_entry_spacing_x=None,
             # legend_entry_spacing_y=None,
             # legend_entry_spacing=None,
             # legend_key=None,
             # legend_background=None,
             # legend_box_background=None,
             strip_background = gg.element_rect(colour="transparent",
                                                fill='transparent'),
             # strip_placement = "outside",
             strip_text_x        = gg.element_text(size=10, face='bold', hjust=0),
             strip_text_y        = gg.element_text(size=9, face="bold", vjust=0,
                                                   angle=-90),
             ##panel_grid_major  = element_blank(),
             # panel_grid_minor_x  = gg.element_blank(),
             # panel_grid_major_x  = gg.element_blank(),
             # panel_grid_minor_y  = gg.element_blank(),
             # panel_grid_major_y  = gg.element_blank(),
             panel_grid_minor_y  = gg.element_line(colour="grey", size=.3, linetype=3),
             panel_grid_major_y  = gg.element_line(colour="grey", size=.3, linetype=3),
             panel_grid_minor_x  = gg.element_line(colour="grey", size=.3, linetype=3),
             panel_grid_major_x  = gg.element_line(colour="grey", size=.3, linetype=3),
             # border 
             # ------
             panel_border      = gg.element_blank(),
             axis_line_x       = gg.element_line(colour="black", size=.2, linetype=1),
             axis_line_y       = gg.element_line(colour="black", size=.2, linetype=1),
             # axis_line_y       = gg.element_line(colour="black"),
             legend_background  = gg.element_rect(fill='transparent'),
             # legend_key_height = grid::unit(.1, "cm"),
             # legend_key_width  = grid::unit(.8, "cm")
             axis_ticks_x        = gg.element_blank(),
             axis_ticks_y        = gg.element_blank(),
             axis_text_y         = ggtxt.element_markdown(),
             plot_title	         = gg.element_text(hjust=0, size = 11,
                                                   colour='grey40', face='bold'),
             plot_subtitle	 = gg.element_text(hjust=0, size = 9,
                                                   colour='grey30'),
             axis_title_y        = gg.element_text(size=10, angle=90),
        )
    return g
def ggguides():
    g= gg.guides(colour = gg.guide_legend(title_position = "top",
                                          title_hjust=0),
                 fill = gg.guide_legend(title_position = "top",
                                          title_hjust=0),
                 linetype = gg.guide_legend(title_position = "top",
                                            title_hjust=0)
                 )
    return g        
