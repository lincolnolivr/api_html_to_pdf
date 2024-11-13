# %%


from weasyprint import HTML

# Caminho para o arquivo HTML
html_file = 'example.html'

# Converter para PDF
HTML(html_file).write_pdf('output.pdf')

# %%

import requests
from weasyprint import HTML

response = requests.get('https://nfe.prefeitura.sp.gov.br/contribuinte/notaprint.aspx?ccm=33555800&nf=29716295&cod=RKGUMGV9')
html_content = response.text
pdf_file = "nota_fiscal.pdf"
HTML(string=html_content).write_pdf(pdf_file)
# %%


from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://nfe.prefeitura.sp.gov.br/contribuinte/notaprint.aspx?ccm=33555800&nf=29716295&cod=RKGUMGV9')


# %%
