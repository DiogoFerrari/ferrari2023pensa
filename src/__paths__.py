from pathlib import Path
import os

ROOT                                   = Path(os.path.abspath(os.curdir))
ROOT                                   = ROOT.parent.parent

# data
PATH_DATA_FINAL                        = ROOT / "data" / "final"
PATH_DATA_RAW                          = ROOT / "data" / "raw"
PATH_DATA_INTERIM                      = ROOT / "data" / "interim"
# scripts
PATH_SRC                               = ROOT / "src"
PATH_SRC_DATA_ORGANIZING               = PATH_SRC / "data-organizing"
PATH_SRC_DATA_COLLECTING               = PATH_SRC / "data-collecting"
PATH_SRC_DATA_MODEL                    = PATH_SRC / "model"
PATH_SRC_DATA_EDA                      = PATH_SRC / "eda"
# manuscript
PATH_MANUSCRIPT                        = ROOT / "manuscript"
PATH_MANUSCRIPT_FIGURES                = PATH_MANUSCRIPT / 'tables-and-figures'
PATH_MANUSCRIPT_TABLES                 = PATH_MANUSCRIPT / 'tables-and-figures'
PATH_MANUSCRIPT_SUPPLEMENTARY_MATERIAL = PATH_MANUSCRIPT / 'supplementary-material'
# output
PATH_OUTPUTS                           = ROOT / 'outputs'
# report
PATH_REPORTS                           = ROOT / 'reports'
PATH_DOCS                              = ROOT / 'docs'

