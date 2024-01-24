Data = input("digite a data EX 00/00/00:  ")
Empresa = input("digite o nome da empresa: ")
Sevico = input("digite o serviço prestado: ")
Descricao = input("digite o que foi realizado: ")



get_ipython().system('pip install fpdf')


from fpdf import FPDF


pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")
pdf.image("fundo.png", x=0, y=0, w= 211, h= 300)
pdf.text(42,73, Data)
pdf.text(48,84,Empresa)
pdf.text(44,99,Sevico)
pdf.text(51,114, Descricao)

pdf.output("relat.pdf")
print("orçamento feito")


