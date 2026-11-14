from pygments.styles.dracula import green
from rich import print, style
from rich.table import Table

tabela = Table(title='Tabela de preços')

tabela.add_column('Nome', justify= 'right',style='red')
tabela.add_column('Preço', justify= 'center',style='blue')
tabela.add_row('Lapís','Borracha'  )
tabela.add_row('Borracha','[green]R$5,00[/]')
print(tabela)