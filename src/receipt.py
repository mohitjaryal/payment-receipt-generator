# import modules
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os

# generate recipt function
def generate_receipt(name, product, quantity, price, payment_method):

    # date
    date = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")

    # generated output will store here
    filename = f"output/recipt_{date}.pdf"

    os.makedirs("output/", exist_ok=True)

    DATA=[
        ["Date", "Custumer", "Product", "Quantity", "Price(Rs)", "Payment"],
        [date, name, product, quantity, price, payment_method]
    ]

    # converting generated recipt into pdf
    pdf = SimpleDocTemplate(filename, pagesize = A4)

    # style
    styles = getSampleStyleSheet()
    title_style = styles['Heading1']
    title_style.alignment = 1

    title = Paragraph('Payement Recipt', title_style)

    style = TableStyle([
        ('BOX',(0,0), (-1,-1), 1, colors.black),
        ('GRID',(0,0), (-1,-1), 1, colors.black),
        ('BACKGROUND',(0,0), (-1, 0), colors.gray),
        ("TEXTCOLOR",(0,0), (-1, 0), colors.whitesmoke),
        ('ALIGN',(0,0), (-1,-1), "CENTER"),
    ])

    table = Table(DATA)
    table.setStyle(style)

    pdf.build([title, table])

    return filename