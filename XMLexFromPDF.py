#


import os
import pypdf


def extract_xml_from_pdfs(directory):
    """
    Keres minden PDF fájlt a megadott könyvtárban, és ha tartalmaz XML csatolmányt,
    akkor leválasztja és elmenti az eredeti fájlnévvel, de .xml kiterjesztéssel.
    """
    for filename in os.listdir(directory):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(directory, filename)
            try:
                with open(pdf_path, "rb") as f:
                    reader = pypdf.PdfReader(f)
                    for file in reader.attachments:
                        if file.endswith(".xml"):
                            xml_data = reader.attachments[file]
                            xml_filename = os.path.splitext(filename)[0] + ".xml"
                            xml_path = os.path.join(directory, xml_filename)

                            with open(xml_path, "wb") as xml_file:
                                xml_file.write(xml_data[0])

                            print(f"Mentve: {xml_filename}")
            except Exception as e:
                print(f"Hiba a(z) {filename} feldolgozásakor: {e}")


if __name__ == "__main__":
    directory= 'C:/Games/'   #win test dir
    cwd = os.getcwd()
    print(cwd)
    directory = cwd
    #directory = input("Add meg a PDF könyvtár útvonalát: ").strip()
    if os.path.isdir(directory):
        extract_xml_from_pdfs(directory)
    else:
        print("Hibás könyvtár útvonal!")
