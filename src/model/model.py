import sys; sys.path.append("..")
from __init__ import *
from __paths__ import *
from __constants__ import *
from __functions__ import *
# 
save=True
save=False

# * R Modules
# Suppress warnings
import warnings
warnings.filterwarnings("ignore")
from rpy2.rinterface_lib.callbacks import logger as rpy2_logger
import logging
rpy2_logger.setLevel(logging.ERROR)   # will display errors, but not warnings
# core
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
pandas2ri.activate()                         # pandas <-> data.frame
# import data from package:
# datar(pkg as loaded into python).fetch('data name')['data name']
# packages
# stats = importr('stats')
# base = importr('base')
# utils = importr("utils")
# broom = importr("broom")
# ggtxt = importr("ggtext")
# ggcp = importr("cowplot")
# ms = importr("modelsummary")
# 
# ggplot
latex = importr("latex2exp")
ggdark = importr("ggdark")
ggtxt = importr("ggtext")

# * functions (R)

def tibble2pd(dfr):
    with (robj.default_converter + pandas2ri.converter).context():
        dfp = robj.conversion.get_conversion().rpy2py(dfr)
    return dfp

def dict2vec(d):
    v = robj.StrVector(d.values())
    v.names = list(d.keys())
    return v

def dict2list(dict):
    '''
    Convert python dictionary to an R named list of vectors
    '''
    dict_final={}
    for k,v in dict.items():
        if isinstance(v[0], str):
            if isinstance(v, str):
                v=[v]
            dict_final[k] = robj.StrVector(v)
        else:
            dict_final[k] = robj.FloatVector(v)
    return robj.vectors.ListVector(dict_final)

def ggtheme():
    gg.theme_set(gg.theme_bw())
    g = gg.theme(
        ## ------
        ## legend
        ## ------ 
        legend_position = "top",
        # legend_position = [0.12, .96],
        legend_justification = FloatVector([0, .9]),
        legend_direction='horizontal',
        # legend_direction='horizontal',
        legend_title = gg.element_text( size=11, face='bold'),
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
        strip_text_y        = gg.element_text(size=10, face="bold", vjust=0,
                                              angle=-90),
        ##panel_grid_major  = element_blank(),
        # panel_grid_minor_x  = gg.element_blank(),
        # panel_grid_major_x  = gg.element_blank(),
        # panel_grid_minor_y  = gg.element_blank(),
        # panel_grid_major_y  = gg.element_blank(),

        panel_grid_minor_y  = gg.element_line(colour="grey90", size=.2, linetype=3),
        panel_grid_major_y  = gg.element_line(colour="grey90", size=.2, linetype=3),
        panel_grid_minor_x  = gg.element_line(colour="grey90", size=.2, linetype=3),
        panel_grid_major_x  = gg.element_line(colour="grey90", size=.2, linetype=3),
        # border 
        # ------
        # panel_border      = gg.element_blank(),
        panel_border          = gg.element_rect(color='gray'),
        # axis_line_x       = gg.element_line(colour="black", size=.2, linetype=1),
        # axis_line_y       = gg.element_line(colour="black", size=.2, linetype=1),
        # axis_line_y       = gg.element_line(colour="black"),
        legend_background  = gg.element_rect(fill='transparent'),
        # legend_key_height = grid::unit(.1, "cm"),
        # legend_key_width  = grid::unit(.8, "cm")
        axis_ticks_x        = gg.element_blank(),
        axis_ticks_y        = gg.element_blank(),
        axis_text_y         = ggtxt.element_markdown(),
        plot_title	         = gg.element_text(hjust=0, size = 13,
                                                   colour='grey40',
                                                   face='bold'),
        plot_subtitle	 = gg.element_text(hjust=0, size = 10,
                                           colour='grey30'),
        axis_title_y        = gg.element_text(size=11, angle=90),
        axis_title_x        = gg.element_text(size=11, angle=0),
    )
    return g

def ggguides(ncol=1, nrow=robj.NULL, keywidth=2, keyheight=.9,
             leg_title_pos="top"):
    g= gg.guides(colour = gg.guide_legend(title_position = leg_title_pos,
                                          ncol=ncol,
                                          nrow=nrow,
                                          size=8,
                                          keywidth=keywidth,
                                          keyheight=keyheight,
                                          title_hjust=0),
                 fill = gg.guide_legend(title_position = leg_title_pos,
                                        ncol=ncol,
                                        nrow=nrow,
                                        size=8,
                                        keywidth=keywidth,
                                        keyheight=keyheight,
                                        title_hjust=0),
                 shape = gg.guide_legend(title_position = leg_title_pos,
                                         ncol=ncol,
                                         nrow=nrow,
                                         size=8,
                                         keywidth=keywidth,
                                         keyheight=keyheight,
                                         title_hjust=0),
                 linetype = gg.guide_legend(title_position = leg_title_pos,
                                            ncol=ncol,
                                            nrow=nrow,
                                            size=8,
                                            keywidth=keywidth,
                                            keyheight=keyheight,
                                            title_hjust=0),
                 alpha = gg.guide_legend(title_position = leg_title_pos,
                                         ncol=ncol,
                                         nrow=nrow,
                                         size=8,
                                         keywidth=keywidth,
                                         keyheight=keyheight,
                                         title_hjust=0),
                 )
    return g        


# * Loading

fn = PATH_DATA_FINAL / "s2013-2018-pt.csv"
df = ds.read_data(fn=fn)
#
fn = PATH_DATA_FINAL / 'lapop.csv'
dfl = ds.read_data(fn=fn, sep=';', index_col=False, decimal='.')
# 
fn = PATH_DATA_FINAL / 'pew.csv'
pew = ds.read_data(fn=fn, parse_dates=['date'])
# 
fn = PATH_DATA_FINAL / 'pew-pty.csv'
pew_pty = ds.read_data(fn=fn, parse_dates=['date'])
#
fn = PATH_DATA_FINAL / 'pres-terms.csv'
pres = ds.read_data(fn=fn, parse_dates=['ini', 'end'], sep=',')


# * Tables
# ** Table 1: Mais vs Menos Poder

tab=(
    df
    .fill_na(value='Missing', vars=['aampwr', 'aalpwr'])
    .freq(vars=['aampwr'], groups='yr', output='df')
    .rename_cols(columns={'aampwr' : 'variable'}, tolower=False)
    .mutate({'var': 'Mais poder'})
    .bind_row(
        df
        .fill_na(value='Missing', vars=['aampwr', 'aalpwr'])
        .freq(vars=['aalpwr'], groups='yr', output='df')
        .rename_cols(columns={'aalpwr' : 'variable'}, tolower=False)
        .mutate({'var': 'Menos poder'})
    )
    # format
    .mutate_rowwise({'freql': lambda x: (
        f"{round(x['freq'], 1)}%\n"+
        f"({round(x['lo'], 1)},"+
        f"{round(x['hi'], 1)})\n"+
        f"n={x['n']}"
    )})
    .select_cols(names=['variable', 'yr', 'freql', 'var'])
    .pivot_wider(id_vars=['yr', 'var'], cols_from='variable',
                 aggfunc='sum')
    .sort_values(['var'], ascending=True)
    .rename_cols(regex={"freql_":""}, tolower=False)
    .drop_cols(regex=' and |Missing')
    .rename_cols(columns={
        "All": "Todos",
        "President":"Presidente",
        "Governor":"Governador",
        "Major":"Prefeito",
        "No one":"Ninguém",
        "var":"Resposta",
        "yr":"Ano",}, tolower=False)    
)
tab
# 
if save:
    # if True:
    tabs=tab.replace({'\\n': ' '} , regex=True, inplace=False)
    fn=PATH_MANUSCRIPT_TABLES / 'table1.xlsx'
    tabs.toexcel(fn)

# * Figures
# ** Figure 1: Decisoes e eleicoes importantes


vars = {'impdec' :'Decisões mais importantes',
        'impelec':'Eleições mais importantes'}
cats = {
    'All Levels'      : "Todos",
    'State Government':"Governo Estadual",
    'Local Government':"Governo Municipal",
    'Federal Government':"Governo Federal",
}
tab=ds.eDataFrame()
for var, label in vars.items():
    tmp=(
        df
        .freq(vars=var, groups='yr', output='df')
        .mutate({"var": lambda x: label})
        .mutate_rowwise({'label': lambda x:
                         f"{round(x['freq'], 1)}%\n(n={x['n']})"})
        .mutate_type(col2type={"yr":'str'}  )
        .rename_cols(columns={var:"govlev"}, tolower=False)
        .replace(cats , regex=False, inplace=False)
        .mutate(var_to_wrap='govlev', wrap=10)
    )
    tab=tab.bind_row(tmp)
tab
# 
x = "govlev"
y = "freq"
facet='var'
dodge=1
g = (
    gg.ggplot(tab)
    + gg.geom_bar(gg.aes_string(x=f"stats::reorder({x}, {y})", y=y, fill='yr'),
                  position = 'dodge', stat="identity", colour='white', alpha=.6)
    + gg.facet_wrap(f"~ {facet}" , ncol=robj.NULL,
                    scales=robj.NULL, labeller="label_value",
                    dir="h", as_table=True) 
    + gg.geom_text(gg.aes_string(x=x, y=y, label='label', group='yr'),
                   colour="black", show_legend=False, parse=False, vjust=0,
                   hjust=.50, position=gg.position_dodge(dodge), angle=0, size=3) 
    + gg.scale_fill_grey(start=.7, end=0, na_value="red") 
    + gg.scale_y_continuous(expand = FloatVector([0, 0]), limits=FloatVector([0, 73]))
    + gg.labs(
        x        = robj.NULL,
        y        = 'Frequência',
        color    = robj.NULL, 
        fill     = robj.NULL,
    	linetype = robj.NULL,
    	shape    = robj.NULL,
        title    = robj.NULL,
        subtitle = robj.NULL,
        caption  = robj.NULL
        )
    + gg.theme_bw()
    + ggtheme()
    + ggguides()
)
g.plot()

# saving 
# ------
fn_root='figure1'
if save:
    # Table
    tabs = tab.replace({"\\n":' '} , regex=True, inplace=False)
    fn = PATH_MANUSCRIPT_TABLES / f"{fn_root}.xlsx"
    tabs.to_excel(fn,  index=False)
    # Figure
    fns = [PATH_MANUSCRIPT_FIGURES  / f'{fn_root}.png',
           PATH_MANUSCRIPT_FIGURES  / f'{fn_root}.pdf']
    [g.save(filename=str(fn), width=8, height=4) for fn in fns]

    

    
# ** Figure 2: Allocation of authority per state (barplot)

var='aaidx5c_loc'
#
# 
tab=(
    df
    .drop_rows(query=f"{var}=='Decentralist'")
    .replace(VAR_LABELS , regex=False, inplace=False)
    # .freq(vars=[var, 'regionos'], groups=['yr'])
    .freq(vars=[var], groups=['regionos', 'yr'], output='df')
    .mutate_type(col2type={'yr':'str'})
    .mutate({'prop': lambda x: x['freq']/100})
    .mutate_rowwise({"label": lambda x: f"{int(x['freq'])}%\n({x['n']})"})
    .mutate_categorical(var=var, cats=[
        "Municipalista",
        'Estadualista',
        'Centralista',
        "Status Quo"

    ], ordered=True, wrap=None)
)
tab
# 
x = 'freq'
y = "regionos"
facet=var
facet = "regionos"
y=var
g = (
    gg.ggplot(tab)
    + gg.geom_bar(gg.aes_string(x=x, y=y,
                                fill='yr'),
               position = 'dodge', stat="identity", colour='white', alpha=.6)
    + gg.geom_errorbarh(gg.aes_string(y=y, xmin='lo', xmax='hi',
                                      group='yr'),
                        height=.1, color='black', alpha=.8,
                        position=gg.position_dodge(1)) 
    + gg.geom_text(gg.aes_string(x=x, y=y, label='label', group="yr"),
                   colour="black", show_legend=False, parse=False, vjust=0,
                   hjust=0.5, position=gg.position_dodge(1), angle=0, size=3.5) 
    # + gg.geom_text(gg.aes_string(x=x, y=y, label='label', group="yr"),
    #                colour="black", show_legend=False, parse=False, vjust=.5,
    #                hjust=-0.05, position=gg.position_dodge(1), angle=0, size=2.5) 
    + gg.facet_wrap(f"~ {facet}" , ncol=4,
                    scales=robj.NULL, labeller="label_value",
                    dir="h", as_table=True) 
    + gg.scale_colour_grey(start=0.2, end=.6, na_value="red") 
    + gg.scale_fill_grey(start=0.2, end=.6, na_value="red") 
    + gg.labs(
        x        = 'Frequência',
        y        = robj.NULL,
        color    = robj.NULL, 
        fill     = robj.NULL,
    	linetype = robj.NULL,
    	shape    = robj.NULL,
        title    = robj.NULL,
        subtitle = robj.NULL,
        caption  = robj.NULL
        )
    + gg.scale_x_continuous(expand = FloatVector([0, 0]),
                            limits=FloatVector([0,57]))
    + gg.theme_bw()
    + ggtheme()
    + ggguides()
    + gg.theme(axis_text_x = gg.element_text(angle = 90, size=13))
    + gg.coord_flip()
)
g.plot()

#
fn_root='figure2'
if save:
    # Table
    tabs = tab.replace({"\\n":' '} , regex=True, inplace=False)
    fn = PATH_MANUSCRIPT_TABLES / f"{fn_root}.xlsx"
    tabs.toexcel(fn)
    # Figure
    fns = [PATH_MANUSCRIPT_FIGURES  / f'{fn_root}.png',
           PATH_MANUSCRIPT_FIGURES  / f'{fn_root}.pdf']
    [g.save(filename=str(fn), width=11, height=6) for fn in fns]
    # for grid_arrange
    # [robj.lib.ggplot2.ggplot2.ggsave(filename=str(fn), width=8, height=4,
    #                                  plot=g) for fn in fns]


# ** Figure 3: Perc. difference bw 2018 and 2013

var='aaidx3c'
tab=(
    df
    .select_cols(names=['yr', 'regionos', var])
    .freq(vars=var, groups=['yr', 'regionos'], include_na=False, output='df')
    .select_cols(names=['yr', 'regionos', 'freq', var])
    .pivot_wider(id_vars=[var, 'regionos'] , cols_from='yr',
                 values_from='freq',
                 aggfunc='sum')
    .mutate({'diff': lambda col: col[2018] - col[2013]})
    # need this to reorder the labels
    .mutate_rowwise({'label': lambda col: f"{col['regionos']}___{col[var]}"})
    .replace({'Centralist':"Centralista",
              'Decentralist':'Descentralista'}, regex=True)
)
tab
# 
x = "diff"
y = "regionos"
facet=var
g = (
    gg.ggplot(tab)
    + gg.geom_bar(gg.aes_string(
        x=x,
        y=f"edar::reorder_within({y}, {x} , {facet})"),
                  position = 'dodge', stat="identity", colour='white', alpha=.6)
    + gg.geom_text(gg.aes_string(x=0, y="label", label=y),
                   colour="black", show_legend=False, parse=False, vjust=.5,
                   fontface='bold', hjust=1.1, position=gg.position_dodge(0),
                   angle=0, size=3) 
    + gg.facet_wrap(f"~ {facet}" , ncol=robj.NULL,
                    scales='free', labeller="label_value",
                    dir="h", as_table=True) 
    # + gg.scale_x_continuous(expand = FloatVector([0, 0]))
    # + edar.scale_x_reordered() ## need to include to reorder axis
    + gg.labs(
        x        = "Diferença Percentual entre 2018 e 2013",
        y        = robj.NULL,
        color    = robj.NULL, 
        fill     = robj.NULL,
    	linetype = robj.NULL,
    	shape    = robj.NULL,
        title    = robj.NULL,
        subtitle = robj.NULL,
        caption  = robj.NULL
        )

    + gg.theme_bw()
    + ggtheme()
    + ggguides()
    + gg.theme(
        axis_ticks_y_left   = gg.element_blank(),
        axis_text_y         = gg.element_blank(),  #remove y axis labels
        axis_ticks_y_right  = gg.element_blank(),
        panel_border        = gg.element_blank(),
        axis_line_x       = gg.element_line(colour="black", size=.2, linetype=1),
        axis_line_y       = gg.element_blank()
    )
)
g.plot()

#
fn_root='figure3'
if save:
    # table
    fn = PATH_MANUSCRIPT_TABLES / f"{fn_root}.xlsx"
    tabs=tab.drop_cols(names='label')
    tabs.to_excel(fn, sheet_name='Sheet1', index=False)
    # plot
    fns = [PATH_MANUSCRIPT_FIGURES  / f'{fn_root}.png',
           PATH_MANUSCRIPT_FIGURES  / f'{fn_root}.pdf']
    [g.save(filename=str(fn), width=9, height=3) for fn in fns]
    # for grid_arrange
    # [robj.lib.ggplot2.ggplot2.ggsave(filename=str(fn), width=8, height=4,
    #                                  plot=g) for fn in fns]


# ** Figure 4: Confidence (USA/PEW)


pres
tab_pres = (
    pres
    .mutate({'shade': lambda col:
             (['white', 'gray']*len(col['ini']))[:len(col['ini'])],})
    .mutate_rowwise({'date_avg': lambda col: col['ini']+(col['end']-col['ini'])/2})
)
# 
# for data use f'as.Date({x/y})'
x = "as.Date(date)"
y = "`moving-avg`"
fill=robj.NULL
facet1=robj.NULL
facet2=robj.NULL
ylab='Confia no Governo Federal (%)'
xlab=robj.NULL
g = (
    gg.ggplot(pew)
    + gg.geom_rect(gg.aes_string(xmin='as.Date(ini)',
                                 xmax="as.Date(end)",
                                 ymin = '-Inf',
                                 ymax = 'Inf',
                                 fill='shade'),
                   show_legend=False, alpha=.5,
                   data=tab_pres[1:]) 
    + gg.geom_text(gg.aes_string(x='as.Date(date_avg)', y=0,
                                 label="surname", group=robj.NULL,
                                 color='party'
                                 ),
                   check_overlap = True,
                   show_legend=False, parse=False, vjust=.5, hjust=0,
                   fontface='bold', position=gg.position_dodge(0),
		   angle=-270, size=3,
                   alpha=1,
                   data=tab_pres) 
    + gg.geom_line(gg.aes_string(x=x, y=y, fill=fill),
                   color='black') 
    + gg.scale_colour_manual(values = dict2vec({'Democrat':'blue',
                                                'Republican':'red'}), name="") 
    + gg.scale_fill_manual(values = dict2vec({"white":'white',
                                                'gray':'gray'}), name="") 
    # + gg.scale_y_continuous(expand = FloatVector([0, 0]))
    + gg.scale_x_date(breaks='10 years', date_labels='%Y') 
    + gg.theme_bw()
    + ggtheme()
    + ggguides()
    + gg.labs(
        x        = xlab,
        y        = ylab,
        color    = robj.NULL, 
        fill     = robj.NULL,
	linetype = robj.NULL,
	shape    = robj.NULL,
        title    = robj.NULL,
        subtitle = robj.NULL,
        caption  = robj.NULL
    )
)
g.plot()
# Save figures
fn_root='figure4'
if save:
    # Table
    fn = PATH_MANUSCRIPT_TABLES / f"{fn_root}.xlsx"
    pew.to_excel(fn,  index=False)
    fn = PATH_MANUSCRIPT_TABLES / f"{fn_root}-pres.xlsx"
    pres.to_excel(fn,  index=False)
    # Figure
    plt.tight_layout()
    fns = [PATH_MANUSCRIPT_FIGURES  / f'{fn_root}.png',
           PATH_MANUSCRIPT_FIGURES  / f'{fn_root}.pdf']
    [g.save(filename=str(fn), width=8, height=2.5) for fn in fns]





# ** Figure 5: Confidence (USA/PEW) by party

pew_pty
tab_pres = (
    pres
    .mutate({'shade': lambda col:
             (['white', 'gray']*len(col['ini']))[:len(col['ini'])],})
    .mutate_rowwise({'date_avg': lambda col: col['ini']+(col['end']-col['ini'])/2})
    .replace({"Democrat":"Eleitor Democrata",
              'Republican':"Eleitor Republicano"},
             regex=False, inplace=False)
)
tab_pty = (
    pew_pty
    .pivot_longer(id_vars=['date', 'source'], value_vars=None,
                  var_name='pty', value_name='moving-avg', ignore_index=True)
    .replace({"dem":"Eleitor Democrata", 'rep':"Eleitor Republicano"},
             regex=False, inplace=False)
)
tab_pty 
# 
# for data use f'as.Date({x/y})'
x = "as.Date(date)"
y = "`moving-avg`"
fill=robj.NULL
facet1=robj.NULL
facet2=robj.NULL
color='pty'
ylab='Confia no Governo Federal (%)'
xlab=robj.NULL
g = (
    gg.ggplot(tab_pty)
    + gg.geom_rect(gg.aes_string(xmin='as.Date(ini)',
                                 xmax="as.Date(end)",
                                 ymin = '-Inf',
                                 ymax = 'Inf',
                                 fill='shade'),
                   show_legend=False, alpha=.5,
                   data=tab_pres[1:]) 
    + gg.geom_text(gg.aes_string(x='as.Date(date_avg)', y=0,
                                 label="surname", group=robj.NULL,
                                 color='party'
                                 ),
                   check_overlap = True,
                   show_legend=False, parse=False, vjust=.5, hjust=0,
                   fontface='bold', position=gg.position_dodge(0),
		   angle=-270, size=3,
                   alpha=1,
                   data=tab_pres) 
    + gg.geom_line(gg.aes_string(x=x, y=y, fill=fill,
                                 color=color, group=color)) 
    + gg.scale_colour_manual(values = dict2vec({'Eleitor Democrata':'blue',
                                                'Eleitor Republicano':'red',
                                                }), name="") 
    + gg.scale_fill_manual(values = dict2vec({"white":'white',
                                                'gray':'gray'}), name="") 
    # + gg.scale_y_continuous(expand = FloatVector([0, 0]))
    + gg.scale_x_date(breaks='10 years', date_labels='%Y') 
    + gg.theme_bw()
    + ggtheme()
    + ggguides(ncol=2)
    + gg.labs(
        x        = xlab,
        y        = ylab,
        color    = robj.NULL, 
        fill     = robj.NULL,
	linetype = robj.NULL,
	shape    = robj.NULL,
        title    = robj.NULL,
        subtitle = robj.NULL,
        caption  = robj.NULL
    )
)
g.plot()
# Save figures
fn_root='figure5'
if save:
    # Table
    fn = PATH_MANUSCRIPT_TABLES / f"{fn_root}.xlsx"
    pew.to_excel(fn,  index=False)
    fn = PATH_MANUSCRIPT_TABLES / f"{fn_root}-pres.xlsx"
    pres.to_excel(fn,  index=False)
    # Figure
    fns = [PATH_MANUSCRIPT_FIGURES  / f'{fn_root}.png',
           PATH_MANUSCRIPT_FIGURES  / f'{fn_root}.pdf']
    [g.save(filename=str(fn), width=8, height=3.5) for fn in fns]





# ------------------------------


pew_pty
ax=pew_pty.plot_line('date', 'dem', figsize=[10, 3], color='blue')
axc=ax[1][0]
axc.plot(pew_pty['date'], pew_pty['rep'], color='red')
# 
axc.set_ylim(0, 100)
axc.set_xlim(pd.Timestamp('1956-01-01'),
             pd.Timestamp('2022-01-01'))
axc.set_ylabel('Confia no Governo Federal (%)')
axc.set_xlabel(None)
# grid
axc.grid(b=None)
axc.grid(b=None, which='major', axis='y', linestyle='-', alpha=.3)
axc.set_axisbelow(True) # to put the grid below the plot
# 
color='grey'
president_previous='first'
for idx, row in pres.iterrows():
    president_next=row.surname
    if president_next!=president_previous:
        color='white' if color=='grey' else 'grey' 
        # color='red' if color=='blue' else 'blue' 
        txt_col='blue' if row.party=='Democrat' else 'red'
        # axc.text((row.end+row.ini)/2, 0, s=row.PRESIDENT,
        d1=row.ini 
        d2=row.end 
        axc.text(d1.date() + (d2-d1)/2, 100, s=str(row.surname),
                 ha='left', va='top', ma='center', rotation=90,
                fontdict=dict(weight='normal', style='normal',
                              color=txt_col, fontsize=9, alpha=1))
        axc.fill_between(x=[row.ini, row.end], y1=0, y2=100, color=color,
                         alpha=.3, edgecolor='white')
    president_previous=row.surname
# for source in pew.source.unique():
#     tabt=pew.select_rows(query=f"source=='{source}'")
#     axc.plot(tabt.date, tabt.avg, color='lightblue', alpha=.3, label='Individual polls')

# Save figures
fn_root='figure5'
if save:
    # table
    fn = PATH_MANUSCRIPT_TABLES / f"{fn_root}.xlsx"
    pew_pty.to_excel(fn,  index=False)
    # plot
    plt.tight_layout()
    fns = [PATH_MANUSCRIPT_FIGURES  / f'{fn_root}.png',
           PATH_MANUSCRIPT_FIGURES  / f'{fn_root}.pdf']
    [plt.savefig(fn) for fn in fns]

# ** Figure 6: Trust drop in Brazil 2010-2022 (LAPOP)

var='trustfedgov'
axs=[]
height=3
# 
# Party id 
# --------
tab=(
    dfl
    .summary(vars=var, groups=['ano', 'ptyid'])
    .mutate_categorical(var='ptyid', cats=[
        'PT',
        'Outro (esquerda)',
        'PSDB',
        'Outro (direita)',
        'Outro',
        'nan',
    ], ordered=True, wrap=False)
)
tab
tab=(
    dfl
    .summary(vars=var, groups=['ano', 'ptyv'])
    .mutate_categorical(var='ptyv', cats=[
        'PT', 'Alternativa (PSDB ou PSL)',
        'Outros', 'Nenhum',], ordered=True, wrap=False)
)
mandates = (
    pd.DataFrame({'mid-date':[2013, 2017,2019.5],
                  'pres': ['Mandato\ndo PT',
                           'Mandato\nTemer',
                           'Mandato\nBolsonaro']})
)
mandates 
# 
# for data use f'as.Date({x/y})'
x = "ano"
y = "Mean"
fill='ptyv'
facet1=robj.NULL
facet2=robj.NULL
leg_title='Partido em quem votou para Presidente'
colors = {'PT':'red',
          'Alternativa (PSDB ou PSL)':'blue',
          'Outros':"darkgreen",
          'Nenhum':'gray'}
ylab="Confiança no Governo Federal\n Não confia                  Confia"
temer_start=2016
temer_end=2018
g = (
    gg.ggplot(tab)
    # lula
    + gg.geom_rect(gg.aes_string(xmin=temer_start, xmax=temer_end,
                                 ymin='-Inf', ymax='Inf'),
                   fill='gray', alpha=0.05)
    + gg.geom_text(gg.aes_string(x="`mid-date`",
                                 y='Inf',
                                 label="pres", group=robj.NULL),
                   check_overlap = True,
                   colour="black", show_legend=False, parse=False, vjust=1.5, hjust=.5,
                   fontface='bold', position=gg.position_dodge(0),
        	   angle=0, size=3, data=mandates) 
    + gg.geom_hline(gg.aes_string(yintercept=0 ),linetype="dashed", col="red")
    + gg.geom_line(gg.aes_string(x=x, y=y, color=fill), size=1) 
    + gg.geom_point(gg.aes_string(x=x, y=y, fill=fill)) 
    + gg.scale_colour_manual(values = dict2vec(colors)) 
    + gg.scale_fill_manual(values = dict2vec(colors)) 
    + gg.scale_x_continuous(limits=FloatVector([2010, 2020])) 
    + gg.scale_y_continuous(limits=FloatVector([-2.6, 2.6])) 
    + gg.theme_bw()
    + ggtheme()
    + ggguides(ncol=4)
    + gg.labs(
        x        = robj.NULL,
        y        = ylab,
        color    = leg_title, 
        fill     = leg_title, 
	linetype = robj.NULL,
	shape    = robj.NULL,
        title    = robj.NULL,
        subtitle = robj.NULL,
        caption  = robj.NULL
    )
)
g.plot()
fn_root='figure6'
if save:
    # table
    fn = PATH_MANUSCRIPT_TABLES / f"{fn_root}.xlsx"
    tab.to_excel(fn, sheet_name='Sheet1', index=False)
    # plot
    plt.figure(1)
    fns = [PATH_MANUSCRIPT_FIGURES  / f'{fn_root}-simpatiza.png',
           PATH_MANUSCRIPT_FIGURES  / f'{fn_root}-simpatiza.pdf']
    [plt.savefig(fn) for fn in fns]
    fns = [PATH_MANUSCRIPT_FIGURES  / f'{fn_root}.png',
           PATH_MANUSCRIPT_FIGURES  / f'{fn_root}.pdf']
    [g.save(filename=str(fn), width=8, height=3.5) for fn in fns]

    

# ** Figure 7: Polar plots

vars = TRUST | EVAL
vars_groups = {
    "Trust" : list(TRUST.values()),
    "Evaluation" : list(EVAL.values()),
}
facet='ptyvpres3'
ptyvs=df.drop_rows(dropna=facet)[facet].unique()
#
tab=ds.eDataFrame()
for i, ptyv in enumerate(ptyvs):
    legend=True if i==0 else False
    tmp = (
        df
        .select_cols(names=vars | {'yr':"Year"} | {facet:facet} )
        .mutate_type(col2type={"Year":'str'})
        .select_rows(query=f"{facet}=='{ptyv}'")
        .summary(vars=None, groups=["Year"])
        .mutate({'vote': ptyv})
    )
    tab=tab.bind_row(tmp)
    ax=(
        df
        .select_cols(names=vars | {'yr':"Year"} | {facet:facet} )
        .mutate_type(col2type={"Year":'str'})
        .select_rows(query=f"{facet}=='{ptyv}'")
        .plot_polar(vars_groups,
                    group='Year',
                    group_linestyles=['-', '--'],
                    labels_wrap=15,
                    # facet=facet
                )

    )
    axc=ax[0]
    leg = axc.legend(loc='lower left', bbox_to_anchor=(-.15, 1.1), handlelength=2,
                     title=None,
                     handletextpad=.3, prop={'size':10},
                     # pad between the legend handle and text
                     labelspacing=.2, #  vertical space between the legend entries.
                     columnspacing=1, # spacing between columns
                     # handlelength=1, #  length of the legend handles
                     ncol=4, mode=None, frameon=False, fancybox=True,
                     framealpha=0.5, facecolor='white')
    leg._legend_box.align = "left"
    axc.tick_params(axis="x",
                    labelsize=13, labelcolor='black')
    # -----
    # Title
    # -----
    plt.subplots_adjust(top=.78)
    xcoord=-.15
    ycoord=1.2
    yoffset=.0
    title="Partido que votou na eleição anterior: "+ptyv
    axc.annotate(title, xy=(xcoord, ycoord),
               xytext=(xcoord, ycoord), xycoords='axes fraction',
		 size=12, alpha=1)
    # Save figures
    fig=axc.get_figure()
    fig.set_size_inches([6,6])
    print(f"{i}", flush=True)
    fn_root=f"figure7"
    if save:
        suffix=re.sub(pattern='/', repl='-', string=ptyv)
        fns = [PATH_MANUSCRIPT_FIGURES  / f'{fn_root}-{i}.png',
               PATH_MANUSCRIPT_FIGURES  / f'{fn_root}-{i}.pdf']
        [plt.savefig(fn, box_inches=[5,5]) for fn in fns]

fn = PATH_MANUSCRIPT_TABLES / f"{fn_root}.xlsx"
tab.to_excel(fn, sheet_name='Sheet1', index=False)
plt.close('all')


# ** Figure 8: Regression

y='aaidx3c'
COVARS = TRUST | EVAL | CONTROLS
covars=list(COVARS.keys())
interaction='region*inchhpc_std'
tab=(
    df
    .select_cols(names=[y] + covars + ['yr'])
    .drop_rows(dropna=True)
    .mutate_categorical(var=y, cats=[
        'Status Quo',
        'Centralist',
        'Decentralist'
    ], ordered=True, wrap=False)
    .nest('yr')
    .mutate({'f': f"{y} ~ {' + '.join(covars)} + {interaction}"})
    .mutate_rowwise({'mod': lambda x: nnet.multinom(x['f'], data=x['data'], Hess=True),
                     'tidy': lambda x: broom.tidy_multinom(x['mod'], conf_int=True),
                     'res': lambda x: get_data_frame(x['tidy'])
                    })
    .mutate_rowwise({'res': lambda col:
                     col['res']
                     .replace({'Centralist':"Centralista",
                               'Decentralist':'Descentralista'} , regex=True, inplace=False)
                     .replace(COVARS , regex=False, inplace=False)
                     .replace(CONTROLS , regex=False, inplace=False)
                     .replace({
                         "Income":"Renda",
                         "inchhpc_std:":"Renda x ",
                         'region':"Região ",
                    } , regex=True, inplace=False)
                     })
)
# 
# Plot 
# ----
ax=(
    tab
    .unnest(id_vars='yr', col='res')
    .mutate_type(col2type={'yr':'str'})
    .rename_cols(columns={'y.level':'y'}, tolower=False)
    .plot_coef('estimate', 'term',se='std.error',
               model_id='yr', facet_x='y',
               colors=['grey', 'black'],
               shapes=['v', '^'],
               dodge=.1,
               size=10,
               leg_pos_manual=[0,1.03],
               leg_ncol=2,
               facet_yoffset=-.12
               )
)
plt.tight_layout()
#

fn_root='figure8'
if save:
    # table
    tabs=(
        tab
        .unnest(id_vars='yr', col='res')
        .mutate_type(col2type={'yr':'str'})
    )
    fn = PATH_MANUSCRIPT_TABLES / f"{fn_root}.xlsx"
    tabs.to_excel(fn, sheet_name='Sheet1', index=False)
    # Save figures
    fns = [PATH_MANUSCRIPT_FIGURES  / f'{fn_root}.png',
           PATH_MANUSCRIPT_FIGURES  / f'{fn_root}.pdf']
    [plt.savefig(fn) for fn in fns]


# ** Difference between beta coefficients

# note: run regression (figure 8 first)

tabt=(
    tab
    .unnest(id_vars='yr', col='res')
    .mutate_type(col2type={'yr':'str'})
    .rename_cols(columns={'y.level':'y', 'std.error':'se'}, tolower=False)
    .pivot_wider(id_vars=['y', 'term'], cols_from='yr',
                 values_from=['estimate', 'se'],
                 aggfunc='sum')
    .mutate({'zdiff': lambda x: (x['estimate_2018']-x['estimate_2013']) /
             np.sqrt(x['se_2013']**2 + x['se_2018']**2),
             'pvalue': lambda x: 1-dnorm.cdf(x=abs(x['zdiff']), loc=0, scale=1)
             })
    .select_rows(query=f"pvalue<0.05")
    .sort_values(['pvalue'], ascending=True)
)
tabt



# * Appendix
# ** DONE Centralism vs perception of importance

var='aaidx5c_loc'
# 
for yr in [2013, 2018]:
    y=df.loc[df.yr==yr, var]
    x=df.loc[df.yr==yr, 'impdec']
    chi2=x2(pd.crosstab(x, y))[0]
    pvalue=x2(pd.crosstab(x, y))[1]
    print(f"Year: {yr}\nchi2:{chi2}\np-value:{pvalue}")
# 
tab=(
    df
    .drop_rows(query=f"{var}=='Decentralist'")
    .replace(VAR_LABELS, regex=False, inplace=False)
     .select_cols(names=[var, 'impdec', 'yr'])
     .fillna(value="NS/NR",  inplace=False, axis=0)
     # .drop_rows(dropna=True)
     )
tab
tab=tab.tab(col=var, row='impdec', groups='yr')
tab.print()

# 
if save:
# if True:
    fn=PATH_MANUSCRIPT_TABLES / "tableA1.xlsx"
    tab.to_excel(fn)






# Support for centralization or status quo among those
# who perceive the federation as centralized
(
    df
    # perceive the Fed Gov as the most important level
    .select_rows(query=f"impdec=='Federal Government'")
    # exclude "decentralist" extra category
    .drop_rows(query=f"{var}=='Decentralist'")
    .select_cols(names=[var, 'impdec', 'yr'])
    .replace({
        "Centralist":'Status Quo or Centralist',
        "Status Quo":'Status Quo or Centralist',
              } , regex=False, inplace=False)
    .freq(vars=var, groups='yr', include_na=True)
)
# Note: equivalent to
(11.98+11.35)/51.84
