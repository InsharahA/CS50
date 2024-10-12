from fpdf import FPDF, Align, XPos, YPos

def main():
    pdf=FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", "B", 16)
    pdf.cell(w=0,align="C",text="CS50 Shirtificate")
    pdf.image(name="https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png",x=0,y=20)
    pdf.set_xy(x=0,y=100)
    pdf.set_font("helvetica", "B", 25)
    pdf.cell(w=0,align=Align.C,text="Insharah Ansari took CS50",new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.output("tuto1.pdf")




if __name__=="__main__":
    main()