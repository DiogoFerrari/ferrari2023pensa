
print(f"Loading constants...", flush=True)
CONTROLS={
    'age_std'       : 'Idade (std)',
    'educ_std'      : 'Educação (std)',
    'tid_rel_std'   : "Id. Territorial (std)",
    'inchhpc_std'   : "Income",
    'gender2'       : "Sexo (Mulher)",
    'ptyidPT'       : "Partidarismo (PT)",
    'region'        : "Região",
    # 'ptyvpres3',   # not in final
}
EVAL={
    'eval_presfpv3' : "Avaliação (Presidente)",
    'eval_preffpv3' : "Avaliação (Prefeito)",
    'eval_govfpv3'  : "Avaliação (Governador)",
}
TRUST={
    'trustfedgov'   : "Confiança (Federal)",
    'truststgov'    : "Confiança (Estado)",
    'trustcitygov'  : "Confiança (Municipio)",
}
TRUST_GAP={
    'trustgapstate' :"Gap de confiança (Estado)", # not in final
    'trustgapcity'  : "Gap de confiança (Municipio)",  # not in final
}

# Labels 
# ------
VAR_LABELS = {
    'aaidx5c_loc':{
        'Centralist'  : "Centralista",
        'Regionalist' : "Estadualista",
        'Localist'    : "Municipalista",
        'Status Quo'  : "Status Quo",
    },
    'impdec':{
        'Federal Government':'Governo Federal',
        'Local Government'  :'Governo Municipal',
        'State Government'  :'Governo Estadual',
        'All Levels'        :'Todos'
    }
}
