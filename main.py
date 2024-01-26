import dependencies.pdfedit as pdfEdit, dependencies.recipient as recipient

name = input("Enter the name of the reciever: ")
pos = input("Enter the position of the reciever: ")
org = input("Enter the organization of the reciever: ")
add = input("Enter the address of the reciever: ")

recipient.createImage(name, pos, org, add)
pdfEdit.createPdf("./dependencies/template.pdf", f'./Output/{org}.pdf', "./temp/" + org + ".png", 90, 640, 180, 43)
print("Pdf saved in Output folder." + f'./Output/{org}.pdf')