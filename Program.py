import yfinance as yf # Import Dataset 

from bokeh.models.widgets import Tabs # import Tabs digunakna untuk membuat tab halaman website
from bokeh.io import curdoc # import curdoc 

# Memanggil fungsi Tab Korelasi dan Line 
from Tab_Corr import Tab_Corellation 
from Tab_Line import Tab_LinePlot 

# Membuat Tab 
tab1 = Tab_Corellation(yf)
tab2 = Tab_LinePlot(yf)

# Masukkan semua tab ke dalam satu aplikasi
tabs = Tabs(tabs = [tab1, tab2])

# Put the tabs in the current document for display
curdoc().add_root(tabs)
curdoc().title = "Pergerakan Saham Bank-Bank Ternama di Indonesia"