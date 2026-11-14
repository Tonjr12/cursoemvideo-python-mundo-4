from rich import print
print(f"ola [green]MUNDO[/]!:earth_americas:")
print('[bold blue]Olá Pequeno Gafanhoto![/]:vulcan_salute:')
print('[bold yellow on white]Olá Pequeno Gafanhoto![/]:vulcan_salute:')
print(':purple_heart: :two_hearts:[purple]ISABEL BORGES JULIÃO[/]:heart_eyes::heart_eyes:'.center(100))
print("Programar em Python é :heart:")
print("Olha esse efeito :heart_eyes:")
print("Combinação de cores e amor :purple_heart: :two_hearts:")

from rich import print

nome = "[purple]ISABEL BORGES JULIÃO[/]"

# 40 corações + 20 do nome + 40 corações = 100 de largura
print("💜" * 40 + nome + "💜" * 40)

from rich import print

centro = "💜 💕 [purple]ISABEL BORGES JULIÃO[/] 😍 😍"

# Preenche o restante da linha até fechar 100 espaços
print("❤️" * 37 + centro + "❤️" * 38)


from rich import print

# 1. Definimos o bloco central com os emojis de destaque e o nome formatado
centro_limpo = "💕 ISABEL BORGES JULIÃO 😍😍"
centro_rich = "💕 [purple]ISABEL BORGES JULIÃO[/] 😍😍"

# 2. Calculamos quantos caracteres as tags do Rich ocupam a mais no código
tamanho_tags = len(centro_rich) - len(centro_limpo)

# 3. Somamos esse tamanho à largura desejada (ex: 100) para compensar o encolhimento
largura_total = 100 + tamanho_tags

# 4. Executamos o centro usando o emoji literal '💜' para preencher o restante da linha
print(centro_rich.center(largura_total, '💜'))
