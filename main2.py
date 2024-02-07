import dependencies.pdfedit as pdfEdit
import dependencies.recipient as recipient

name = input("Enter the name of the reciever: ")
pos = input("Enter the position of the reciever: ")
org = input("Enter the organization of the reciever: ")
add = input("Enter the address of the reciever: ")

# recipient.createImage(name, pos, org, add)
# pdfEdit.createPdf("./dependencies/template.pdf",
#                   f'./Output/{org}.pdf', "./temp/" + org + ".png", 87, 630, 280, 55)
# print("Pdf saved in Output folder." + f'./Output/{org}.pdf')


def createProposal(name, pos, org, add):
    recipient.createImage(name, pos, org, add)
    pdfEdit.createPdf("./dependencies/template.pdf",
                      f'./Output/{name}.pdf', "./temp/" + name + ".png", 87, 170, 280, 55)
    print("Pdf saved in Output folder." + f'./Output/{name}.pdf')
 
companies = ['Digituall',
'DIGITUALL',
'Yellowloop',
'Exim logistics pvt ldt',
'Nibav home lifts',
'Otechnos',
'Achivia seek know grow',
'Dearlife',
'2050 healthcare',
'Credencesoft',
'Finmatrix',
'Laxmifoods',
'Prsons Group',
'Quantumware',
'Riaxe enterprise software consulting',
'Aibek Solutions',
'Luminous Infoways',
'Oditek Sol',
'Camera queen productions',
'Oditek solutions',
'Orive solutions PVT LMT',
'Spikewell',
'Swostitech Solution',
'Insta Safe',
'ARF design pvt ltd',
'Sapphire Technocrates',
'Ecometrix consultancy PVT LMT',
'ECOMETRIX',
'Shree cement',
'JBAS and Associates',
'CASA Infotech',
'Small day',
'OVO Farms fresh',
'Asiczen',
'Teceds',
'Bankify',
'Shyaam steel',
'SONY',
'SMA Experts Ltd',
'Buildlay',
'Valnize health care',
'JIBE development service PVT LMT',
'WEIR minerals India PVT LMT',
'Luigong konark Infracore',
'ZOCA Courtyard',
'Usha',
'Cohopers',
'Tetratrion',
'Quocent pvt ltd',
'MedKart24',
'KT ADVISOR LLP',
'Ntspl and astutenext',
'Etg research',
'PRM',
'Infuidity solution',
'Fortis',
'Shiftu technology']

createProposal(name, pos, org, add)