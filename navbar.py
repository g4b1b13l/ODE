import dash_bootstrap_components as dbc
def Navbar():
  navbar = dbc.NavbarSimple(
           children=[
              #dbc.NavItem(dbc.NavLink("Time-Series", href="/time-series")),
              #dbc.NavItem(dbc.NavLink("Time-Series", href="/time-series")),
              #dbc.NavItem(dbc.NavLink("Time-Series", href="/time-series")),
              dbc.DropdownMenu(
                 nav=True,
                 in_navbar=True, 
                 label="Menu",
                 children=[
                    dbc.DropdownMenuItem("Mapa UFPB", href="/mapa-ufpb"),       
                    dbc.DropdownMenuItem(divider=True),   
                    dbc.DropdownMenuItem("João", href="/joao"),       
                    dbc.DropdownMenuItem("Rafael", href="/rafael"),      
                    dbc.DropdownMenuItem("Emmanuela", href="/emmanuela"),
                          ],       
                      ),
                    ],
          brand="Home",
          brand_href="/home",
          sticky="top",
        )
  return navbar








